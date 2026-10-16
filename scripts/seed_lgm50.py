"""Extend the OCP seed with non-OCP parameters and linked full-cell experiments."""

import ast
import csv
import hashlib
import json
import math
import re
import shutil

import numpy as np
import pandas as pd

from seed_v01 import CACHE, DATA, obtain, write_json

KEYS = {
    "geometry": [
        "Negative current collector thickness [m]",
        "Negative electrode thickness [m]",
        "Separator thickness [m]",
        "Positive electrode thickness [m]",
        "Positive current collector thickness [m]",
        "Electrode height [m]",
        "Electrode width [m]",
        "Cell volume [m3]",
        "Cell cooling surface area [m2]",
    ],
    "electrode": [
        f"{side} {suffix}"
        for side in ["Negative", "Positive"]
        for suffix in [
            "electrode porosity",
            "electrode active material volume fraction",
            "particle radius [m]",
            "electrode conductivity [S.m-1]",
            "particle diffusivity [m2.s-1]",
        ]
    ]
    + [
        "Maximum concentration in negative electrode [mol.m-3]",
        "Maximum concentration in positive electrode [mol.m-3]",
    ],
    "thermal": [
        f"{side} {suffix}"
        for side in ["Negative electrode", "Positive electrode", "Separator"]
        for suffix in [
            "density [kg.m-3]",
            "specific heat capacity [J.kg-1.K-1]",
            "thermal conductivity [W.m-1.K-1]",
        ]
    ],
    "operating_limits": [
        "Nominal cell capacity [A.h]",
        "Lower voltage cut-off [V]",
        "Upper voltage cut-off [V]",
    ],
    "initial_state": [
        "Initial concentration in electrolyte [mol.m-3]",
        "Initial concentration in negative electrode [mol.m-3]",
        "Initial concentration in positive electrode [mol.m-3]",
    ],
}


def extend(download=False):
    load = lambda name: json.loads((DATA / name).read_text())
    sources, assets, cells = load("sources.json"), load("assets.json"), load("cells.json")
    url = "https://raw.githubusercontent.com/pybamm-team/PyBaMM/v25.4.2/src/pybamm/input/parameters/lithium_ion/Chen2020.py"
    code = obtain(
        "Chen2020-v25.4.2.py",
        url,
        sha256="eb6a13879cad6ae1bc86d222ce5189f3e3edb400e23f69331779b8aae2437906",
        download=download,
    )
    assets["pybamm-chen-code"] = {
        "source_id": "pybamm-25-4-2",
        "filename": code.name,
        "url": url,
        "sha256": hashlib.sha256(code.read_bytes()).hexdigest(),
        "license": "BSD-3-Clause",
    }
    # Read numeric literals from the return dictionary, without executing upstream code.
    module = ast.parse(code.read_text())
    function = next(
        node
        for node in module.body
        if isinstance(node, ast.FunctionDef) and node.name == "get_parameter_values"
    )
    returned = next(node.value for node in function.body if isinstance(node, ast.Return))
    scalars = {
        ast.literal_eval(k): ast.literal_eval(v)
        for k, v in zip(returned.keys, returned.values)
        if isinstance(v, ast.Constant) and type(v.value) in (int, float)
    }
    parameters = []
    for category, keys in KEYS.items():
        for key in keys:
            rid = "lgm50-" + re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
            unit = key.split("[")[1].rstrip("]") if "[" in key else "1"
            parameters.append(
                {
                    "id": rid,
                    "version": "1",
                    "cell_id": "lg-m50",
                    "category": category,
                    "name": key,
                    "unit": unit,
                    "representation": {"kind": "scalar", "value": scalars[key]},
                    "source_ids": ["chen-2020", "pybamm-25-4-2"],
                    "provenance": {
                        "asset_id": "pybamm-chen-code",
                        "location": "Chen2020.py::get_parameter_values::" + key,
                        "origin_status": "upstream_implementation_value; individual measurement/fit/borrowing origin not independently audited",
                    },
                    "license": "BSD-3-Clause",
                    "independent_validation": False,
                    "limitations": [
                        "Same-model literature implementation value, not a newly measured parameter.",
                        "Do not assume all values in a named parameter set were directly measured on one specimen.",
                        "This record alone does not form a complete model parameterization.",
                    ],
                }
            )
    for side, function, prefactor, activation in [
        (
            "negative",
            "graphite_LGM50_electrolyte_exchange_current_density_Chen2020",
            "6.48e-7",
            "35000",
        ),
        ("positive", "nmc_LGM50_electrolyte_exchange_current_density_Chen2020", "3.42e-6", "17800"),
    ]:
        parameters.append(
            {
                "id": f"lgm50-{side}-exchange-current-density",
                "version": "1",
                "cell_id": "lg-m50",
                "category": "kinetics",
                "name": f"{side.capitalize()} electrode exchange-current density [A.m-2]",
                "unit": "A.m-2",
                "representation": {
                    "kind": "expression",
                    "expression": f"{prefactor}*exp({activation}/8.314462618*(1/298.15-1/T))*c_e**0.5*c_s_surf**0.5*(c_s_max-c_s_surf)**0.5",
                    "variables": {
                        "c_e": "mol.m-3",
                        "c_s_surf": "mol.m-3",
                        "c_s_max": "mol.m-3",
                        "T": "K",
                    },
                    "domain": "Mathematical domain: c_e>=0, c_s_max>0, 0<=c_s_surf<=c_s_max, T>0. Experimental validity range not established here.",
                    "gas_constant_J_mol_K": 8.314462618,
                },
                "source_ids": ["chen-2020", "pybamm-25-4-2"],
                "provenance": {
                    "asset_id": "pybamm-chen-code",
                    "location": "Chen2020.py::" + function,
                    "origin_status": "upstream_implementation_function; original equation not independently audited",
                },
                "license": "BSD-3-Clause",
                "independent_validation": False,
                "limitations": [
                    "Exchange-current density law, not an interchangeable reaction-rate constant.",
                    "Uses the upstream concentration dependence and area convention; inspect the original model before transferring.",
                    "Gas constant fixed to 8.314462618 J/mol/K for portable numerical evaluation.",
                    "Mathematical input checks do not establish an experimentally validated temperature range.",
                ],
            }
        )
    write_json("parameters.json", {"schema_version": "0.1", "records": parameters})
    sources["chen-validation-2020"] = {
        "kind": "dataset",
        "title": 'Experimental data for "Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models"',
        "authors": sources["chen-2020"]["authors"],
        "year": 2020,
        "doi": "10.5281/zenodo.4032561",
        "url": "https://zenodo.org/records/4032561",
        "version": "v1",
        "license": "CC-BY-4.0",
        "license_evidence": "Zenodo API metadata.license.id=cc-by-4.0, checked 2026-10-16",
        "role": "Full-cell validation tests published alongside Chen2020; not proof of identical specimen to the dissected characterization cell.",
    }
    tests = []
    (DATA / "full_cell").mkdir(exist_ok=True)
    for n, md5 in [
        ("02", "0bbf959cbfc367296ec69d7a74d2f5c1"),
        ("03", "a09cbd8eff0af55dfe9bc8728fa89908"),
        ("04", "f17615476283d2e15087165697ff9d7c"),
    ]:
        filename = f"LGM50_cell{n}.csv"
        url = f"https://zenodo.org/api/records/4032561/files/{filename}/content"
        raw = obtain(filename, url, md5=md5, download=download)
        aid = f"chen-lgm50-cell{n}"
        assets[aid] = {
            "source_id": "chen-validation-2020",
            "filename": filename,
            "url": url,
            "md5": md5,
            "sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
            "license": "CC-BY-4.0",
        }
        # Distributed originals remain byte-identical to the deposited CSV files.
        shutil.copyfile(raw, DATA / "full_cell" / filename)
        frame = pd.read_csv(raw, skiprows=13, float_precision="round_trip")
        required = [
            "Rec",
            "Step",
            "Cycle C",
            "Test Time [s]",
            "Current [A]",
            "Voltage [V]",
            "Md",
            "Temperature Cell [degC]",
            "Temperature Chamber [degC]",
        ]
        if not set(required).issubset(frame.columns) or not np.all(
            np.diff(frame["Test Time [s]"]) >= 0
        ):
            raise ValueError("Unexpected Maccor CSV structure or time order")
        normalized = DATA / "full_cell" / f"LGM50_cell{n}-normalized.csv"
        with normalized.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "time_s",
                    "current_charge_positive_A",
                    "voltage_V",
                    "cell_temperature_K",
                    "ambient_temperature_K",
                    "cycle",
                    "step",
                    "mode",
                    "source_record",
                    "source_file_row",
                ]
            )
            for i, row in frame.iterrows():
                mode = row["Md"]
                magnitude = float(row["Current [A]"])
                if magnitude < 0 or (mode not in ("C", "D") and magnitude != 0):
                    raise ValueError("Unrecognized Maccor current sign/mode combination")
                current = magnitude if mode == "C" else -magnitude if mode == "D" else 0.0
                writer.writerow(
                    [
                        repr(float(row["Test Time [s]"])),
                        repr(current),
                        repr(float(row["Voltage [V]"])),
                        repr(float(row["Temperature Cell [degC]"]) + 273.15),
                        repr(float(row["Temperature Chamber [degC]"]) + 273.15),
                        int(row["Cycle C"]),
                        int(row["Step"]),
                        mode,
                        int(row["Rec"]),
                        int(i) + 14,
                    ]
                )
        segments = []
        for step, group in frame[frame["Md"] == "D"].groupby("Step", sort=True):
            segments.append(
                {
                    "step": int(step),
                    "mean_discharge_current_A": math.fsum(group["Current [A]"]) / len(group),
                    "nominal_C_rate": round(math.fsum(group["Current [A]"]) / len(group) / 5, 2),
                    "initial_preconditioning": int(step) == 2,
                    "points": len(group),
                }
            )
        tests.append(
            {
                "id": aid,
                "cell_id": "lg-m50",
                "sample_id": f"cell{n}",
                "asset_id": aid,
                "source_id": "chen-validation-2020",
                "path": f"full_cell/{filename}",
                "normalized_path": f"full_cell/{normalized.name}",
                "normalized_sha256": hashlib.sha256(normalized.read_bytes()).hexdigest(),
                "current_convention": "normalized: positive=charge, negative=discharge; source current is unsigned magnitude interpreted using Md=C/D",
                "processing": "Original copied byte-for-byte. Normalized: skip 13 instrument banner lines; derive current sign from Md; temperatures degC+273.15; preserve source record and zero-based source file row; no smoothing or resampling.",
                "license": "CC-BY-4.0",
                "protocol": "CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description)",
                "relationship_to_parameters": "same_model_same_study",
                "evidence": "Dataset is explicitly supplementary validation data for Chen et al. 2020; LG M50 model and individual test sample IDs are given. Exact link to a dissected electrode specimen is not established.",
                "independent_validation_by_this_project": False,
                "row_count": len(frame),
                "columns": frame.columns.tolist(),
                "discharge_segments": segments,
                "format": "original CSV + explicitly normalized CSV",
            }
        )
    write_json("full_cell_tests.json", {"schema_version": "0.1", "records": tests})
    cells["lg-m50"]["parameter_ids"] = [p["id"] for p in parameters]
    cells["lg-m50"]["full_cell_test_ids"] = [t["id"] for t in tests]
    cells["lg-m50"]["ocp_record_ids"] = ["graphite-chen2020-formula"]
    cells["lg-m50"][
        "note"
    ] = "Parameters and full-cell tests are linked at same-model/same-study level. No exact characterization-specimen match or independently reproduced full-cell fit is claimed. This is an intentionally partial parameter collection."
    for name, value in [("sources.json", sources), ("assets.json", assets), ("cells.json", cells)]:
        write_json(name, value)
    print(
        f"Linked LG M50: {len(parameters)} non-OCP parameters and {len(tests)} original full-cell test files."
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    extend(parser.parse_args().download)
