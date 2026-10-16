"""Build an English static viewer with cell-scoped, provenance-rich downloads."""

from importlib.resources import files
from pathlib import Path
import json
import csv
import copy
import math


def _preview(test, samples):
    """Display decimation only: downloads always retain every observation."""
    if test["path"] is None:
        groups = [(test["protocol"], samples)]
    else:
        groups = [
            (
                f"{s['nominal_C_rate']:g}C discharge, step {s['step']}",
                [
                    r
                    for r in samples
                    if int(r["step"]) == s["step"] and r["mode"] == "D"
                ],
            )
            for s in test["discharge_segments"]
            if not s["initial_preconditioning"]
        ]
    result = []
    for label, points in groups:
        valid = [
            r for r in points if r["voltage_V"] and math.isfinite(float(r["voltage_V"]))
        ]
        if not valid:
            continue
        start = float(points[0]["time_s"])
        # Include valid endpoints; source missing counts are shown beside the plot.
        stride = max(1, math.ceil(len(valid) / 300))
        selected = valid[::stride]
        if selected[-1] is not valid[-1]:
            selected.append(valid[-1])
        result.append(
            {
                "label": label,
                "points": [
                    [(float(r["time_s"]) - start) / 3600, float(r["voltage_V"])]
                    for r in selected
                ],
                "valid_voltage_rows": len(valid),
                "source_rows": len(points),
            }
        )
    return result


def build_site(catalog, output):
    errors = catalog.validate()
    if errors:
        raise ValueError("Catalog validation failed: " + "; ".join(errors))
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    downloads = output / "downloads"
    downloads.mkdir(exist_ok=True)

    def write_json(name, value):
        (downloads / name).write_text(
            json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8"
        )

    records = []
    for curve in catalog.search():
        record = copy.deepcopy(curve.record)
        x, y = curve.sample(801)
        record["display_points"] = [[float(a), float(b)] for a, b in zip(x, y)]
        record["display_note"] = (
            "801 sampled display points. Table downloads retain every extracted point; formula CSVs are generated 2001-point samples."
        )
        records.append(record)
        curve.export_csv(
            downloads / f"{curve.id}.csv",
            count=2001 if record["representation"]["kind"] == "expression" else None,
        )
        write_json(
            f"{curve.id}.json",
            {
                "record": curve.record,
                "sources": {sid: catalog.sources[sid] for sid in record["source_ids"]},
                "experiment": catalog.experiments.get(record["experiment_id"]),
                "material": catalog.materials[record["material_id"]],
                "cell": catalog.cells.get(record["cell_link"]["cell_id"]),
                "upstream_assets": {
                    aid: catalog.assets[aid]
                    for aid in record["provenance"]["asset_ids"]
                },
            },
        )
    for cid, cell in catalog.cells.items():
        parameters = [p for p in catalog.parameters if p["cell_id"] == cid]
        tests = catalog.linked_tests(cid)
        ocp = [r.record for r in catalog.search(cell_id=cid)]
        source_ids = set(cell["source_ids"])
        source_ids.update(sid for p in parameters for sid in p["source_ids"])
        source_ids.update(sid for r in ocp for sid in r["source_ids"])
        source_ids.update(t["source_id"] for t in tests)
        asset_ids = {p["provenance"]["asset_id"] for p in parameters}
        asset_ids.update(aid for r in ocp for aid in r["provenance"]["asset_ids"])
        asset_ids.update(t["asset_id"] for t in tests)
        write_json(
            f"{cid}-parameters.json",
            {
                "cell_id": cid,
                "cell": cell,
                "parameters": parameters,
                "ocp_records": ocp,
                "full_cell_tests": tests,
                "sources": {sid: catalog.sources[sid] for sid in sorted(source_ids)},
                "upstream_assets": {
                    aid: catalog.assets[aid] for aid in sorted(asset_ids)
                },
                "independent_full_cell_validation": False,
            },
        )
        with (downloads / f"{cid}-parameters.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "id",
                    "cell_id",
                    "name",
                    "category",
                    "value_or_expression",
                    "unit",
                    "conditions_json",
                    "definition",
                    "source_ids",
                    "origin_status",
                ]
            )
            for p in parameters:
                rep = p["representation"]
                writer.writerow(
                    [
                        p["id"],
                        cid,
                        p["name"],
                        p["category"],
                        rep.get("value", rep.get("expression")),
                        p["unit"],
                        json.dumps(p.get("conditions", {}), sort_keys=True),
                        p.get("definition", p["name"]),
                        ";".join(p["source_ids"]),
                        p["provenance"]["origin_status"],
                    ]
                )
    data = {
        "release": catalog.document["release"],
        "records": records,
        "sources": catalog.sources,
        "experiments": catalog.experiments,
        "materials": catalog.materials,
        "cells": catalog.cells,
        "assets": catalog.assets,
        "parameters": catalog.parameters,
        "full_cell_tests": copy.deepcopy(catalog.full_cell_tests),
    }
    for test in data["full_cell_tests"]:
        for key in ("path", "normalized_path"):
            relative = test[key]
            if relative:
                (downloads / Path(relative).name).write_bytes(
                    (catalog.root / relative).read_bytes()
                )
        test["preview_segments"] = _preview(
            test, catalog.full_cell_data(test["id"], normalized=True)
        )
    (output / "catalog.js").write_text(
        "window.EBP_DATA = " + json.dumps(data, allow_nan=False) + ";\n",
        encoding="utf-8",
    )
    for name in ("index.html", "style.css", "app.js", "logo.png"):
        (output / name).write_bytes(files("ebp").joinpath("web", name).read_bytes())
    license_dir = output / "licenses"
    license_dir.mkdir(exist_ok=True)
    for item in files("ebp").joinpath("licenses").iterdir():
        (license_dir / item.name).write_bytes(item.read_bytes())
    return output
