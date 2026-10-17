"""Read pinned XLSX source values without Excel, macros or formula execution.

This is a deliberately small read-only OOXML reader for the ISU workbook, not a
general spreadsheet evaluator. Formula cells and unsupported types fail closed.
Original row/column addresses are preserved for observation-level provenance.
"""

from pathlib import PurePosixPath
import re
import zipfile
import xml.etree.ElementTree as ET

NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


class SourceWorkbook:
    def __init__(self, path):
        self.path = path
        with zipfile.ZipFile(path) as z:
            if z.testzip() is not None:
                raise ValueError("Corrupt XLSX source")
            self.strings = []
            if "xl/sharedStrings.xml" in z.namelist():
                self.strings = [
                    "".join(item.itertext())
                    for item in ET.fromstring(z.read("xl/sharedStrings.xml"))
                ]
            rels = {
                r.attrib["Id"]: r.attrib["Target"]
                for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
            }
            self.sheets = {}
            for sheet in ET.fromstring(z.read("xl/workbook.xml")).findall("s:sheets/s:sheet", NS):
                target = rels[sheet.attrib[REL]]
                member = target.lstrip("/") if target.startswith("/") else str(PurePosixPath("xl") / target)
                if ".." in PurePosixPath(member).parts:
                    raise ValueError("Unsafe worksheet relationship")
                self.sheets[sheet.attrib["name"]] = member

    def read(self, name):
        """Return {Excel row number: {column letters: typed value}}."""
        with zipfile.ZipFile(self.path) as z:
            root = ET.fromstring(z.read(self.sheets[name]))
        rows = {}
        for row in root.findall("s:sheetData/s:row", NS):
            number = int(row.attrib["r"])
            values = {}
            for cell in row.findall("s:c", NS):
                if cell.find("s:f", NS) is not None:
                    raise ValueError(f"Formula in source: {name}!{cell.attrib['r']}")
                column = re.fullmatch(r"([A-Z]+)[0-9]+", cell.attrib["r"]).group(1)
                kind = cell.attrib.get("t", "n")
                node = cell.find("s:v", NS)
                if kind == "inlineStr":
                    value = "".join(cell.find("s:is", NS).itertext())
                elif node is None or node.text is None:
                    continue
                elif kind == "s":
                    value = self.strings[int(node.text)]
                elif kind == "n":
                    value = float(node.text)
                else:
                    raise ValueError(f"Unsupported XLSX type {kind}")
                values[column] = value
            rows[number] = values
        return rows


def column_after(column):
    number = 0
    for letter in column:
        number = number * 26 + ord(letter) - 64
    number += 1
    result = ""
    while number:
        number, digit = divmod(number - 1, 26)
        result = chr(65 + digit) + result
    return result


def capacity_blocks(rows, column):
    """Split numeric capacity/voltage pairs at blank delimiters, preserving rows."""
    adjacent = column_after(column)
    if rows[1].get(column) != "Capacity/mAh" or rows[1].get(adjacent) != "Voltage/V":
        raise ValueError("Source column headers changed")
    blocks, block = [], []
    for number in range(2, max(rows) + 1):
        q, v = (rows.get(number, {}).get(c) for c in [column, adjacent])
        if q is None and v is None:
            if block:
                blocks.append(block)
                block = []
        elif isinstance(q, (int, float)) and isinstance(v, (int, float)):
            block.append([number, q, v])
        else:
            raise ValueError(f"Incomplete/non-numeric pair at row {number}")
    if block:
        blocks.append(block)
    return blocks
