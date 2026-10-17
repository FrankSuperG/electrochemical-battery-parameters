"""Curate MJ1 source tables without executing upstream simulation/fit code.

The workbook is authoritative for laboratory D/i0 values: its missing entries
must not become the zeros found in some processed Parquet exports.
"""

import argparse
import hashlib
import json
import re
import shutil

import numpy as np
import pandas as pd

from seed_v01 import CACHE, DATA, ROOT, base_record, obtain, write_json
from seed_fullcell import audit_links, write_csv
from xlsx_source import SourceWorkbook

CELL = "lg-mj1-dlr-sintef"
DIRECT = "mj1-zenodo-15497193"
PAPER = "kuhn-2026-workflows"
SCRIPT = "scripts/seed_mj1.py"
GAPS = ["No same-study intact commercial MJ1 full-cell I/V/T validation series verified",
        "No standalone intact-cell constant-current charge/discharge observations imported",
        "Exact specimen chain between direct cell #001, GITT electrodes and an intact validation cell unresolved",
        "Source SOC/stoichiometry coordinates need explicit balancing before model use",
        "Exchange-current active/geometric area convention not independently established",
        "Independent electrochemical model validation not performed"]
# Workbook rows are an explicit selection, not a scrape of the simulation dict.
# (slug, name, row, scale, unit, category)
SCALARS = [
    ("negative-thickness", "Negative electrode coating thickness", 3, 1e-6, "m", "geometry"),
    ("negative-collector-thickness", "Negative current collector full thickness", 4, 1e-6, "m", "geometry"),
    ("positive-thickness", "Positive electrode coating thickness", 5, 1e-6, "m", "geometry"),
    ("positive-collector-thickness", "Positive current collector full thickness", 6, 1e-6, "m", "geometry"),
    ("original-separator-thickness", "Original commercial separator thickness", 7, 1e-6, "m", "geometry"),
    ("negative-total-area", "Reported negative electrode total area", 8, 1e-4, "m2", "geometry"),
    ("positive-total-area", "Reported positive electrode total area", 9, 1e-4, "m2", "geometry"),
    ("negative-porosity", "Negative electrode porosity", 11, 1, "1", "electrode"),
    ("positive-porosity", "Positive electrode porosity", 12, 1, "1", "electrode"),
    ("original-separator-porosity", "Original commercial separator porosity", 13, 1, "1", "electrode"),
    ("graphite-particle-diameter", "Graphite particle diameter", 23, 1e-6, "m", "geometry"),
    ("silicon-particle-diameter", "Silicon-phase particle diameter", 24, 1e-6, "m", "geometry"),
    ("positive-particle-diameter", "NMC particle diameter", 25, 1e-6, "m", "geometry"),
    ("negative-bet-area", "Negative electrode BET specific surface area", 26, 1000, "m2.kg-1", "geometry"),
    ("positive-bet-area", "Positive electrode BET specific surface area", 27, 1000, "m2.kg-1", "geometry"),
    ("negative-kinetic-activation-energy", "Negative exchange-current activation energy at source SOC15", 38, 1000, "J.mol-1", "kinetics"),
    ("positive-kinetic-activation-energy", "Positive exchange-current activation energy at source SOC50", 39, 1000, "J.mol-1", "kinetics"),
    ("negative-diffusion-activation-energy", "Negative diffusion activation energy at source SOC15", 41, 1000, "J.mol-1", "diffusion"),
    ("positive-diffusion-activation-energy", "Positive diffusion activation energy at source SOC50", 42, 1000, "J.mol-1", "diffusion"),
    ("negative-electronic-conductivity", "Negative electrode electronic conductivity", 43, 1, "S.m-1", "transport"),
    ("positive-electronic-conductivity", "Positive electrode electronic conductivity", 44, 1, "S.m-1", "transport"),
]


def workbook_selection(original, source):
    """Select authored laboratory cells; exclude the literature-containing OCV sheet."""
    w = SourceWorkbook(original)
    physical = w.read("physical_quantities")
    return {"source_asset_id": "mj1-workbook", "source_sha256": source["sha256"],
            "source_md5": source["md5"],
            "scope": "Selected laboratory cells only. Entire OCV/electrolyte sheets excluded; no literature silicon OCV columns.",
            "sheets": {"physical_quantities": {str(row): physical[row] for _,_,row,_,_,_ in SCALARS},
                       "cell_specifications": {"9": w.read("cell_specifications")[9]},
                       "Di": {str(k):v for k,v in w.read("Di").items()},
                       "i0": {str(k):v for k,v in w.read("i0").items()}}}


def extend(download=False):
    load = lambda n: json.loads((DATA / (n+".json")).read_text())
    doc, params = load("catalog"), load("parameters")["records"]
    cells, sources, assets, materials, experiments, audit = [load(n) for n in ["cells", "sources", "assets", "materials", "experiments", "matching_audit"]]
    doc["records"] = [r for r in doc["records"] if r["cell_link"]["cell_id"] != CELL]
    params = [p for p in params if p["cell_id"] != CELL]
    pins = json.loads((ROOT / "scripts/mj1_assets.json").read_text())
    CACHE.mkdir(parents=True, exist_ok=True)
    for aid, asset in pins.items():
        if asset.get("role") == "workbook_cell_selection":
            continue
        if asset.get("path"):
            path = DATA / asset["path"]
            if not path.exists():
                original = obtain(asset["filename"], asset["url"], sha256=asset["sha256"], md5=asset.get("md5"), download=download)
                shutil.copyfile(original, path)
            b = path.read_bytes()
            if hashlib.sha256(b).hexdigest() != asset["sha256"] or asset.get("md5") and hashlib.md5(b).hexdigest() != asset["md5"]:
                raise ValueError(f"Source checksum mismatch: {aid}")
        assets[aid] = asset
    selection_asset = pins["mj1-workbook-selection"]
    original = CACHE / pins["mj1-workbook"]["filename"]
    selected_path = DATA / selection_asset["path"]
    if original.exists() or download:
        source = pins["mj1-workbook"]
        original = obtain(source["filename"],source["url"],md5=source["md5"],sha256=source["sha256"],download=download)
        selected = workbook_selection(original,source)
        selected_path.write_text(json.dumps(selected,ensure_ascii=False,indent=2)+"\n")
    else:
        selected = json.loads(selected_path.read_text())
    if hashlib.sha256(selected_path.read_bytes()).hexdigest() != selection_asset["sha256"] or selected["source_sha256"] != pins["mj1-workbook"]["sha256"]:
        raise ValueError("Workbook cell-selection evidence mismatch")
    assets["mj1-workbook-selection"] = selection_asset
    for aid, asset in pins.items():
        if asset.get("role") != "record_metadata":
            continue
        d = json.loads((DATA / asset["path"]).read_text())
        m = d["metadata"]
        if m["license"]["id"] != "cc-by-4.0":
            raise ValueError("Unexpected MJ1 license")
        sources[asset["source_id"]] = {"kind": "dataset", "title": m["title"], "authors": [x["name"] for x in m["creators"]],
            "year": 2025, "version": f"Zenodo fixed record {d['id']}; {m.get('version', 'version not supplied')}", "doi": m["doi"],
            "url": f"https://zenodo.org/records/{d['id']}", "license": "CC-BY-4.0",
            "license_evidence": f"Packaged fixed-record API metadata {asset['path']}: metadata.license.id=cc-by-4.0; source file MD5 checked against that record.",
            "role": "Same MJ1 characterization collection. Harvested/reassembled electrode characterization, not proof of intact commercial-cell validation."}
    sources[PAPER] = {"kind": "paper", "title": "Workflows and principles for collaboration and communication in battery research",
        "authors": sources[DIRECT]["authors"], "year": 2026, "doi": "10.1039/D5DD00247H", "url": "https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00247h", "license": "CC-BY-3.0",
        "role": "Digital Discovery 2026, 5, 177-192; first published 2025-11-05. Section 3.4 establishes harvested/reassembled three-electrode configuration, replacement separator and 25 degC chamber."}
    def path(aid): return DATA / pins[aid]["path"]
    sheets = {name:{int(k):v for k,v in rows.items()} for name,rows in selected["sheets"].items()}
    physical = sheets["physical_quantities"]
    new_params = []
    common = ["Same model/study association; exact serialized specimen linkage to intact validation tests unresolved.",
              "Partial characterization package; not a complete independently validated commercial-cell parameter set."]
    def parameter(rid, name, category, unit, aid, location, origin, definition, conditions):
        return {"id": rid, "version": "1", "cell_id": CELL, "name": name, "category": category, "unit": unit,
                "source_ids": [pins[aid]["source_id"], PAPER], "provenance": {"asset_id": aid, "location": location, "origin_status": origin},
                "license": "CC-BY-4.0", "independent_validation": False, "definition": definition, "conditions": conditions,
                "limitations": list(common)}
    for slug, name, row, factor, unit, category in SCALARS:
        source = physical[row]
        p = parameter("mj1-"+slug, name, category, unit, "mj1-workbook", f"MJ1_parameters.xlsx::physical_quantities!F{row}",
                      "reported_laboratory_result; source method retained", name+"; source description/measurement method retained without model substitution.",
                      {"parameterization_variant": "direct-laboratory", "source_row": row, "source_unit": source["G"], "unit_multiplier": factor,
                       "source_method": source.get("H"), "source_comment": source.get("I"), "assembly_scope": "Harvested original component; original separator differs from the 260 um replacement used in GITT"})
        p["representation"] = {"kind": "scalar", "value": float(source["F"])*factor}
        if source.get("H") == "\u00b5CT":
            p["provenance"]["origin_status"] = "reported_microstructure_estimate; later paper uses external Heenan MJ1 tomography"
            p["conditions"]["specimen_scope"] = "Microstructure image lineage is external in the paper; not independently tied to harvested cell #001"
            p["limitations"].append("Paper microstructure reconstruction uses Heenan et al. MJ1 images; these particle diameters are not asserted as same-specimen measurements of cell #001.")
        if "activation-energy" in slug:
            p["limitations"].append("Activation energy is reported at one source SOC; no general Arrhenius extension of the entire table is constructed.")
        new_params.append(p)
    cap = sheets["cell_specifications"][9]
    p = parameter("mj1-nominal-capacity", "Nominal commercial cell capacity", "operating_limits", "Ah", "mj1-workbook", "MJ1_parameters.xlsx::cell_specifications!D9",
                  "reported_nominal_specification", "Commercial nominal capacity, not the reassembled 18 mm electrode cell's measured capacity.", {"parameterization_variant": "direct-laboratory"})
    p["representation"] = {"kind": "scalar", "value": cap["D"]}
    new_params.append(p)

    def table(p, x, y, x_kind, variable, xunit, extra=None):
        x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
        order = np.argsort(x, kind="stable")
        x, y = x[order], y[order]
        if len(x)<2 or not np.isfinite(x).all() or not np.isfinite(y).all() or np.any(np.diff(x)<=0) or np.any(y<=0):
            raise ValueError("Invalid positive parameter observations")
        columns = [variable, "value"] + list(extra or {})
        values = [x,y] + [np.asarray(v)[order] for v in (extra or {}).values()]
        relative = f"parameter_tables/{p['id']}.csv"
        digest = write_csv(relative, columns, zip(*values))
        p["representation"] = {"kind": "table", "path": relative, "sha256": digest, "point_count": len(x),
            "x": {"column": variable, "variable": variable, "unit": xunit, "kind": x_kind, "domain": [float(x[0]),float(x[-1])],
                  "definition": "Source electrode SOC/stoichiometry coordinate; not automatically full-cell SOC or verified absolute lithium fraction."},
            "y_column": "value", "default_interpolation": "linear"}
        p["limitations"].append("Arithmetic linear interpolation of retained nodes only; no extrapolation. Coordinate mapping and model conventions remain the caller's responsibility.")
        new_params.append(p)
    for sheet, category, unit, scale in [("Di", "diffusion", "m2.s-1", 1e-4), ("i0", "kinetics", "A.m-2", 10)]:
        rows = sheets[sheet]
        for col, side, branch in [("C","negative","discharging"),("D","negative","charging"),("E","positive","discharging"),("F","positive","charging")]:
            valid = [(n, r) for n,r in rows.items() if n>=5 and isinstance(r.get("B"),(int,float)) and isinstance(r.get(col),(int,float))]
            if any(float(r[col])<=0 for _,r in valid): raise ValueError("Unexpected nonpositive workbook observation")
            rid = f"mj1-lab-{side}-{sheet.lower()}-{branch}"
            p = parameter(rid, f"{side.title()} electrode {'diffusivity' if sheet=='Di' else 'exchange-current density'} | source {branch}", category, unit,
                "mj1-workbook", f"MJ1_parameters.xlsx::{sheet}!B5:B41,{col}5:{col}41", "laboratory_GITT_estimate" if sheet=="Di" else "laboratory_EIS_derived_exchange_current_density",
                "Reported electrode coefficient versus source SOC; charging/discharging is the original branch label, not a new electrode-direction inference.",
                {"parameterization_variant": "direct-laboratory", "source_branch": branch, "electrode": side, "source_unit": "cm2.s-1" if sheet=="Di" else "mA.cm-2", "unit_multiplier": scale,
                 "missing_source_rows": [n for n in range(5,42) if n not in {n for n,_ in valid}], "chamber_setpoint_K": 298.15, "temperature_scope": "Paper experimental setting; no measured temperature array",
                 "area_basis": "Source-reported area basis; active versus geometric area not independently established" if sheet=="i0" else "Not applicable"})
            p["limitations"].append("Workbook NA/blanks are omitted, never zero-filled; corresponding Parquet exports contain zero/NaN substitutions and rounded values.")
            table(p, [r["B"] for _,r in valid], [r[col]*scale for _,r in valid], "source_electrode_soc", "source_soc_percent", "%", {"source_excel_row": [n for n,_ in valid]})
    for aid, asset in pins.items():
        if asset.get("role") != "gitt_diffusion_fit": continue
        d = json.loads(path(aid).read_text())
        side = "Negative" if "negative-" in asset["source_filename"] else "Positive"
        match = re.search(r"_(de)?lithiation_from_(SPM|SPMe|DFN)\.json$", asset["source_filename"])
        direction, model = ("delithiation" if match[1] else "lithiation"), match[2]
        xkey, ykey = f"{side} electrode SOC [-]", f"{side} electrode diffusivity [m2.s-1]"
        bounds = np.asarray(d["error bounds of "+ykey], dtype=float)
        if bounds.shape != (len(d[xkey]),2) or not np.isfinite(bounds).all() or np.any(bounds<=0) or np.any(bounds[:,0]>np.asarray(d[ykey])) or np.any(bounds[:,1]<np.asarray(d[ykey])):
            raise ValueError("Invalid source error bounds")
        rid = f"mj1-gitt-{side.lower()}-{model.lower()}-{direction}"
        p = parameter(rid, f"{side} electrode diffusivity | {model} | {direction}", "diffusion", "m2.s-1", aid, asset["source_filename"],
                      "EP-BOLFI_model_dependent_GITT_fit", "Fitted effective solid diffusivity under the named model and direction; source SOC alignment retained.",
                      {"parameterization_variant": f"gitt-{model.lower()}-{direction}", "model": model, "direction": direction, "electrode": side.lower(),
                       "uncertainty": "Original lower/upper error bounds retained per node; no coverage probability assigned or interpolated.", "temperature_note": "Paper chamber setting 25 degC; no temperature trace imported"})
        p["limitations"].append("SPM, SPMe and DFN fits are alternatives, not independent measurements or interchangeable inputs. Broad error bounds remain visible.")
        table(p,d[xkey],d[ykey],"source_reported_stoichiometry","source_sto","1",{"source_error_lower":bounds[:,0],"source_error_upper":bounds[:,1],"source_record":np.arange(len(bounds))+1})
    evidence = "Explicit LG MJ1 model and common DLR/SINTEF collection. Direct characterization identifies harvested cell #001; fit records link to their GITT processing chain. No intact-cell validation specimen correspondence established."
    for side, material in [("negative","Graphite-SiOx"),("positive","NMC")]:
        mid = f"mj1-{side}-material"
        materials[mid] = {"name": material, "family": material, "note": "Source MJ1 harvested electrode; NMC ratio differs between laboratory workbook and later paper, so no exact composition is assigned."}
        for branch in ["charging","discharging"]:
            aid = f"mj1-ocp-{side}-{branch}"
            frame = pd.read_parquet(path(aid))
            a = frame[["stoichiometry_unit_one","voltage_volt"]].to_numpy(dtype=float)
            finite = np.isfinite(a).all(axis=1)
            indices = np.flatnonzero(finite)
            # Stable first occurrence, then sort native x; no fitting or smoothing.
            _, first = np.unique(a[finite,0],return_index=True)
            selected = indices[first]
            x,y = a[selected].T
            rid = f"mj1-{side}-ocp-{branch}"
            r = base_record(rid,material)
            r.update(title=f"LG MJ1 {material} | source {branch} | pseudo-OCP",material_id=mid,electrode_role=side,
                     direction="unspecified",measurement="pseudo_ocp",license="CC-BY-4.0",source_ids=[DIRECT,PAPER])
            r["temperature"] = {"value_K": None,"description":"Paper reports 25 degC chamber; no per-node temperature or separate file setpoint verified."}
            r["x"] = {"kind":"source_reported_stoichiometry","symbol":"x","unit":"1","domain":[float(x[0]),float(x[-1])],
                      "definition":"Native stoichiometry_unit_one from the source Parquet; calibration to absolute lithium fraction not independently verified. Not full-cell SOC or branch progress.",
                      "domain_basis":"Finite retained native endpoints; no extrapolation or endpoint reconstruction."}
            rel = f"curves/{rid}.csv"
            digest = write_csv(rel,["x","potential_V","source_parquet_row"],zip(x,y,selected+1))
            r["representation"] = {"kind":"table","path":rel,"sha256":digest,"point_count":len(x),"default_interpolation":"linear"}
            r["cell_link"] = {"cell_id":CELL,"relationship":"same_model","evidence":evidence}
            r["provenance"] = {"asset_ids":[aid,"mj1-workbook","mj1-direct-jsonld"],"derivation":"source_pseudo_ocp_table_extraction",
                "location":pins[aid]["source_filename"],"processing":{"script":SCRIPT,"source_branch":branch,"source_rows":len(a),"nonfinite_rows_omitted":int((~finite).sum()),
                    "duplicate_coordinate_rows_omitted":int(finite.sum()-len(x)),"selection":"First source occurrence per finite coordinate; sort ascending; source_parquet_row is one-based. No smoothing or resampling."}}
            r["quality"] = {"source_review":"raw_file_checked","axis_status":"source_reported_stoichiometry","raw_data":"published_table_not_instrument_raw","model_status":"requires_stoichiometry_mapping","independent_validation":False}
            r["limitations"] = list(common)+["Finite-current pseudo-OCP; source metadata describes 0.05 C. Not a claimed equilibrium OCP.",
                "Source charging/discharging label retained in title/provenance; physical lithiation direction is left unspecified.",
                "Original Parquet/workbook retain discarded duplicate-coordinate voltages and missing rows; no coordinate or potential imputation.",
                "Reference versus lithium is documented in source JSON-LD; copied generic graphite descriptions for NMC are not used as material evidence."]
            doc["records"].append(r)
    params += new_params
    cell = {"manufacturer":"LG Chem","model":"MJ1","display_name":"LG MJ1 | DLR-SINTEF harvested-electrode characterization","format":"18650 commercial source; 18 mm harvested electrodes in laboratory cells",
        "chemistry":"NMC/Graphite-SiOx; exact NMC composition differs between source versions","nominal_capacity_Ah":3.5,"identity_level":"explicit_commercial_model",
        "source_ids":["mj1-zenodo-15407849",DIRECT,"mj1-zenodo-15496570","mj1-zenodo-15528177","mj1-zenodo-15538164","mj1-zenodo-15520717",PAPER],
        "model_context":"Laboratory characterization and direction/model-specific GITT fits; original components and reassembled-cell model settings are distinct",
        "match_level":"same_model_same_study","match_evidence":evidence,"curation_guide":"docs/LG_MJ1.md",
        "supporting_asset_ids":[aid for aid,a in pins.items() if a.get("path")],
        "note":"No same-study intact MJ1 full-cell trace imported. Three-electrode GITT is electrode-versus-Li voltage, with a 260 um replacement separator; it is not an original commercial-cell validation trace. Do not combine all diffusion variants.",
        "coverage":{"ocp":"Four laboratory pseudo-OCP tables, lithium reference; native reported coordinate requires explicit model balancing.",
                    "diffusion":"Four workbook GITT tables, twelve model/direction-dependent GITT fit tables with source error bounds, and two SOC-specific activation energies.",
                    "kinetics":"Four EIS-derived exchange-current tables and two SOC-specific activation energies; area-basis and concentration/temperature extension remain unresolved.",
                    "full_cell_tests":"No intact commercial-cell test verified. Structured anode GITT inspected: t/I/working-versus-Li voltage only, no measured T or intact-cell CC cycle."}}
    audit_links({CELL:cell},doc["records"],params,[])
    cell["missing_items"] = sorted(set(cell["missing_items"]+GAPS))
    for key in ["ocp","diffusion","kinetics"]:
        cell["evidence_matrix"][key]["missing_items"] += [GAPS[2],GAPS[3]]
    cell["evidence_matrix"]["kinetics"]["missing_items"].append(GAPS[4])
    cells[CELL] = cell
    audit["cell_matches"][CELL] = {"display_name":cell["display_name"],"match_level":cell["match_level"],"components":cell["evidence_matrix"],"missing_items":cell["missing_items"]}
    audit["checked_date"] = "2026-10-17"
    for rejection in ["MJ1 three-electrode working-versus-Li GITT is not intact commercial-cell terminal voltage or a full-cell validation trace.","MJ1 simulation substitutions, 260 um laboratory separator, inconsistent concentration units/initial states, and other-model tests are not imported as intact-cell measurements."]:
        if rejection not in audit["rejected_joins"]:audit["rejected_joins"].append(rejection)
    doc["release"] = "0.8.0"
    for n,v in [("catalog",doc),("parameters",{"schema_version":"0.1","records":params}),("cells",cells),("sources",sources),("assets",assets),("materials",materials),("experiments",experiments),("matching_audit",audit)]:write_json(n+".json",v)
    print(f"MJ1: 4 pseudo-OCP tables; {len(new_params)} parameter records; no intact full-cell test imported.")


if __name__ == "__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--download",action="store_true")
    extend(parser.parse_args().download)
