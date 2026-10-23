"""Offline O'Regan LG M50 extraction: experimental tables and separate model inputs.

Read pinned originals with an AST allowlist; never execute downloaded source.
The three suspect DSC/Cp CSVs stay quarantined in the source archive.
"""

import ast
import copy
import csv
import hashlib
import io
import json
import re
import zipfile

import numpy as np

from seed_v01 import DATA, ROOT, write_json
from seed_fullcell import audit_links, write_csv
from seed_materials import MathTranscriber, R, read_module, ocp_record
from seed_parameter_sources import slug

CID = "lg-m50-oregan2022"
SID = "oregan-2021-data"
SCRIPT = "scripts/seed_oregan.py"


class SourceMath(MathTranscriber):
    """Small importer-only extension for constant arrays and named local helpers."""

    def __init__(self, variables, scalars, functions):
        super().__init__(variables, scalars)
        self.functions = functions

    def resolve(self, node):
        if isinstance(node, ast.Attribute) and ast.unparse(node) in {"pybamm.constants.k_b", "pybamm.constants.q_e"}:
            return ast.Constant({"pybamm.constants.k_b":1.380649e-23, "pybamm.constants.q_e":1.602176634e-19}[ast.unparse(node)])
        if isinstance(node, ast.Dict) and all(isinstance(k,ast.Constant) and isinstance(k.value,str) for k in node.keys):
            return ast.Dict(keys=copy.deepcopy(node.keys), values=[self.resolve(v) for v in node.values])
        if isinstance(node, ast.Call) and not node.keywords:
            name = ast.unparse(node.func)
            if name == "np.cosh" and len(node.args) == 1:
                value = self.resolve(node.args[0])
                return ast.parse(f"(exp({ast.unparse(value)})+exp(-({ast.unparse(value)})))/2",mode="eval").body
            if name == "pybamm.FunctionParameter" and len(node.args) == 2 and isinstance(node.args[0],ast.Constant) and node.args[0].value == "Electrolyte conductivity [S.m-1]":
                inputs = self.resolve(node.args[1])
                if not isinstance(inputs,ast.Dict) or [k.value for k in inputs.keys] != ["Electrolyte concentration [mol.m-3]","Temperature [K]"]:
                    raise ValueError("Changed Ecker conductivity dependency")
                child = SourceMath({},self.scalars,{})
                child.bindings = dict(zip(["c_e","T"],inputs.values))
                return ast.parse(child.transcribe(self.functions["electrolyte_conductivity_Ecker2015"]),mode="eval").body
            if name == "np.array" and len(node.args) == 1:
                values = ast.literal_eval(node.args[0])
                if not isinstance(values, list) or not all(type(x) in (int, float) for x in values):
                    raise ValueError("Only constant numeric coefficient arrays allowed")
                return ast.Tuple(elts=[ast.Constant(x) for x in values], ctx=ast.Load())
            if name == "pybamm.sqrt" and len(node.args) == 1:
                return ast.Call(func=ast.Name(id="sqrt", ctx=ast.Load()), args=[self.resolve(node.args[0])], keywords=[])
            if name in self.functions and name.startswith("electrolyte_") and "_base_" in name:
                helper = self.functions[name]
                if len(helper.args.args) != len(node.args):
                    raise ValueError("Helper signature changed")
                child = SourceMath({}, self.scalars, {})  # No recursive helper execution.
                child.bindings = {arg.arg: self.resolve(value) for arg, value in zip(helper.args.args, node.args)}
                return ast.parse(child.transcribe(helper), mode="eval").body
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            base = node.left
            try:
                power = ast.literal_eval(node.right)
            except (ValueError,TypeError):
                power = None
            arg = None
            if power == -2 and isinstance(base,ast.Call) and ast.unparse(base.func) == "np.cosh":
                arg = base.args[0]
            elif power == 2 and isinstance(base,ast.BinOp) and isinstance(base.op,ast.Div) and isinstance(base.left,ast.Constant) and base.left.value == 1 and isinstance(base.right,ast.Call) and ast.unparse(base.right.func) == "np.cosh":
                arg = base.right.args[0]
            if arg is not None:
                z=ast.unparse(self.resolve(arg))
                return ast.parse(f"1-tanh({z})**2",mode="eval").body
            left, right = self.resolve(node.left), self.resolve(node.right)
            if isinstance(left, ast.Constant) and left.value == 10 and not isinstance(right, ast.Constant):
                # exp(log(10)*f) is equivalent to 10**f, without variable exponents
                # in the bounded runtime language. No interpreter permission changes.
                return ast.Call(func=ast.Name(id="exp", ctx=ast.Load()), args=[ast.BinOp(
                    left=ast.Call(func=ast.Name(id="log", ctx=ast.Load()), args=[left], keywords=[]),
                    op=ast.Mult(), right=right)], keywords=[])
        return super().resolve(node)

    def transcribe(self, function):
        transformed = copy.deepcopy(function)
        for node in transformed.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Tuple):
                values = self.resolve(node.value)
                if not isinstance(values, ast.Tuple) or len(values.elts) != len(node.targets[0].elts):
                    raise ValueError("Only fixed coefficient tuple unpacking allowed")
                for target, value in zip(node.targets[0].elts, values.elts):
                    if not isinstance(target, ast.Name):
                        raise ValueError("Unsupported coefficient target")
                    self.bindings[target.id] = value
            else:
                # Process in source order, including coefficients defined before unpacking.
                partial = copy.deepcopy(function)
                partial.body = [node]
                if isinstance(node, ast.Return):
                    return super().transcribe(partial)
                if isinstance(node, ast.Assign):
                    if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
                        raise ValueError("Unsupported assignment")
                    self.bindings[node.targets[0].id] = self.resolve(node.value)
                elif not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)):
                    raise ValueError("Unsupported statement")
        raise ValueError("Missing return")


def record(rid, name, category, unit, aid, location, variant, license):
    return {"id": rid, "version": "1", "cell_id": CID, "name": name,
            "category": category, "unit": unit, "source_ids": [SID] if license == "CC-BY-4.0" else ["pybamm-25-4-2", "oregan-2022"],
            "provenance": {"asset_id": aid, "location": location,
                           "origin_status": "experimentally_derived_source_table" if license == "CC-BY-4.0" else "published_model_input; measured/fitted/borrowed/assumed origins differ"},
            "license": license, "independent_validation": False,
            "conditions": {"parameterization_variant": variant},
            "limitations": ["Study-specific LG M50 parameter, not M50T or M50LT.",
                            "Identical serialized half-cell/full-cell specimens not established; no independent model validation.",
                            "Experimental tables and published model inputs are alternatives, not a set to combine automatically."]}


def experimental_tables(path):
    records, quarantined = [], []
    with zipfile.ZipFile(path) as archive:
        for member in sorted(n for n in archive.namelist() if n.endswith(".csv")):
            raw = archive.read(member)
            try:
                text, encoding = raw.decode("utf-8-sig"), "utf-8-sig"
            except UnicodeDecodeError:
                text, encoding = raw.decode("cp1252"), "cp1252"
            rows = list(csv.reader(io.StringIO(text)))
            folder, filename = member.split("/")[-2:]
            if folder == "Specific Heat Capacity":
                values = np.array([float(row[1]) for row in rows[1:]])
                quarantined.append({"member": member, "status": "definition_unresolved",
                    "rows": len(values), "negative_values": int(np.sum(values < 0)),
                    "source_value_range": [float(values.min()), float(values.max())],
                    "reason": "Header claims J kg-1 K-1, but sign and magnitude are inconsistent with a physical specific heat capacity. No undocumented correction or substitution.",
                    "source_header": rows[0], "encoding": encoding})
                continue
            is_d = folder == "Solid-state Diffusivity"
            a = np.array([[float(value) for value in row[:5 if is_d else 2]] for row in rows[1:]])
            xi, yi = (1, 2) if is_d else (0, 1)
            order = np.argsort(a[:, xi], kind="stable")
            a = a[order]
            if not np.isfinite(a).all() or np.any(np.diff(a[:, xi]) <= 0):
                raise ValueError("Non-finite or duplicate experimental coordinate: " + member)
            category = {"Solid-state Diffusivity": "diffusion", "Exchange Current": "kinetics",
                        "Entropic Term": "thermodynamics", "Electronic Conductivity": "transport", "Thermal Conductivity": "thermal"}[folder]
            unit, scale = {"diffusion": ("m2.s-1", 1), "kinetics": ("A.m-2", 10),
                           "thermodynamics": ("V.K-1", .001), "transport": ("S.m-1", 1), "thermal": ("W.m-1.K-1", 1)}[category]
            xkey = "T" if category in {"transport", "thermal"} else "sto"
            rid = "oregan-data-" + slug(filename[:-4])
            p = record(rid, filename[:-4].replace("_", " "), category, unit, "oregan-data-archive", member, "oregan-experimental-tables", "CC-BY-4.0")
            side = "negative" if "Negative" in filename else "positive"
            specimen = re.search(r"Cell_?(00[12])", filename)
            temp = re.search(r"_(\d+)_?deg", filename)
            p["conditions"].update(electrode=side, specimen_id=specimen.group(1) if specimen else None,
                temperature_K=float(a[0,4]) if is_d else int(temp.group(1))+273.15 if temp else None,
                direction=("delithiation" if filename.endswith("_delit.csv") else "lithiation" if filename.endswith("_lit.csv") else "unspecified"),
                source_encoding=encoding, source_y_header=rows[0][yi], conversion_factor_to_native=scale)
            if is_d and not np.all(a[:,4] == p["conditions"]["temperature_K"]):
                raise ValueError("Mixed temperatures in source table")
            columns = ["x", "value", "source_csv_row", "source_value"]
            values = [[row[xi], row[yi]*scale, int(index)+2, row[yi]] for index, row in zip(order, a)]
            if is_d:
                columns += ["source_capacity_mAh_cm2", "source_R_squared", "source_temperature_K"]
                values = [v+[row[0], row[3], row[4]] for v,row in zip(values,a)]
            relative = f"parameter_tables/{rid}.csv"
            digest = write_csv(relative, columns, values)
            p["representation"] = {"kind": "table", "path": relative, "sha256": digest, "point_count": len(a),
                "x": {"column": "x", "variable": xkey, "unit": "K" if xkey == "T" else "1",
                      "kind": "source_temperature" if xkey == "T" else "source_reported_stoichiometry",
                      "domain": [float(a[0,xi]), float(a[-1,xi])],
                      "definition": rows[0][xi] + "; ascending order, no resampling or extrapolation."},
                "y_column": "value", "default_interpolation": "linear"}
            p["definition"] = ("Source-derived GITT solid diffusivity; R-squared is a fit-quality value, not an uncertainty interval." if is_d else
                               "Exchange-current density per source electrode area, not an intrinsic reaction constant; 1 mA/cm2 = 10 A/m2." if category == "kinetics" else
                               "Electrode OCP entropic coefficient; 1 mV/K = 0.001 V/K." if category == "thermodynamics" else rows[0][1].strip())
            records.append(p)
    if len(records) != 55 or len(quarantined) != 3:
        raise ValueError("Experimental inventory changed")
    return records, quarantined


def model_inputs(path):
    functions, values, scalars = read_module(path)
    records, curves = [], []
    for key, node in values.items():
        if key in {"chemistry", "citations"}:
            continue
        rid = "oregan-model-" + slug(key)
        if key.endswith("electrode OCP [V]"):
            side = "negative" if key.startswith("Negative") else "positive"
            p, _ = ocp_record(rid, "graphite" if side == "negative" else "NMC811", side,
                SourceMath({"sto":"x"}, scalars, functions).transcribe(functions[node.id]), node.id,
                "oregan-pybamm-code", ["pybamm-25-4-2", "chen-2020", "oregan-2022"], CID,
                evidence="O'Regan2022 explicitly reuses Chen2020 OCP functions; no new O'Regan half-cell OCP measurement is deposited.", origin="borrowed_Chen2020_model_expression")
            p["provenance"]["processing"]["script"] = SCRIPT
            curves.append(p)
            continue
        category = ("diffusion" if "diffusivity" in key else "kinetics" if any(s in key for s in ["exchange-current", "charge transfer", "double-layer"]) else
                    "thermodynamics" if "entropic" in key or key == "Thermodynamic factor" else
                    "transport" if "conductivity [S" in key or key == "Cation transference number" or "Bruggeman" in key else
                    "thermal" if any(s in key.lower() for s in ["heat", "temperature", "density", "thermal"]) else
                    "initial_state" if key.startswith("Initial") else
                    "operating_limits" if any(s in key for s in ["voltage", "capacity [A.h]", "Current function", "Contact resistance"]) else
                    "geometry" if any(s in key.lower() for s in ["thickness", "height", "width", "area", "volume", "radius", "connected"]) else "electrode")
        p = record(rid, key, category, key.split("[")[-1].rstrip("]") if "[" in key else "1", "oregan-pybamm-code",
                   "get_parameter_values::"+key if key in scalars else node.id,
                   "oregan-pybamm-v25-4-2", "BSD-3-Clause")
        p["conditions"]["reference_temperature_K"] = 298.15
        p["definition"] = key + "; published implementation convention retained. Defaults and borrowed laws are not new specimen measurements."
        if key in scalars:
            p["representation"] = {"kind": "scalar", "value": scalars[key]}
        else:
            fn = functions[node.id]
            names = [a.arg for a in fn.args.args]
            p["representation"] = {"kind": "expression", "expression": SourceMath({n:n for n in names}, scalars, functions).transcribe(fn),
                "variables": {n: {"sto":"1", "T":"K", "c_e":"mol.m-3", "c_s_surf":"mol.m-3", "c_s_max":"mol.m-3"}[n] for n in names},
                "domain": "Mathematical domain only: 0<=sto<=1; c_e>=0; c_s_max>0; 0<=c_s_surf<=c_s_max; T>0 where present. Experimental fit validity is not established by this domain.",
                "gas_constant_J_mol_K": R}
            if "Landesfeind" in node.id:
                p["provenance"]["origin_status"] = "borrowed_Landesfeind2019_EC_EMC_3_7_electrolyte_law"
            elif "CRC" in node.id:
                p["provenance"]["origin_status"] = "borrowed_CRC_material_law"
            p["limitations"] += ["AST coefficient substitution only; fixed 10**f is rewritten as exp(log(10)*f). Source porosity and reference concentration are inlined from this variant."]
        records.append(p)
    if len(curves) != 2 or len(records) != 73:
        raise ValueError("Published model inventory changed")
    return curves, records


def extend():
    load = lambda name: json.loads((DATA/(name+".json")).read_text())
    catalog, parameters = load("catalog"), load("parameters")["records"]
    sources, assets, cells, materials, audit = [load(n) for n in ["sources", "assets", "cells", "materials", "matching_audit"]]
    pins = json.loads((ROOT/"scripts/oregan_assets.json").read_text())
    for aid, asset in pins.items():
        if hashlib.sha256((DATA/asset["path"]).read_bytes()).hexdigest() != asset["sha256"]:
            raise ValueError("O'Regan checksum mismatch: "+aid)
        assets[aid] = asset
    sources[SID] = {"kind":"dataset", "title":"O'Regan thermal-electrochemical characterisation parameter tables", "authors":["Kieran O'Regan", "Ferran Brosa-Planella", "W. Dhammika Widanage", "Emma Kendrick"],
        "year":2021, "url":"https://zenodo.org/records/5171874", "doi":"10.5281/zenodo.5171874", "version":"1.0; fixed record 5171874", "license":"CC-BY-4.0",
        "license_evidence":"Packaged fixed-record API metadata reports cc-by-4.0; source archive checksum preserved.", "role":"55 native experimental parameter tables; three suspect Cp files quarantined in original archive; no full-cell traces in this ZIP."}
    sources["oregan-2022"] = {"kind":"paper", "title":"Thermal-electrochemical parameters of a high energy lithium-ion cylindrical battery", "authors":["Kieran O'Regan", "Ferran Brosa-Planella", "W. Dhammika Widanage", "Emma Kendrick"],
        "year":2022, "doi":"10.1016/j.electacta.2022.140700", "url":"https://doi.org/10.1016/j.electacta.2022.140700", "role":"LG M50 study context. Native formulas redistributed from BSD-licensed PyBaMM, not the article PDF."}
    source_note=" ORegan2022 is also pinned; Chen OCP, CRC and Landesfeind origins remain explicit."
    if source_note not in sources["pybamm-25-4-2"]["role"]:sources["pybamm-25-4-2"]["role"] += source_note
    table_params, quarantined = experimental_tables(DATA/pins["oregan-data-archive"]["path"])
    curves, model_params = model_inputs(DATA/pins["oregan-pybamm-code"]["path"])
    catalog["records"] = [r for r in catalog["records"] if r["cell_link"]["cell_id"] != CID]+curves
    parameters = [p for p in parameters if p["cell_id"] != CID]+table_params+model_params
    cell = {"manufacturer":"LG Chem", "model":"M50", "display_name":"LG M50 | O'Regan2022 characterization and model", "format":"21700 cylindrical", "chemistry":"NMC811/graphite-SiOx", "nominal_capacity_Ah":5.0,
        "identity_level":"explicit_commercial_model", "source_ids":[SID,"oregan-2022","pybamm-25-4-2"], "model_context":"Experimental tables and separately labeled published DFN/SPM/SPMe model inputs", "match_level":"same_model_same_study",
        "match_evidence":"Parameter tables and published model refer to LG M50. OCP functions are borrowed from Chen2020. TEC/Chen full-cell comparisons are separate studies; same serialized specimens are not established.",
        "coverage":{"ocp":"Two stored Chen2020 expressions explicitly reused by O'Regan; no new measured OCP table in this deposit.", "diffusion":"40 experimental tables: two electrodes, two specimens, five temperatures, two directions; plus two separately labeled model laws and a borrowed electrolyte law.",
                    "kinetics":"Eight experimental i0 tables at 15/25/35/45 C; two separate concentration/temperature model laws and source charge-transfer/double-layer inputs.", "full_cell_tests":"External same-model Chen/TEC discovery links only; no same-specimen assertion or new full-cell payload."},
        "note":"Do not merge experimental-table and published-model variants automatically; M50, M50T and M50LT are distinct identities.",
        "quarantined_source_files":quarantined}
    audit_links({CID:cell}, catalog["records"], parameters, [])
    cell["missing_items"] += ["Three source Cp tables quarantined: physical definition/units unresolved", "Same-specimen full-cell mapping unresolved; linked comparisons are cross-study", "Original measured OCP points not deposited here; expressions are reused Chen2020 fits"]
    cells[CID] = cell
    audit["cell_matches"][CID] = {"display_name":cell["display_name"], "match_level":cell["match_level"], "components":cell["evidence_matrix"], "missing_items":cell["missing_items"]}
    audit["checked_date"] = "2026-10-23"
    for r in curves:
        materials[r["material_id"]] = {"chemistry":r["material"], "description":"Reused Chen2020 implementation function; not a new measured O'Regan electrode."}
    for name,value in [("catalog",catalog), ("parameters",{"schema_version":"0.1","records":parameters}), ("sources",sources), ("assets",assets), ("cells",cells), ("materials",materials), ("matching_audit",audit)]:
        write_json(name+".json",value)
    print("O'Regan: 55 experimental tables, 73 separate model parameters, 2 borrowed OCP expressions; 3 Cp files quarantined.")


if __name__ == "__main__":
    extend()
