"""Curate ISU–UConn half/full-cell branches and Jahn2024 A123 model/test data.

Reads pinned XLSX/MAT/CSV values; never executes author notebooks or MATLAB.
Missing current/time/temperature are not reconstructed. OCPn model tables stay
distinct from measured pseudo-OCP and require an explicit coordinate mapping.
"""

import argparse
import copy
import csv
import hashlib
import json
import shutil

import numpy as np
from scipy.io import loadmat

from seed_v01 import CACHE, DATA, ROOT, base_record, obtain, write_json
from seed_fullcell import audit_links, write_csv
from xlsx_source import SourceWorkbook, capacity_blocks, column_after

ISU = "isu-uconn-lfp-graphite-lab"
A123 = "a123-18650m1a-jahn2024"
SCRIPT = "scripts/seed_lfp_studies.py"
ISU_DATA, ISU_CODE = "isu-uconn-2026-data", "isu-uconn-2026-code"
JAHN_DATA, JAHN_CODE = "jahn-2024-data-v2", "jahn-2024-code"
HEADERS = ["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K",
           "ambient_temperature_K", "cycle", "step", "mode", "source_record"]
COMMON_GAPS = ["Absolute measured temperature", "Ambient temperature trace",
               "Same-specimen file-to-electrode provenance unresolved",
               "Independent full-cell model reproduction not performed"]


def finite(values):
    a = np.asarray(values, dtype=float)
    if not np.isfinite(a).all():
        raise ValueError("Non-finite source observations")
    return a


def native_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {k: finite([r[k] for r in rows]) for k in rows[0]}


def test_record(rid, cid, sample, aid, asset, rows, extra, protocol, kind, evidence,
                current_present=False, charge=True, discharge=False, coordinate=None):
    columns = HEADERS + extra
    digest = write_csv(f"full_cell/{rid}-normalized.csv", columns, rows)
    return {
        "id": rid, "cell_id": cid, "sample_id": sample, "asset_id": aid,
        "source_id": asset["source_id"], "path": None,
        "original_download_path": asset["path"],
        "original_format": asset["path"].rsplit(".", 1)[1].upper(),
        "normalized_path": f"full_cell/{rid}-normalized.csv", "normalized_sha256": digest,
        "csv_header_rows": 0, "license": "CC-BY-4.0", "protocol": protocol,
        "relationship_to_parameters": "same_study_cell_family" if cid == ISU else "same_model_same_study",
        "evidence": evidence, "independent_validation_by_this_project": False,
        "observation_kind": "published_experimental_series", "row_count": len(rows),
        "columns": columns, "discharge_segments": [],
        "format": "Source branch/array extracted without smoothing or resampling; packaged original retained",
        "current_convention": ("Charge positive, discharge negative; supplied signed current retained and checked against stored-charge increments."
                               if current_present else "Measured current absent; blank is not zero and no current was inferred from capacity or C-rate."),
        "temperature_definition": ("25 degC chamber setting in Methods; no measured cell or ambient temperature trace."
                                   if cid == A123 else "No numeric temperature or sensor trace verified from the accessible workbook and author notebook."),
        "basic_test": {"type": kind, "current_measurement": "supplied" if current_present else "not_supplied",
                       "charge_trace": "available" if charge else "not_selected",
                       "voltage_trace": "available", "discharge_trace": "available" if discharge else "not_selected"},
        "missing_items": COMMON_GAPS + ([] if current_present else ["Measured current trace"]),
        **({"independent_variable": coordinate} if coordinate else {}),
    }


def empty_row(source, voltage, time="", current="", mode="U", step=""):
    return [time, current, voltage, "", "", "", step, mode, source]


def ocp_table(rid, material, x, y, source_ids, aids, cid, kind, coordinate, location, evidence):
    x, y = finite(x), finite(y)
    if len(x) != len(y) or np.any(np.diff(x) <= 0):
        raise ValueError("OCP nodes must have a strictly increasing source coordinate")
    record = base_record(rid, material)
    record.update(material_id=rid+"-material", measurement=kind, license="CC-BY-4.0", source_ids=source_ids)
    record["x"] = {"kind": coordinate, "symbol": "x", "unit": "1",
                   "domain": [float(x[0]), float(x[-1])],
                   "definition": "Author model SOC/DOL coordinate, not verified absolute electrode lithium fraction." if coordinate == "model_soc" else "Passed capacity normalized over this retained branch; not absolute stoichiometry or full-cell SOC.",
                   "domain_basis": "Retained native coordinate endpoints; no extrapolation."}
    relative = f"curves/{rid}.csv"
    digest = write_csv(relative, ["x", "potential_V"], zip(x, y))
    record["representation"] = {"kind": "table", "path": relative, "sha256": digest,
                                "point_count": len(x), "default_interpolation": "linear"}
    record["cell_link"] = {"cell_id": cid,
                           "relationship": "same_study_cell_family" if cid == ISU else "same_parameter_set",
                           "evidence": evidence}
    record["provenance"] = {"asset_ids": aids, "derivation": "measured_capacity_branch_extraction" if cid == ISU else "author_parameterized_pd_ecm_ocpn_nodes",
                            "location": location, "processing": {"script": SCRIPT}}
    record["quality"] = {"source_review": "raw_file_checked", "axis_status": "model_coordinate" if cid == A123 else "relative_capacity_only",
                         "raw_data": "published_table_not_instrument_raw", "model_status": "requires_stoichiometry_mapping",
                         "independent_validation": False}
    return record


def extend(download=False):
    load = lambda name: json.loads((DATA / name).read_text(encoding="utf-8"))
    doc, tests, params = load("catalog.json"), load("full_cell_tests.json")["records"], load("parameters.json")["records"]
    sources, assets, cells, materials, experiments = [load(name+".json") for name in ["sources", "assets", "cells", "materials", "experiments"]]
    doc["records"] = [r for r in doc["records"] if r["cell_link"]["cell_id"] not in [ISU, A123]]
    tests = [t for t in tests if t["cell_id"] not in [ISU, A123]]
    pins = json.loads((ROOT / "scripts/lfp_study_assets.json").read_text())
    CACHE.mkdir(parents=True, exist_ok=True)
    for aid, asset in pins.items():
        if asset.get("path"):
            local = DATA / asset["path"]
            if not local.exists():
                original = obtain(asset["filename"], asset["url"], sha256=asset["sha256"], download=download)
                shutil.copyfile(original, local)
            if hashlib.sha256(local.read_bytes()).hexdigest() != asset["sha256"]:
                raise ValueError(f"Source checksum mismatch: {aid}")
        # External author notebook/loader/README are pinned for evidence; they
        # are not executed or needed to reconstruct the fixed selections.
        assets[aid] = asset

    sources.update({
        ISU_DATA: {"kind": "dataset", "title": "ISU-UConn LFP/Graphite Emulated Degradation Dataset",
                   "authors": ["Yifan Zhang", "Tingkai Li", "Shan Hu", "Chao Hu"], "year": 2026,
                   "url": "https://digitalcommons.lib.uconn.edu/reil_datasets/6/", "license": "CC-BY-4.0",
                   "version": "Author-hosted workbook at commit 1188c371e5836df4a7e5f5acf336a34ffd4027e6",
                   "license_evidence": "Primary deposit Terms of Use CC BY 4.0; pinned author README explicitly assigns this workbook to that dataset (checked 2026-10-17).",
                   "role": "Laboratory CR2032 half/full-cell voltage-capacity observations. Author-hosted copy; byte identity to university download not established (HTTP 403)."},
        ISU_CODE: {"kind": "software", "title": "REIL-UConn half-cell fitting notebook and loader",
                   "authors": ["Tingkai Li", "Yifan Zhang", "Benjamin Nowacki", "Sina Navidi", "Thomas Schmitt", "Shan Hu", "Chao Hu"],
                   "year": 2026, "url": "https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics/tree/1188c371e5836df4a7e5f5acf336a34ffd4027e6",
                   "version": "1188c371e5836df4a7e5f5acf336a34ffd4027e6", "license": "MIT",
                   "role": "Selection and linkage evidence only; no author code executed or copied into project code. Dataset has separate CC BY 4.0 terms."},
        "li-2026-benchmarking": {"kind": "paper", "title": "Benchmarking half-cell model fitting approaches for lithium-ion battery degradation diagnostics",
                                "authors": ["Tingkai Li", "Yifan Zhang", "Benjamin Nowacki", "Sina Navidi", "Thomas Schmitt", "Shan Hu", "Chao Hu"],
                                "year": 2026, "doi": "10.1016/j.etran.2026.100593", "url": "https://doi.org/10.1016/j.etran.2026.100593",
                                "role": "Scientific study associated by primary deposit and author repository; full experimental procedures were not accessible in this import."},
        JAHN_DATA: {"kind": "dataset", "title": "Probability distributed equivalent circuit model - Data (v2)",
                    "authors": ["Leonard Jahn"], "year": 2024, "version": "v2; fixed record 11958572",
                    "doi": "10.5281/zenodo.11958572", "url": "https://zenodo.org/records/11958572", "license": "CC-BY-4.0",
                    "license_evidence": "Packaged Zenodo API metadata metadata.license.id=cc-by-4.0; files verified against published MD5 and SHA-256.",
                    "role": "Experimental whole-cell observations and modeled electrode OCPn arrays; these are different evidence types."},
        JAHN_CODE: {"kind": "software", "title": "Probability distributed equivalent circuit model - Code",
                    "authors": ["Leonard Jahn"], "year": 2024, "doi": "10.5281/zenodo.10852695",
                    "url": "https://zenodo.org/records/10852695", "license": "CC-BY-4.0",
                    "license_evidence": "Packaged fixed-record API metadata metadata.license.id=cc-by-4.0.",
                    "role": "Original MATLAB inspected as text for coordinate, signs, column units and file linkage; never executed."},
        "jahn-2024-paper": {"kind": "paper", "title": "A physically motivated voltage hysteresis model for lithium-ion batteries using a probability distributed equivalent circuit",
                            "authors": ["Leonard Jahn", "Patrick Moessle", "Fridolin Roeder", "Michael A. Danzer"], "year": 2024,
                            "doi": "10.1038/s44172-024-00221-4", "url": "https://www.nature.com/articles/s44172-024-00221-4",
                            "role": "Methods names A123 18650M1A, 25 degC chamber, subsequent harvested-electrode tests and approximated OCPn parameterization."},
    })
    isu_evidence = "Author notebook cells 6 and 8 use the selected LFP/graphite half-cell pair for eleven full-cell configurations in the same laboratory study. Shared MTI electrode family, not an identified commercial model or proven identical harvested specimen."
    a123_evidence = "Paper Methods names A123 18650M1A and electrode harvesting after intact-cell tests. The deposited author script loads these OCPn MATs and the A123_01 full-cell files. Exact serialized specimen/file mapping is not supplied."
    new_cells = {
        ISU: {"manufacturer": "ISU / UConn laboratory", "model": None,
              "display_name": "ISU-UConn | laboratory LFP/graphite CR2032 family", "format": "CR2032 laboratory coin cell",
              "chemistry": "LFP/graphite", "nominal_capacity_Ah": None, "identity_level": "laboratory_cell_family",
              "source_ids": [ISU_DATA, ISU_CODE, "li-2026-benchmarking"], "model_context": "Empirical electrode balancing / degradation-diagnostic half-cell fitting",
              "match_level": "same_study_cell_family", "match_evidence": isu_evidence,
              "note": "Only a documented subset is curated. The deposit describes 50 cells; retained branches and configuration labels are not independent studies or 50 imported specimens.",
              "coverage": {"ocp": "Four C/20 half-cell pseudo-OCP branches from the author-selected two specimens; reference electrode detail and temperature not verified.",
                           "diffusion": "No matched solid diffusion characterization imported.", "kinetics": "No matched intrinsic reaction-rate or exchange-current characterization imported.",
                           "full_cell_tests": "Eleven author-selected charge branches and available following discharge branches; native capacity/voltage only."}},
        A123: {"manufacturer": "A123 Systems", "model": "18650M1A", "display_name": "A123 18650M1A | Jahn2024 LFP/graphite",
               "format": "18650", "chemistry": "LFP/graphite", "nominal_capacity_Ah": None, "identity_level": "explicit_commercial_model",
               "source_ids": [JAHN_DATA, JAHN_CODE, "jahn-2024-paper"], "model_context": "Probability-distributed ECM with parameterized single-string OCPn, not a DFN parameter set",
               "match_level": "same_model_same_study", "match_evidence": a123_evidence,
               "note": "18650M1A is separate from AMP20M1HD-A, the 9 Ah pouch family and APR18650M1B. PD-ECM resistances are not intrinsic Butler-Volmer kinetic constants.",
               "coverage": {"ocp": "Two modeled OCPn node arrays (LFP 399; graphite 602); raw measured electrode/GITT points are not included in these files.",
                            "diffusion": "No intrinsic solid diffusivity imported.", "kinetics": "No intrinsic Butler-Volmer coefficient or exchange-current density imported; ECM parameters remain separate.",
                            "full_cell_tests": "Low-rate full cycle, incremental OCV charge/discharge branches, two power tests and nine partial hysteresis loops. Current is present only in power/loop files; no temperature trace."}},
    }

    selection = json.loads((ROOT / "scripts/isu_uconn_selection.json").read_text())
    workbook = SourceWorkbook(DATA / pins["isu-uconn-workbook"]["path"])
    workbook_rows = {}
    def blocks(item):
        name = item["sheet"]
        if name not in workbook_rows:
            workbook_rows[name] = workbook.read(name)
        return capacity_blocks(workbook_rows[name], item["pair_column"])

    new_tests = []
    for spec in selection["half_cells"]:
        material = spec["material"]
        eid = "isu-uconn-" + material.lower() + "-selected-s2"
        experiments[eid] = {"source_id": ISU_DATA, "asset_id": "isu-uconn-workbook", "sample_id": spec["sample_label"],
                            "configuration": "Laboratory CR2032 half-cell; detailed counter/reference construction not verified because primary README returned HTTP 403.",
                            "protocol": "C/20 half-cell cycling per deposit and sheet name; blocks 6 and 7 (zero-based blank-delimited capacity branches).",
                            "cycle_selected": None, "cycle_selection_reason": "Block 6 / S2 is selected by author notebook cell 6; block 7 is the following reverse branch. No instrument cycle IDs are supplied.",
                            "temperature_K": None, "temperature_description": "Numeric temperature not supplied in accessible workbook/notebook.",
                            "electrode_metadata": {"supplier": "MTI Corporation per primary deposit", "sheet": spec["sheet"], "capacity_column": spec["pair_column"]},
                            "known_issues": ["Reference chemistry not independently verified", "No current/time/temperature columns"]}
        for idx in spec["blocks"]:
            branch = finite(blocks(spec)[idx])
            imax = int(np.argmax(branch[:, 1]))
            cc = branch[:imax+1]
            _, keep = np.unique(cc[:, 1], return_index=True)
            nodes = cc[np.sort(keep)]
            q, v = nodes[:, 1], nodes[:, 2]
            x = (q-q[0])/(q[-1]-q[0])
            direction = ("delithiation" if v[-1] > v[0] else "lithiation")
            rid = f"isu-uconn-{material.lower()}-s2-b{idx}-{direction}"
            r = ocp_table(rid, material, x, v, [ISU_DATA, ISU_CODE, "li-2026-benchmarking"],
                          ["isu-uconn-workbook", "isu-uconn-author-notebook", "isu-uconn-author-loader"], ISU,
                          "pseudo_ocp", "normalized_branch_capacity", f"LFP_Data.xlsx::{spec['sheet']}::{spec['pair_column']}:{column_after(spec['pair_column'])}::block {idx}", isu_evidence)
            r["title"] = f"{material} | ISU-UConn S2 | C/20 pseudo-OCP | block {idx} {direction}"
            r["direction"], r["experiment_id"], r["reference"] = direction, eid, "unresolved"
            r["temperature"] = {"value_K": None, "description": "Numeric temperature/setpoint not verified from the accessible workbook and author notebook."}
            r["y"]["definition"] = "Published half-cell terminal voltage. Counter/reference chemistry was not verified from the accessible workbook and notebook."
            r["provenance"]["processing"].update({"sheet": spec["sheet"], "capacity_column": spec["pair_column"], "voltage_column": column_after(spec["pair_column"]),
                "blank_delimited_block_zero_based": idx, "source_rows": [int(branch[0,0]), int(branch[-1,0])], "source_branch_points": len(branch),
                "tail_points_after_first_capacity_maximum": len(branch)-len(cc), "duplicate_capacity_points_removed": len(cc)-len(nodes),
                "changes": "Truncate after first maximum capacity to omit the constant-capacity tail; first occurrence per capacity retained; normalize branch capacity to 0..1. No smoothing/resampling. Direction inferred from electrode potential trend; source cycle IDs unavailable."})
            relative = r["representation"]["path"]
            r["representation"]["sha256"] = write_csv(relative, ["x", "potential_V", "source_capacity_mAh", "source_excel_row"], zip(x, v, q, nodes[:,0].astype(int)))
            r["limitations"] = [isu_evidence, "Finite-current pseudo-OCP includes polarization and branch hysteresis; not equilibrium OCP.",
                                   "Reference chemistry and numerical temperature not verified; Li/Li+ is not asserted. PyBaMM adaptation is blocked until reference evidence is curated.",
                                   "Relative branch throughput requires independently justified stoichiometry endpoints; no full-cell SOC mapping is inferred."]
            doc["records"].append(r)
            materials[r["material_id"]] = {"chemistry": material, "description": "MTI laboratory electrode family in the ISU-UConn deposit; no batch-to-commercial-model mapping."}

    for item in selection["full_cells"]:
        all_blocks = blocks(item)
        primary = item["block"]
        branch_ids = [primary]
        if primary+1 < len(all_blocks):
            branch_ids.append(primary+1)
        for idx in branch_ids:
            b = finite(all_blocks[idx]); q, v = b[:,1], b[:,2]
            charge = bool(v[-1] > v[0])
            label = "charge" if charge else "discharge"
            rid = f"isu-uconn-{item['label']}-b{idx}-{label}"
            rows = [empty_row(int(row), float(voltage), step=idx)+[float(capacity)/1000]
                    for row,capacity,voltage in b]
            t = test_record(rid, ISU, f"{item['sheet']}::{item['pair_column']}:{column_after(item['pair_column'])}",
                            "isu-uconn-workbook", pins["isu-uconn-workbook"], rows, ["passed_capacity_Ah"],
                            f"{item['label']}: C/20 {label} capacity branch, source block {idx}; constant-capacity tail retained",
                            "constant_current_charge" if charge else "constant_current_discharge", isu_evidence,
                            charge=charge, discharge=not charge,
                            coordinate={"column": "passed_capacity_Ah", "unit": "Ah", "label": "Branch passed capacity / Ah",
                                        "definition": "Source positive cumulative Capacity/mAh divided by 1000 for this branch, including discharge. No time inferred."})
            t["basic_test"]["nominal_C_rate"] = .05
            t["scientific_source_ids"] = [ISU_CODE, "li-2026-benchmarking"]
            t["supporting_asset_ids"] = ["isu-uconn-author-notebook", "isu-uconn-author-loader"]
            t["processing"] = "Retain every numeric row in the selected source capacity block, including repeated capacities and constant-capacity tails; mAh divided by 1000. Header/date markers and blank delimiters are not observations. No smoothing, resampling, current synthesis or timestamps. source_record is the one-based Excel row."
            t["source_location"] = {**item, "selected_block": idx, "first_row": int(b[0,0]), "last_row": int(b[-1,0]),
                                    "voltage_column": column_after(item["pair_column"]), "selection_role": "author_primary" if idx == primary else "following_reverse_branch"}
            t["missing_items"] += ["Original timestamps", "Instrument cycle/step identifiers", "Verified numeric temperature and reference details for associated half-cells"]
            new_tests.append(t)

    def aid(filename):
        return next(key for key,a in pins.items() if a["filename"] == "jahn-"+filename)
    for material, suffix in [("LFP", "lfp"), ("graphite", "graphite")]:
        filename = "param_ocpn_"+suffix+".mat"; key = aid(filename)
        mat = loadmat(DATA/pins[key]["path"], simplify_cells=True)
        x, y = finite(mat["pot_dol"]), finite(mat["pot"])
        rid = f"jahn-a123-{suffix}-model-ocpn"
        r = ocp_table(rid, material, x, y, [JAHN_DATA, JAHN_CODE, "jahn-2024-paper"],
                      [key, aid("pdecm_fullcell.m")], A123, "model_ocp", "model_soc", filename+"::pot_dol, pot", a123_evidence)
        r["title"] = f"{material} | A123 18650M1A / Jahn2024 | modeled PD-ECM OCPn"
        r["temperature"] = {"value_K": 298.15, "description": "Characterization protocol at 25 degC per Methods; parameterized model table, not a temperature sensor trace."}
        r["provenance"]["processing"]["changes"] = "Native pot_dol and positive electrode-potential pot nodes copied unchanged. Source model negates graphite pot during full-cell assembly; this catalog retains its physical positive potential versus Li/Li+. Author spline/PCHIP/extrapolation is not reproduced by the catalog's bounded linear interpolation."
        r["limitations"] = [a123_evidence, "OCPn is approximated and parameterized from electrode data; it cannot be measured directly (paper Parameterization). These arrays are not raw GITT/half-cell measurements.",
                              "Model SOC/DOL is not established as absolute stoichiometry. LFP potential rises with this coordinate. Geometry, balancing and coordinate orientation need explicit review before DFN/SPM/SPMe reuse.",
                              "No intrinsic diffusivity or Butler-Volmer kinetics inferred from ECM quantities."]
        doc["records"].append(r)
        materials[r["material_id"]] = {"chemistry": material, "description": "Harvested A123 18650M1A electrode context; approximated single-string PD-ECM potential."}

    def jahn_test(rid, filename, arrays, protocol, kind, current=None, extra=None, coordinate=None, source_indices=None, charge=True, discharge=True):
        key = aid(filename); v = finite(arrays["voltage"]); n = len(v)
        time = finite(arrays["time"]) if "time" in arrays else None
        current = finite(current) if current is not None else None
        extra = extra or {}
        if any(len(a) != n for a in [*arrays.values(), *extra.values()] + ([] if current is None else [current])):
            raise ValueError("Jahn source channel lengths differ")
        indices = list(range(n)) if source_indices is None else source_indices
        rows = [empty_row(int(indices[i]), float(v[i]), "" if time is None else float(time[i]),
                          "" if current is None else float(current[i]),
                          "U" if current is None else "C" if current[i]>0 else "D" if current[i]<0 else "R")
                + [float(a[i]) for a in extra.values()] for i in range(n)]
        t = test_record(rid, A123, "A123_01 (shared file label; serialized identity unresolved)", key, pins[key], rows, list(extra), protocol,
                        kind, a123_evidence, current_present=current is not None, coordinate=coordinate, charge=charge, discharge=discharge)
        t["scientific_source_ids"] = ["jahn-2024-paper", JAHN_CODE]
        t["supporting_asset_ids"] = [aid("hys_sim_lfp_fc.m"), aid("pdecm_fullcell.m"),
                                     "jahn-2024-data-v2-metadata", "jahn-2024-code-metadata"]
        t["processing"] = "Native observation values/order retained; no smoothing, resampling, imputation or author MATLAB execution. source_record is zero-based numeric CSV row (excluding header) or the explicitly named MAT-array index. Absolute source time retained where available. Stored-charge offsets and published SOC are retained as source channels, not normalized silently."
        if time is None: t["missing_items"] += ["Original timestamps"]
        new_tests.append(t)
        return t

    name = "20230125_Hys_A123_01_25deg_pOCV.csv"
    a = native_csv(DATA/pins[aid(name)]["path"])
    t = jahn_test("jahn-a123-pocv-full-cycle", name, {"voltage": a["pOCVAux"], "time": a["pt"]},
                  "C/20 pseudo-OCV full charge/discharge cycle; t/Q/U supplied, measured current absent", "constant_current_cycle",
                  extra={"source_stored_charge_Ah": a["pQ"]})
    t["basic_test"]["nominal_C_rate"] = .05
    t["source_issues"] = ["Author script differentiates Q to generate its simulation current; that derived current is not imported as measured current."]
    for label in ["SOC50", "SOC100"]:
        name = f"20230125_HysPowerTest_A123_01_25deg_{label}.csv"
        a = native_csv(DATA/pins[aid(name)]["path"]); prefix = "ch" if label == "SOC50" else "dc"
        t = jahn_test("jahn-a123-power-"+label.lower(), name, {"time": a[f"t_{prefix}_power"], "voltage": a[f"U_{prefix}_power"]},
                      f"{label} path-dependency power test; full deposited record including conditioning and rest retained", "constant_current_steps",
                      current=a[f"I_{prefix}_power"], extra={"source_stored_charge_Ah": a[f"Q_{prefix}_power"]})
        t["source_issues"] = ["Deposit describes C/2 conditioning and 4C discharge; retain measured amperes and do not infer a capacity denominator. SOC100 file also contains initial positive-current conditioning.",
                              "Author simulation truncates SOC50 to 275 rows; catalog retains all 336 rows."]
    name = "20230125_Hys_A123_01_25deg_incrOCV.csv"
    a = native_csv(DATA/pins[aid(name)]["path"]); split = int(np.argmax(a["Q"]))+1
    for label, slc, charge in [("charge", slice(0,split), True), ("discharge", slice(split,None), False)]:
        q = a["Q"][slc]
        passed = q-q[0] if charge else q[0]-q
        t = jahn_test("jahn-a123-incremental-ocv-"+label, name, {"voltage": a["OCV"][slc]},
                      "Incremental full-cell OCV "+label+" endpoints after current interruptions; Q/U only", "incremental_ocv",
                      extra={"passed_capacity_Ah": passed, "source_stored_charge_Ah": q},
                      coordinate={"column": "passed_capacity_Ah", "unit": "Ah", "label": "Branch passed capacity / Ah",
                                  "definition": "Charge: source Q-Q_start; discharge: Q_start-Q. Original source stored charge Q is retained separately. No clock or current inferred."},
                      source_indices=list(range(len(a["Q"])))[slc], charge=charge, discharge=not charge)
        t["processing"] += " Split after first global maximum stored charge; no observation is duplicated or deleted across the two branch exports."
        t["source_issues"] = ["These are whole-cell OCV points, not electrode OCP or a continuous CC time series."]
    name = "Hysteresis_SOC50Loops_C10_A123_01_t_SOC_U_I_Ah.mat"
    loops = loadmat(DATA/pins[aid(name)]["path"], simplify_cells=True)["minor_loops"]
    if loops.shape != (9,5): raise ValueError("Unexpected minor_loops structure")
    for idx,row in enumerate(loops):
        t = jahn_test(f"jahn-a123-hysteresis-loop-{idx+1}", name, {"time": row[0], "voltage": row[2]},
                      f"C/10 partial hysteresis cycle {idx+1}; nominal SOC window {45-idx*5} to {55+idx*5} percent per deposit",
                      "constant_current_partial_cycle", current=row[3], extra={"source_stored_charge_Ah": row[4], "source_soc_fraction": row[1]})
        t["basic_test"]["nominal_C_rate"] = .1
        t["original_member"] = f"minor_loops({idx+1},:) [t,SOC,U,I,Q]"
        t["processing"] += f" source_record refers to the zero-based sample in minor_loops({idx+1},:)."

    audit_links(new_cells, doc["records"], params, new_tests)
    for t in new_tests:
        with (DATA/t["normalized_path"]).open(newline="") as f:
            rows = list(csv.DictReader(f))
        t["missing_values"] = {k: sum(not r[k] for r in rows) for k in ["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K", "ambient_temperature_K"]}
        for k in ["time_s"] + ([t["independent_variable"]["column"]] if "independent_variable" in t else []):
            t["channel_availability"][k] = {"present_rows": sum(bool(r[k]) for r in rows), "total_rows": len(rows)}
    tests += new_tests
    for cid,cell in new_cells.items():
        cell["missing_items"] += ["Intrinsic solid diffusivity not imported", "Intrinsic reaction kinetics not imported", "Absolute measured cell/ambient temperature traces"]
        if cid == ISU:
            cell["missing_items"] += ["Measured current and timestamps", "Verified reference chemistry and numerical temperature for selected half-cells"]
        else:
            cell["missing_items"] += ["Raw measured electrode OCP/GITT points", "Measured current in pseudo-OCV file", "Time/current in incremental OCV file", "Nominal capacity denominator not independently established"]
        cell["missing_items"] = sorted(set(cell["missing_items"]))
        cell["evidence_matrix"]["ocp"]["missing_items"] += (["Verified reference chemistry", "Absolute stoichiometry mapping"] if cid == ISU else ["Raw electrode OCP observations", "PD-ECM coordinate to lithium-fraction mapping"])
        cell["evidence_matrix"]["full_cell_tests"]["missing_items"] = sorted(set(COMMON_GAPS + ([] if cid == A123 else ["Measured current trace", "Original timestamps"])))
        if cid == A123:
            cell["evidence_matrix"]["full_cell_tests"]["missing_items"] += ["Measured current in pseudo-OCV file", "Time/current in incremental OCV file"]
    cells.update(new_cells)
    audit = load("matching_audit.json")
    audit["checked_date"] = "2026-10-17"
    for cid,cell in new_cells.items():
        audit["cell_matches"][cid] = {"display_name": cell["display_name"], "match_level": cell["match_level"],
                                      "components": cell["evidence_matrix"], "missing_items": cell["missing_items"]}
    for rejection in ["ISU-UConn laboratory CR2032 cells are not matched to a commercial A123 model or to the separate APR18650M1B aging study.",
                      "Jahn2024 modeled single-string OCPn arrays are not labeled raw measured OCP; ECM resistances are not imported as DFN diffusion/kinetic properties."]:
        if rejection not in audit["rejected_joins"]: audit["rejected_joins"].append(rejection)
    doc["release"] = "0.6.0"
    for name,value in [("catalog.json",doc),("full_cell_tests.json",{"schema_version":"0.1","records":tests}),
                       ("cells.json",cells),("sources.json",sources),("assets.json",assets),("materials.json",materials),
                       ("experiments.json",experiments),("matching_audit.json",audit)]:
        write_json(name,value)
    print(f"LFP studies: 4 measured pseudo-OCP branches + 2 modeled OCPn tables; {len(new_tests)} new full-cell branch/array files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    extend(parser.parse_args().download)
