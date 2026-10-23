#!/usr/bin/env python3
"""Reproduce the base catalog and LFP expansion from checksum-pinned assets; no fabricated or digitized points.

Run from the repository root after installing .[dev]. Cached raw data are excluded
from Git. Use --download to retrieve missing assets from the public source.
"""

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import subprocess

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src/ebp/data"
CACHE = ROOT / ".cache/upstream"
PINNED = [
    (
        "sintef-lfp-d07eb6",
        "sintef__sintef-lfp-R2032-gelon-d07eb6__20250602__p-ocv__RT.bdf.parquet",
        "3efea83aa4a59c500bde5723a67e3c3c",
        "LFP",
    ),
    (
        "sintef-lfp-178617",
        "sintef__sintef-lfp-R2032-gelon-178617__20250706__p-ocv__RT.bdf.parquet",
        "20e8f367ef71c570c1d5a172b5c321d7",
        "LFP",
    ),
    (
        "sintef-graphite-1d5628",
        "sintef__sintef-graphite-R2032-intelligent-1d5628__20250528__p-ocv__RT.bdf.parquet",
        "22cddf70cdf1a4432440cf94c19e3e6a",
        "graphite",
    ),
    (
        "sintef-graphite-4ccc47",
        "sintef__sintef-graphite-R2032-intelligent-4ccc47__20250514__p-ocv__RT.bdf.parquet",
        "251c6977b9606e6791c871b9bffe7595",
        "graphite",
    ),
]


def write_json(name, value):
    (DATA / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )


def obtain(filename, url, md5=None, sha256=None, download=False):
    path = CACHE / filename
    if not path.exists():
        if not download:
            raise SystemExit(f"Missing {path}; rerun with --download")
        subprocess.run(
            [
                "curl",
                "--fail",
                "--location",
                "--silent",
                "--show-error",
                "--retry",
                "2",
                url,
                "-o",
                str(path),
            ],
            check=True,
        )
    content = path.read_bytes()
    if md5 and hashlib.md5(content).hexdigest() != md5:
        raise ValueError(f"Upstream MD5 mismatch: {filename}")
    if sha256 and hashlib.sha256(content).hexdigest() != sha256:
        raise ValueError(f"Upstream SHA-256 mismatch: {filename}")
    return path


def base_record(rid, material):
    return {
        "id": rid,
        "version": "1",
        "title": "",
        "parameter": "electrode_ocp",
        "material": material,
        "material_id": "",
        "electrode_role": "positive" if material == "LFP" else "negative",
        "direction": "unspecified",
        "measurement": "literature_formula",
        "temperature": {
            "value_K": None,
            "description": "Not established from the upstream OCP function; no temperature dependence supplied.",
        },
        "reference": "Li/Li+",
        "x": {},
        "y": {"unit": "V", "definition": "Working electrode potential versus Li/Li+"},
        "representation": {},
        "source_ids": [],
        "experiment_id": None,
        "cell_link": {
            "cell_id": None,
            "relationship": "material_only",
            "evidence": "No commercial cell identity established for this record.",
        },
        "provenance": {},
        "quality": {},
        "limitations": [],
        "license": "",
    }


def main(download=False):
    CACHE.mkdir(parents=True, exist_ok=True)
    (DATA / "curves").mkdir(exist_ok=True)
    old_assets = (
        json.loads((DATA / "assets.json").read_text()) if (DATA / "assets.json").exists() else {}
    )
    code_url = "https://raw.githubusercontent.com/pybamm-team/PyBaMM/v25.4.2/src/pybamm/input/parameters/lithium_ion/Prada2013.py"
    code = obtain(
        "Prada2013-v25.4.2.py",
        code_url,
        sha256="9cec4ad9e6afac112b44c5ea4c73ee2c2c0882a7c6fc5398bd789b78617cb052",
        download=download,
    )
    metadata_url = "https://zenodo.org/api/records/20086298/files/metadata.csv/content"
    meta_path = obtain(
        "metadata.csv", metadata_url, md5="daa9d9229c6fbe53cf099ea1a9645a9d", download=download
    )
    metadata = pd.read_csv(meta_path, float_precision="round_trip")
    assets = {
        "pybamm-prada-code": {
            "source_id": "pybamm-25-4-2",
            "filename": code.name,
            "url": code_url,
            "sha256": hashlib.sha256(code.read_bytes()).hexdigest(),
            "license": "BSD-3-Clause",
        },
        "sintef-metadata": {
            "source_id": "sintef-2026-v3",
            "filename": "metadata.csv",
            "url": metadata_url,
            "md5": "daa9d9229c6fbe53cf099ea1a9645a9d",
            "sha256": hashlib.sha256(meta_path.read_bytes()).hexdigest(),
            "license": "CC-BY-4.0",
        },
    }
    sources = {
        "afshar-2017": {
            "kind": "paper",
            "title": "Efficient electrochemical model for lithium-ion cells",
            "authors": ["Sepideh Afshar", "Kirsten Morris", "Amir Khajepour"],
            "year": 2017,
            "url": "https://arxiv.org/abs/1709.03970v1",
            "doi": "10.48550/arXiv.1709.03970",
            "role": "Scientific attribution supplied by the upstream implementation; original equation not independently checked.",
        },
        "chen-2020": {
            "kind": "paper",
            "title": "Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models",
            "authors": [
                "Chang-Hui Chen",
                "Ferran Brosa Planella",
                "Kieran O'Regan",
                "Dominika Gastol",
                "W. Dhammika Widanage",
                "Emma Kendrick",
            ],
            "year": 2020,
            "doi": "10.1149/1945-7111/ab9050",
            "url": "https://doi.org/10.1149/1945-7111/ab9050",
            "role": "Scientific attribution of the LG M50 graphite OCP and non-OCP parameter implementations; individual measurement/fit/borrowing origins not independently audited.",
        },
        "pybamm-25-4-2": {
            "kind": "software",
            "title": "PyBaMM v25.4.2: Prada2013.py and Chen2020.py",
            "authors": ["The PyBaMM team"],
            "year": 2025,
            "url": "https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion",
            "version": "v25.4.2",
            "license": "BSD-3-Clause",
            "role": "Redistributable implementation source. OCPs are borrowed from Afshar2017 and Chen2020, not measured by Prada2013.",
        },
        "sintef-2026-v3": {
            "kind": "dataset",
            "title": "Half-Cell Open-Circuit Voltage of Several Lithium-Ion Battery Active Materials Measured under Various Electrochemical Protocols",
            "authors": [
                "Eibar Flores",
                "Sridevi Krishnamurthi",
                "Killian Stokes-Rodriguez",
                "Julie Cathrine Guldahl",
                "Charifa Hakim",
                "Simon Clark",
                "Nils Peter Wagner",
                "Sergi Obrador",
                "Andrés Bernabeu Santisteban",
            ],
            "year": 2026,
            "doi": "10.5281/zenodo.20086298",
            "url": "https://zenodo.org/records/20086298",
            "version": "v3",
            "license": "CC-BY-4.0",
            "license_evidence": "Zenodo record API metadata.license.id=cc-by-4.0, checked 2026-10-16",
            "role": "Raw measured half-cell time series and electrode metadata.",
        },
    }
    materials = {
        "lfp-afshar-formula": {
            "chemistry": "LFP",
            "description": "LFP formula attributed to Afshar2017 by PyBaMM; material supplier and batch not established.",
        },
        "graphite-chen-lgm50": {
            "chemistry": "graphite",
            "description": "LG M50 negative-electrode effective OCP formula, labeled graphite by upstream; the original commercial electrode contains graphite/SiOx.",
        },
        "lfp-gelon-nmp-1": {
            "chemistry": "LFP",
            "supplier": "Gelon",
            "public_label": "LFP-NMP-1",
            "description": "Commercial LFP electrode tested in laboratory Li-metal half-cells; no commercial full-cell model assigned.",
        },
        "graphite-aq-1": {
            "chemistry": "graphite",
            "public_label": "Gr-AQ-1",
            "description": "Aqueous-processed graphite electrode tested in laboratory Li-metal half-cells.",
        },
    }
    cells = {
        "lg-m50": {
            "manufacturer": "LG",
            "model": "M50",
            "format": "21700",
            "identity_level": "commercial_model_only",
            "source_ids": ["chen-2020"],
            "note": "Linked only to the Chen formula; no full-cell validation is bundled in v0.1.",
        }
    }
    formulas = [
        (
            "lfp-afshar2017-formula",
            "LFP",
            "lfp-afshar-formula",
            "afshar-2017",
            "LFP_ocp_Afshar2017",
            "3.4077 - 0.020269*x + 0.5*exp(-150*x) - 0.9*exp(-30*(1-x))",
            ["exp"],
        ),
        (
            "graphite-chen2020-formula",
            "graphite",
            "graphite-chen-lgm50",
            "chen-2020",
            "graphite_LGM50_ocp_Chen2020",
            "1.9793*exp(-39.3631*x) + 0.2482 - 0.0909*tanh(29.8538*(x-0.1234)) - 0.04478*tanh(14.9159*(x-0.2769)) - 0.0205*tanh(30.4444*(x-0.6103))",
            ["exp", "tanh"],
        ),
    ]
    records = []
    for rid, material, mid, sid, function, formula, functions in formulas:
        r = base_record(rid, material)
        r.update(
            title=f"{material} · {sid} · analytical formula",
            material_id=mid,
            source_ids=[sid, "pybamm-25-4-2"],
            license="BSD-3-Clause",
        )
        r["x"] = {
            "kind": "stoichiometry",
            "symbol": "theta",
            "unit": "1",
            "domain": [0.0, 1.0],
            "definition": "Electrode lithium fraction c_s/c_s,max as defined by the upstream implementation; not whole-cell SOC.",
            "domain_basis": "Mathematical stoichiometry interval; an experimentally validated fitting interval is not established here.",
        }
        r["representation"] = {
            "kind": "expression",
            "expression": formula,
            "functions": functions,
            "source_function": function,
        }
        r["provenance"] = {
            "asset_ids": ["pybamm-prada-code"],
            "derivation": "upstream_formula_transcription",
            "location": f"Prada2013.py::{function}",
            "processing": {
                "changes": "Renamed sto to x; removed numpy namespace. Coefficients unchanged.",
                "script": "scripts/seed_v01.py",
            },
        }
        r["quality"] = {
            "source_review": "upstream_code_checked",
            "axis_status": "upstream_stoichiometry",
            "raw_data": "not_deposited_with_formula",
            "model_status": "ocp_component_only",
            "independent_validation": False,
        }
        r["limitations"] = [
            "No raw experimental points are claimed for this expression.",
            "No separate lithiation/delithiation branch or temperature law is supplied.",
            "Not a complete or independently validated cell parameter set.",
        ]
        if material == "graphite":
            r["cell_link"] = {
                "cell_id": "lg-m50",
                "relationship": "same_model",
                "evidence": "Upstream function docstring identifies LG M50; exact specimen and batch are not established.",
            }
            r["limitations"].append(
                "Effective commercial negative-electrode formula; do not interpret as a universal pure-graphite material law."
            )
        records.append(r)

    experiments = {}
    for aid, filename, md5, material in PINNED:
        url = f"https://zenodo.org/api/records/20086298/files/{filename}/content"
        raw = obtain(
            filename, url, md5=md5, sha256=old_assets.get(aid, {}).get("sha256"), download=download
        )
        assets[aid] = {
            "source_id": "sintef-2026-v3",
            "filename": filename,
            "url": url,
            "md5": md5,
            "sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
            "license": "CC-BY-4.0",
        }
        frame = pd.read_parquet(raw)
        if not np.array_equal(frame.index.to_numpy(), np.arange(len(frame))):
            raise ValueError("Source row labels are not zero-based positions")
        meta = metadata.loc[metadata["BDF names"] == filename].iloc[0]
        if pd.notna(meta["Known Issues"]):
            raise ValueError(
                f"Selected specimen has a known issue requiring manual review: {filename}"
            )
        eid = aid + "-pocv"
        sample_id = aid.split("-")[-1]
        experiments[eid] = {
            "source_id": "sintef-2026-v3",
            "asset_id": aid,
            "sample_id": sample_id,
            "configuration": "active electrode versus lithium metal, laboratory R2032 half-cell",
            "protocol": "p-OCV: C/50 constant current; 8 h rest at upper/lower cutoffs",
            "cycle_selected": 3,
            "cycle_selection_reason": "Fixed third recorded cycle for all four specimens; not selected by fit quality.",
            "temperature_K": None,
            "temperature_description": "Room temperature per source; numeric setpoint not supplied.",
            "electrode_metadata": {
                k: None if pd.isna(v) else v.item() if hasattr(v, "item") else v
                for k, v in meta.items()
            },
            "known_issues": [],
        }
        for step in (2, 4):
            branch = frame.loc[
                (frame["Cycle Count / 1"] == 3) & (frame["Step Index / 1"] == step)
            ].copy()
            if len(branch) < 100 or np.any(np.abs(branch["Current / A"]) < 1e-9):
                raise ValueError("Selected step is not a continuous constant-current branch")
            dv = float(branch["Voltage / V"].iloc[-1] - branch["Voltage / V"].iloc[0])
            direction = "delithiation" if dv > 0 else "lithiation"
            expected_sign = 1 if direction == "delithiation" else -1
            if not np.all(np.sign(branch["Current / A"]) == expected_sign):
                raise ValueError(
                    "Current sign and voltage direction disagree for Li-metal half-cell"
                )
            before = len(branch)
            branch = branch.drop_duplicates("Cumulative Capacity / Ah", keep="first")
            q = branch["Cumulative Capacity / Ah"].to_numpy()
            if not np.all(np.diff(q) > 0):
                raise ValueError("Source branch capacity is not strictly increasing")
            x = (q - q[0]) / (q[-1] - q[0])
            rid = f"{aid}-c3-{direction}"
            path = DATA / "curves" / f"{rid}.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(
                    ["x", "potential_V", "capacity_Ah", "test_time_s", "current_A", "source_row"]
                )
                for i, (_, row) in enumerate(branch.iterrows()):
                    writer.writerow(
                        [
                            repr(float(x[i])),
                            repr(float(row["Voltage / V"])),
                            repr(float(row["Cumulative Capacity / Ah"])),
                            repr(float(row["Test Time / s"])),
                            repr(float(row["Current / A"])),
                            int(branch.index[i]),
                        ]
                    )
            r = base_record(rid, material)
            r.update(
                title=f"{material} · SINTEF {sample_id} · cycle 3 · {direction}",
                material_id="lfp-gelon-nmp-1" if material == "LFP" else "graphite-aq-1",
                direction=direction,
                measurement="pseudo_ocp",
                experiment_id=eid,
                source_ids=["sintef-2026-v3"],
                license="CC-BY-4.0",
            )
            r["temperature"] = {
                "value_K": None,
                "description": "Room temperature (source); numeric setpoint unavailable.",
            }
            r["x"] = {
                "kind": "normalized_branch_capacity",
                "symbol": "q_branch",
                "unit": "1",
                "domain": [0.0, 1.0],
                "definition": "(Q - Q_first)/(Q_last - Q_first), from first to last retained point of this branch. Increases with passed capacity in BOTH directions. Not absolute stoichiometry or whole-cell SOC.",
                "domain_basis": "Measured branch endpoints, independently normalized for each specimen and direction.",
            }
            r["representation"] = {
                "kind": "table",
                "path": f"curves/{rid}.csv",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "point_count": len(branch),
                "default_interpolation": "linear",
            }
            r["provenance"] = {
                "asset_ids": [aid, "sintef-metadata"],
                "derivation": "constant_current_branch_extraction",
                "location": f"cycle=3; step={step}; source_row is zero-based row position in Parquet",
                "processing": {
                    "script": "scripts/seed_v01.py",
                    "cycle": 3,
                    "step": step,
                    "input_branch_points": before,
                    "retained_points": len(branch),
                    "duplicate_capacity_points_removed": before - len(branch),
                    "capacity_first_Ah": float(q[0]),
                    "capacity_last_Ah": float(q[-1]),
                    "mean_current_A": math.fsum(branch["Current / A"]) / len(branch),
                    "direction_rule": "Li-metal half-cell: positive current and increasing working-electrode potential = delithiation; negative current and decreasing potential = lithiation; verified for this branch.",
                    "smoothing": "none",
                    "resampling": "none",
                    "potential_changes": "none; native source floating-point values preserved",
                    "rest_steps": "excluded; these are finite-current pseudo-OCP points, not GITT equilibrium points",
                },
            }
            r["quality"] = {
                "source_review": "raw_file_checked",
                "axis_status": "relative_capacity_only",
                "raw_data": "external_checksum_pinned",
                "model_status": "requires_stoichiometry_mapping",
                "independent_validation": False,
            }
            r["limitations"] = [
                "C/50 pseudo-OCP retains finite-current polarization; not a claimed equilibrium OCP.",
                "Absolute stoichiometric endpoints are unknown and require external balancing evidence.",
                "Each branch is normalized separately; branch endpoints are not assumed to represent identical lithium fractions.",
                "Two specimens and their branches are replicates from ONE dataset, not independent literature sources.",
                "No commercial full-cell identity or full-cell model validation is established.",
            ]
            records.append(r)

    write_json("catalog.json", {"schema_version": "0.1", "release": "0.1.0", "records": records})
    for name, value in [
        ("sources.json", sources),
        ("materials.json", materials),
        ("cells.json", cells),
        ("experiments.json", experiments),
        ("assets.json", assets),
    ]:
        write_json(name, value)
    print(
        f"Seeded {len(records)} curves from 3 scientific sources + 1 software distribution; 4 measured specimens."
    )
    from seed_lgm50 import extend

    extend(download=download)
    from seed_lfp import extend as extend_lfp

    extend_lfp(download=download)
    from seed_materials import extend as extend_materials

    extend_materials(download=download)
    from seed_fullcell import extend as extend_fullcell

    extend_fullcell(download=download)
    from seed_mohtat import extend as extend_mohtat

    extend_mohtat()
    from seed_lfp_studies import extend as extend_lfp_studies

    extend_lfp_studies(download=download)
    from seed_hallemans import extend as extend_hallemans

    extend_hallemans(download=download)
    from seed_mj1 import extend as extend_mj1

    extend_mj1(download=download)

    from seed_parameter_sources import extend as extend_parameter_sources

    extend_parameter_sources()

    # The manually reviewed external-link registry is committed metadata. It is
    # never fetched here; reconstructing observations must not download its payloads.
    from ebp import __version__

    document = json.loads((DATA / "catalog.json").read_text())
    document["release"] = __version__
    write_json("catalog.json", document)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    main(parser.parse_args().download)
