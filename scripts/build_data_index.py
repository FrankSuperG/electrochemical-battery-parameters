"""Generate the GitHub browsing index from the authoritative packaged catalog.

No downloads are performed. Large native OCP/test files are linked, not copied.
Run after catalog changes; --check detects stale exports and navigation links.
"""

import argparse
import csv
import io
import json
import os
from pathlib import Path
import re

from ebp import Catalog


REPO = Path(__file__).resolve().parents[1]
START = "<!-- DATA_QUICKLINKS_START -->"
END = "<!-- DATA_QUICKLINKS_END -->"
FORMULA_SAMPLES = 2001


def text_cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def csv_bytes(headers, rows):
    handle = io.StringIO(newline="")
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return handle.getvalue().encode("utf-8")


def json_bytes(value):
    return (json.dumps(value, indent=2, allow_nan=False) + "\n").encode("utf-8")


def parameter_csv(parameters):
    return csv_bytes(
        ["id", "cell_id", "name", "category", "value_or_expression", "unit",
         "conditions_json", "definition", "source_ids", "origin_status",
         "parameterization_variant"],
        [
            [p["id"], p["cell_id"], p["name"], p["category"],
             p["representation"].get("value", p["representation"].get("expression")),
             p["unit"], json.dumps(p.get("conditions", {}), sort_keys=True),
             p.get("definition", p["name"]), ";".join(p["source_ids"]),
             p["provenance"]["origin_status"],
             p.get("conditions", {}).get("parameterization_variant", "")]
            for p in parameters
        ],
    )


def render_index(repo=REPO):
    """Return relative output paths and deterministic bytes; never mutate sources."""
    repo = Path(repo)
    catalog = Catalog(repo / "src/ebp/data")
    errors = catalog.validate()
    if errors:
        raise ValueError("; ".join(errors))
    output = {}

    def relative(page, target):
        return Path(os.path.relpath(target, Path(page).parent)).as_posix()

    def link(page, target, label):
        return f"[{text_cell(label)}]({relative(page, target)})"

    def source_path(path):
        return Path("src/ebp/data") / path

    def ocp_table(page, curves):
        lines = [
            "| Record | Electrode / material | Coordinate and domain | CSV | Metadata |",
            "|---|---|---|---|---|",
        ]
        for curve in curves:
            r = curve.record
            is_formula = r["representation"]["kind"] == "expression"
            target = (Path("data/ocp") / f"{curve.id}-sampled.csv" if is_formula
                      else source_path(r["representation"]["path"]))
            label = "Generated samples" if is_formula else "Retained table"
            lines.append(
                f"| `{curve.id}` | {r['electrode_role']} / {r['material']} | "
                f"{r['x']['kind']}; {r['x']['domain']} | "
                f"{link(page, target, label)} | "
                f"{link(page, Path('data/ocp') / f'{curve.id}.json', 'JSON')} |"
            )
        return "\n".join(lines)

    for curve in catalog.search():
        r = curve.record
        formula = r["representation"]["kind"] == "expression"
        if formula:
            x, y = curve.sample(FORMULA_SAMPLES)
            output[f"data/ocp/{curve.id}-sampled.csv"] = csv_bytes(
                ["x", "potential_V"],
                ((f"{a:.12g}", f"{b:.12g}") for a, b in zip(x, y)),
            )
        output[f"data/ocp/{curve.id}.json"] = json_bytes({
            "record": r,
            "sources": {sid: catalog.sources[sid] for sid in r["source_ids"]},
            "experiment": catalog.experiments.get(r["experiment_id"]),
            "upstream_assets": {aid: catalog.assets[aid] for aid in r["provenance"]["asset_ids"]},
            "export": {
                "kind": "generated_formula_samples" if formula else "retained_source_table",
                "sample_count": FORMULA_SAMPLES if formula else None,
                "significant_digits": 12 if formula else None,
                "canonical_data_root": "../../src/ebp/data",
                "note": "Formula samples are calculated, not measurements. Read the record's coordinate, direction, conditions and license.",
            },
        })

    cell_rows = []
    for cid, cell in catalog.cells.items():
        page = Path("data/cells") / f"{cid}.md"
        curves = catalog.search(cell_id=cid)
        parameters = [p for p in catalog.parameters if p["cell_id"] == cid]
        tests = catalog.linked_tests(cid)
        lines = [f"# {cell['display_name']}", "",
                 f"[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)", "",
                 f"Cell ID: `{cid}`. Match level: `{cell['match_level']}`.", "",
                 cell["match_evidence"], "", cell["note"], "",
                 "## Parameters", ""]
        if parameters:
            csv_path = Path("data/parameters") / f"{cid}.csv"
            json_path = csv_path.with_suffix(".json")
            output[str(csv_path)] = parameter_csv(parameters)
            source_ids = set(cell["source_ids"])
            source_ids.update(s for p in parameters for s in p["source_ids"])
            source_ids.update(s for curve in curves for s in curve.record["source_ids"])
            source_ids.update(t["source_id"] for t in tests)
            asset_ids = {p["provenance"]["asset_id"] for p in parameters}
            asset_ids.update(a for curve in curves for a in curve.record["provenance"]["asset_ids"])
            asset_ids.update(t["asset_id"] for t in tests)
            asset_ids.update(a for t in tests for a in t.get("supporting_asset_ids", []))
            asset_ids.update(s["asset_id"] for t in tests for s in t.get("sidecars", []))
            output[str(json_path)] = json_bytes({
                "cell_id": cid, "cell": cell, "parameters": parameters,
                "ocp_records": [c.record for c in curves], "full_cell_tests": tests,
                "sources": {s: catalog.sources[s] for s in sorted(source_ids)},
                "upstream_assets": {a: catalog.assets[a] for a in sorted(asset_ids)},
                "canonical_data_root": "../../src/ebp/data",
                "independent_full_cell_validation": False,
            })
            lines += [f"{link(page, csv_path, f'All {len(parameters)} parameter records (CSV)')} · "
                      f"{link(page, json_path, 'Definitions, sources and linked-test metadata (JSON)')}", "",
                      "CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.", ""]
            variants = sorted({p.get("conditions", {}).get("parameterization_variant") for p in parameters}
                              - {None, ""})
            if len(variants) > 1:
                lines += ["**Choose one parameterization variant. Do not combine these alternatives. The all-record CSV is for inspection.**", "",
                          "| Variant | Records | CSV |", "|---|---:|---|"]
                for variant in variants:
                    subset = [p for p in parameters if p.get("conditions", {}).get("parameterization_variant") == variant]
                    target = csv_path.with_name(f"{cid}--{variant}.csv")
                    output[str(target)] = parameter_csv(subset)
                    lines.append(f"| `{variant}` | {len(subset)} | {link(page, target, 'Download CSV')} |")
                lines.append("")
        else:
            lines += ["No non-OCP parameters imported for this entry. No placeholder parameter values are supplied.", ""]
        lines += ["## OCP curves", ""]
        lines += [ocp_table(page, curves) if curves else "No electrode-resolved OCP record linked to this cell. Full-cell pseudo-OCV and unrelated same-chemistry curves do not fill this gap.", ""]
        lines += ["Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.", "",
                  "## Full-cell tests", ""]
        if tests:
            lines += ["CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.", "",
                      "| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |",
                      "|---|---|---|---|---|"]
            for test in tests:
                original = test.get("original_download_path") or test.get("path")
                original_link = (link(page, source_path(original), Path(original).suffix.lstrip(".").upper())
                                 if original else f"[Source download](<{catalog.assets[test['asset_id']]['url']}>)")
                coordinate = test.get("independent_variable", {}).get("column", "time_s")
                availability = test["channel_availability"]
                rows = catalog.full_cell_data(test["id"], normalized=True)
                counts = [sum(bool(r.get(key)) for r in rows) for key in
                          ["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K"]]
                # Existing metadata counts are checked against the exported rows.
                for key, count in zip(["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K"], counts):
                    if key in availability and count != availability[key]["present_rows"]:
                        raise ValueError(f"Channel count mismatch: {test['id']} {key}")
                lines.append(f"| `{test['id']}` — {text_cell(test['protocol'])} | `{coordinate}` | "
                             f"{link(page, source_path(test['normalized_path']), 'CSV')} | {original_link} | "
                             f"{' / '.join(map(str, counts))} of {len(rows)} |")
            lines += ["", "### Test gaps and extra channels", ""]
            for test in tests:
                gaps = "; ".join(test["missing_items"]) or "No missing measurement channels recorded; specimen and validation limits still apply."
                lines.append(f"- `{test['id']}`: {gaps}")
                for side in test.get("sidecars", []):
                    lines.append(f"  - {link(page, source_path(side['path']), 'Separate temperature-rise CSV')}; its own timebase is retained, not absolute cell temperature.")
        else:
            lines += ["No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match."]
        lines += ["", "## Cell-level gaps", ""]
        lines += [f"- {item}" for item in cell["missing_items"]]
        lines += ["", "## Sources and reuse", ""]
        sources = set(cell["source_ids"])
        sources.update(t["source_id"] for t in tests)
        for sid in sorted(sources):
            source = catalog.sources[sid]
            lines.append(f"- [{source['title']}](<{source['url']}>) (`{sid}`)")
        lines += ["", "Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.", ""]
        output[str(page)] = "\n".join(lines).encode("utf-8")
        cell_rows.append((cid, cell, len(curves), len(parameters), len(tests)))

    def cells_table(page):
        lines = ["| Cell / study entry | OCP | Other parameters | Full-cell tests | Match level |",
                 "|---|---|---|---|---|"]
        for cid, cell, n_ocp, n_param, n_test in cell_rows:
            target = Path("data/cells") / f"{cid}.md"
            href = relative(page, target)
            ocp = f"[{n_ocp} records]({href}#ocp-curves)" if n_ocp else "Not linked"
            param = f"[{n_param} records]({href}#parameters)" if n_param else "Not imported"
            tests = f"[{n_test} {'file' if n_test == 1 else 'files'}]({href}#full-cell-tests)" if n_test else "Not imported"
            lines.append(f"| {link(page, target, cell['display_name'])} | {ocp} | {param} | {tests} | `{cell['match_level']}` |")
        return "\n".join(lines)

    page = Path("data/ocp/README.md")
    lines = ["# OCP data by material", "", "[All cells](../README.md) · [Download and use the data](../../docs/DATA_ACCESS.md)", "",
             "Every CSV link below is available from the repository without installing E-BatP. Retained tables preserve all stored points and source columns; generated samples contain 2,001 calculated points rounded to 12 significant digits and have `-sampled.csv` filenames. Read the adjacent JSON for original formulas, provenance, licensing and coordinate definitions.", "",
             "Material-level measurements are not automatically linked to a commercial cell. Whole-cell SOC, electrode stoichiometry and normalized branch capacity are different coordinates.", ""]
    materials = sorted({curve.record["material"] for curve in catalog.search()}, key=lambda x: (x != "LFP", x.casefold()))
    for material in materials:
        lines += [f"## {material}", "", ocp_table(page, catalog.search(material=material)), ""]
    output[str(page)] = "\n".join(lines).encode("utf-8")

    page = Path("data/README.md")
    lines = ["# Browse and download the data", "",
             "Start here when browsing on GitHub. No Python installation or hosted website is required to find files.", "",
             "1. Choose a cell below, or [browse OCP by material](ocp/README.md).",
             "2. Open the linked **CSV** for data and **JSON** for definitions, source evidence and missing items.",
             "3. Use the file page's **Raw / download raw file** controls to save the complete file. GitHub previews may not display large files. Keep the metadata and source license with your copy.", "",
             "See [how to download, interpret and use files](../docs/DATA_ACCESS.md) for Excel, Python and model examples. The repository remains private; sign in with an account that has access.", "",
             f"Snapshot: {len(catalog.search())} OCP records, {len(catalog.parameters)} other parameter records, {len(catalog.full_cell_tests)} full-cell test files.", "",
             "## Choose a cell or study", "", cells_table(page), "",
             "## Find data by type", "",
             "| Need | Entry point |", "|---|---|",
             "| LFP or another material's OCP | [OCP index](ocp/README.md), with CSV and per-record JSON links |",
             "| Diffusion, kinetics, geometry, transport or thermal values | [Cell parameter CSV/JSON exports](parameters/); filter CSV by `name` / `category` and inspect `definition`, units, conditions and origin |",
             "| Current / voltage / temperature and CC tests | Choose a cell above, then its Full-cell tests table; [stored test files](../src/ebp/data/full_cell/) |",
             "| Original Mohtat MATs and author files | [Packaged evidence](../src/ebp/data/evidence/) and [source audit](../docs/MOHTAT2020.md) |",
             "| Matching evidence and missing items | Cell pages above and the [matching audit](../src/ebp/data/matching_audit.json) |",
             "| Primary papers, datasets, versions and hashes | [Sources](../src/ebp/data/sources.json), [assets](../src/ebp/data/assets.json) and each export's metadata |", "",
             "## Where the files live", "",
             "`src/ebp/data/` is authoritative. This `data/` directory is a generated browsing view: parameter CSV/JSON exports, small formula samples, per-record OCP metadata and Markdown links. Large native OCP and full-cell observations are linked to their canonical files rather than duplicated.", "",
             "Paths inside JSON records are relative to `src/ebp/data/`; use each export's `canonical_data_root` when reading the export from a checkout. GitHub navigation does not change the observations, definitions or validation status.", "",
             "Maintainers: regenerate with `python scripts/build_data_index.py` after catalog updates. Check freshness with `python scripts/build_data_index.py --check`. Read [CONTRIBUTING.md](../CONTRIBUTING.md) before changing source data.", ""]
    output[str(page)] = "\n".join(lines).encode("utf-8")
    readme = (repo / "README.md").read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        raise ValueError("README data-navigation markers are missing")
    replacement = START + "\n\n" + cells_table(Path("README.md")) + "\n\n" + END
    output["README.md"] = re.sub(re.escape(START) + r".*?" + re.escape(END),
                                 lambda _: replacement, readme, flags=re.DOTALL).encode("utf-8")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render_index()
    stale = [name for name, value in expected.items()
             if not (REPO / name).exists() or (REPO / name).read_bytes() != value]
    extra = [str(p.relative_to(REPO)) for p in (REPO / "data").rglob("*")
             if p.is_file() and str(p.relative_to(REPO)) not in expected]
    if args.check:
        if stale or extra:
            parser.exit(1, "Stale data navigation; regenerate with python scripts/build_data_index.py.\n"
                        + "\n".join(stale + extra) + "\n")
        print(f"OK: {len(expected) - 1} generated data-navigation files and README links are current")
        return
    for name, value in expected.items():
        target = REPO / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_bytes() != value:
            target.write_bytes(value)
    if extra:
        parser.exit(1, "Obsolete generated files need review/removal:\n" + "\n".join(extra) + "\n")
    print(f"Generated {len(expected) - 1} data-navigation files and updated README links")


if __name__ == "__main__":
    main()
