"""Expand material coverage from pinned measurements and PyBaMM implementations.

No upstream Python code is executed by this importer. Simple mathematical
functions are transcribed with an AST allowlist and evaluated by ebp's interpreter.
"""

import ast
import copy
import csv
import hashlib
import json
import math
import operator
import re

import numpy as np
import pandas as pd

from seed_v01 import CACHE, DATA, ROOT, base_record, obtain, write_json
from seed_lgm50 import KEYS

R = 8.314462618
SETS = [
    {
        "name": "Marquis2019",
        "cell_id": "kokam-slpb78205130h-marquis2019",
        "positive": "LCO",
        "paper": "marquis-2019",
        "manufacturer": "Kokam",
        "model": "SLPB78205130H",
        "match_level": "parameter_set_only",
        "identity_level": "commercial_model_named_by_implementation",
        "ocp_origin": "Dualfoil1998 borrowed OCP implementation; no same-cell half-cell measurement match established",
        "note": "The upstream set names a Kokam model but borrows Dualfoil electrode functions. Model association does not establish that the OCP, diffusion or kinetics were measured on that commercial specimen.",
    },
    {
        "name": "Mohtat2020",
        "cell_id": "mohtat2020-nmc532-pouch",
        "positive": "NMC532",
        "paper": "mohtat-2020",
        "manufacturer": None,
        "model": None,
        "match_level": "parameter_set_only",
        "identity_level": "study_cell_family; commercial_part_undisclosed",
        "ocp_origin": "Peyman MPM / Mohtat2020 implementation, as attributed by upstream function docstrings",
        "note": "The implementation specifies a 5 Ah graphite/NMC532 pouch. Commercial manufacturer, part number, specimen mapping and matching raw full-cell files are not established in this release. SINTEF NMC532 half-cells are a separate source and are not assigned to this pouch.",
    },
    {
        "name": "NCA_Kim2011",
        "cell_id": "kim2011-nca-nominal-design",
        "positive": "NCA",
        "paper": "kim-2011",
        "manufacturer": None,
        "model": None,
        "match_level": "unmatched",
        "identity_level": "nominal_design_only",
        "ocp_origin": "Kim2011 nominal-design implementation",
        "note": "A nominal design, not an identified commercial cell. Upstream thermal properties combine Marquis2019 material inputs with effective-heat-capacity scaling; they are not independently measured NCA-cell material properties. No matching raw test is assigned.",
    },
]


class MathTranscriber:
    """Inline simple local math; reject executable or unresolved source constructs."""

    def __init__(self, variables, scalars):
        self.bindings = {
            name: ast.Name(id=alias, ctx=ast.Load())
            for name, alias in variables.items()
        }
        self.scalars = scalars

    def resolve(self, node):
        if isinstance(node, ast.Name):
            if node.id not in self.bindings:
                raise ValueError(f"Unresolved upstream variable: {node.id}")
            return copy.deepcopy(self.bindings[node.id])
        if isinstance(node, ast.Constant) and type(node.value) in (float, int):
            return copy.deepcopy(node)
        if (
            isinstance(node, ast.Attribute)
            and ast.unparse(node) == "pybamm.constants.R"
        ):
            return ast.Constant(R)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            operand = self.resolve(node.operand)
            if isinstance(operand, ast.Constant):
                return ast.Constant(
                    -operand.value if isinstance(node.op, ast.USub) else operand.value
                )
            return ast.UnaryOp(op=node.op, operand=operand)
        if isinstance(node, ast.BinOp) and type(node.op) in {
            ast.Add,
            ast.Sub,
            ast.Mult,
            ast.Div,
            ast.Pow,
        }:
            left, right = self.resolve(node.left), self.resolve(node.right)
            if isinstance(left, ast.Constant) and isinstance(right, ast.Constant):
                operations = {
                    ast.Add: operator.add,
                    ast.Sub: operator.sub,
                    ast.Mult: operator.mul,
                    ast.Div: operator.truediv,
                    ast.Pow: operator.pow,
                }
                value = operations[type(node.op)](left.value, right.value)
                if not math.isfinite(value):
                    raise ValueError("Non-finite source constant")
                return ast.Constant(value)
            return ast.BinOp(left=left, op=node.op, right=right)
        if isinstance(node, ast.Call) and not node.keywords and len(node.args) == 1:
            func = ast.unparse(node.func)
            if func in {"np.exp", "np.tanh", "np.log", "np.sqrt"}:
                return ast.Call(
                    func=ast.Name(id=func[3:], ctx=ast.Load()),
                    args=[self.resolve(node.args[0])],
                    keywords=[],
                )
            if func == "pybamm.Parameter" and isinstance(node.args[0], ast.Constant):
                key = node.args[0].value
                if key not in self.scalars:
                    raise ValueError(f"Unresolved upstream parameter: {key}")
                return ast.Constant(self.scalars[key])
        raise ValueError(f"Unsupported upstream math: {ast.unparse(node)}")

    def transcribe(self, function):
        for node in function.body:
            if (
                isinstance(node, ast.Expr)
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)
            ):
                continue
            if (
                isinstance(node, ast.Assign)
                and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
            ):
                self.bindings[node.targets[0].id] = self.resolve(node.value)
            elif isinstance(node, ast.Return):
                return ast.unparse(ast.fix_missing_locations(self.resolve(node.value)))
            else:
                raise ValueError(f"Unsupported upstream statement in {function.name}")
        raise ValueError("No return expression")


def read_module(path):
    functions = {
        f.name: f
        for f in ast.parse(path.read_text()).body
        if isinstance(f, ast.FunctionDef)
    }
    dictionary = next(
        n.value
        for n in functions["get_parameter_values"].body
        if isinstance(n, ast.Return)
    )
    values = {
        ast.literal_eval(k): v for k, v in zip(dictionary.keys, dictionary.values)
    }
    scalars = {}
    for key, node in values.items():
        try:
            value = ast.literal_eval(node)
        except (ValueError, TypeError):
            continue
        if type(value) in (int, float):
            scalars[key] = value
    return functions, values, scalars


def ocp_record(
    rid,
    material,
    role,
    expression,
    function,
    aid,
    source_ids,
    cell_id=None,
    relationship="material_only",
    evidence="No commercial full-cell identity established.",
    origin="upstream_formula_transcription",
):
    record = base_record(rid, material)
    mid = rid + "-material"
    record.update(
        title=f"{material} | {function} | implementation expression",
        material_id=mid,
        electrode_role=role,
        source_ids=source_ids,
        license="BSD-3-Clause",
    )
    record["x"] = {
        "kind": "stoichiometry",
        "symbol": "theta",
        "unit": "1",
        "domain": [0.0, 1.0],
        "definition": "Electrode lithium fraction c_s/c_s,max in the upstream function; not whole-cell SOC.",
        "domain_basis": "Mathematical 0..1 evaluation interval. Fit validity and usable operating stoichiometry limits have not been independently established; endpoint voltages may be outside cell operating limits.",
    }
    record["representation"] = {
        "kind": "expression",
        "expression": expression,
        "functions": sorted(
            {
                node.func.id
                for node in ast.walk(ast.parse(expression))
                if isinstance(node, ast.Call)
            }
        ),
        "source_function": function,
    }
    record["cell_link"] = {
        "cell_id": cell_id,
        "relationship": relationship,
        "evidence": evidence,
    }
    record["provenance"] = {
        "asset_ids": [aid],
        "derivation": origin,
        "location": function,
        "processing": {
            "script": "scripts/seed_materials.py",
            "changes": "AST-checked local-variable substitution; sto renamed to x. Numeric constants and mathematical operations retained. No upstream function is executed by the importer.",
        },
    }
    record["quality"] = {
        "source_review": "upstream_code_checked",
        "axis_status": "upstream_stoichiometry",
        "raw_data": "not_deposited_with_formula",
        "model_status": "ocp_component_only",
        "independent_validation": False,
    }
    record["limitations"] = [
        "An implementation expression, not original measured points or a newly fitted curve.",
        "The mathematical domain is not an experimentally verified validity range; do not use endpoint values as operating cutoffs.",
        "No separate lithiation/delithiation branch is supplied; no independent full-cell model validation is claimed.",
        evidence,
    ]
    return record, {"chemistry": material, "description": evidence}


def measured_branches(aid, asset, metadata):
    raw = obtain(
        asset["filename"], asset["url"], md5=asset["md5"], sha256=asset["sha256"]
    )
    frame = pd.read_parquet(raw)
    if not np.array_equal(frame.index.to_numpy(), np.arange(len(frame))):
        raise ValueError("Source index is not a zero-based row coordinate")
    meta = metadata.loc[metadata["BDF names"] == asset["filename"]].iloc[0]
    if pd.notna(meta["Known Issues"]):
        raise ValueError("Selected specimen needs a separate known-issue audit")
    sample_id = aid.split("-")[-1]
    eid, mid = aid + "-pocv", "sintef-" + asset["public_label"].lower()
    experiment = {
        "source_id": "sintef-2026-v3",
        "asset_id": aid,
        "sample_id": sample_id,
        "configuration": "Active electrode versus lithium metal, laboratory R2032 half-cell",
        "protocol": "p-OCV: C/50 constant current; 8 h rest at upper/lower cutoffs",
        "cycle_selected": 3,
        "cycle_selection_reason": "Fixed third recorded cycle for all selected specimens; not selected by fit quality.",
        "temperature_K": None,
        "temperature_description": "Room temperature in source; numeric setpoint unavailable.",
        "electrode_metadata": {
            k: None if pd.isna(v) else v.item() if hasattr(v, "item") else v
            for k, v in meta.items()
        },
        "known_issues": [],
    }
    material = {
        "chemistry": asset["material"],
        "description": f"SINTEF {asset['public_label']}; processing route, composition/loading and specimen identity retained in experiment metadata. No commercial full-cell match established.",
    }
    records = []
    for step in [2, 4]:
        branch = frame.loc[
            (frame["Cycle Count / 1"] == 3) & (frame["Step Index / 1"] == step)
        ].copy()
        if len(branch) < 100:
            raise ValueError("Insufficient branch measurements")
        dv = float(branch["Voltage / V"].iloc[-1] - branch["Voltage / V"].iloc[0])
        direction = "delithiation" if dv > 0 else "lithiation"
        if not np.all(
            np.sign(branch["Current / A"]) == (1 if direction == "delithiation" else -1)
        ):
            raise ValueError("Current sign and working-electrode direction disagree")
        before = len(branch)
        branch = branch.drop_duplicates("Cumulative Capacity / Ah", keep="first")
        q = branch["Cumulative Capacity / Ah"].to_numpy()
        if not np.all(np.diff(q) > 0):
            raise ValueError("Capacity does not increase strictly")
        x = (q - q[0]) / (q[-1] - q[0])
        rid = f"{aid}-c3-{direction}"
        path = DATA / "curves" / f"{rid}.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "x",
                    "potential_V",
                    "capacity_Ah",
                    "test_time_s",
                    "current_A",
                    "source_row",
                ]
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
        record = base_record(rid, asset["material"])
        record.update(
            title=f"{asset['material']} | {asset['public_label']} | {sample_id} | cycle 3 | {direction}",
            material_id=mid,
            electrode_role=asset["electrode_role"],
            direction=direction,
            measurement="pseudo_ocp",
            experiment_id=eid,
            source_ids=["sintef-2026-v3"],
            license="CC-BY-4.0",
        )
        record["temperature"] = {
            "value_K": None,
            "description": "Room temperature (source); numeric setpoint unavailable.",
        }
        record["x"] = {
            "kind": "normalized_branch_capacity",
            "symbol": "q_branch",
            "unit": "1",
            "domain": [0.0, 1.0],
            "definition": "(Q-Q_first)/(Q_last-Q_first) within this branch, increasing with test progress in both directions. Not absolute stoichiometry or whole-cell SOC.",
            "domain_basis": "Independent normalization of retained measured branch endpoints.",
        }
        record["representation"] = {
            "kind": "table",
            "path": f"curves/{rid}.csv",
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "point_count": len(branch),
            "default_interpolation": "linear",
        }
        record["provenance"] = {
            "asset_ids": [aid, "sintef-metadata"],
            "derivation": "constant_current_branch_extraction",
            "location": f"cycle=3; step={step}; source_row is the zero-based Parquet row coordinate",
            "processing": {
                "script": "scripts/seed_materials.py",
                "cycle": 3,
                "step": step,
                "input_branch_points": before,
                "retained_points": len(branch),
                "duplicate_capacity_points_removed": before - len(branch),
                "capacity_first_Ah": float(q[0]),
                "capacity_last_Ah": float(q[-1]),
                "mean_current_A": math.fsum(branch["Current / A"]) / len(branch),
                "direction_rule": "Li-metal half-cell: positive current with rising potential = delithiation; negative current with falling potential = lithiation.",
                "smoothing": "none",
                "resampling": "none",
                "potential_changes": "none; source floating-point values preserved",
                "rest_steps": "excluded; finite-current pseudo-OCP, not GITT equilibrium points",
            },
        }
        record["quality"] = {
            "source_review": "raw_file_checked",
            "axis_status": "relative_capacity_only",
            "raw_data": "external_checksum_pinned",
            "model_status": "requires_stoichiometry_mapping",
            "independent_validation": False,
        }
        record["limitations"] = [
            "C/50 pseudo-OCP includes finite-current polarization and is not claimed to be an equilibrium curve.",
            "Absolute stoichiometry and commercial full-cell association are unresolved.",
            "Branches are independently normalized; endpoints are not assumed to represent equal lithium content.",
            "Repeated specimens and branches are from one dataset, not independent literature sources.",
        ]
        records.append(record)
    return records, (eid, experiment), (mid, material)


def extend(download=False):
    load = lambda name: json.loads((DATA / name).read_text())
    document, sources, assets = (
        load("catalog.json"),
        load("sources.json"),
        load("assets.json"),
    )
    cells, materials, experiments = (
        load("cells.json"),
        load("materials.json"),
        load("experiments.json"),
    )
    parameters, tests = (
        load("parameters.json")["records"],
        load("full_cell_tests.json")["records"],
    )
    # Re-running this extension does not duplicate its own generated records.
    document["records"] = [
        r
        for r in document["records"]
        if r["provenance"]["processing"].get("script") != "scripts/seed_materials.py"
    ]
    parameters = [
        p for p in parameters if p["cell_id"] not in {s["cell_id"] for s in SETS}
    ]
    pins = json.loads((ROOT / "scripts/material_assets.json").read_text())
    metadata = pd.read_csv(CACHE / "metadata.csv", float_precision="round_trip")
    for aid, asset in pins.items():
        obtain(
            asset["filename"],
            asset["url"],
            md5=asset.get("md5"),
            sha256=asset["sha256"],
            download=download,
        )
        assets[aid] = asset
        if "material" in asset:
            records, (eid, experiment), (mid, material) = measured_branches(
                aid, asset, metadata
            )
            document["records"].extend(records)
            experiments[eid], materials[mid] = experiment, material
    sources.update(
        {
            "marquis-2019": {
                "kind": "paper",
                "title": "An asymptotic derivation of a single particle model with electrolyte",
                "authors": [
                    "Scott G. Marquis",
                    "Valentin Sulzer",
                    "Robert Timms",
                    "Colin P. Please",
                    "S. Jon Chapman",
                ],
                "year": 2019,
                "doi": "10.1149/2.0341915jes",
                "url": "https://doi.org/10.1149/2.0341915jes",
                "role": "Context of the Kokam SLPB78205130H parameter set. OCP, diffusion and kinetic function docstrings attribute their origin to Dualfoil; no same-cell measurement provenance is inferred.",
            },
            "dualfoil-attribution": {
                "kind": "software",
                "title": "Dualfoil electrode functions, as attributed by PyBaMM Marquis2019",
                "authors": ["John Newman / Dualfoil developers"],
                "year": 1998,
                "url": pins["pybamm-marquis2019-code"]["url"],
                "role": "Scientific/code origin named in upstream function docstrings. This URL identifies the checked redistributable PyBaMM transcription, not a separately audited Dualfoil release or original measurement deposit.",
            },
            "mohtat-2020": {
                "kind": "paper",
                "title": "Differential Expansion and Voltage Model for Li-ion Batteries at Practical Charging Rates",
                "authors": [
                    "Peyman Mohtat",
                    "Suhak Lee",
                    "Valentin Sulzer",
                    "Jason B. Siegel",
                    "Anna G. Stefanopoulou",
                ],
                "year": 2020,
                "doi": "10.1149/1945-7111/aba5d1",
                "url": "https://doi.org/10.1149/1945-7111/aba5d1",
                "role": "Graphite/NMC532 pouch parameter attribution via the pinned Mohtat2020 implementation; per-value original measurement/fit/borrowing origins and matching raw tests are not independently audited.",
            },
            "kim-2011": {
                "kind": "paper",
                "title": "Multi-domain modeling of lithium-ion batteries encompassing multi-physics in varied length scales",
                "authors": [
                    "Gi-Heon Kim",
                    "Kandler Smith",
                    "Kyu-Jin Lee",
                    "Shriram Santhanagopalan",
                    "Ahmad Pesaran",
                ],
                "year": 2011,
                "doi": "10.1149/1.3597614",
                "url": "https://doi.org/10.1149/1.3597614",
                "role": "Nominal-design graphite/NCA parameter attribution. Commercial identity and matching raw full-cell data are unresolved. Thermal inputs in the implementation include borrowed/scaled Marquis values.",
            },
        }
    )
    # Complete the existing LG M50 electrode pair with its own positive OCP.
    functions, values, scalars = read_module(CACHE / "Chen2020-v25.4.2.py")
    name = "nmc_LGM50_ocp_Chen2020"
    record, material = ocp_record(
        "nmc811-lgm50-chen2020-formula",
        "NMC811",
        "positive",
        MathTranscriber({"sto": "x"}, scalars).transcribe(functions[name]),
        name,
        "pybamm-chen-code",
        ["chen-2020", "pybamm-25-4-2"],
        "lg-m50",
        "same_model",
        "Same LG M50 model and Chen2020 study as the existing negative OCP and three full-cell test files. Identical characterization/validation specimen not established.",
    )
    document["records"].append(record)
    materials[record["material_id"]] = material
    cells["lg-m50"]["coverage"][
        "ocp"
    ] = "Both electrode OCP expressions available; effective graphite-SiOx negative and NMC811 positive"
    for spec in SETS:
        name, cid = spec["name"], spec["cell_id"]
        aid = "pybamm-" + name.lower() + "-code"
        functions, values, scalars = read_module(CACHE / pins[aid]["filename"])
        ids = [spec["paper"], "pybamm-25-4-2"]
        if name == "Marquis2019":
            ids.insert(0, "dualfoil-attribution")
        cells[cid] = {
            "manufacturer": spec["manufacturer"],
            "model": spec["model"],
            "display_name": f"{spec['model'] or name} | {spec['positive']}/graphite | {scalars['Nominal cell capacity [A.h]']:g} Ah model input",
            "format": "pouch",
            "chemistry": spec["positive"] + "/graphite",
            "nominal_capacity_Ah": scalars["Nominal cell capacity [A.h]"],
            "identity_level": spec["identity_level"],
            "match_level": spec["match_level"],
            "match_evidence": spec["note"],
            "source_ids": ids,
            "model_context": f"Partial {name} DFN/SPM/SPMe implementation inputs; model options and initialization still require review",
            "note": spec["note"],
            "coverage": {
                "ocp": spec["ocp_origin"],
                "diffusion": "Two Arrhenius particle-diffusivity functions, with source stoichiometry/temperature inputs retained",
                "kinetics": "Two concentration/temperature exchange-current laws; source area and concentration convention retained",
                "full_cell_tests": "No matching raw full-cell trace imported for this parameter set",
            },
        }
        for side, mat in [("Negative", "graphite"), ("Positive", spec["positive"])]:
            function = values[f"{side} electrode OCP [V]"].id
            record, material = ocp_record(
                f"{name.lower().replace('_','-')}-{mat.lower()}-ocp",
                mat,
                side.lower(),
                MathTranscriber({"sto": "x"}, scalars).transcribe(functions[function]),
                function,
                aid,
                ids,
                cid,
                "surrogate" if name == "Marquis2019" else "same_parameter_set",
                spec["ocp_origin"] + "; " + spec["note"],
            )
            if mat == "NCA":
                record["limitations"].append(
                    "The positive upstream function docstring incorrectly says Graphite. Electrode classification follows the positive-OCP dictionary entry and NCA parameter-set context; coefficients are unchanged."
                )
            document["records"].append(record)
            materials[record["material_id"]] = material
        for category, keys in KEYS.items():
            for key in keys:
                if key not in scalars:
                    if "particle diffusivity" in key:
                        continue
                    raise ValueError(f"Missing scalar selected for {name}: {key}")
                parameters.append(
                    {
                        "id": name.lower().replace("_", "-")
                        + "-"
                        + re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-"),
                        "version": "1",
                        "cell_id": cid,
                        "category": category,
                        "name": key,
                        "unit": key.split("[")[-1].rstrip("]") if "[" in key else "1",
                        "representation": {"kind": "scalar", "value": scalars[key]},
                        "source_ids": ids,
                        "provenance": {
                            "asset_id": aid,
                            "location": f"{name}.py::get_parameter_values::{key}",
                            "origin_status": "upstream_implementation_value; individual measurement/fit/borrowed/assumed origin not independently audited",
                        },
                        "license": "BSD-3-Clause",
                        "independent_validation": False,
                        "limitations": [
                            spec["note"],
                            "A partial model input collection, not a validated complete parameter set.",
                        ],
                        "conditions": {
                            "reference_temperature_K": scalars[
                                "Reference temperature [K]"
                            ]
                        },
                    }
                )
        for side in ["Negative", "Positive"]:
            for key, category, unit in [
                (f"{side} particle diffusivity [m2.s-1]", "diffusion", "m2.s-1"),
                (
                    f"{side} electrode exchange-current density [A.m-2]",
                    "kinetics",
                    "A.m-2",
                ),
            ]:
                function = functions[values[key].id]
                names = [arg.arg for arg in function.args.args]
                expression = MathTranscriber({n: n for n in names}, scalars).transcribe(
                    function
                )
                variables = {
                    n: {
                        "sto": "1",
                        "T": "K",
                        "c_e": "mol.m-3",
                        "c_s_surf": "mol.m-3",
                        "c_s_max": "mol.m-3",
                    }[n]
                    for n in names
                }
                parameters.append(
                    {
                        "id": name.lower().replace("_", "-")
                        + "-"
                        + side.lower()
                        + (
                            "-diffusivity"
                            if category == "diffusion"
                            else "-exchange-current-density"
                        ),
                        "version": "1",
                        "cell_id": cid,
                        "name": key,
                        "category": category,
                        "unit": unit,
                        "representation": {
                            "kind": "expression",
                            "expression": expression,
                            "variables": variables,
                            "domain": "Mathematical domain only: 0<=sto<=1 for diffusivity; c_e>=0, c_s_max>0, 0<=c_s_surf<=c_s_max for kinetics; T>0. Experimental validity range unestablished.",
                            "gas_constant_J_mol_K": R,
                        },
                        "source_ids": ids,
                        "provenance": {
                            "asset_id": aid,
                            "location": f"{name}.py::{function.name}",
                            "origin_status": (
                                "borrowed_dualfoil_implementation_function"
                                if name == "Marquis2019"
                                else "upstream_implementation_function; original equations and fit data not independently audited"
                            ),
                        },
                        "license": "BSD-3-Clause",
                        "independent_validation": False,
                        "definition": key
                        + "; retains the upstream particle/area/concentration convention",
                        "conditions": {
                            "reference_temperature_K": 298.15,
                            "resolved_source_electrolyte_reference_concentration_mol_m3": (
                                scalars[
                                    "Initial concentration in electrolyte [mol.m-3]"
                                ]
                                if name == "NCA_Kim2011" and category == "kinetics"
                                else None
                            ),
                        },
                        "limitations": [
                            spec["note"],
                            "AST-local substitutions preserve coefficients. Gas constant fixed at 8.314462618 J/mol/K.",
                            "Source parameters referenced within Kim kinetics are resolved from this same pinned set; this law is not an interchangeable rate constant.",
                        ],
                    }
                )
    for cid, cell in cells.items():
        cell["parameter_ids"] = [p["id"] for p in parameters if p["cell_id"] == cid]
        cell["ocp_record_ids"] = [
            r["id"] for r in document["records"] if r["cell_link"]["cell_id"] == cid
        ]
        cell["full_cell_test_ids"] = [t["id"] for t in tests if t["cell_id"] == cid]
    document["release"] = "0.3.0"
    for filename, value in [
        ("catalog.json", document),
        ("sources.json", sources),
        ("assets.json", assets),
        ("cells.json", cells),
        ("materials.json", materials),
        ("experiments.json", experiments),
        ("parameters.json", {"schema_version": "0.1", "records": parameters}),
    ]:
        write_json(filename, value)
    print(
        f"Material expansion: {len(document['records'])} OCP records across {len({r['material'] for r in document['records']})} material families, {len(parameters)} other parameters, {len(tests)} full-cell files."
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    extend(parser.parse_args().download)
