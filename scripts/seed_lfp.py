"""LFP expansion: pinned BPX examples and model-linked Oxford experiments.

Reuses the v0.1 reconstruction helpers. Downloaded MAT/ZIP originals remain in
.cache; normalized observations, provenance, and source metadata are distributed.
"""

import copy
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path

import numpy as np
from scipy.io import loadmat

from seed_v01 import CACHE, DATA, ROOT, base_record, obtain, write_json


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parameter(
    rid,
    cell,
    name,
    category,
    value,
    unit,
    source_ids,
    asset_id,
    location,
    status,
    conditions=None,
    limitations=None,
    license="CC-BY-4.0",
    definition=None,
):
    return {
        "id": rid,
        "version": "1",
        "cell_id": cell,
        "name": name,
        "category": category,
        "unit": unit,
        "representation": {"kind": "scalar", "value": float(value)},
        "source_ids": source_ids,
        "provenance": {
            "asset_id": asset_id,
            "location": location,
            "origin_status": status,
        },
        "conditions": conditions or {},
        "definition": definition or name,
        "license": license,
        "independent_validation": False,
        "limitations": limitations
        or [
            "A model-specific parameter; transferability to another cell or formulation is not established."
        ],
    }


def normalized_test(
    rid,
    cell_id,
    sample_id,
    asset_id,
    source_id,
    time,
    current,
    voltage,
    temperature,
    protocol,
    nominal_rate,
    sample_evidence,
    original_member=None,
    temperature_definition="not supplied",
    license="CC-BY-4.0",
):
    arrays = [np.asarray(v, dtype=float).reshape(-1) for v in [time, current, voltage]]
    time, current, voltage = arrays
    if (
        len({len(v) for v in arrays}) != 1
        or not np.isfinite(time).all()
        or any(np.isinf(v).any() for v in arrays)
    ):
        raise ValueError("Invalid full-cell measurements")
    if np.any(np.diff(time) < 0):
        raise ValueError("Non-monotone source timebase")
    if temperature is not None:
        temperature = np.asarray(temperature, dtype=float).reshape(-1)
        if len(temperature) != len(time) or np.isinf(temperature).any():
            raise ValueError("Invalid measured temperature")
    path = DATA / "full_cell" / f"{rid}-normalized.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
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
            ]
        )
        for i, (t, c, v) in enumerate(zip(time, current, voltage)):
            writer.writerow(
                [
                    repr(float(t)),
                    repr(float(c)) if np.isfinite(c) else "",
                    repr(float(v)) if np.isfinite(v) else "",
                    (
                        ""
                        if temperature is None or not np.isfinite(temperature[i])
                        else repr(float(temperature[i]) + 273.15)
                    ),
                    "",
                    0,
                    1,
                    (
                        "U"
                        if not np.isfinite(c)
                        else "D" if c < 0 else "C" if c > 0 else "R"
                    ),
                    i,
                ]
            )
    return {
        "id": rid,
        "cell_id": cell_id,
        "sample_id": sample_id,
        "asset_id": asset_id,
        "source_id": source_id,
        "path": None,
        "original_member": original_member,
        "normalized_path": f"full_cell/{path.name}",
        "normalized_sha256": digest(path),
        "current_convention": "Source signed current retained: charge positive, discharge negative; checked against protocol and voltage trend.",
        "processing": "No voltage/current smoothing, resampling, or row deletion. Source NaNs become empty CSV fields; U denotes unknown current mode. Time is relative sample index on the documented 1 Hz timebase. Celsius temperatures converted to kelvin. Full MAT/ZIP originals remain checksum-pinned at the source.",
        "missing_values": {
            "current_charge_positive_A": int(np.isnan(current).sum()),
            "voltage_V": int(np.isnan(voltage).sum()),
            "cell_temperature_K": (
                len(time) if temperature is None else int(np.isnan(temperature).sum())
            ),
        },
        "temperature_definition": temperature_definition,
        "csv_header_rows": 0,
        "license": license,
        "protocol": protocol,
        "relationship_to_parameters": "same_model_same_study",
        "evidence": sample_evidence,
        "independent_validation_by_this_project": False,
        "row_count": len(time),
        "columns": [
            "time_s",
            "current_charge_positive_A",
            "voltage_V",
            "cell_temperature_K",
        ],
        "discharge_segments": (
            [
                {
                    "step": 1,
                    "mean_discharge_current_A": float(-np.mean(current[current < 0])),
                    "nominal_C_rate": nominal_rate,
                    "initial_preconditioning": False,
                    "points": int(np.count_nonzero(current < 0)),
                }
            ]
            if np.any(current < 0)
            else []
        ),
        "format": "Normalized measurements; original MAT/ZIP is external and checksum-pinned",
    }


def extend(download=False):
    load = lambda name: json.loads((DATA / name).read_text(encoding="utf-8"))
    sources, assets, cells = (
        load("sources.json"),
        load("assets.json"),
        load("cells.json"),
    )
    materials, document = load("materials.json"), load("catalog.json")
    parameters, tests = (
        load("parameters.json")["records"],
        load("full_cell_tests.json")["records"],
    )
    extension_cells = {
        "bpx-lfp-18650-2ah-undisclosed",
        "a123-amp20m1hd-a",
    }
    parameters = [p for p in parameters if p["cell_id"] not in extension_cells]
    tests = [t for t in tests if t["cell_id"] not in extension_cells]
    document["records"] = [
        r for r in document["records"] if "bpx-lfp-2022" not in r["source_ids"]
    ]
    pins = json.loads((ROOT / "scripts/lfp_assets.json").read_text())
    for aid, asset in pins.items():
        obtain(
            asset["filename"], asset["url"], sha256=asset["sha256"], download=download
        )
        assets[aid] = asset
    license_dir = ROOT / "src/ebp/licenses"
    shutil.copyfile(CACHE / "lin-license.txt", license_dir / "Oxford-BSD-2-Clause.txt")
    shutil.copyfile(CACHE / "bpx-license.txt", license_dir / "BPX-MIT.txt")
    # The dataset's copyright/attribution notice supplements the CC license text.
    shutil.copyfile(
        CACHE / "lin-readme.txt", license_dir / "Oxford-Lin2022-data-notice.txt"
    )
    sources.update(
        {
            "bpx-lfp-2022": {
                "kind": "parameter_set",
                "title": "BPX LFP/graphite 2 Ah 18650 example",
                "authors": [
                    "About:Energy Limited",
                    "University of Oxford / Faraday Institution",
                ],
                "year": 2022,
                "url": pins["bpx-lfp-example"]["url"],
                "license": "MIT",
                "version": "BPX 0.1.0 example, repository commit 0f591336937c2c57509f20ab23f9908e58f7a757",
                "role": "Parameter example based on cycling and electrode teardown. Manufacturer, commercial part number, and matching raw cycling files are not disclosed in this example. Electrolyte and entropy data include borrowed sources.",
            },
            "lin-2022-paper": {
                "kind": "paper",
                "title": "Multiscale coupling of surface temperature with solid diffusion in large lithium-ion pouch cells",
                "authors": [
                    "Jie Lin",
                    "Howie N. Chu",
                    "David A. Howey",
                    "Charles W. Monroe",
                ],
                "year": 2022,
                "doi": "10.1038/s44172-022-00005-8",
                "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/",
                "license": "CC-BY-4.0",
                "role": "Table 1 fitted effective parameters at 30/50/70% SOC; Methods explicitly identify AMP20M1HD-A. Lumped diffusion time is shared by both electrodes.",
            },
            "lin-2022-data": {
                "kind": "dataset",
                "title": "Oxford experimental data for Lin et al. 2022",
                "authors": [
                    "Jie Lin",
                    "Howie N. Chu",
                    "David A. Howey",
                    "Charles W. Monroe",
                ],
                "year": 2022,
                "doi": "10.5287/bodleian:NGQkq49wG",
                "url": "https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513",
                "license": "CC-BY-4.0",
                "role": "Original Cell I 4C full-discharge voltage, current, and thermal-grid observations. Source README explicitly permits redistribution under CC BY 4.0.",
            },
            "lin-2022-code": {
                "kind": "software",
                "title": "Oxford multiscale-coupling COMSOL/MATLAB implementation",
                "authors": ["University of Oxford", "Multiscale coupling developers"],
                "year": 2022,
                "url": "https://github.com/Battery-Intelligence-Lab/multiscale-coupling/tree/dba3649f2eeb4228d2849e4d4e748c91ed6ad7a4",
                "version": "dba3649f2eeb4228d2849e4d4e748c91ed6ad7a4",
                "license": "BSD-2-Clause",
                "role": "Model geometry and assumed 5 micrometre particle radius. Optimizer initial guesses are not treated as final fitted parameters. Through-plane scaling is model specific.",
            },
        }
    )
    # Official BPX example: no commercial identity is inferred from chemistry/form factor.
    bpx = json.loads((CACHE / "bpx-lfp18650.json").read_text())
    cid = "bpx-lfp-18650-2ah-undisclosed"
    cells[cid] = {
        "manufacturer": None,
        "model": None,
        "display_name": "Undisclosed LFP/graphite 18650, 2 Ah (BPX)",
        "format": "18650",
        "chemistry": "LFP/graphite",
        "nominal_capacity_Ah": 2,
        "identity_level": "commercial_part_undisclosed",
        "source_ids": ["bpx-lfp-2022"],
        "model_context": "DFN BPX example; not a uniquely identified commercial cell",
        "coverage": {
            "ocp": "Two electrode OCP fits available",
            "diffusion": "Two particle diffusivities and activation energies available",
            "kinetics": "BPX-defined rate constants; not exchange-current densities",
            "full_cell_tests": "No matching raw full-cell tests supplied in the example",
        },
        "match_level": "unmatched",
        "match_evidence": "The example title specifies chemistry, capacity and format only. No raw tests can be assigned to an exact commercial model.",
        "note": "Do not match this example to another 2 Ah LFP cell using nominal capacity alone.",
    }
    for side, material in [
        ("Positive electrode", "LFP"),
        ("Negative electrode", "graphite"),
    ]:
        group = bpx["Parameterisation"][side]
        mid = f"bpx-lfp18650-{material.lower()}"
        materials[mid] = {
            "chemistry": material,
            "description": "Electrode fit in the BPX example; supplier, batch, and commercial cell part number undisclosed.",
        }
        rid = f"bpx-lfp18650-{material.lower()}-ocp"
        r = base_record(rid, material)
        r.update(
            title=f"{material} | BPX LFP 18650 example | OCP fit",
            material_id=mid,
            source_ids=["bpx-lfp-2022"],
            license="MIT",
        )
        r["temperature"] = {
            "value_K": bpx["Parameterisation"]["Cell"]["Reference temperature [K]"],
            "description": "BPX reference temperature; no independently verified OCP measurement temperature is asserted.",
        }
        r["x"] = {
            "kind": "stoichiometry",
            "symbol": "theta",
            "unit": "1",
            "domain": [group["Minimum stoichiometry"], group["Maximum stoichiometry"]],
            "definition": "Electrode lithium fraction as defined by BPX; not whole-cell SOC.",
            "domain_basis": "Operating minimum/maximum stoichiometry provided by this exact BPX example. No extrapolation to 0 or 1.",
        }
        r["representation"] = {
            "kind": "expression",
            "expression": group["OCP [V]"],
            "functions": ["exp", "tanh"],
            "source_function": f"BPX::Parameterisation::{side}::OCP [V]",
        }
        r["cell_link"] = {
            "cell_id": cid,
            "relationship": "same_parameter_set",
            "evidence": "Same BPX parameter file; manufacturer and commercial part remain undisclosed, so this does not establish a commercial model identity.",
        }
        r["provenance"] = {
            "asset_ids": ["bpx-lfp-example"],
            "derivation": "verbatim_bpx_expression",
            "location": f"Parameterisation/{side}/OCP [V]",
            "processing": {"changes": "none", "script": "scripts/seed_lfp.py"},
        }
        r["quality"] = {
            "source_review": "upstream_code_checked",
            "axis_status": "upstream_stoichiometry",
            "raw_data": "not_deposited_with_formula",
            "model_status": "ocp_component_only",
            "independent_validation": False,
        }
        r["limitations"] = [
            "Fit coefficients from a parameter example; original OCP points are not supplied.",
            "Commercial model identity and raw full-cell validation match are unresolved.",
            "This is not an independent validation of BPX or the cell model.",
        ]
        document["records"].append(r)
    for component, group in bpx["Parameterisation"].items():
        for name, value in group.items():
            if type(value) not in (int, float):
                continue
            unit = name.split("[")[-1].rstrip("]") if "[" in name else "1"
            category = (
                "operating_limits"
                if any(w in name for w in ["cut-off", "Nominal cell capacity"])
                else (
                    "kinetics"
                    if "Reaction" in name
                    else (
                        "diffusion"
                        if "Diffus" in name
                        else (
                            "thermal"
                            if any(w in name for w in ["heat", "Thermal", "Density"])
                            else (
                                "initial_state"
                                if any(w in name for w in ["Initial", "Ambient"])
                                else (
                                    "transport"
                                    if component == "Electrolyte"
                                    else "geometry"
                                )
                            )
                        )
                    )
                )
            )
            pid = "bpx-lfp18650-" + re.sub(
                r"[^a-z0-9]+", "-", (component + "-" + name).lower()
            ).strip("-")
            assumptions = (
                "estimated_thermal_property"
                if category == "thermal"
                else "bpx_parameter_value; individual measurement/fit/borrowed origin not independently audited"
            )
            limits = [
                "Commercial part number and matching experimental files are undisclosed.",
                "BPX v0.1 parameter definitions apply. Do not interchange rate constants, volumetric kinetics, and surface exchange-current densities.",
            ]
            if category == "thermal":
                limits.append(
                    "Header explicitly states other thermal properties are estimated."
                )
            parameters.append(
                parameter(
                    pid,
                    cid,
                    f"{component}: {name}",
                    category,
                    value,
                    unit,
                    ["bpx-lfp-2022"],
                    "bpx-lfp-example",
                    f"Parameterisation/{component}/{name}",
                    assumptions,
                    license="MIT",
                    limitations=limits,
                    conditions={
                        "reference_temperature_K": bpx["Parameterisation"]["Cell"][
                            "Reference temperature [K]"
                        ]
                    },
                )
            )
    # Published fitted parameters, never optimizer starting guesses.
    cid = "a123-amp20m1hd-a"
    cells[cid] = {
        "manufacturer": "A123 Systems",
        "model": "AMP20M1HD-A",
        "display_name": "A123 AMP20M1HD-A | 20 Ah LFP pouch",
        "format": "pouch",
        "chemistry": "LFP/graphite",
        "nominal_capacity_Ah": 20,
        "identity_level": "explicit_commercial_model",
        "source_ids": ["lin-2022-paper", "lin-2022-data", "lin-2022-code"],
        "model_context": "Thermal DFN-derived reduced model with one lumped diffusion time shared by the two electrodes",
        "match_level": "same_model_same_study",
        "match_evidence": "Methods names AMP20M1HD-A; paper links the ORA dataset; archive filename identifies Cell I. Table 1 is for one cell but its letter is not explicitly established here, so a same-specimen parameter claim is withheld.",
        "coverage": {
            "ocp": "C/25 full-cell pseudo-OCV reported in Methods; no downloadable electrode-resolved OCP points located in the selected deposit",
            "diffusion": "Fitted shared diffusion times at three SOCs; effective D derived using the model's assumed radius",
            "kinetics": "Fitted volumetric exchange-current density and activation energy at three SOCs",
            "full_cell_tests": "Cell I 4C full-discharge voltage/current/thermal grid available",
        },
        "note": "Do not label the full-cell pseudo-OCV as an LFP half-cell OCP, or assign a shared effective diffusion coefficient to a specific material without the model assumptions.",
    }
    table = [
        (
            "volumetric-exchange-current",
            "Volumetric exchange-current density",
            "kinetics",
            [1.86, 1.80, 1.86],
            1e6,
            "A.m-3",
            "Table 1: a*i0 (A.cm-3); multiplied by 1e6 to obtain A.m-3. Not surface i0.",
        ),
        (
            "reaction-activation-energy",
            "Reaction activation energy",
            "kinetics",
            [29.5, 29.2, 29.7],
            1000,
            "J.mol-1",
            "Table 1: E_theta (kJ.mol-1); multiplied by 1000.",
        ),
        (
            "effective-ionic-conductivity",
            "Effective ionic conductivity",
            "transport",
            [0.046, 0.043, 0.045],
            1,
            "S.m-1",
            "Table 1: fitted effective kappa; use the paper's homogenization convention.",
        ),
        (
            "ionic-temperature-coefficient",
            "Temperature coefficient of effective ionic conductivity",
            "transport",
            [2.4, 2.7, 2.4],
            0.001,
            "S.m-1.K-1",
            "Table 1: alpha (mS.m-1.K-1); multiplied by 0.001.",
        ),
        (
            "ocv-gradient",
            "Local full-cell OCV gradient",
            "thermodynamics",
            [0.35, 0.24, 0.18],
            1,
            "V",
            "Table 1: k_U, derivative with respect to fractional cell SOC. Not an electrode OCP curve.",
        ),
        (
            "shared-diffusion-time",
            "Shared solid diffusion time",
            "diffusion",
            [552, 590, 622],
            1,
            "s",
            "Table 1: t_d=r0^2/D_s; same lumped time for both electrodes.",
        ),
        (
            "reaction-entropy",
            "Full-cell reaction entropy change",
            "thermodynamics",
            [-13.5, 7.7, 9.7],
            1,
            "J.mol-1.K-1",
            "Table 1: Delta S at the specified cell SOC.",
        ),
        (
            "heat-transfer-velocity",
            "Heat transfer velocity h/Cp_vol",
            "thermal",
            [5.11, 5.06, 5],
            1e-6,
            "m.s-1",
            "Table 1: h/Cp_vol (micrometres.s-1); not h alone.",
        ),
        (
            "effective-thermal-conductivity",
            "Effective thermal conductivity",
            "thermal",
            [1.1, 1.2, 1.1],
            1,
            "W.m-1.K-1",
            "Table 1: effective fitted k; not collector or active-material intrinsic conductivity.",
        ),
    ]
    for slug, name, category, values, factor, unit, definition in table:
        for soc, value in zip([30, 50, 70], values):
            parameters.append(
                parameter(
                    f"a123-amp20-{slug}-soc{soc}",
                    cid,
                    name,
                    category,
                    value * factor,
                    unit,
                    ["lin-2022-paper"],
                    "lin2022-table1",
                    f"Table 1 / This work / {soc}% SOC",
                    "fitted_effective_parameter",
                    conditions={
                        "cell_SOC_fraction": soc / 100,
                        "fit_protocol": "4C, 100 s period square wave",
                        "temperature_K": None,
                    },
                    definition=definition,
                )
            )
    # Radius is a model assumption. The data identify t_d, not independent r and D.
    for soc, td in zip([30, 50, 70], [552, 590, 622]):
        parameters.append(
            parameter(
                f"a123-amp20-effective-diffusivity-soc{soc}",
                cid,
                "Effective shared solid diffusivity inferred from t_d",
                "diffusion",
                (5e-6) ** 2 / td,
                "m2.s-1",
                ["lin-2022-paper", "lin-2022-code"],
                "lin2022-model",
                "Table 1 t_d + Battery_model.m::rp_pos/rp_neg=5 um",
                "derived_from_fitted_time_and_assumed_radius",
                conditions={
                    "cell_SOC_fraction": soc / 100,
                    "assumed_particle_radius_m": 5e-6,
                    "diffusion_time_s": td,
                },
                limitations=[
                    "Derived D=r^2/t_d, conditional on the model's assumed 5 um radius.",
                    "One effective D is shared by both electrodes; this is not an independently measured intrinsic LFP diffusion coefficient.",
                    "Changing radius changes inferred D quadratically; the inverse experiment identifies the time scale.",
                ],
                definition="Conditional effective coefficient D=(5e-6 m)^2/t_d.",
            )
        )
    # Small source transcription is explicit and separate from downloaded originals.
    evidence = DATA / "evidence"
    evidence.mkdir(exist_ok=True)
    transcription = {
        "source_url": sources["lin-2022-paper"]["url"],
        "location": "Table 1, This work columns at 30/50/70% SOC",
        "rows": [
            {
                "name": row[1],
                "source_values": row[3],
                "SI_multiplier": row[4],
                "SI_unit": row[5],
            }
            for row in table
        ],
    }
    transcription_path = evidence / "lin2022-table1.json"
    transcription_path.write_text(json.dumps(transcription, indent=2) + "\n")
    assets["lin2022-table1"] = {
        "source_id": "lin-2022-paper",
        "filename": "lin2022-table1.json",
        "url": sources["lin-2022-paper"]["url"],
        "sha256": digest(transcription_path),
        "path": "evidence/lin2022-table1.json",
        "digest_scope": "local curated Table 1 transcription, not the publisher HTML",
        "license": "CC-BY-4.0",
    }
    measured = loadmat(CACHE / "lin-full-discharge.mat", simplify_cells=True)
    tests.append(
        normalized_test(
            "a123-amp20-cell-i-4c",
            cid,
            "Cell I",
            "lin2022-full-discharge",
            "lin-2022-data",
            np.arange(len(measured["V"])),
            measured["I"],
            measured["V"],
            np.mean(measured["A"], axis=(0, 1)),
            "4C full discharge after CCCV charging and 1 h rest; 1 Hz source timebase",
            4,
            cells[cid]["match_evidence"],
            temperature_definition="Arithmetic mean of every pixel in the deposited calibrated thermal grid A, no additional ROI mask; degrees Celsius in source. Ambient temperature is not available as a separate trace.",
        )
    )
    # Full-cell-only Oxford 9 Ah data were removed in v0.16: no admitted
    # electrode OCP, diffusion or kinetics records support that cell package.
    # Coverage and explicit identities for the pre-existing NMC reference case.
    cells["lg-m50"].update(
        display_name="LG M50 | 5 Ah NMC811/graphite-SiOx",
        chemistry="NMC811/graphite-SiOx",
        nominal_capacity_Ah=5,
        match_level="same_model_same_study",
        match_evidence=cells["lg-m50"]["note"],
        coverage={
            "ocp": "Graphite effective fit available",
            "diffusion": "Two scalar particle diffusivities in upstream implementation",
            "kinetics": "Two exchange-current density laws",
            "full_cell_tests": "Three same-model validation samples",
        },
    )
    for cell_id, cell in cells.items():
        cell["parameter_ids"] = [p["id"] for p in parameters if p["cell_id"] == cell_id]
        cell["full_cell_test_ids"] = [t["id"] for t in tests if t["cell_id"] == cell_id]
        cell["ocp_record_ids"] = [
            r["id"] for r in document["records"] if r["cell_link"]["cell_id"] == cell_id
        ]
    document["release"] = "0.2.0"
    for name, value in [
        ("catalog.json", document),
        ("sources.json", sources),
        ("assets.json", assets),
        ("cells.json", cells),
        ("materials.json", materials),
        ("parameters.json", {"schema_version": "0.1", "records": parameters}),
        ("full_cell_tests.json", {"schema_version": "0.1", "records": tests}),
    ]:
        write_json(name, value)
    print(
        f"LFP expansion: {len(document['records'])} OCP records, {len(parameters)} model parameters, {len(tests)} full-cell tests, {len(cells)} cell/family entries."
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    extend(parser.parse_args().download)
