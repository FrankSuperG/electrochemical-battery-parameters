"""Independent source-node checks and conservative LFP study associations."""

import csv
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import numpy as np
import pytest
from scipy.io import loadmat

from ebp import Catalog, StoichiometryMapping

ISU = "isu-uconn-lfp-graphite-lab"
A123 = "a123-18650m1a-jahn2024"
ROOT = Path(__file__).resolve().parents[1]
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


@lru_cache
def numeric_sheet(name):
    """Read numeric XML cells independently of the ingestion XLSX decoder."""
    path = ROOT / "src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx"
    with zipfile.ZipFile(path) as z:
        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        sheet = next(s for s in workbook.findall("s:sheets/s:sheet", NS) if s.attrib["name"] == name)
        rid = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
        rel = next(r for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels")) if r.attrib["Id"] == rid)
        target = rel.attrib["Target"]
        member = target.lstrip("/") if target.startswith("/") else "xl/" + target
        sheet_xml = ET.fromstring(z.read(member))
    return {cell.attrib["r"]: float(cell.find("s:v", NS).text)
            for cell in sheet_xml.findall("s:sheetData/s:row/s:c", NS)
            if cell.attrib.get("t", "n") == "n" and cell.find("s:v", NS) is not None}


def test_pinned_packaged_originals_and_separate_license_roles():
    c = Catalog()
    pins = json.loads((ROOT/"scripts/lfp_study_assets.json").read_text())
    for aid, asset in pins.items():
        assert c.assets[aid] == asset
        if "path" in asset:
            data = (c.root/asset["path"]).read_bytes()
            assert hashlib.sha256(data).hexdigest() == asset["sha256"]
            if "md5" in asset:
                assert hashlib.md5(data).hexdigest() == asset["md5"]
    assert c.sources["isu-uconn-2026-data"]["license"] == "CC-BY-4.0"
    assert c.sources["isu-uconn-2026-code"]["license"] == "MIT"
    for sid in ["jahn-2024-data-v2", "jahn-2024-code"]:
        metadata = json.loads((c.root/f"evidence/{sid}-metadata.json").read_text())
        assert metadata["metadata"]["license"]["id"] == "cc-by-4.0"
    assert "11958572" in c.sources["jahn-2024-data-v2"]["url"]


def test_isu_half_cell_nodes_match_raw_addresses_and_explicit_selection():
    c = Catalog()
    curves = c.search(cell_id=ISU)
    assert len(curves) == 4
    for curve in curves:
        r = curve.record
        p = r["provenance"]["processing"]
        source = numeric_sheet(p["sheet"])
        with (c.root/r["representation"]["path"]).open(newline="") as f:
            rows = list(csv.DictReader(f))
        original = [(idx,source[p["capacity_column"]+str(idx)], source[p["voltage_column"]+str(idx)])
                    for idx in range(p["source_rows"][0], p["source_rows"][1]+1)]
        maximum = max(row[1] for row in original)
        cutoff = next(i for i,row in enumerate(original) if row[1] == maximum)
        firsts = {}
        for idx,q,v in original[:cutoff+1]:
            firsts.setdefault(q,(idx,v))
        assert [int(row["source_excel_row"]) for row in rows] == [pair[0] for pair in firsts.values()]
        q = np.array(list(firsts))
        x,v = curve.points()
        np.testing.assert_array_equal(x,(q-q[0])/(q[-1]-q[0]))
        np.testing.assert_array_equal(v,[pair[1] for pair in firsts.values()])
        np.testing.assert_array_equal([float(row["source_capacity_mAh"]) for row in rows],q)
        assert r["reference"] == "unresolved"
        assert r["measurement"] == "pseudo_ocp"
        assert r["cell_link"]["relationship"] == "same_study_cell_family"
        with pytest.raises(ValueError,match="Reference chemistry"):
            curve.to_pybamm(mapping=StoichiometryMapping(.9,.1,"Test-only hypothetical endpoints"))


def test_isu_full_cell_branch_rows_units_and_missing_channels():
    c = Catalog()
    tests = c.linked_tests(ISU)
    assert len(tests) == 21
    assert sum(t["source_location"]["selection_role"] == "author_primary" for t in tests) == 11
    for t in tests:
        location = t["source_location"]
        source = numeric_sheet(location["sheet"])
        rows = c.full_cell_data(t["id"], normalized=True)
        assert len(rows) == location["last_row"]-location["first_row"]+1
        for expected,row in zip(range(location["first_row"],location["last_row"]+1),rows):
            assert int(row["source_record"]) == expected
            assert float(row["voltage_V"]) == source[location["voltage_column"]+str(expected)]
            assert float(row["passed_capacity_Ah"]) == source[location["pair_column"]+str(expected)]/1000
            assert all(row[k] == "" for k in ["time_s","current_charge_positive_A","cell_temperature_K","ambient_temperature_K","cycle"])
        assert t["independent_variable"]["column"] == "passed_capacity_Ah"
        assert t["relationship_to_parameters"] == "same_study_cell_family"
    assert c.cells[ISU]["model"] is None


def test_a123_ocpn_retains_model_nodes_and_requires_mapping():
    c = Catalog()
    curves = c.search(cell_id=A123)
    assert len(curves) == 2
    for curve in curves:
        r = curve.record
        asset = c.assets[r["provenance"]["asset_ids"][0]]
        mat = loadmat(c.root/asset["path"],simplify_cells=True)
        x,y = curve.points()
        np.testing.assert_array_equal(x,mat["pot_dol"])
        np.testing.assert_array_equal(y,mat["pot"])
        assert r["measurement"] == "model_ocp"
        assert r["x"]["kind"] == "model_soc"
        assert r["quality"]["raw_data"] == "published_table_not_instrument_raw"
        with pytest.raises(ValueError,match="Absolute stoichiometry"):
            curve.to_pybamm()
    # Keep the non-monotonic LFP potential. Sorting potentials would change the model.
    assert np.any(np.diff(c.get("jahn-a123-lfp-model-ocpn").points()[1]) < 0)


@pytest.mark.parametrize("rid,prefix",[("jahn-a123-power-soc50","ch"),("jahn-a123-power-soc100","dc"),("jahn-a123-pocv-full-cycle",None)])
def test_a123_csv_observations_retain_rows_units_and_current_origin(rid,prefix):
    c = Catalog()
    t = next(t for t in c.linked_tests(A123) if t["id"] == rid)
    original = np.genfromtxt(c.root/t["original_download_path"],delimiter=",",names=True)
    rows = c.full_cell_data(rid,normalized=True)
    assert len(rows) == len(original)
    np.testing.assert_array_equal([float(r["time_s"]) for r in rows],original["pt" if prefix is None else f"t_{prefix}_power"])
    np.testing.assert_array_equal([float(r["voltage_V"]) for r in rows],original["pOCVAux" if prefix is None else f"U_{prefix}_power"])
    q = original["pQ" if prefix is None else f"Q_{prefix}_power"]
    np.testing.assert_array_equal([float(r["source_stored_charge_Ah"]) for r in rows],q)
    assert all(r["cell_temperature_K"] == r["ambient_temperature_K"] == "" for r in rows)
    if prefix is None:
        assert all(r["current_charge_positive_A"] == "" for r in rows)
        assert t["missing_values"]["current_charge_positive_A"] == len(rows)
    else:
        current = original[f"I_{prefix}_power"]
        np.testing.assert_array_equal([float(r["current_charge_positive_A"]) for r in rows],current)
        active = (np.abs(current[1:])>.05) & (np.abs(np.diff(q))>1e-8)
        assert np.mean(np.sign(current[1:][active]) == np.sign(np.diff(q)[active])) > .98
    if prefix == "ch":
        assert len(rows) == 336  # Do not inherit the author's 275-row simulation trim.


def test_incremental_ocv_split_preserves_every_observation_and_no_clock():
    c = Catalog()
    tests = [t for t in c.linked_tests(A123) if t["basic_test"]["type"] == "incremental_ocv"]
    assert len(tests) == 2
    original = np.genfromtxt(c.root/tests[0]["original_download_path"],delimiter=",",names=True)
    all_rows = [r for t in tests for r in c.full_cell_data(t["id"],normalized=True)]
    assert [int(r["source_record"]) for r in all_rows] == list(range(202))
    np.testing.assert_array_equal([float(r["source_stored_charge_Ah"]) for r in all_rows],original["Q"])
    np.testing.assert_array_equal([float(r["voltage_V"]) for r in all_rows],original["OCV"])
    assert all(r["time_s"] == r["current_charge_positive_A"] == "" for r in all_rows)


def test_minor_loop_mat_channels_and_absolute_clocks_are_unchanged():
    c = Catalog()
    tests = [t for t in c.linked_tests(A123) if t["id"].startswith("jahn-a123-hysteresis-loop-")]
    assert len(tests) == 9
    mat = loadmat(c.root/tests[0]["original_download_path"],simplify_cells=True)["minor_loops"]
    for t,original in zip(tests,mat):
        rows = c.full_cell_data(t["id"],normalized=True)
        assert len(rows) == len(original[0])
        for key,idx in [("time_s",0),("source_soc_fraction",1),("voltage_V",2),("current_charge_positive_A",3),("source_stored_charge_Ah",4)]:
            np.testing.assert_array_equal([float(r[key]) for r in rows],original[idx])
        assert [int(r["source_record"]) for r in rows] == list(range(len(rows)))


def test_study_links_leave_intrinsic_diffusion_kinetics_and_specimen_gaps_open():
    c = Catalog()
    assert len(c.linked_tests(A123)) == 14
    for cid in [ISU,A123]:
        assert not c.search_parameters(cell_id=cid)
        cell = c.cells[cid]
        for component in ["diffusion","kinetics"]:
            assert cell["evidence_matrix"][component]["match_level"] == "missing"
        assert c.matching_audit["cell_matches"][cid]["components"] == cell["evidence_matrix"]
        assert any("specimen" in item.lower() for item in cell["missing_items"])
    assert c.cells[A123]["model"] == "18650M1A"
    assert not set(c.cells[A123]["ocp_record_ids"]) & set(c.cells["a123-amp20m1hd-a"]["ocp_record_ids"])
