"""Transcribe BPX user-defined laws after reviewing pinned AEPyBaMM definitions.

No original author source is executed. Coefficient flags are function selectors,
not physical zero-valued parameters. The original BPX and parser are retained.
"""

import ast
import json

from seed_materials import F, R
from seed_parameter_sources import P45B, slug


def extract(data, pins):
    bpx = json.loads((data/pins["aepy-p45b-bpx"]["path"]).read_text())["Parameterisation"]
    user = bpx["User-defined"]
    definitions = []
    for name in ["Cation transference number", "Thermodynamic factor"]:
        if name+" func_type crosspoly" not in user:
            raise ValueError("Changed BPX cross-polynomial selector")
        terms = []
        for i in range(9):
            prefix = f"{name} poly.poly{i}."
            a,m,n = (user[prefix+k] for k in ["a","m","n"])
            terms.append(f"({a!r} * c_e**{m!r} * T**{n!r})")
        definitions.append((name, "+".join(terms), "transport" if name.startswith("Cation") else "thermodynamics", "1", ["c_e","T"]))
    name = "Electrolyte diffusivity [m2.s-1]"
    if name+" func_type Landesfeind2019_diff" not in user:
        raise ValueError("Changed diffusivity selector")
    p1,p2,p3,p4 = (user[name+f" p{i}"] for i in range(1,5))
    definitions.append((name, f"{p1!r} * exp({p2!r} * (c_e/1000)) * exp({p3!r}/T) * exp({p4!r}*(c_e/1000)/T)", "diffusion", "m2.s-1", ["c_e","T"]))
    name = "Electrolyte conductivity [S.m-1]"
    if name+" func_type Landesfeind2019_cond" not in user:
        raise ValueError("Changed conductivity selector")
    p1,p2,p3,p4,p5,p6 = (user[name+f" p{i}"] for i in range(1,7))
    definitions.append((name, f"({p1!r}*(1+T-{p2!r})*(c_e/1000))*(1+{p3!r}*sqrt(c_e/1000)+{p4!r}*(c_e/1000)*(1+{p5!r}*exp(1000/T)))/(1+(c_e/1000)**4*{p6!r}*exp(1000/T))", "transport", "S.m-1", ["c_e","T"]))

    class ReplaceX(ast.NodeTransformer):
        def visit_Name(self,node):
            return ast.parse("c_s_surf/c_s_max",mode="eval").body if node.id == "x" else node

    for phase, label in [("Graphite","Graphite"),("Silicon Additive","Silicon Additive")]:
        particle = bpx["Negative electrode"]["Particle"][phase]
        name = label+": Negative electrode exchange-current density"
        modifier = user[name+" pre-multiplier"]
        expression = ast.unparse(ast.fix_missing_locations(ReplaceX().visit(ast.parse(modifier,mode="eval"))))
        k = particle["Reaction rate constant [mol.m-2.s-1]"]
        ea = particle["Reaction rate constant activation energy [J.mol-1]"]
        tref = bpx["Cell"]["Reference temperature [K]"]
        expression = f"({expression}) * {F!r} * {k!r} * exp({ea!r}/{R!r}*(1/{tref!r}-1/T))"
        definitions.append((name+" [A.m-2]",expression,"kinetics","A.m-2",["c_e","c_s_surf","c_s_max","T"]))

    definitions.append(("Contact resistance [Ohm]",user["Contact resistance [Ohm]"],"operating_limits","Ohm",[]))
    output=[]
    for name, expression, category, unit, variables in definitions:
        rec={"id":"aepy-p45b-user-"+slug(name), "version":"1", "cell_id":P45B,
             "name":name, "category":category,"unit":unit,"source_ids":["aepy-p45b-2026"],
             "provenance":{"asset_id":"aepy-p45b-bpx","location":"Parameterisation/User-defined/"+name,
                           "origin_status":"author_defined_BPX_extension; parser checked in pinned aepy-func.py and aepy-params.py"},
             "license":"BSD-3-Clause","independent_validation":False,
             "definition":"Author-defined BPX extension with coefficients inlined from this P45B source. c_e is mol/m3, T is K. " +
                          ("This phase-specific i0 uses F*k*modifier(c_s/c_s_max)*Arrhenius; it is not a conventional concentration-power intrinsic k law." if category=="kinetics" else "Selector zeros are not measured zero transport coefficients."),
             "conditions":{"parameterization_variant":"aepy-bpx-1.1-dfn","reference_temperature_K":298.15,
                           "definition_asset_ids":["aepy-func-code","aepy-params-code"]},
             "limitations":["Published fitted implementation, not independently measured raw points or an independently validated complete model.",
                            "Use with the source composite-electrode model options; do not combine unrelated studies automatically.",
                            "Mathematical domain is not an established experimental validity interval; electrolyte fits can become unphysical outside their original range."]}
        rec["representation"] = ({"kind":"expression","expression":expression,
            "variables":{v:{"c_e":"mol.m-3","T":"K","c_s_surf":"mol.m-3","c_s_max":"mol.m-3"}[v] for v in variables},
            "domain":"c_e>=0; T>0; c_s_max>0 and 0<=c_s_surf<=c_s_max where present. Source-fit validity must be checked separately.","gas_constant_J_mol_K":R} if variables else
            {"kind":"scalar","value":expression})
        output.append(rec)
    return output
