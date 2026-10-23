"""Finish numeric/analytic inputs of six already-curated PyBaMM parameter sets.

Do not infer new experimental cell matches from implementation defaults. Optional
SEI/plating/mechanics inputs remain explicitly modeled/borrowed assumptions.
"""

import ast
import hashlib
import json

from seed_v01 import DATA, ROOT, write_json
from seed_materials import R, read_module, ocp_record
from seed_fullcell import audit_links
from seed_oregan import SourceMath
from seed_parameter_sources import slug

SETS = {
    "Chen2020":"lg-m50", "Marquis2019":"kokam-slpb78205130h-marquis2019",
    "Mohtat2020":"mohtat2020-nmc532-pouch", "NCA_Kim2011":"kim2011-nca-nominal-design",
    "Ai2020":"enertech-lco-pouch-ai2020", "Ecker2015":"kokam-slpb75106100-ecker2015",
    "Prada2013":"prada2013-lfp-nominal-design"}
PREFIX = "model-completion-"
UNITS = {"sto":"1", "T":"K", "T_dim":"K", "c_e":"mol.m-3", "c_s_surf":"mol.m-3", "c_s_max":"mol.m-3", "c_Li":"mol.m-3", "L_sei":"m"}


def category(key):
    return ("diffusion" if "diffusiv" in key.lower() else
            "kinetics" if any(s in key.lower() for s in ["exchange-current", "kinetic", "charge transfer", "double-layer", "reaction rate"]) else
            "thermodynamics" if "entropic" in key or key == "Thermodynamic factor" else
            "transport" if any(s in key.lower() for s in ["conductivity [s", "bruggeman", "transport efficiency", "transference"]) else
            "initial_state" if key.startswith("Initial") else
            "thermal" if any(s in key.lower() for s in ["heat", "temperature", "density", "thermal", "emissivity"]) else
            "operating_limits" if any(s in key.lower() for s in ["voltage", "current function", "contact resistance", "cell capacity"]) else
            "geometry" if any(s in key.lower() for s in ["thickness", "width", "height", "centre", "area", "volume", "radius", "connected"]) else "electrode")


def extend():
    load = lambda n: json.loads((DATA/(n+".json")).read_text())
    params = [p for p in load("parameters")["records"] if not p["id"].startswith(PREFIX)]
    assets, cells, audit = [load(n) for n in ["assets","cells","matching_audit"]]
    catalog, materials = load("catalog"), load("materials")
    cid = SETS["Prada2013"]
    catalog["records"] = [r for r in catalog["records"] if r["cell_link"]["cell_id"] != cid]
    cells[cid] = {"manufacturer":None,"model":None,"display_name":"LFP 2.3 Ah | Prada2013 implementation | part unresolved",
        "format":"Not independently confirmed", "chemistry":"LFP/graphite", "nominal_capacity_Ah":2.3,
        "identity_level":"nominal_design_only", "source_ids":["pybamm-25-4-2"], "model_context":"Published Prada2013 LFP implementation inputs",
        "match_level":"parameter_set_only", "match_evidence":"One published implementation dictionary. Its LFP OCP is borrowed from Afshar2017 and negative OCP from Chen2020. No identified commercial cell or original same-study half-cell pair is established.",
        "note":"Do not infer A123 18650M1A, AMP20, 26650 m1b or the undisclosed BPX 2 Ah cell from chemistry/capacity; this is a separate nominal parameter set.",
        "coverage":{"ocp":"Two explicitly borrowed OCP implementation expressions; not new measured points.","diffusion":"Two source scalar solid diffusivities; no cell-specific measurement claim.","kinetics":"Two source exchange-current laws; original convention retained.","full_cell_tests":"No matching full-cell test source established."}}
    additions=[]
    for name,cid in SETS.items():
        aid = next(aid for aid,a in assets.items() if a["filename"] == name+"-v25.4.2.py")
        asset = assets[aid]
        relative = "evidence/"+asset["filename"]
        source = DATA/relative
        if hashlib.sha256(source.read_bytes()).hexdigest() != asset["sha256"]:
            raise ValueError("Source pin mismatch: "+name)
        asset["path"] = relative
        functions, values, scalars = read_module(source)
        if name == "Prada2013":
            for side,material,origin in [("Negative","graphite","Chen2020"),("Positive","LFP","Afshar2017")]:
                fn=functions[values[side+" electrode OCP [V]"].id]
                r,m=ocp_record("prada2013-"+side.lower()+"-borrowed-ocp",material,side.lower(),
                    SourceMath({"sto":"x"},scalars,functions).transcribe(fn),fn.name,aid,
                    ["pybamm-25-4-2","chen-2020" if side=="Negative" else "afshar-2017"],cid,
                    evidence="Borrowed "+origin+" function within the Prada2013 model; no common measured electrode pair or commercial specimen established.",origin="borrowed_implementation_function")
                r["provenance"]["processing"]["script"]="scripts/seed_model_completeness.py"
                catalog["records"].append(r);materials[r["material_id"]]=m
        for key,node in values.items():
            if key not in scalars and isinstance(node,ast.BinOp):
                value=ast.literal_eval(SourceMath({},scalars,functions).resolve(node))
                if type(value) in (float,int):scalars[key]=value
        existing = {p["name"] for p in params if p["cell_id"] == cid and not p["id"].startswith("mohtat-author-")}
        ids=[]
        for key,node in values.items():
            if key in existing or key in {"chemistry","citations"} or key.endswith("electrode OCP [V]"):
                continue
            rid = PREFIX+slug(name)+"-"+slug(key)
            optional = any(s in key.lower() for s in ["sei", "plating", "stripping", "plated", "dead lithium", "ec diffusivity", "ec initial", "solvent", "interstitial", "crack", "paris", "lam ", "stress", "poisson", "young", "lame", "deformation", "partial molar", "volume change"])
            p = {"id":rid, "version":"1", "cell_id":cid, "name":key,
                 "category":category(key), "unit":key.split("[")[-1].rstrip("]") if "[" in key else "1",
                 "source_ids":["pybamm-25-4-2"], "license":"BSD-3-Clause", "independent_validation":False,
                 "provenance":{"asset_id":aid, "location":f"{name}.py::get_parameter_values::{key}" if key in scalars else f"{name}.py::{node.id}",
                               "origin_status":"published_implementation_input; individual measurement/fit/borrowed/assumed origin not independently established"},
                 "conditions":{"parameterization_variant":"pybamm_v25_4_2" if name=="Mohtat2020" else slug(name)+"-pybamm-v25-4-2",
                               "model_set":name, "submodel_scope":"optional degradation/mechanics input" if optional else "electrochemical/thermal/circuit model input"},
                 "definition":key+"; literal value or function in the pinned upstream parameter dictionary. Native source units and conventions retained.",
                 "limitations":[cells[cid]["note"],
                     "Implementation input, not an assertion that this number was measured on this commercial cell. Source defaults, assumptions and borrowed submodels remain distinct from measured characterization.",
                     "Optional degradation/mechanics entries require their corresponding model options; including a parameter does not establish cell-specific ageing evidence or a validated model."]}
            if key in scalars:
                p["representation"]={"kind":"scalar","value":scalars[key]}
            else:
                fn=functions[node.id]
                aliases={a.arg:"T" if a.arg=="T_dim" else a.arg for a in fn.args.args}
                expression=SourceMath(aliases,scalars,functions).transcribe(fn)
                # Upstream optional arguments T_ref/t_plus are overwritten by source
                # assignments, so they are not independent inputs of this expression.
                free={n.id for n in ast.walk(ast.parse(expression)) if isinstance(n,ast.Name)} - {"exp","log","sqrt","tanh"}
                variables={alias:UNITS[original] for original,alias in aliases.items()
                           if original not in {"T_ref","t_plus"} or alias in free}
                p["representation"]={"kind":"expression","expression":expression,"variables":variables,
                    "domain":"Mathematical input domain only: 0<=sto<=1, nonnegative concentrations, c_s_max>0, c_s_surf<=c_s_max, T>0 and L_sei>0 where present. Fit validity must be checked independently.","gas_constant_J_mol_K":R}
                p["conditions"]["source_function"]=fn.name
                p["conditions"]["source_argument_aliases"]={k:v for k,v in aliases.items() if v in variables}
                p["conditions"]["source_function_docstring"]=ast.get_docstring(fn)
                p["limitations"] += ["AST local substitution only. sech(z)^2 becomes 1-tanh(z)^2 (roundoff may zero negligible tails). Ecker electrolyte conductivity dependency is inlined from the same pinned module. No downloaded source is executed."]
                if name=="Ai2020" and "graphite_entropy" in fn.name:
                    p["limitations"] += ["Source docstring gives fit range 0.43<sto<0.9936 and incorrectly calls the material LCO. Negative-electrode classification follows the dictionary entry, not that copied docstring."]
            additions.append(p);ids.append(rid)
        cell=cells[cid]
        cell["parameter_ids"]=[p["id"] for p in params+additions if p["cell_id"]==cid]
        cell["implementation_completion"]={"source_asset_id":aid,"parameter_ids":ids,
            "status":"All non-OCP numeric and analytic entries in this pinned dictionary are represented, including explicitly labeled optional submodels; string/citation metadata excluded."}
        audit["cell_matches"].setdefault(cid,{})["implementation_completion"]=cell["implementation_completion"]
    # The original MIT BPX example also contains three non-OCP expressions that
    # were previously skipped by its scalar-only import loop.
    aid="bpx-lfp-example"
    assets[aid]["path"]="evidence/"+assets[aid]["filename"]
    raw=DATA/assets[aid]["path"]
    if hashlib.sha256(raw.read_bytes()).hexdigest()!=assets[aid]["sha256"]:
        raise ValueError("BPX example checksum mismatch")
    bpx=json.loads(raw.read_text())
    cid="bpx-lfp-18650-2ah-undisclosed"
    for component,group in bpx["Parameterisation"].items():
        for key,value in group.items():
            if not isinstance(value,str) or key=="OCP [V]":continue
            variable="c_e" if component=="Electrolyte" else "sto"
            class Rename(ast.NodeTransformer):
                def visit_Name(self,node):
                    return ast.Name(id=variable,ctx=ast.Load()) if node.id=="x" else node
            expression=ast.unparse(ast.fix_missing_locations(Rename().visit(ast.parse(value,mode="eval"))))
            p={"id":PREFIX+"bpx-lfp-"+slug(component+"-"+key),"version":"1","cell_id":cid,"name":component+": "+key,
                "category":"diffusion" if "Diffusivity" in key else "thermodynamics" if "Entropic" in key else "transport",
                "unit":key.split("[")[-1].rstrip("]"),"source_ids":["bpx-lfp-2022"],"license":"MIT","independent_validation":False,
                "provenance":{"asset_id":aid,"location":"Parameterisation/"+component+"/"+key,"origin_status":"borrowed_Nyman2008_electrolyte_or_ORegan2022_entropic_fit; source header attribution"},
                "definition":"BPX v0.1 reference-temperature expression. x renamed to electrolyte concentration in mol/m3 or electrode lithium fraction; no additional Arrhenius factor applied here.",
                "conditions":{"parameterization_variant":"bpx-0.1-example","reference_temperature_K":298.15},
                "representation":{"kind":"expression","expression":expression,"variables":{variable:"mol.m-3" if variable=="c_e" else "1"},"domain":"Reference-temperature law only; c_e>=0 or 0<=sto<=1. Experimental validity not established.","gas_constant_J_mol_K":R},
                "limitations":[cells[cid]["note"],"Borrowed reference law, not a new measurement of this undisclosed cell. BPX activation-energy scalars are separate inputs; the expression itself is a reference-temperature law."]}
            additions.append(p)
    cells[cid]["parameter_ids"]=[p["id"] for p in params+additions if p["cell_id"]==cid]
    cid=SETS["Prada2013"]
    audit_links({cid:cells[cid]},catalog["records"],params+additions,[])
    audit["cell_matches"][cid]={"display_name":cells[cid]["display_name"],"match_level":cells[cid]["match_level"],"components":cells[cid]["evidence_matrix"],"missing_items":cells[cid]["missing_items"],"implementation_completion":cells[cid]["implementation_completion"]}
    for cid in list(SETS.values())+["bpx-lfp-18650-2ah-undisclosed"]:
        cell=cells[cid]
        for component in ["diffusion","kinetics"]:
            selected=[p for p in params+additions if p["cell_id"]==cid and p["category"]==component]
            if component in cell.get("evidence_matrix",{}):
                evidence=cell["evidence_matrix"][component]
                evidence["record_ids"]=[p["id"] for p in selected]
                evidence["source_ids"]=sorted({s for p in selected for s in p["source_ids"]})
                note=" Completed dictionary inputs may also include separately labeled electrolyte or optional SEI/plating coefficients; their presence is not electrode-specific measured diffusion/kinetics."
                if note not in evidence["evidence"]:evidence["evidence"] += note
        if cid in audit["cell_matches"]:audit["cell_matches"][cid]["components"]=cell["evidence_matrix"]
    for name,value in [("catalog",catalog),("materials",materials),("parameters",{"schema_version":"0.1","records":params+additions}), ("assets",assets), ("cells",cells), ("matching_audit",audit)]:
        write_json(name+".json",value)
    print(f"Existing model completeness: {len(additions)} additional parameters across {len(SETS)} pinned sets.")


if __name__=="__main__":
    extend()
