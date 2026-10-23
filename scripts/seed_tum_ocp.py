"""Extract seven first-party TUM half-cell branches from a fixed MIT release.

Only checksum-pinned, explicitly allowlisted originals are read. The surrounding
archive includes third-party inputs and full-cell observations; neither is copied
into this package. No author MATLAB code is executed.
"""

import hashlib
import json

import numpy as np
from scipy.io import loadmat

from seed_v01 import DATA, ROOT, write_json
from seed_fullcell import audit_links
from seed_parameter_sources import table_record, slug

CID = "molicel-p45b-tum-rehm2026"
SID = "tum-rehm2026-v2"
PAPER = "rehm-2026"
SCRIPT = "scripts/seed_tum_ocp.py"
BRANCHES = [
    ("P45B_Cathode_Delithiation_0C03", "NCA", "delithiation", .03, 5481),
    ("P45B_Anode_Delithiation_0C02", "silicon-graphite", "delithiation", .02, 9386),
    ("P45B_Anode_Delithiation_0C03", "silicon-graphite", "delithiation", .03, 5579),
    ("P45B_Anode_Lithiation_0C02", "silicon-graphite", "lithiation", .02, 9400),
    ("P45B_Anode_Lithiation_0C03", "silicon-graphite", "lithiation", .03, 5601),
    ("Gr_Delithiation_Rehm2026", "graphite", "delithiation", .0145, 2481),
    ("Gr_Lithiation_Rehm2026", "graphite", "lithiation", .0145, 2450),
]


def extract(pins):
    records = []
    for stem, material, direction, rate, count in BRANCHES:
        aid = "tum-rehm2026-" + slug(stem)
        asset = pins[aid]
        variable = stem.replace("Rehm2026", "Kuecher")
        source = loadmat(DATA / asset["path"], simplify_cells=True)
        if set(k for k in source if not k.startswith("__")) != {variable}:
            raise ValueError("Changed TUM MAT variable: " + stem)
        source = source[variable]
        if set(source) != {"normalizedCapacity", "voltage"}:
            raise ValueError("Changed TUM MAT fields: " + stem)
        q, voltage = [np.asarray(source[k], dtype=float) for k in ["normalizedCapacity", "voltage"]]
        if q.ndim != 1 or voltage.shape != q.shape or len(q) != count:
            raise ValueError("Changed TUM branch shape: " + stem)
        if not np.isfinite(q).all() or not np.isfinite(voltage).all() or len(np.unique(q)) != count:
            raise ValueError("Nonfinite or repeated TUM coordinate: " + stem)
        # Input normalizedCapacity can run against branch progress and slightly
        # beyond [0,1]. Retain it exactly; min/max scaling is not clipping.
        x = (q - q.min()) / (q.max() - q.min())
        desired_sign = -1 if direction == "lithiation" else 1
        reversed_axis = np.sign(voltage[np.argmax(q)] - voltage[np.argmin(q)]) != desired_sign
        if reversed_axis:
            x = 1 - x
        order = np.argsort(x, kind="stable")
        is_p45b = stem.startswith("P45B")
        rid = "tum-rehm2026-" + slug(stem)
        r = table_record(rid, material, CID if is_p45b else None, aid, SID, "MIT", x[order], voltage[order],
            ["source_normalized_capacity", "source_mat_row"],
            zip(x[order], voltage[order], q[order], order+1), variable,
            {"script": SCRIPT, "source_variable": variable, "source_fields": ["normalizedCapacity", "voltage"],
             "source_member": asset["archive_member"], "source_rows": count, "omitted_rows": 0,
             "source_capacity_bounds": [float(q.min()), float(q.max())], "reverse_normalized_axis": bool(reversed_axis),
             "coordinate_transform": "q01=(q-min(q))/(max(q)-min(q)); x=1-q01 if reverse_normalized_axis else q01; stable sort ascending x",
             "orientation_basis": "Author filename electrode direction and endpoint potentials: potential decreases on lithiation, increases on delithiation. This is a curation coordinate, not a reconstruction of chronological acquisition order.",
             "nominal_rate_C": rate,
             "nominal_rate_basis": "Source filename and author folder notice" if is_p45b else "Original paper Section 2.4 laboratory graphite protocol",
             "paper_protocol_rate_C": .033 if rate == .03 else rate,
             "selection": "Entire author-processed branch, without smoothing, interpolation, clipping, row deletion or endpoint insertion. Source row is one-based in the original MAT vector."}, direction=direction)
        r["title"] = ("Molicel P45B harvested " if is_p45b else "SGL Carbon laboratory ") + material + " | " + direction + f" | {rate}C | Rehm2026"
        r["source_ids"].append(PAPER)
        r["experiment_id"] = "tum-rehm2026-p45b-coincell" if is_p45b else "tum-rehm2026-graphite-coincell"
        r["cell_link"] = {"cell_id": CID if is_p45b else None, "relationship": "same_model" if is_p45b else "material_only",
            "evidence": "Harvested P45B electrodes in the same study as serial23 ageing checkups; exact donor-to-serial mapping unresolved." if is_p45b else
                        "Laboratory graphite electrode; not a harvested P45B graphite phase or a commercial full-cell identification."}
        r["x"]["definition"] = "Branch progress normalized to [0,1], oriented by the named electrode lithiation/delithiation direction; not absolute stoichiometry or full-cell SOC. Original normalizedCapacity and row positions are retained in auxiliary CSV columns."
        r["temperature"] = {"value_K": None, "description": "Half-cell numeric temperature not independently confirmed; the paper's 25 C full-cell ageing condition is not transferred."}
        r["quality"]["raw_data"] = "published_table_not_instrument_raw"
        r["limitations"] += ["Author-processed normalized-capacity/potential table; time, measured current and absolute capacity are absent.",
            "Filename 0C03 means 0.03C per author notice; paper Section 2.4 states 0.033C. Both labels retained; no numerical rate correction.",
            "Protocol voltage cutoffs do not establish that each supplied table contains every protocol endpoint."] if rate == .03 else [
            "Author-processed normalized-capacity/potential table; time, measured current and absolute capacity are absent.",
            "Protocol voltage cutoffs do not establish that each supplied table contains every protocol endpoint."]
        records.append(r)
    return records


def extend():
    load = lambda name: json.loads((DATA/(name+".json")).read_text())
    catalog, sources, assets, cells, materials, experiments, audit = [load(n) for n in
        ["catalog", "sources", "assets", "cells", "materials", "experiments", "matching_audit"]]
    pins = json.loads((ROOT/"scripts/tum_ocp_assets.json").read_text())
    for aid, asset in pins.items():
        if hashlib.sha256((DATA/asset["path"]).read_bytes()).hexdigest() != asset["sha256"]:
            raise ValueError("TUM checksum mismatch: " + aid)
        assets[aid] = asset
    sources[SID] = {"kind": "dataset", "title": "First-party Rehm2026 half-cell tables bundled with DegradationModeAnalysis v2.0.0",
        "authors": ["Mathias Rehm", "Josef Eizenhammer", "Moritz Guenthner"], "year": 2026,
        "url": "https://zenodo.org/records/19555109", "doi": "10.5281/zenodo.19555109", "version": "v2.0.0; archive d2e80c7",
        "license": "MIT", "license_evidence": "Fixed release metadata states MIT; bundled Mathias Rehm MIT notice and per-folder own-measurement attribution retained. Admission is limited to seven Rehm2026 first-party MATs, not third-party literature inputs.",
        "role": "Five harvested P45B branches and two laboratory graphite branches. Full-cell data remain externally linked."}
    sources[PAPER] = {"kind": "paper", "title": "How to determine the degradation modes of lithium-ion batteries with silicon-graphite blend electrodes",
        "authors": ["Mathias Rehm", "Johannes Natterer", "Josef Eizenhammer", "Moritz Guenthner", "Simon Kuecher", "Can Korkmaz", "Franz Roehrer", "Andreas Jossen"],
        "year": 2026, "doi": "10.1016/j.jpowsour.2026.239418", "url": "https://doi.org/10.1016/j.jpowsour.2026.239418",
        "role": "Methods Section 2.4 establishes lithium-counter coin-cell measurements; Data availability points to author GitHub. Article license is not used to relicense external tables."}
    sources["tum-rights-review-2026"] = {"kind": "documentation", "title": "M50LT and TUM OCP reuse/definition audit, 2026-10-23",
        "authors": ["E-BatP maintainers"],
        "url": "https://github.com/FrankSuperG/electrochemical-battery-parameters/blob/main/docs/TUM_OCP_RIGHTS.md", "year": 2026,
        "role": "Fixed-release metadata and unresolved third-party-source review; no third-party MAT files admitted."}
    curves = extract(pins)
    catalog["records"] = [r for r in catalog["records"] if r["provenance"]["processing"].get("script") != SCRIPT] + curves
    cell = {"manufacturer": "Molicel", "model": "INR21700-P45B", "display_name": "Molicel P45B | TUM Rehm2026 measured half-cells",
        "format": "21700 cylindrical; harvested electrodes in CR2032 half-cells", "chemistry": "NCA/silicon-graphite", "nominal_capacity_Ah": 4.5,
        "identity_level": "explicit_commercial_model", "source_ids": [SID, PAPER], "model_context": "Partial measured pseudo-OCP source package",
        "match_level": "same_model_same_study", "match_evidence": "Five harvested P45B half-cell branches and external serial23 checkups share paper/model; exact donor/serial identity unresolved. About:Energy P45B parameters are a separate study.",
        "coverage": {"ocp": "Five native finite-current pseudo-OCP branches, original nodes retained; Li/Li+ reference confirmed in Section 2.4.",
            "diffusion": "No same-study intrinsic diffusivity admitted.", "kinetics": "No same-study intrinsic kinetic law admitted.",
            "full_cell_tests": "External serial23 ageing pOCV checkups only; continuous I/V/T, dynamic/EIS and multi-temperature matrices not established."},
        "note": "Laboratory graphite comparator is material-only; reconstructed silicon is not a measured pure-material half cell."}
    audit_links({CID: cell}, catalog["records"], load("parameters")["records"], [])
    cell["missing_items"] += ["Exact harvested donor to serial23 mapping unresolved", "Numeric half-cell temperature not established",
        "Absolute half-cell capacity and stoichiometric balancing not supplied", "Same-study intrinsic D and kinetic coefficients not located",
        "0C03 filename rate is 0.03C; original paper protocol states 0.033C",
        "Full-cell tests are external links; 25 C is a paper condition, not a verified measured temperature channel"]
    cells[CID] = cell
    audit["cell_matches"][CID] = {"display_name": cell["display_name"], "match_level": cell["match_level"], "components": cell["evidence_matrix"], "missing_items": cell["missing_items"]}
    audit["checked_date"] = "2026-10-23"
    unlinked = next(row for row in audit["unmatched_material_records"] if row["material"] == "graphite")
    unlinked["record_ids"] += [r["id"] for r in curves
        if r["cell_link"]["cell_id"] is None and r["id"] not in unlinked["record_ids"]]
    for r in curves:
        materials[r["material_id"]] = {"label": r["material"], "cell_id": r["cell_link"]["cell_id"], "note": "Source-specific measured electrode, not a universal material curve."}
    for family in ["p45b", "graphite"]:
        associated = [r for r in curves if (r["cell_link"]["cell_id"] == CID) == (family == "p45b")]
        asset_ids = [r["provenance"]["asset_ids"][0] for r in associated]
        experiments[f"tum-rehm2026-{family}-coincell"] = {"source_id": SID, "asset_id": asset_ids[0], "asset_ids": asset_ids,
            "configuration": "CR2032 half-cell versus metallic lithium",
            "protocol": "Two cycles each at 0.05C, 0.033C and 0.02C; supplied filenames use 0.03C/0.02C. PE 3.0-4.3 V; SiGr 0.05-1.7 V vs Li." if family == "p45b" else
                        "SGL Carbon laboratory graphite at 0.0145C; protocol 0.01-1.5 V vs Li. Supplied branches can cover a narrower voltage interval.",
            "cycle_selected": None, "temperature_K": None, "known_issues": [],
            "selection": "All seven allowlisted author-processed branches; exact cycle index not supplied."}
    for name, value in [("catalog", catalog), ("sources", sources), ("assets", assets), ("cells", cells), ("materials", materials), ("experiments", experiments), ("matching_audit", audit)]:
        write_json(name+".json", value)
    print("TUM: 7 first-party pseudo-OCP branches, 40,378 original points; 5 P45B-linked, 2 material-only. No full-cell payload added.")


if __name__ == "__main__":
    extend()
