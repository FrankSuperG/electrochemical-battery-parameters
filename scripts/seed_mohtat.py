"""Curate capacity-coordinate charging observations from the official author deposit.

Original bytes are committed because automated Deep Blue clients receive 403.
No MATLAB is executed. Missing time/current channels are never reconstructed.
"""

import copy
import csv
import hashlib
import json
import re

import numpy as np
from scipy.io import loadmat

from seed_v01 import DATA, ROOT, write_json
from seed_materials import ocp_record
from seed_fullcell import audit_links, write_csv

CID = "mohtat2020-nmc532-pouch"
SID = "mohtat-2020-data"
SCRIPT = "scripts/seed_mohtat.py"


def extend():
    load = lambda name: json.loads((DATA / name).read_text())
    doc, parameters, tests = (
        load("catalog.json"),
        load("parameters.json")["records"],
        load("full_cell_tests.json")["records"],
    )
    assets, sources, cells, materials = (
        load("assets.json"),
        load("sources.json"),
        load("cells.json"),
        load("materials.json"),
    )
    pins = json.loads((ROOT / "scripts/mohtat_assets.json").read_text())
    for aid, asset in pins.items():
        assert (
            hashlib.sha256((DATA / asset["path"]).read_bytes()).hexdigest()
            == asset["sha256"]
        ), aid
        assets[aid] = asset
    doc["records"] = [
        r for r in doc["records"] if not r["id"].startswith("mohtat-author-")
    ]
    parameters = [p for p in parameters if not p["id"].startswith("mohtat-author-")]
    tests = [t for t in tests if not t["id"].startswith("mohtat-charge-")]
    main_id = "mohtat2020-main-m"
    code = (DATA / pins[main_id]["path"]).read_text(encoding="cp1252")
    literals = dict(
        re.findall(
            r"^\s*CC\.(\w+)\s*=\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*;",
            code,
            re.M,
        )
    )
    values = {key: float(value) for key, value in literals.items()}
    windows = {
        key: float(value)
        for key, value in re.findall(
            r"^\s*(x0_percent_n|x100_percent_n|y0_percent_p|y100_percent_p)\s*=\s*([.\d]+)\s*;",
            code,
            re.M,
        )
    }
    evidence = "Original author model is bundled with these five experimental charging files in the same DOI deposit. Cell is fabricated by UMBL, not an identified commercial part. Exact specimen identity is not given."
    for role, material, key, variable, bounds in [
        (
            "negative",
            "graphite",
            "Un_0",
            "x",
            [windows["x0_percent_n"], windows["x100_percent_n"]],
        ),
        (
            "positive",
            "NMC532",
            "Up_0",
            "y",
            [windows["y100_percent_p"], windows["y0_percent_p"]],
        ),
    ]:
        matlab = re.search(
            r"CC\." + key + r"\s*=\s*@\(" + variable + r"\)\s*(.*?);", code, re.S
        ).group(1)
        expression = re.sub(
            r"\b" + variable + r"\b",
            "x",
            matlab.replace("...", "").replace(".^", "**").replace("^", "**"),
        )
        expression = " ".join(expression.split())
        record, meta = ocp_record(
            "mohtat-author-" + material.lower() + "-ocp",
            material,
            role,
            expression,
            "main.m::CC." + key,
            main_id,
            [SID, "mohtat-2020"],
            CID,
            "same_parameter_set",
            evidence,
            "original_author_matlab_expression_transcription",
        )
        record["license"] = "CC-BY-4.0"
        record["title"] = material + " | Mohtat2020 original author model | " + key
        record["x"]["domain"] = bounds
        record["x"][
            "domain_basis"
        ] = "Author's full-cell balancing endpoints in main.m; source expression retained. Not a claim of independent electrode characterization."
        record["provenance"]["processing"] = {
            "script": SCRIPT,
            "changes": "MATLAB continuation and element-wise powers transcribed to the restricted expression language; source coefficients unchanged; no MATLAB executed.",
        }
        record["limitations"] = [
            evidence,
            "NMC532 label is stated in the pinned PyBaMM implementation; the deposited model/README use NMC without an independent composition assay.",
            "Original graphite expression uses x+0.007. PyBaMM v25.4.2 uses x+0.001. These are distinct implementation variants; do not mix their OCPs silently.",
        ]
        doc["records"].append(record)
        materials[record["material_id"]] = meta
    selected = {
        "Ds_n": ("diffusion", "Negative particle diffusivity", "m2.s-1"),
        "Ds_p": ("diffusion", "Positive particle diffusivity", "m2.s-1"),
        "k0_n": (
            "kinetics",
            "Negative reaction-rate coefficient k0",
            "mol.m-2.s-1.(mol.m-3)^-1.5",
        ),
        "k0_p": (
            "kinetics",
            "Positive reaction-rate coefficient k0",
            "mol.m-2.s-1.(mol.m-3)^-1.5",
        ),
        "cs_max_n": ("electrode", "Negative maximum concentration", "mol.m-3"),
        "cs_max_p": ("electrode", "Positive maximum concentration", "mol.m-3"),
        "es_n": ("electrode", "Negative active material fraction", "1"),
        "es_p": ("electrode", "Positive active material fraction", "1"),
        "del_n": ("geometry", "Negative electrode thickness", "m"),
        "del_s": ("geometry", "Separator thickness", "m"),
        "del_p": ("geometry", "Positive electrode thickness", "m"),
        "epsilon_e_n": ("electrode", "Negative electrolyte porosity", "1"),
        "epsilon_e_s": ("electrode", "Separator electrolyte porosity", "1"),
        "epsilon_e_p": ("electrode", "Positive electrolyte porosity", "1"),
        "A": ("geometry", "Electrode area in original author model", "m2"),
        "ce_init": ("initial_state", "Initial electrolyte concentration", "mol.m-3"),
        "kappa": ("transport", "Electrolyte ionic conductivity", "S.m-1"),
        "D_e": ("transport", "Electrolyte diffusivity", "m2.s-1"),
        "t_plus": ("transport", "Cation transference number", "1"),
        "rho": ("thermal", "Lumped cell density", "kg.m-3"),
        "Cp": ("thermal", "Lumped cell specific heat capacity", "J.kg-1.K-1"),
        "h": ("thermal", "Lumped convective heat-transfer coefficient", "W.m-2.K-1"),
    }
    for key in ["Rn_0", "Rn_1", "Rn_2", "Rn_3", "Rn_4", "Rp_0"]:
        selected[key] = (
            "electrode",
            key + " particle radius in author multiparticle model",
            "m",
        )
    for i in range(5):
        selected["zeta_n_" + str(i)] = (
            "electrode",
            "Negative particle population fraction " + str(i),
            "1",
        )
    for key, (category, name, unit) in selected.items():
        assert key in values, key
        parameters.append(
            {
                "id": "mohtat-author-" + key.lower().replace("_", "-"),
                "version": "1",
                "cell_id": CID,
                "category": category,
                "name": name,
                "unit": unit,
                "representation": {"kind": "scalar", "value": values[key]},
                "source_ids": [SID, "mohtat-2020"],
                "provenance": {
                    "asset_id": main_id,
                    "location": "main.m::CC." + key,
                    "origin_status": "original_author_model_input; individual measurement/fit/assumption origin not fully audited",
                },
                "license": "CC-BY-4.0",
                "independent_validation": False,
                "conditions": {
                    "parameterization_variant": "original_author_mpm",
                    "reference_temperature_K": 298.15,
                },
                "definition": (
                    "Source DAE uses i0=F*k0*sqrt(c_e)*c_s,max*sqrt(theta*(1-theta)); unit follows this equation. Source inline k0 unit comment is incomplete. Not interchangeable with exchange-current density."
                    if key.startswith("k0")
                    else name
                ),
                "limitations": [
                    evidence,
                    "Partial author-model inputs, not a complete validated drop-in DFN/SPM/SPMe set. Multiparticle radii and fractions are distinct inputs; no effective radius is inferred.",
                    "Source uses constant D and k0; PyBaMM adds temperature-dependent laws. Same study does not mean identical implementation.",
                ],
            }
        )
    for record in doc["records"]:
        if record["cell_link"]["cell_id"] == CID and not record["id"].startswith(
            "mohtat-author-"
        ):
            record["cell_link"][
                "evidence"
            ] = "Same Mohtat2020 study design as the retrieved author deposit; this PyBaMM variant differs from the bundled original model. Exact specimen correspondence and raw half-cell points are unresolved."
            note = "v0.5: official UMBL research-pouch charging exports retrieved. NMC532 is an implementation label; the deposit does not establish a commercial model or composition assay. Author graphite offset differs."
            if note not in record["limitations"]:
                record["limitations"].append(note)
    for p in parameters:
        if p["cell_id"] == CID and not p["id"].startswith("mohtat-author-"):
            p.setdefault("conditions", {})[
                "parameterization_variant"
            ] = "pybamm_v25_4_2"
    readme_id = "mohtat2020-read-me-pdf"
    plot_id = "mohtat2020-plot-data-only-m"
    for filename, rate, current in [
        ("Cover10.mat", 0.1, 0.5),
        ("Cover5.mat", 0.2, 1),
        ("Cover2.mat", 0.5, 2.5),
        ("Cover1.mat", 1, 5),
        ("2C.mat", 2, 10),
    ]:
        aid = next(a for a, p in pins.items() if p["filename"] == filename)
        source = loadmat(DATA / pins[aid]["path"], simplify_cells=True)
        q, v, t = (
            np.asarray(source[k], dtype=float)
            for k in ["Q_data", "Vt_data", "Temp_data"]
        )
        assert (
            q.shape == v.shape == t.shape
            and np.isfinite([q, v, t]).all()
            and np.all(np.diff(q) >= 0)
        )
        tid = "mohtat-charge-" + str(rate).replace(".", "p") + "c"
        relative = "full_cell/" + tid + "-normalized.csv"
        cols = [
            "time_s",
            "charge_capacity_Ah",
            "current_charge_positive_A",
            "voltage_V",
            "cell_temperature_K",
            "ambient_temperature_K",
            "cycle",
            "step",
            "mode",
            "source_record",
        ]
        rows = [
            [
                "",
                repr(float(qi)),
                "",
                repr(float(vi)),
                repr(float(ti + 273.15)),
                "",
                "",
                "",
                "C",
                i + 1,
            ]
            for i, (qi, vi, ti) in enumerate(zip(q, v, t))
        ]
        checksum = write_csv(relative, cols, rows)
        issues = [
            "No measured current or original timestamps in the deposited MAT arrays.",
            "README states 10 s acquisition, but the exported arrays contain no timestamps. No 10 s or Q/I time reconstruction is applied.",
            "Only charging files are deposited. C/20, discharge, complete CV/rest and original cycler records are not separately supplied.",
        ]
        if filename == "Cover2.mat":
            issues.append(
                "README Methods says C/2.5, while its inventory says C/2 and main.m assigns -2.5 A to Cover2. This record uses nominal 0.5C / 2.5 A per inventory and code; actual current trace is unavailable."
            )
        tests.append(
            {
                "id": tid,
                "cell_id": CID,
                "sample_id": "not_disclosed",
                "asset_id": aid,
                "source_id": SID,
                "scientific_source_ids": ["mohtat-2020"],
                "path": None,
                "original_download_path": pins[aid]["path"],
                "original_format": "MAT",
                "normalized_path": relative,
                "normalized_sha256": checksum,
                "format": "capacity_voltage_temperature; original current and time not exported",
                "license": "CC-BY-4.0",
                "row_count": len(q),
                "columns": cols,
                "discharge_segments": [],
                "protocol": f"Nominal {rate:g}C charge to 4.2 V; capacity-coordinate experimental export",
                "relationship_to_parameters": "same_study_cell_family",
                "evidence": evidence,
                "observation_kind": "published_experimental_series",
                "independent_validation_by_this_project": False,
                "independent_variable": {
                    "column": "charge_capacity_Ah",
                    "unit": "Ah",
                    "label": "Charge capacity / Ah",
                    "definition": "Q_data paired with Vt_data and Temp_data in the source MAT; not whole-cell SOC or inferred time.",
                },
                "basic_test": {
                    "type": "constant_current_charge",
                    "nominal_C_rate": rate,
                    "nominal_current_charge_positive_A": current,
                    "current_measurement": "not_supplied; current magnitude is protocol metadata from main.m",
                    "charge_trace": "available",
                    "discharge_trace": "not_supplied",
                    "voltage_trace": "available",
                    "reported_sampling_interval_s": 10,
                    "sampling_interval_applied_to_time": False,
                    "protocol_temperature_K": 298.15,
                },
                "current_convention": "Charge-positive convention; measured current column stays empty. main.m uses negative current for charging, only retained as protocol provenance.",
                "temperature_definition": "Source Temp_data is cell surface temperature in degC per Plot_data_only.m; converted to kelvin without the movmean smoothing used by main.m.",
                "missing_values": {
                    "time_s": len(q),
                    "current_charge_positive_A": len(q),
                    "ambient_temperature_K": len(q),
                    "voltage_V": 0,
                    "cell_temperature_K": 0,
                },
                "missing_items": [
                    "Measured current trace",
                    "Original timestamps",
                    "Discharge trace",
                    "Full CV/rest trace",
                    "C/20 OCV test",
                    "Exact specimen identifier",
                    "Original half-cell OCP points",
                ],
                "source_issues": issues,
                "source_variable_mapping": {
                    "charge_capacity_Ah": "Q_data",
                    "voltage_V": "Vt_data",
                    "cell_temperature_K": "Temp_data+273.15",
                },
                "supporting_asset_ids": [
                    main_id,
                    readme_id,
                    plot_id,
                    "mohtat2020-battery-mpm-electrolyte-dae-m",
                    "mohtat2020-daeeventsfcn-m",
                ],
                "processing": {
                    "script": SCRIPT,
                    "changes": "All Q/V/T source rows retained, no smoothing/resampling. No timestamps, current or phase markers invented. Mode C is protocol-derived. Other expansion/derivative arrays remain in the original MAT.",
                },
            }
        )
    cell = cells[CID]
    cell.update(
        manufacturer="University of Michigan Battery Lab",
        model=None,
        identity_level="study_defined_laboratory_cell; commercial_part_not_applicable",
        display_name="UMBL Mohtat2020 | 5 Ah NMC/graphite research pouch",
        match_level="same_study_cell_family",
        match_evidence=evidence,
        model_context="Author MPMe model and PyBaMM Mohtat2020 variant; selectable parameter origins",
        note="Custom laboratory pouch. NMC532 label follows the PyBaMM implementation, not a composition assay in this deposit. Author and PyBaMM graphite OCP offsets, thermal geometry and temperature laws differ. Capacity-axis charge files have measured voltage/temperature but no exported current/time. Source Cover2 rate description conflicts are retained.",
    )
    cell["coverage"] = {
        "ocp": "Two original author OCP expressions plus two PyBaMM variants; graphite x-offset differs (0.007 versus 0.001). Raw half-cell points absent.",
        "diffusion": "Original author D_n=5e-15 and D_p=8e-15 m2/s; PyBaMM same reference values with added Arrhenius dependence.",
        "kinetics": "Original k0_n=1.1e-11 and k0_p=5e-11 with source i0 definition; PyBaMM exchange-current prefactors are rounded/unit-converted and have added temperature dependence.",
        "full_cell_tests": "Five original charging MAT files, 0.1/0.2/0.5/1/2C by code/inventory. Measured voltage and temperature versus capacity; current, timestamps, discharge and C/20 files absent.",
    }
    sources[SID][
        "role"
    ] = "Official author dataset downloaded through the normal browser on 2026-10-16. Five experimental charging MATs, four MATLAB model/plot files and README reviewed. Earlier automated HTTP 403 was an access-method failure. Packaged originals retain hashes and CC BY 4.0."
    sources[SID][
        "url"
    ] = "https://deepblue.lib.umich.edu/data/concern/data_sets/kp78gg60j"
    sources["mohtat-2020"][
        "role"
    ] = "Same-study electrochemical/mechanical model and charging observations. Original author-code and PyBaMM implementation variants are distinguished; exact specimen and raw OCP/current/time exports remain unresolved."
    audit_links(cells, doc["records"], parameters, tests)
    for test in tests:
        if test["cell_id"] == CID:
            test["channel_availability"]["time_s"] = {
                "present_rows": 0,
                "total_rows": test["row_count"],
            }
    cell["missing_items"] = [
        "Exact specimen identifier",
        "Measured current trace",
        "Original timestamps",
        "Discharge/CV/rest and C/20 files",
        "Raw electrode OCP points",
        "Independent full-cell model reproduction",
    ]
    for comp in cell["evidence_matrix"].values():
        comp["missing_items"] += [
            "Author and PyBaMM variants require explicit selection; not identical parameterizations"
        ]
    crosswalk = {
        "cell_id": CID,
        "author_asset_id": main_id,
        "pybamm_asset_id": "pybamm-mohtat2020-code",
        "same_study": True,
        "identical_parameterization": False,
        "differences": [
            {
                "component": "graphite_ocp",
                "author": "exp(-75*(x+0.007))",
                "pybamm": "exp(-75*(x+0.001))",
                "status": "different",
            },
            {"component": "positive_ocp", "status": "same_coefficients"},
            {
                "component": "particle_diffusion",
                "author_reference_m2_s": [5e-15, 8e-15],
                "status": "same_reference_values; PyBaMM temperature extension absent from author code",
            },
            {
                "component": "kinetics",
                "author_k0": [1.1e-11, 5e-11],
                "author_F_C_mol": values["F"],
                "pybamm_i0_prefactors": [1.061e-6, 4.824e-6],
                "status": "unit conversion with rounding and PyBaMM temperature extension",
            },
            {
                "component": "thermal_geometry",
                "status": "different; author cell dimensions/outer cooling area must not be replaced by PyBaMM model geometry silently",
            },
        ],
        "source_review": "main.m, Battery_MPM_Electrolyte_DAE.m, Plot_data_only.m, README; no upstream code executed",
    }
    cell["parameter_crosswalk"] = crosswalk
    write_json("evidence/mohtat2020-parameter-crosswalk.json", crosswalk)
    audit = load("matching_audit.json")
    audit["cell_matches"][CID] = {
        "display_name": cell["display_name"],
        "match_level": cell["match_level"],
        "components": cell["evidence_matrix"],
        "missing_items": cell["missing_items"],
    }
    audit["research_leads"] = [
        {
            "source_id": SID,
            "cell_id": CID,
            "status": "official_files_imported; partial_channels_only",
            "doi": "10.7302/wwma-hx25",
            "access_result": "Normal browser downloaded official ZIP. Earlier automated 403 does not imply dataset unavailability.",
            "missing_items": cell["missing_items"],
        }
    ]
    rejection = "Mohtat2021 cyclic-aging dataset is a different study; not silently substituted for the Mohtat2020 charging deposit."
    if rejection not in audit["rejected_joins"]:
        audit["rejected_joins"].append(rejection)
    doc["release"] = "0.5.0"
    for filename, value in [
        ("catalog.json", doc),
        ("parameters.json", {"schema_version": "0.1", "records": parameters}),
        ("full_cell_tests.json", {"schema_version": "0.1", "records": tests}),
        ("assets.json", assets),
        ("sources.json", sources),
        ("cells.json", cells),
        ("materials.json", materials),
        ("matching_audit.json", audit),
    ]:
        write_json(filename, value)
    print(
        f"Mohtat author deposit: 5 charge files / 6474 paired Q/V/T rows; {len(doc['records'])} OCPs, {len(parameters)} parameters, {len(tests)} test files."
    )


if __name__ == "__main__":
    extend()
