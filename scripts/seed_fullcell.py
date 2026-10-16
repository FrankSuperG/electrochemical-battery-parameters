"""Link experimental discharge observations to explicitly identified model inputs.

Never manufacture a measured current from a nominal C-rate, or align separate
temperature-rise clocks by interpolation. Upstream Python is parsed, not run.
"""

import ast
import csv
import hashlib
import json
import re
import shutil

import numpy as np

from seed_v01 import CACHE, DATA, ROOT, base_record, obtain, write_json
from seed_lgm50 import KEYS
from seed_materials import F, R, MathTranscriber, ocp_record, read_module

SCRIPT = "scripts/seed_fullcell.py"
ECKER = "kokam-slpb75106100-ecker2015"
ENERTECH = "enertech-lco-pouch-ai2020"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aid_for(pins, filename):
    return next(aid for aid, asset in pins.items() if asset["filename"] == filename)


def write_csv(relative, columns, rows):
    path = DATA / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        writer.writerows(rows)
    return sha(path)


def add_parameters(name, cid, source_ids, pins, parameters):
    aid = "pybamm-" + name.lower() + "-code"
    functions, values, scalars = read_module(CACHE / pins[aid]["filename"])
    borrowed = name == "Ai2020"
    for category, keys in KEYS.items():
        for key in keys:
            if key not in scalars:
                if "particle diffusivity" in key:
                    continue
                raise ValueError(f"Missing {name} scalar: {key}")
            parameters.append(
                {
                    "id": name.lower()
                    + "-"
                    + re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-"),
                    "version": "1",
                    "cell_id": cid,
                    "category": category,
                    "name": key,
                    "unit": key.split("[")[-1].rstrip("]") if "[" in key else "1",
                    "representation": {"kind": "scalar", "value": scalars[key]},
                    "source_ids": source_ids,
                    "provenance": {
                        "asset_id": aid,
                        "location": f"{name}.py::get_parameter_values::{key}",
                        "origin_status": "upstream_implementation_value; per-value measurement origin not independently audited",
                    },
                    "license": "BSD-3-Clause",
                    "independent_validation": False,
                    "conditions": {
                        "reference_temperature_K": scalars["Reference temperature [K]"]
                    },
                    "limitations": [
                        "Partial implementation inputs; not a complete independently validated parameter set.",
                        (
                            "Ecker implementation capacity is 0.15625 Ah, versus the commercial cell's 7.5 Ah. Geometry/current scaling must be reviewed before comparison. Thermal properties are borrowed from another 5 Ah Kokam cell."
                            if cid == ECKER
                            else "Commercial Enertech part number and exact parameterization/validation specimen link are unresolved."
                        ),
                    ],
                }
            )
    for side in ["Negative", "Positive"]:
        for suffix, category, unit in [
            ("particle diffusivity [m2.s-1]", "diffusion", "m2.s-1"),
            ("electrode exchange-current density [A.m-2]", "kinetics", "A.m-2"),
        ]:
            key = side + " " + suffix
            function = functions[values[key].id]
            names = [arg.arg for arg in function.args.args]
            expression = MathTranscriber({n: n for n in names}, scalars).transcribe(
                function
            )
            parameters.append(
                {
                    "id": name.lower()
                    + "-"
                    + side.lower()
                    + (
                        "-diffusivity"
                        if category == "diffusion"
                        else "-exchange-current-density"
                    ),
                    "version": "1",
                    "cell_id": cid,
                    "category": category,
                    "name": key,
                    "unit": unit,
                    "representation": {
                        "kind": "expression",
                        "expression": expression,
                        "variables": {
                            n: {
                                "sto": "1",
                                "T": "K",
                                "c_e": "mol.m-3",
                                "c_s_surf": "mol.m-3",
                                "c_s_max": "mol.m-3",
                            }[n]
                            for n in names
                        },
                        "domain": "Mathematical domain: 0<=sto<=1; c_e>=0; c_s_max>0; 0<=c_s_surf<=c_s_max; T>0. Experimental validity range not established.",
                        "gas_constant_J_mol_K": R,
                    },
                    "source_ids": source_ids
                    + (["dualfoil-attribution"] if borrowed else []),
                    "provenance": {
                        "asset_id": aid,
                        "location": f"{name}.py::{function.name}",
                        "origin_status": (
                            "borrowed_dualfoil_implementation_function"
                            if borrowed
                            else "Ecker study data fitted by Richardson2020 / Simon O'Kane; upstream implementation function"
                        ),
                    },
                    "conditions": {
                        "gas_constant_J_mol_K": R,
                        "faraday_constant_C_mol": F,
                        "temperature_reference_note": (
                            "Ecker negative diffusivity uses 296 K; its other three imported functions use 296.15 K."
                            if cid == ECKER
                            else "298.15 K in upstream laws"
                        ),
                    },
                    "license": "BSD-3-Clause",
                    "independent_validation": False,
                    "definition": key
                    + "; source concentration and active-area convention retained",
                    "limitations": [
                        "Not a measured current or a newly estimated parameter; source mathematical operations retained by AST substitution.",
                        (
                            "Borrowed Dualfoil functions are used in the Enertech model; they are not claimed to be same-cell measurements."
                            if borrowed
                            else "Fitted functions retain the upstream Ecker/Richardson attribution; original fit data and instrument records are distinct from these expressions."
                        ),
                    ],
                }
            )
    return functions, values, scalars


def add_ocp(name, cid, positive, source_ids, pins, document, materials):
    aid = "pybamm-" + name.lower() + "-code"
    functions, values, scalars = read_module(CACHE / pins[aid]["filename"])
    for side, material in [("Negative", "graphite"), ("Positive", positive)]:
        function = values[f"{side} electrode OCP [V]"].id
        rid = f"{name.lower()}-{material.lower()}-ocp"
        evidence = (
            "Kokam SLPB75106100, Ecker2015 study; electrode fits and digitized whole-cell curves share a model/study lineage, not a proven identical specimen."
            if cid == ECKER
            else "Enertech pouch family in Ai2020/Rieger2016; commercial part number and exact specimen correspondence unresolved."
        )
        if cid == ECKER:
            record, meta = ocp_record(
                rid,
                material,
                side.lower(),
                MathTranscriber({"sto": "x"}, scalars).transcribe(functions[function]),
                function,
                aid,
                source_ids,
                cid,
                "same_model",
                evidence,
                "literature_figure_fit_in_upstream_implementation",
            )
            record["provenance"]["processing"]["script"] = SCRIPT
            record["limitations"].append(
                "Upstream OCP fits were obtained with WebPlotDigitizer and gnuplot. The positive-fit coefficient m was modified by Simon O'Kane. NCO is retained as the upstream material label; no NMC/NCA ratio is inferred."
            )
        else:
            filename = (
                "graphite_ocp_Enertech_Ai2020.csv"
                if side == "Negative"
                else "lico2_ocp_Ai2020.csv"
            )
            table_aid = aid_for(pins, filename)
            source = CACHE / filename
            rows = []
            for line_number, line in enumerate(source.read_text().splitlines(), 1):
                if line.strip() and not line.startswith("#"):
                    x, y = map(float, line.split(","))
                    # Explicitly labeled synthetic extrapolation guard in source.
                    if side == "Negative" and x == 0 and y == 3.5:
                        continue
                    rows.append([repr(x), repr(y), line_number])
            x = np.array([float(r[0]) for r in rows])
            assert np.all(np.diff(x) > 0)
            relative = f"curves/{rid}.csv"
            checksum = write_csv(relative, ["x", "potential_V", "source_line"], rows)
            record = base_record(rid, material)
            record.update(
                title=f"{material} | Enertech / Ai2020-Rieger2016 | published OCP table",
                material_id=rid + "-material",
                electrode_role=side.lower(),
                measurement="literature_table",
                source_ids=source_ids + ["pybamm-data-1-0-2"],
                license="BSD-3-Clause",
            )
            record["x"] = {
                "kind": "stoichiometry",
                "symbol": "theta",
                "unit": "1",
                "domain": [float(x[0]), float(x[-1])],
                "definition": "Electrode stoichiometry as supplied by upstream; not full-cell SOC.",
                "domain_basis": "Retained table endpoints; no extrapolation. Negative synthetic x=0 guard omitted.",
            }
            record["representation"] = {
                "kind": "table",
                "path": relative,
                "sha256": checksum,
                "point_count": len(rows),
                "default_interpolation": "linear",
            }
            record["cell_link"] = {
                "cell_id": cid,
                "relationship": "same_parameter_set",
                "evidence": evidence,
            }
            record["provenance"] = {
                "asset_ids": [table_aid, aid],
                "derivation": "upstream_published_table_transcription",
                "location": filename,
                "processing": {
                    "script": SCRIPT,
                    "removed_synthetic_guard_points": 1 if side == "Negative" else 0,
                    "changes": "Comment lines omitted; original numeric values and one-based source lines retained; no smoothing or resampling. Source graphite x=0,3.5 V extrapolation guard omitted.",
                },
            }
            record["quality"] = {
                "source_review": "upstream_code_checked",
                "axis_status": "upstream_stoichiometry",
                "raw_data": "published_table_not_instrument_raw",
                "model_status": "ocp_component_only",
                "independent_validation": False,
            }
            record["limitations"] = [
                evidence,
                "Published implementation table, not newly measured OCP or a claim of original instrument points. Positive table attribution is Rieger2016 in source comments; negative table attribution is Ai2020.",
                "OCP protocol, branch direction and numerical measurement temperature are unresolved. No independent model validation.",
                "Project evaluation uses linear interpolation by default, with optional PCHIP. Upstream Ai2020 uses cubic interpolation; only retained table nodes, not between-node interpolation, are claimed to match.",
            ]
            meta = {"chemistry": material, "description": evidence}
        document["records"].append(record)
        materials[record["material_id"]] = meta


def add_test(filename, cid, rate, pins, assets, tests):
    aid = aid_for(pins, filename)
    source = CACHE / filename
    ecker = cid == ECKER
    values = np.loadtxt(source, delimiter="," if ecker else None)
    assert values.ndim == 2 and values.shape[1] == 2
    assert np.isfinite(values).all() and np.all(np.diff(values[:, 0]) >= 0)
    test_id = (
        ("ecker-kokam-" if ecker else "enertech-")
        + str(rate).replace(".", "p")
        + "c-discharge"
    )
    columns = [
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
    rows = [
        [repr(float(t)), "", repr(float(v)), "", "", "", "", "D", i + 1]
        for i, (t, v) in enumerate(values)
    ]
    relative = f"full_cell/{test_id}-normalized.csv"
    checksum = write_csv(relative, columns, rows)
    raw_relative = "evidence/" + filename
    shutil.copyfile(source, DATA / raw_relative)
    assets[aid]["path"] = raw_relative
    count = len(rows)
    test = {
        "id": test_id,
        "cell_id": cid,
        "sample_id": "not_disclosed",
        "asset_id": aid,
        "source_id": "pybamm-data-1-0-2",
        "path": None,
        "original_download_path": raw_relative,
        "original_format": "CSV" if ecker else "TXT",
        "normalized_path": relative,
        "normalized_sha256": checksum,
        "row_count": count,
        "columns": columns,
        "format": "time_voltage_only",
        "license": "BSD-3-Clause",
        "discharge_segments": [],
        "protocol": f"{rate:g}C constant-current discharge"
        + (
            " at 25 degC; published-figure digitization"
            if ecker
            else "; Enertech beginning-of-life observations"
        ),
        "relationship_to_parameters": (
            "same_model_same_study" if ecker else "same_study_cell_family"
        ),
        "evidence": (
            "Official PyBaMM data release attributes the curve to Ecker2015ii, digitized from Richardson2020 Figure 8; same named Kokam model as Ecker2015 parameters."
            if ecker
            else "Official PyBaMM data release attributes the Enertech observations to Ai2020 and Rieger2016, the same study family cited by Ai2020.py. Commercial part and exact specimen remain unresolved."
        ),
        "observation_kind": (
            "published_figure_digitization"
            if ecker
            else "published_experimental_series"
        ),
        "current_convention": "Charge-positive column reserved but empty: current is absent from the source; nominal C-rate is protocol metadata only.",
        "basic_test": {
            "type": "constant_current_discharge",
            "nominal_C_rate": rate,
            "current_measurement": "not_supplied",
            "charge_trace": "not_supplied",
            "voltage_trace": "available",
            "protocol_temperature_K": 298.15 if ecker else None,
        },
        "missing_items": [
            "Measured current trace",
            "Charge trace",
            "Capacity channel",
            "Exact specimen identifier",
            "Absolute measured temperature",
        ],
        "missing_values": {
            "current_charge_positive_A": count,
            "cell_temperature_K": count,
            "ambient_temperature_K": count,
            "voltage_V": 0,
        },
        "temperature_definition": "No absolute measured temperature channel. Enertech rise channels, where available, retain their own timebase in separate sidecars.",
        "processing": {
            "script": SCRIPT,
            "smoothing": "none",
            "resampling": "none",
            "imputation": "none",
            "source_columns": ["time_s", "voltage_V"],
            "changes": "Retain every source pair and row order; add one-based source_record. Current, absolute temperatures, cycle and step are empty. Mode D comes from the documented protocol.",
        },
        "independent_validation_by_this_project": False,
        "sidecars": [],
    }
    if not ecker and rate in [0.5, 1, 2]:
        side_filename = f"{rate:g}C_discharge_T.txt"
        side_aid = aid_for(pins, side_filename)
        side_values = np.loadtxt(CACHE / side_filename)
        assert np.isfinite(side_values).all() and np.all(
            np.diff(side_values[:, 0]) >= 0
        )
        side_path = f"full_cell/{test_id}-temperature-rise.csv"
        side_sha = write_csv(
            side_path,
            ["time_s", "temperature_rise_K", "source_record"],
            [
                [repr(float(t)), repr(float(v)), i + 1]
                for i, (t, v) in enumerate(side_values)
            ],
        )
        original = "evidence/" + side_filename
        shutil.copyfile(CACHE / side_filename, DATA / original)
        assets[side_aid]["path"] = original
        test["sidecars"].append(
            {
                "kind": "temperature_rise",
                "path": side_path,
                "sha256": side_sha,
                "asset_id": side_aid,
                "original_download_path": original,
                "row_count": len(side_values),
                "unit": "K",
                "relationship": "same nominal C-rate and study family; identical run and clock synchronization not established",
                "processing": "Separate native timebase retained; not interpolated, merged or converted to absolute temperature.",
            }
        )
    tests.append(test)


def audit_links(cells, records, parameters, tests):
    for test in tests:
        with (DATA / test["normalized_path"]).open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        test["channel_availability"] = {
            key: {
                "present_rows": sum(bool(r.get(key)) for r in rows),
                "total_rows": len(rows),
            }
            for key in [
                "voltage_V",
                "current_charge_positive_A",
                "cell_temperature_K",
                "ambient_temperature_K",
            ]
        }
        if "basic_test" not in test:
            modes = {r["mode"] for r in rows}
            test["basic_test"] = {
                "type": (
                    "CCCV_charge_and_CC_discharge"
                    if test["cell_id"] == "lg-m50"
                    else (
                        "constant_current_charge"
                        if "C" in modes
                        else "constant_current_discharge"
                    )
                ),
                "current_measurement": "supplied; missing rows remain empty",
                "charge_trace": "available" if "C" in modes else "not_supplied",
                "voltage_trace": "available",
                "protocol_evidence": test["protocol"],
            }
        test.setdefault("observation_kind", "instrument_series")
        test.setdefault("missing_items", [])
        for key, availability in test["channel_availability"].items():
            if availability["present_rows"] == 0:
                test["missing_items"].append(
                    {
                        "voltage_V": "Voltage trace",
                        "current_charge_positive_A": "Measured current trace",
                        "cell_temperature_K": "Absolute measured temperature",
                        "ambient_temperature_K": "Ambient temperature trace",
                    }[key]
                )
        test["missing_items"] = sorted(set(test["missing_items"]))
    for cid, cell in cells.items():
        cell["parameter_ids"] = [p["id"] for p in parameters if p["cell_id"] == cid]
        cell["ocp_record_ids"] = [
            r["id"] for r in records if r["cell_link"]["cell_id"] == cid
        ]
        cell["full_cell_test_ids"] = [t["id"] for t in tests if t["cell_id"] == cid]
        matrix = {}
        for component in ["ocp", "diffusion", "kinetics", "full_cell_tests"]:
            if component == "ocp":
                selected = [r for r in records if r["id"] in cell["ocp_record_ids"]]
                borrowed = any(
                    r["cell_link"]["relationship"] == "surrogate" for r in selected
                )
            elif component == "full_cell_tests":
                selected = [t for t in tests if t["cell_id"] == cid]
                borrowed = False
            else:
                selected = [
                    p
                    for p in parameters
                    if p["cell_id"] == cid
                    and (
                        p["category"] == component
                        or (
                            component == "diffusion"
                            and "diffusivity" in p["name"].lower()
                            and "particle" in p["name"].lower()
                        )
                    )
                ]
                borrowed = any(
                    "borrowed_dualfoil" in p["provenance"]["origin_status"]
                    for p in selected
                )
            source_ids = sorted(
                {
                    sid
                    for r in selected
                    for sid in r.get("source_ids", [r.get("source_id")])
                    if sid
                }
            )
            matrix[component] = {
                "record_ids": [r["id"] for r in selected],
                "source_ids": source_ids,
                "match_level": (
                    "missing"
                    if not selected
                    else "borrowed_model_input" if borrowed else cell["match_level"]
                ),
                "evidence": cell["coverage"][component],
                "missing_items": (
                    (
                        [
                            "Same-cell measured values not established; borrowed functions retained"
                        ]
                        if borrowed
                        else ["Same-specimen measurement provenance unresolved"]
                    )
                    if selected
                    else ["No matching imported records"]
                ),
            }
        linked = [t for t in tests if t["cell_id"] == cid]
        matrix["basic_charge_discharge"] = {
            "record_ids": [t["id"] for t in linked],
            "source_ids": sorted({t["source_id"] for t in linked}),
            "match_level": cell["match_level"] if linked else "missing",
            "evidence": (
                "; ".join(sorted({t["basic_test"]["type"] for t in linked}))
                if linked
                else "No matching imported basic test"
            ),
            "missing_items": (
                sorted({item for t in linked for item in t["missing_items"]})
                if linked
                else ["Matching CC charge/discharge observations"]
            ),
        }
        cell["evidence_matrix"] = matrix
        cell["missing_items"] = [
            "Identical characterization/validation specimen not established",
            "Independent full-cell model reproduction not performed",
        ]
        if not cell["model"]:
            cell["missing_items"].append("Commercial part number unresolved")
        if not cell["full_cell_test_ids"]:
            cell["missing_items"].append(
                "Matching full-cell charge/discharge observations not imported"
            )


def extend(download=False):
    load = lambda name: json.loads((DATA / name).read_text())
    document, sources, assets = (
        load("catalog.json"),
        load("sources.json"),
        load("assets.json"),
    )
    cells, materials = load("cells.json"), load("materials.json")
    parameters, tests = (
        load("parameters.json")["records"],
        load("full_cell_tests.json")["records"],
    )
    document["records"] = [
        r
        for r in document["records"]
        if r["provenance"]["processing"].get("script") != SCRIPT
    ]
    parameters = [p for p in parameters if p["cell_id"] not in [ECKER, ENERTECH]]
    tests = [
        t
        for t in tests
        if not (
            isinstance(t["processing"], dict)
            and t["processing"].get("script") == SCRIPT
        )
    ]
    pins = json.loads((ROOT / "scripts/fullcell_assets.json").read_text())
    for aid, asset in pins.items():
        obtain(
            asset["filename"], asset["url"], sha256=asset["sha256"], download=download
        )
        assets[aid] = dict(asset)
    sources.update(
        {
            "pybamm-data-1-0-2": {
                "kind": "dataset",
                "title": "PyBaMM experimental data release v1.0.2",
                "authors": [
                    "PyBaMM team; original experimental authors named per study"
                ],
                "year": 2026,
                "url": "https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2",
                "license": "BSD-3-Clause",
                "role": "Versioned redistribution. Experimental origins and figure-digitization history are documented in v1.0.0 release notes; v1.0.2 hashes match those files.",
                "provenance_url": "https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.0",
                "license_url": "https://github.com/pybamm-team/pybamm-data/blob/bed4e1b816afb4ec11e49fabef0d5996ff0a31e5/LICENSE",
            },
            "ecker-2015-i": {
                "kind": "paper",
                "title": "Parameterization of a Physico-Chemical Model of a Lithium-Ion Battery: I. Determination of Parameters",
                "authors": [
                    "Madeleine Ecker",
                    "Thi Kim Dung Tran",
                    "Philipp Dechent",
                    "Stefan Kabitz",
                    "Alexander Warnecke",
                    "Dirk Uwe Sauer",
                ],
                "year": 2015,
                "doi": "10.1149/2.0551509jes",
                "url": "https://doi.org/10.1149/2.0551509jes",
                "role": "7.5 Ah Kokam SLPB75106100 electrochemical characterization; model/fit lineage, not identical-specimen proof.",
            },
            "ecker-2015-ii": {
                "kind": "paper",
                "title": "Parameterization of a Physico-Chemical Model of a Lithium-Ion Battery: II. Model Validation",
                "authors": [
                    "Madeleine Ecker",
                    "Stefan Kabitz",
                    "Izaro Laresgoiti",
                    "Dirk Uwe Sauer",
                ],
                "year": 2015,
                "doi": "10.1149/2.0541509jes",
                "url": "https://doi.org/10.1149/2.0541509jes",
                "role": "Experimental origin attributed by PyBaMM's release notes for the digitized 1C/5C curves.",
            },
            "richardson-2020": {
                "kind": "paper",
                "title": "Generalised single particle models for high-rate operation of graded lithium-ion electrodes: Systematic derivation and validation",
                "authors": [
                    "Giles Richardson",
                    "Ivan Korotkin",
                    "Rahifa Ranom",
                    "Michael Castle",
                    "Jamie M. Foster",
                ],
                "year": 2020,
                "doi": "10.1016/j.electacta.2020.135862",
                "url": "https://doi.org/10.1016/j.electacta.2020.135862",
                "role": "Figure 8 was digitized by upstream for the Ecker test files; fits supplied by Simon O'Kane are used in Ecker2015.py.",
            },
            "ai-2020": {
                "kind": "paper",
                "title": "Electrochemical Thermal-Mechanical Modelling of Stress Inhomogeneity in Lithium-Ion Pouch Cells",
                "authors": [
                    "Weilong Ai",
                    "Ludwig Kraft",
                    "Johannes Sturm",
                    "Andreas Jossen",
                    "Billy Wu",
                ],
                "year": 2020,
                "doi": "10.1149/2.0122001JES",
                "url": "https://doi.org/10.1149/2.0122001JES",
                "role": "Enertech pouch model; validates against Rieger observations. Diffusion/kinetics borrowing remains explicit.",
            },
            "rieger-2016": {
                "kind": "paper",
                "title": "A new method to model the thickness change of a commercial pouch cell during discharge",
                "authors": [
                    "Bernhard Rieger",
                    "Simon V. Erhard",
                    "Katharina Rumpf",
                    "Andreas Jossen",
                ],
                "year": 2016,
                "doi": "10.1149/2.0441608jes",
                "url": "https://doi.org/10.1149/2.0441608jes",
                "role": "Experimental origin named by Ai2020 and official PyBaMM data notes; part number not independently verified.",
            },
            "mohtat-2020-data": {
                "kind": "dataset",
                "title": "UofM pouch cell voltage and expansion dataset and modeling code",
                "authors": [
                    "Peyman Mohtat",
                    "Jason B. Siegel",
                    "Anna G. Stefanopoulou",
                ],
                "year": 2020,
                "doi": "10.7302/wwma-hx25",
                "url": "https://doi.org/10.7302/wwma-hx25",
                "license": "CC-BY-4.0",
                "role": "DataCite explicitly links the Mohtat2020 paper. Public landing page and listed file downloads returned HTTP 403 during this audit; file contents and cell/protocol mapping unverified, so no test imported.",
            },
        }
    )
    for name, cid, positive, ids in [
        (
            "Ecker2015",
            ECKER,
            "NCO",
            ["ecker-2015-i", "ecker-2015-ii", "richardson-2020", "pybamm-25-4-2"],
        ),
        ("Ai2020", ENERTECH, "LCO", ["ai-2020", "rieger-2016", "pybamm-25-4-2"]),
    ]:
        _, _, scalars = add_parameters(name, cid, ids, pins, parameters)
        add_ocp(name, cid, positive, ids, pins, document, materials)
        ecker = cid == ECKER
        cells[cid] = {
            "manufacturer": "Kokam" if ecker else "Enertech",
            "model": "SLPB75106100" if ecker else None,
            "display_name": (
                "Kokam SLPB75106100 | 7.5 Ah NCO/graphite"
                if ecker
                else "Enertech | LCO/graphite | 2.28 Ah model input"
            ),
            "chemistry": positive + "/graphite",
            "format": "pouch",
            "nominal_capacity_Ah": 7.5 if ecker else 2.28,
            "implementation_capacity_Ah": scalars["Nominal cell capacity [A.h]"],
            "identity_level": (
                "explicit_commercial_model"
                if ecker
                else "study_cell_family; commercial_part_unresolved"
            ),
            "match_level": (
                "same_model_same_study" if ecker else "same_study_cell_family"
            ),
            "source_ids": ids + ["pybamm-data-1-0-2"],
            "model_context": "Partial DFN/SPM/SPMe inputs and source-backed CC discharge observations",
            "match_evidence": (
                "Ecker characterization and validation share the named Kokam SLPB75106100 model. Whole-cell voltage points are digitized from Richardson2020 Figure 8. Exact specimen match is not established."
                if ecker
                else "Enertech observations and Ai2020 implementation share the Ai/Rieger study family. Exact commercial model and specimen remain unresolved; borrowed electrode functions do not become measurements through this link."
            ),
            "note": (
                "Commercial capacity is 7.5 Ah; pinned implementation uses 0.15625 Ah. Do not apply full-cell current directly to the reduced implementation without reviewing scaling. NCO label follows upstream; composition ratio unresolved. Thermal values are borrowed from another 5 Ah Kokam."
                if ecker
                else "OCP tables have Ai/Rieger attribution. Diffusivity and kinetics functions explicitly use Dualfoil. Separate temperature-rise files are not merged into absolute temperature or assumed synchronized with voltage."
            ),
            "coverage": {
                "ocp": (
                    "Two upstream figure-fitted expressions; same model/study lineage"
                    if ecker
                    else "Two published OCP tables; negative synthetic extrapolation guard removed"
                ),
                "diffusion": (
                    "Two stoichiometry/temperature diffusivity fits; Ecker/Richardson lineage"
                    if ecker
                    else "Two borrowed Dualfoil Arrhenius diffusivity functions; not same-cell measured D"
                ),
                "kinetics": (
                    "Two concentration/temperature exchange-current laws; Ecker/Richardson lineage"
                    if ecker
                    else "Two borrowed Dualfoil exchange-current laws; not same-cell measured kinetics"
                ),
                "full_cell_tests": (
                    "Two digitized CC discharges: 1C and 5C; time/voltage only"
                    if ecker
                    else "Four experimental voltage series: 0.1/0.5/1/2C; three separate temperature-rise sidecars; measured current absent"
                ),
            },
        }
    for filename, cid, rate in [
        ("Ecker_1C.csv", ECKER, 1),
        ("Ecker_5C.csv", ECKER, 5),
        ("0.1C_discharge_U.txt", ENERTECH, 0.1),
        ("0.5C_discharge_U.txt", ENERTECH, 0.5),
        ("1C_discharge_U.txt", ENERTECH, 1),
        ("2C_discharge_U.txt", ENERTECH, 2),
    ]:
        add_test(filename, cid, rate, pins, assets, tests)
    cells["mohtat2020-nmc532-pouch"]["source_ids"] = sorted(
        set(cells["mohtat2020-nmc532-pouch"]["source_ids"] + ["mohtat-2020-data"])
    )
    cells["mohtat2020-nmc532-pouch"]["coverage"][
        "full_cell_tests"
    ] = "Same-paper dataset DOI 10.7302/wwma-hx25 located; file access returned HTTP 403, so contents and model/protocol correspondence remain unverified. No trace imported."
    sources["dualfoil-attribution"][
        "title"
    ] = "Dualfoil electrode functions, as attributed by PyBaMM Marquis2019 and Ai2020"
    sources["dualfoil-attribution"][
        "role"
    ] = "Borrowed mathematical function origin named in upstream modules; no same-cell measurement origin inferred."
    if "Ecker2015 and Ai2020" not in sources["pybamm-25-4-2"]["role"]:
        sources["pybamm-25-4-2"][
            "role"
        ] += " Ecker2015 and Ai2020 modules are also pinned; original and borrowed function origins are recorded separately."
    shutil.copyfile(
        CACHE / "pybamm-data-LICENSE",
        ROOT / "src/ebp/licenses/PyBaMM-data-BSD-3-Clause.txt",
    )
    for test in tests:
        if test["cell_id"] in [ECKER, ENERTECH]:
            test["instrument_raw_status"] = (
                "not instrument raw; published figure digitization"
                if test["cell_id"] == ECKER
                else "unestablished for published experimental series"
            )
            test["scientific_source_ids"] = (
                ["ecker-2015-ii", "richardson-2020"]
                if test["cell_id"] == ECKER
                else ["ai-2020", "rieger-2016"]
            )
    audit_links(cells, document["records"], parameters, tests)
    cells["mohtat2020-nmc532-pouch"]["evidence_matrix"]["full_cell_tests"][
        "source_ids"
    ] = ["mohtat-2020-data"]
    unlinked = {}
    for record in document["records"]:
        if record["cell_link"]["cell_id"] is None:
            unlinked.setdefault(record["material"], []).append(record["id"])
    audit = {
        "checked_date": "2026-10-16",
        "scope": "Imported sources and investigated leads; not an exhaustive claim about all available literature",
        "cell_matches": {
            cid: {
                "display_name": cell["display_name"],
                "match_level": cell["match_level"],
                "components": cell["evidence_matrix"],
                "missing_items": cell["missing_items"],
            }
            for cid, cell in cells.items()
        },
        "unmatched_material_records": [
            {
                "material": material,
                "record_ids": ids,
                "match_level": "material_only",
                "missing_items": [
                    "Commercial full-cell identity",
                    "Same-cell full-cell CC charge/discharge trace",
                    "Same-cell diffusion and kinetic measurements",
                ],
            }
            for material, ids in sorted(unlinked.items())
        ],
        "research_leads": [
            {
                "source_id": "mohtat-2020-data",
                "cell_id": "mohtat2020-nmc532-pouch",
                "status": "same_paper_dataset_located; files_not_imported",
                "doi": "10.7302/wwma-hx25",
                "metadata_url": "https://api.datacite.org/dois/10.7302/wwma-hx25",
                "evidence": "DataCite lists paper DOI 10.1149/1945-7111/aba5d1 as IsReferencedBy and CC BY 4.0. It describes recorded voltage, current, temperature and expansion.",
                "access_result": "HTTP 403 from landing page and two public file endpoints on 2026-10-16",
                "missing_items": [
                    "File bytes and checksums",
                    "Per-file protocol",
                    "Column units/current convention",
                    "Commercial part and specimen mapping",
                ],
            }
        ],
        "rejected_joins": [
            "SINTEF NMC532 half-cells are not assigned to the Mohtat pouch based on chemistry.",
            "Enertech LCO observations are not assigned to Kokam SLPB78205130H / Marquis2019.",
            "Kokam SLPB75106100 / Ecker2015 and SLPB78205130H / Marquis2019 are distinct models.",
            "COMSOL outputs and drive-cycle input profiles are not counted as measured full-cell observations.",
        ],
    }
    write_json("matching_audit.json", audit)
    document["release"] = "0.4.0"
    for filename, value in [
        ("catalog.json", document),
        ("sources.json", sources),
        ("assets.json", assets),
        ("cells.json", cells),
        ("materials.json", materials),
        ("parameters.json", {"schema_version": "0.1", "records": parameters}),
        ("full_cell_tests.json", {"schema_version": "0.1", "records": tests}),
    ]:
        write_json(filename, value)
    print(
        f"Full-cell expansion: {len(document['records'])} OCPs, {len(parameters)} parameters, {len(tests)} test files, {len(cells)} cells/model entries."
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    extend(parser.parse_args().download)
