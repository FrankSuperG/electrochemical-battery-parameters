"""Extract pinned half-cell/OCP and BPX inputs; never fetch full-cell observations.

Packaged originals make this step offline and reproducible. No author code runs.
Finite-current branches, published fits and component particles stay distinct.
"""

import csv
import hashlib
import json
import re

import numpy as np
from scipy.io import loadmat

from seed_v01 import DATA, ROOT, base_record, write_json
from seed_fullcell import audit_links, write_csv

NCR = "panasonic-ncr18650b-hnei2016"
NEXT = "calb-gen3b-nextbms2026"
P45B = "molicel-p45b-aboutenergy2026"
CELLS = {NCR, NEXT, P45B}
SCRIPT = "scripts/seed_parameter_sources.py"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def table_record(rid, material, cid, aid, source, license, x, voltage, columns,
                 rows, location, processing, *, fitted=False, direction="unspecified"):
    x, voltage = np.asarray(x), np.asarray(voltage)
    if not np.isfinite(x).all() or not np.isfinite(voltage).all() or np.any(np.diff(x) <= 0):
        raise ValueError(f"Invalid source coordinate: {rid}")
    relative = f"curves/{rid}.csv"
    digest = write_csv(relative, ["x", "potential_V"] + columns, rows)
    r = base_record(rid, material)
    r.update(title=rid.replace("-", " "), material_id=rid+"-material",
             electrode_role="positive" if material in {"NCA", "NMC532"} else "negative",
             direction=direction, measurement="literature_table" if fitted else "pseudo_ocp",
             source_ids=[source], license=license)
    r["x"] = {"kind": "source_reported_stoichiometry" if fitted else "normalized_branch_capacity",
              "symbol": "x", "unit": "1", "domain": [float(x[0]), float(x[-1])],
              "definition": ("Native BPX particle stoichiometry; graphite and silicon are separate phases."
                             if fitted else "Passed capacity normalized independently over this branch; not absolute lithium fraction or full-cell SOC."),
              "domain_basis": "Retained native nodes only; no extrapolation, resampling or endpoint insertion."}
    r["representation"] = {"kind": "table", "path": relative, "sha256": digest,
                           "point_count": len(x), "default_interpolation": "linear"}
    r["cell_link"] = {"cell_id": cid, "relationship": "same_parameter_set" if fitted else "same_model",
                      "evidence": "Explicit source model and study; no common serialized specimen asserted across studies."}
    r["provenance"] = {"asset_ids": [aid], "derivation": "published_BPX_fit_nodes" if fitted else "finite_current_half_cell_branch",
                       "location": location, "processing": {"script": SCRIPT, **processing}}
    r["quality"] = {"source_review": "raw_file_checked",
                    "axis_status": "source_reported_stoichiometry" if fitted else "relative_capacity_only",
                    "raw_data": "published_table_not_instrument_raw" if fitted else "external_checksum_pinned",
                    "model_status": "requires_stoichiometry_mapping", "independent_validation": False}
    r["limitations"] = [
        "Published fitted nodes, not independently measured raw half-cell points." if fitted else
        "Finite-current pseudo-OCP; polarization and branch hysteresis are retained, not a certified equilibrium OCP.",
        "Same study/model does not establish identical half-cell/full-cell specimens.",
        "Half-cell temperature not independently established; full-cell temperature settings are not transferred.",
        "No independent electrochemical-model validation is claimed."]
    return r


def extract_hnei(pins):
    records = []
    for role, material in [("NE", "graphite"), ("PE", "NCA")]:
        aid = "hnei-ncr-"+role.lower()
        d = loadmat(DATA/pins[aid]["path"], simplify_cells=True)
        for field, idx, label in [("dis_data", 0, "lithiation"), ("ch_data", 1, "delithiation")]:
            a = np.asarray(d[field][idx, 0], dtype=float)
            # Columns are corroborated by Q = integral(I dt)/3600 and the paper's voltage windows.
            q, voltage, t, current = a.T
            integrated = np.cumsum((current[1:]+current[:-1])*np.diff(t)/7200)
            if not np.allclose(q[1:]-q[0], integrated, rtol=1e-8, atol=1e-12):
                raise ValueError("HNEI charge/current/time consistency failure")
            x = (q-q[0])/(q[-1]-q[0])
            info = d["disinfo" if field == "dis_data" else "chinfo"][idx]
            rid = f"hnei-ncr18650b-{role.lower()}-{label}"
            r = table_record(rid, material, NCR, aid, "hnei-ncr-2016-data", "CC0-1.0", x, voltage,
                             ["source_capacity_Ah", "source_time_s", "source_current_A", "source_mat_row"],
                             zip(x, voltage, q, t, current, range(1, len(x)+1)),
                             f"{field}[{idx},0] (zero-based MATLAB-cell-array indices)",
                             {"field": field, "cell_array_row_zero_based": idx, "cell_array_column_zero_based": 0,
                              "source_columns": ["capacity_Ah", "potential_V", "time_s", "current_A"],
                              "source_rate_denominator": float(info[2]),
                              "selection": "Lowest-rate complete main branch; initial short charge, remnant-capacity column and all higher-rate branches excluded.",
                              "source_rows": len(x), "omitted_rows": 0}, direction=label)
            r["source_ids"].append("devie-dubarry-2016")
            r["limitations"] += ["Paper names C/40; positive-electrode MAT rate field is 39. Both labels retained.",
                                 "Column units are inferred from exact current-time charge integration and the documented voltage windows; no MAT column header is supplied."]
            records.append(r)
    return records


def extract_nextbms(pins):
    records = []
    for aid, asset in pins.items():
        if not aid.startswith("nextbms-") or not asset["path"].endswith(".csv"):
            continue
        with (DATA/asset["path"]).open(newline="") as f:
            original = list(csv.DictReader(f))
        q = np.array([float(row["Capacity(mAh/g)"]) for row in original])
        v = np.array([float(row["Voltage(V)"]) for row in original])
        if np.any(np.diff(q) < 0):
            raise ValueError("Unexpected reversed NEXTBMS branch capacity")
        # Preserve the last source voltage at repeated coordinates; keep all originals for audit.
        retained = np.flatnonzero(np.r_[np.diff(q) > 0, True])
        x = (q[retained]-q[retained[0]])/(q[retained[-1]]-q[retained[0]])
        cathode = "cathode" in asset["filename"]
        branch = "charge" if "fCharge" in asset["filename"] else "discharge"
        rid = f"nextbms-calb-{'positive' if cathode else 'negative'}-{branch}"
        r = table_record(rid, "NMC532" if cathode else "graphite", NEXT, aid,
                         "nextbms-calb-2026-data", "CC-BY-4.0", x, v[retained],
                         ["source_specific_capacity_mAh_g", "source_csv_row"],
                         zip(x, v[retained], q[retained], retained+2), asset["archive_member"],
                         {"source_branch": branch, "source_rows": len(q),
                          "duplicate_coordinate_rows_omitted": len(q)-len(retained),
                          "selection": "Last source occurrence per capacity; one-based CSV line includes header; no smoothing or resampling."})
        r["provenance"]["asset_ids"].append("nextbms-half-readme")
        r["limitations"] += ["Source charge/discharge labels are retained; physical direction left unspecified because source naming text is ambiguous.",
                             "Half-cell separator/electrolyte differ from the intact commercial full cell."]
        records.append(r)
    return records


def extract_bpx(pins):
    aid, source = "aepy-p45b-bpx", "aepy-p45b-2026"
    bpx = json.loads((DATA/pins[aid]["path"]).read_text())
    if bpx["Header"]["BPX"] != "1.1" or bpx["Header"]["Model"] != "DFN":
        raise ValueError("Unexpected P45B BPX definition")
    p = bpx["Parameterisation"]
    particles = [("negative-graphite", "graphite", p["Negative electrode"]["Particle"]["Graphite"], "Parameterisation/Negative electrode/Particle/Graphite"),
                 ("negative-silicon", "silicon", p["Negative electrode"]["Particle"]["Silicon Additive"], "Parameterisation/Negative electrode/Particle/Silicon Additive"),
                 ("positive-nca", "NCA", p["Positive electrode"], "Parameterisation/Positive electrode")]
    curves, params = [], []
    for component, material, particle, path in particles:
        for key, table in particle.items():
            if not isinstance(table, dict) or "OCP" not in key:
                continue
            x, y = np.array(table["x"]), np.array(table["y"])
            lo, hi = particle["Minimum stoichiometry"], particle["Maximum stoichiometry"]
            selection = np.flatnonzero((x >= lo) & (x <= hi))
            direction = "delithiation" if "delithiation" in key else "lithiation" if "lithiation" in key else "unspecified"
            rid = "aepy-p45b-"+component+"-"+slug(key)
            r = table_record(rid, material, P45B, aid, source, "BSD-3-Clause", x[selection], y[selection],
                             ["source_bpx_index"], zip(x[selection], y[selection], selection), path+"/"+key,
                             {"source_pointer": path+"/"+key, "source_nodes": len(x),
                              "source_particle_bounds": [lo, hi], "excluded_outside_particle_bounds": len(x)-len(selection),
                              "selection": "Keep native nodes inside configured particle min/max stoichiometry; no extrapolation or boundary insertion."},
                             fitted=True, direction=direction)
            r["limitations"] += ["Source fits contain extreme extrapolated potentials near 0/1; complete original BPX retained, catalog domain restricted to configured particle bounds.",
                                 "Three negative silicon branches are model inputs, not three independent measured experiments."]
            curves.append(r)

    def walk(obj, path):
        for name, value in obj.items():
            pointer = path+"/"+name
            if path == "Parameterisation/Electrolyte" or path.startswith("Parameterisation/User-defined"):
                continue  # Placeholder zeros are replaced by user-defined laws in author code.
            if isinstance(value, dict) and set(value) != {"x", "y"}:
                walk(value, pointer)
                continue
            if ("OCP" in name and isinstance(value, dict)) or not (isinstance(value, (int, float)) or isinstance(value, dict)):
                continue
            category = ("diffusion" if "Diffusivity" in name else "kinetics" if "Reaction rate" in name else
                        "thermodynamics" if "Entropic" in name else "initial_state" if path.startswith("State/") else
                        "thermal" if any(s in name.lower() for s in ["temperature", "heat", "density"] ) else
                        "operating_limits" if any(s in name for s in ["cut-off", "Nominal cell capacity"]) else
                        "transport" if "Conductivity" in name or "Transport efficiency" in name else
                        "geometry" if any(s in name.lower() for s in ["thickness", "area", "volume", "radius", "pairs"]) else "electrode")
            rid = "aepy-p45b-"+slug(pointer)
            unit = name.split("[")[-1].rstrip("]") if "[" in name else "1"
            rec = {"id": rid, "version": "1", "cell_id": P45B, "category": category,
                   "name": pointer, "unit": unit, "source_ids": [source],
                   "provenance": {"asset_id": aid, "location": pointer, "origin_status": "published_BPX_model_input"},
                   "license": "BSD-3-Clause", "independent_validation": False,
                   "definition": "Native BPX 1.1 model input, with source particle path and units retained; no conversion to another kinetic convention.",
                   "conditions": {"parameterization_variant": "aepy-bpx-1.1-dfn", "reference_temperature_K": 298.15,
                                  "source_pointer": pointer},
                   "limitations": ["Published parameterisation, not an independent measurement of every input.",
                                   "Composite graphite/silicon particles must remain distinct; rate constants retain BPX units and are not automatically intrinsic k or A/m2 i0.",
                                   "Electrolyte placeholder zeros are excluded. Seven additional native records transcribe the user-defined transport, thermodynamic, kinetic and contact-resistance definitions; full BPX retains all coefficients and selector flags."]}
            if isinstance(value, dict):
                x, y = np.array(value["x"]), np.array(value["y"])
                rel = f"parameter_tables/{rid}.csv"
                digest = write_csv(rel, ["source_sto", "value", "source_bpx_index"], zip(x, y, range(len(x))))
                rec["representation"] = {"kind": "table", "path": rel, "sha256": digest, "point_count": len(x),
                    "x": {"column": "source_sto", "variable": "sto", "unit": "1", "kind": "source_reported_stoichiometry",
                          "domain": [float(x[0]), float(x[-1])], "definition": "Native particle stoichiometry."},
                    "y_column": "value", "default_interpolation": "linear"}
            else:
                rec["representation"] = {"kind": "scalar", "value": value}
            params.append(rec)
    walk(p, "Parameterisation")
    walk(bpx["State"], "State")
    from extract_p45b_functions import extract
    params += extract(DATA, pins)
    return curves, params


def extend(download=False):
    load = lambda n: json.loads((DATA/(n+".json")).read_text())
    doc, params = load("catalog"), load("parameters")["records"]
    cells, sources, assets, materials, audit = [load(n) for n in ["cells", "sources", "assets", "materials", "matching_audit"]]
    pins = json.loads((ROOT/"scripts/parameter_source_assets.json").read_text())
    for aid, asset in pins.items():
        if hashlib.sha256((DATA/asset["path"]).read_bytes()).hexdigest() != asset["sha256"]:
            raise ValueError("Pinned source checksum mismatch: "+aid)
        assets[aid] = asset
    sources.update({
        "hnei-ncr-2016-data": {"kind": "dataset", "title": "Panasonic NCR18650B formation, RPT and half cell data set", "authors": ["Matthieu Dubarry"], "year": 2016,
            "url": "https://zenodo.org/records/60232", "doi": "10.5281/zenodo.60232", "license": "CC0-1.0", "version": "v1; fixed record 60232",
            "license_evidence": "Packaged Zenodo metadata reports cc-zero; fixed-record export identifies CC0 1.0.", "role": "Two original half-cell MAT members only; full-cell tests stay external."},
        "devie-dubarry-2016": {"kind": "paper", "title": "Durability and Reliability of Electric Vehicle Batteries under Electric Utility Grid Operations. Part 1: Cell-to-Cell Variations and Preliminary Testing",
            "authors": ["Arnaud Devie", "Matthieu Dubarry"], "year": 2016, "url": "https://doi.org/10.3390/batteries2030028", "doi": "10.3390/batteries2030028", "role": "Methods p3 confirms Li reference/counter, harvested electrodes and RPT rates."},
        "nextbms-calb-2026-data": {"kind": "dataset", "title": "NEXTBMS CALB generation 3b NMC532 half-cell and full-cell dataset", "year": 2026,
            "authors": ["Robinson Medina", "Alessio Alberto Lodge", "Feye Hoekstra", "Steven Wilkins", "Damian Cupid", "Akzhan Bekzhanov", "Dominik Dvorak", "Hansjorg Kapeller", "Joze Moskon", "Igor Mele", "Tomaz Katrasnik"],
            "doi": "10.5281/zenodo.22301764",
            "url": "https://zenodo.org/records/22301764", "license": "CC-BY-4.0", "version": "Fixed record 22301764",
            "role": "Four slow half-cell sweeps and author README retained; full-cell characterization and ageing remain external."},
        "aepy-p45b-2026": {"kind": "software", "title": "About:Energy Molicel P45B BPX 1.1 parameterisation", "authors": ["About:Energy Limited"], "year": 2026,
            "url": "https://github.com/About-Energy-OpenSource/AEPyBaMM/tree/188bd62ee2347cc486b66dc43e31fb9597759db1", "license": "BSD-3-Clause", "version": "188bd62ee2347cc486b66dc43e31fb9597759db1",
            "role": "Original BPX model inputs and author BSD notice retained; fitted OCP is not raw half-cell measurement."}})
    curves, bp = extract_bpx(pins)
    curves = extract_hnei(pins)+extract_nextbms(pins)+curves
    doc["records"] = [r for r in doc["records"] if r["cell_link"]["cell_id"] not in CELLS]+curves
    params = [p for p in params if p["cell_id"] not in CELLS]+bp
    specs = [(NCR, "Panasonic", "NCR18650B", "Panasonic NCR18650B | HNEI2016", "NCA/graphite", "hnei-ncr-2016-data"),
             (NEXT, "CALB", None, "CALB generation 3b | NEXTBMS2026", "NMC532/graphite", "nextbms-calb-2026-data"),
             (P45B, "Molicel", "INR21700-P45B", "Molicel P45B | About:Energy2026 BPX", "NCA/graphite-SiOx", "aepy-p45b-2026")]
    new_cells = {}
    for cid, maker, model, title, chemistry, sid in specs:
        new_cells[cid] = {"manufacturer": maker, "model": model, "display_name": title, "chemistry": chemistry,
            "format": "Source cell format; half-cell and full-cell configurations differ", "nominal_capacity_Ah": None,
            "identity_level": "explicit_commercial_model" if model else "study_cell_family", "source_ids": [sid],
            "model_context": "Partial electrochemical parameter/source package", "match_level": "same_model_same_study",
            "match_evidence": "Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.",
            "note": "Other studies sharing a model name are separate sources, not a single measured parameter set.",
            "coverage": {"ocp": "Published BPX phase-specific fits; original measured half-cell points not located." if cid == P45B else "Four extracted finite-current half-cell branches, with original coordinates and source rows retained.",
                         "diffusion": "Three phase-specific D inputs and three activation energies in BPX." if cid == P45B else "No matched diffusivity values imported.",
                         "kinetics": "BPX-native reaction coefficients/activation energies and two author-defined negative-phase i0 laws with explicitly checked F*k and modifier convention." if cid == P45B else "No matched intrinsic kinetic values imported.",
                         "full_cell_tests": "External dataset links only; no new full-cell observations packaged."},
            "missing_items": ["Identical half-cell/full-cell serialized specimen mapping unresolved", "Half-cell OCP measurement temperature not independently verified", "Independent model validation not performed"]}
    audit_links(new_cells, doc["records"], params, [])
    for cid, cell in new_cells.items():
        cell["missing_items"] += ["Half-cell measurement temperature and identical donor/full-cell serial mapping unresolved"]
        cells[cid] = cell
        audit["cell_matches"][cid] = {"display_name": cell["display_name"], "match_level": cell["match_level"], "components": cell["evidence_matrix"], "missing_items": cell["missing_items"]}
    audit["checked_date"] = "2026-10-23"
    for r in curves:
        materials[r["material_id"]] = {"label": r["material"], "cell_id": r["cell_link"]["cell_id"], "note": "Source-specific phase/electrode; not a universal material curve."}
    for name, value in [("catalog", doc), ("parameters", {"schema_version": "0.1", "records": params}), ("cells", cells), ("sources", sources), ("assets", assets), ("materials", materials), ("matching_audit", audit)]:
        write_json(name+".json", value)
    print(f"Parameter sources: {len(curves)} OCP branches/fits and {len(bp)} BPX parameter records; no full-cell observations added.")


if __name__ == "__main__":
    extend()
