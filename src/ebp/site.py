"""Build a static, network-free viewer. Hosting is deliberately opt-in."""

from importlib.resources import files
from pathlib import Path
import json
import csv
import copy


def build_site(catalog, output):
    errors = catalog.validate()
    if errors:
        raise ValueError("Catalog validation failed: " + "; ".join(errors))
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    assets_dir = output / "downloads"
    assets_dir.mkdir(exist_ok=True)
    rows = []
    for curve in catalog.search():
        record = dict(curve.record)
        x, y = curve.sample(801)
        record["display_points"] = [[float(a), float(b)] for a, b in zip(x, y)]
        record["display_note"] = (
            "801 linearly sampled display points; table CSV download preserves all retained native points. Formula CSV is a generated 2001-point sample."
        )
        rows.append(record)
        curve.export_csv(
            assets_dir / f"{curve.id}.csv",
            count=2001 if record["representation"]["kind"] == "expression" else None,
        )
        package = {
            "record": curve.record,
            "sources": {sid: catalog.sources[sid] for sid in record["source_ids"]},
            "experiment": catalog.experiments.get(record["experiment_id"]),
            "material": catalog.materials[record["material_id"]],
            "cell": catalog.cells.get(record["cell_link"]["cell_id"]),
            "upstream_assets": {
                aid: catalog.assets[aid] for aid in record["provenance"]["asset_ids"]
            },
        }
        (assets_dir / f"{curve.id}.json").write_text(
            json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    data = {
        "release": catalog.document["release"],
        "records": rows,
        "sources": catalog.sources,
        "experiments": catalog.experiments,
        "materials": catalog.materials,
        "cells": catalog.cells,
        "parameters": catalog.parameters,
        "full_cell_tests": copy.deepcopy(catalog.full_cell_tests),
    }
    (assets_dir / "lg-m50-parameters.json").write_text(
        json.dumps(
            {
                "cell": catalog.cells["lg-m50"],
                "parameters": catalog.parameters,
                "sources": catalog.sources,
                "upstream_assets": catalog.assets,
                "full_cell_tests": catalog.full_cell_tests,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    with (assets_dir / "lg-m50-parameters.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["id", "name", "category", "value_or_expression", "unit", "source_ids", "origin_status"]
        )
        for p in catalog.parameters:
            rep = p["representation"]
            writer.writerow(
                [
                    p["id"],
                    p["name"],
                    p["category"],
                    rep.get("value", rep.get("expression")),
                    p["unit"],
                    ";".join(p["source_ids"]),
                    p["provenance"]["origin_status"],
                ]
            )
    for test in data["full_cell_tests"]:
        for key in ("path", "normalized_path"):
            relative = test[key]
            (assets_dir / Path(relative).name).write_bytes((catalog.root / relative).read_bytes())
        test["preview_segments"] = []
        with (catalog.root / test["normalized_path"]).open(newline="", encoding="utf-8") as handle:
            samples = list(csv.DictReader(handle))
        for segment in test["discharge_segments"]:
            if segment["initial_preconditioning"]:
                continue
            points = [r for r in samples if int(r["step"]) == segment["step"] and r["mode"] == "D"]
            start = float(points[0]["time_s"])
            # Display only; original and normalized downloads retain every observation.
            stride = max(1, len(points) // 300)
            selected = points[::stride]
            if selected[-1] is not points[-1]:
                selected.append(points[-1])
            test["preview_segments"].append(
                {
                    "C_rate": segment["nominal_C_rate"],
                    "step": segment["step"],
                    "points": [
                        [(float(r["time_s"]) - start) / 3600, float(r["voltage_V"])]
                        for r in selected
                    ],
                }
            )
    (output / "catalog.js").write_text(
        "window.EBP_DATA = " + json.dumps(data, ensure_ascii=False, allow_nan=False) + ";\n",
        encoding="utf-8",
    )
    for name in ("index.html", "style.css", "app.js"):
        (output / name).write_bytes(files("ebp").joinpath("web", name).read_bytes())
    license_dir = output / "licenses"
    license_dir.mkdir(exist_ok=True)
    for item in files("ebp").joinpath("licenses").iterdir():
        (license_dir / item.name).write_bytes(item.read_bytes())
    return output
