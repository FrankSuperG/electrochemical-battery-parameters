"""Offline HAIDI extraction from author-processed, checksum-pinned half-cells.

Dataset CC BY 4.0 is established through exact-DOI publisher catalog metadata,
not the framework's MIT license. A protocol-inconsistent branch is quarantined.
No full-cell observation payload or author MATLAB code is read or executed.
"""

import hashlib
import json

import numpy as np
from scipy.io import loadmat

from seed_v01 import DATA, ROOT, write_json
from seed_fullcell import audit_links
from seed_parameter_sources import table_record

CID = "haidi-hdcf18650-1800-rehm2025"
SID = "haidi-rehm2025-data"
PAPER = "rehm-2025"
SCRIPT = "scripts/seed_haidi.py"


def extract(pins, review):
    curves = []
    for branch in review["branch_reports"]:
        aid = branch["asset_id"]
        source = loadmat(DATA/pins[aid]["path"], simplify_cells=True)
        if {k for k in source if not k.startswith("__")} != {"batteryData"}:
            raise ValueError("Changed HAIDI MAT variable")
        values = source["batteryData"]
        if set(values) != {"normalizedCapacity", "voltage"}:
            raise ValueError("Changed HAIDI MAT fields")
        q, voltage = [np.asarray(values[k], dtype=float) for k in ["normalizedCapacity", "voltage"]]
        if q.ndim != 1 or voltage.shape != q.shape or len(q) != branch["point_count"]:
            raise ValueError("Changed HAIDI array shape")
        if not np.isfinite(q).all() or not np.isfinite(voltage).all() or len(np.unique(q)) != len(q):
            raise ValueError("Invalid HAIDI source nodes")
        if branch["admission"] == "quarantined_protocol_mismatch":
            if (np.flatnonzero(voltage < 2.0)+1).tolist() != review["quarantine"]["rows_below_protocol_minimum"]:
                raise ValueError("Changed quarantined HAIDI source")
            continue
        if branch["admission"] != "native_pseudo_ocp":
            raise ValueError("Unreviewed HAIDI admission state")
        filename = branch["filename"]
        material = "LFP" if "Cathode" in filename else "graphite"
        direction = "delithiation" if "Delithiation" in filename else "lithiation"
        rate = .02 if "0C02" in filename else .05
        q01 = (q-q.min())/(q.max()-q.min())
        desired_sign = -1 if direction == "lithiation" else 1
        reverse = np.sign(voltage[np.argmax(q)]-voltage[np.argmin(q)]) != desired_sign
        x = 1-q01 if reverse else q01
        order = np.argsort(x, kind="stable")
        rid = "haidi-rehm2025-" + filename.removeprefix("HAIDI18650_").removesuffix(".mat").lower().replace("_", "-")
        r = table_record(rid, material, CID, aid, SID, "CC-BY-4.0", x[order], voltage[order],
            ["source_normalized_capacity", "source_mat_row"], zip(x[order], voltage[order], q[order], order+1),
            "batteryData.normalizedCapacity; batteryData.voltage",
            {"script": SCRIPT, "source_variable": "batteryData", "source_member": pins[aid]["archive_member"],
             "source_rows": len(q), "omitted_rows": 0, "nominal_rate_C": rate,
             "source_capacity_bounds": [float(q.min()), float(q.max())], "reverse_normalized_axis": bool(reverse),
             "coordinate_transform": "q01=(q-min(q))/(max(q)-min(q)); x=1-q01 if reverse_normalized_axis else q01; stable sort ascending x",
             "orientation_basis": "Author notice names electrode lithiation/delithiation. Endpoint potential decreases on lithiation and increases on delithiation. Original capacity and row retained; no chronological acquisition order inferred.",
             "filtering": "No additional smoothing, clipping, resampling, deleted nodes or inserted endpoints. The original paper reports filtered displayed curves; exact MAT filtering history is unresolved."},
            direction=direction)
        r.update(title=f"HAIDI HDCF18650-1800 | {material} | {direction} | {rate}C | Rehm2025",
                 electrode_role="positive" if material == "LFP" else "negative",
                 experiment_id="haidi-rehm2025-"+material+"-halfcell")
        r["source_ids"] += [PAPER, "rehm-2026"]
        r["provenance"]["asset_ids"] += ["haidi-tum-source-notice", "haidi-rights-quality-review"]
        r["provenance"]["derivation"] = "author_processed_finite_current_half_cell_branch; original dataset byte identity unresolved"
        r["temperature"] = {"value_K": 298.15, "description": "Original Rehm2025 paper Section 1 states half-cell measurements at 25 C; full-cell temperatures are stored separately."}
        r["x"]["definition"] = "Normalized branch progress, not absolute lithium fraction or full-cell SOC. The author notice reports swapped anode direction/capacity conventions; named electrode direction and source endpoint potentials define this curation axis. Original source capacity/row are retained."
        r["quality"]["raw_data"] = "published_table_not_instrument_raw"
        r["cell_link"]["evidence"] = "Original paper identifies HAIDI HDCF18650-1800 (LIBHE); author notice links these electrode branches to that paper. Same-study full-cell tests are externally linked; exact harvested donor and test serials unresolved."
        r["limitations"] = [
            "Author-processed finite-current pseudo-OCP, not certified equilibrium or an original instrument recording.",
            "Absolute half-cell Ah, lithium stoichiometry, exact cycle selection and MAT filtering history are not supplied.",
            "Mirror-to-original-dataset byte identity cannot be checked while provider file inventory is unavailable.",
            "Supplied voltage coverage may be narrower than the complete protocol; no missing cutoff endpoints are inserted.",
            "Millivolt-scale cutoff excursions remain unchanged; source voltages are not clipped.",
            "Same-study association does not establish identical serialized half-cell/full-cell specimens or a transferable complete D/kinetics set.",
            "No independent electrochemical-model validation is claimed."]
        if material == "graphite" and direction == "delithiation" and rate == .05:
            r["limitations"].append("Two source nodes exceed the 1.5 V graphite cutoff by up to 2.8033 mV; retained as provided.")
        curves.append(r)
    if len(curves) != 7 or sum(r["representation"]["point_count"] for r in curves) != 98695:
        raise ValueError("Changed HAIDI admitted inventory")
    return curves


def extend():
    load = lambda name: json.loads((DATA/(name+".json")).read_text())
    catalog, sources, assets, cells, materials, experiments, audit = [load(n) for n in
        ["catalog", "sources", "assets", "cells", "materials", "experiments", "matching_audit"]]
    pins = json.loads((ROOT/"scripts/haidi_assets.json").read_text())
    for aid, asset in pins.items():
        if hashlib.sha256((DATA/asset["path"]).read_bytes()).hexdigest() != asset["sha256"]:
            raise ValueError("HAIDI checksum mismatch: "+aid)
        assets[aid] = asset
    review = json.loads((DATA/pins["haidi-rights-quality-review"]["path"]).read_text())
    if review["license_decision"]["identifier"] != "CC-BY-4.0":
        raise ValueError("HAIDI reuse decision not cleared")
    authors = ["Mathias Rehm", "Marco Fischer", "Manuel Rubio-Gomez", "Moritz Schuette", "Dirk Uwe Sauer", "Andreas Jossen"]
    sources[SID] = {"kind": "dataset", "title": "Rehm2025 HAIDI LFP/graphite subset of rate, OCV, impedance and half-cell dataset",
        "authors": authors, "year": 2025, "doi": "10.14459/2024mp1762675", "url": "https://mediatum.ub.tum.de/1762675",
        "license": "CC-BY-4.0", "version": "Dataset published 2025-01-31; author branch mirror from fixed release 19555109",
        "license_evidence": "Exact-DOI TUM publisher metadata in open.bydata/GovData identifies cc-by with author attribution; GovData and the official DCAT vocabulary map it to CC BY 4.0. Empty/incomplete duplicate metadata are retained in the review. Framework MIT is not the data grant.",
        "role": "Seven native author-processed half-cell branches, one quarantined original; same-study full-cell tests remain external. Original provider file inventory and mirror/raw-file identity unresolved."}
    sources[PAPER] = {"kind": "paper", "title": "Comparing the electrical performance of commercial sodium-ion and lithium-iron-phosphate batteries",
        "authors": authors, "year": 2025, "doi": "10.1016/j.jpowsour.2025.236290", "url": "https://doi.org/10.1016/j.jpowsour.2025.236290",
        "role": "Model identity, half-cell Li/25 C/rate definitions and full-cell multi-temperature charge/discharge/GEIS protocols. Only LIBHE selected; sodium-ion cell types excluded."}
    sources["haidi-review-2026"] = {"kind": "documentation", "title": "HAIDI source, license and quality review, 2026-10-24",
        "authors": ["E-BatP maintainers"], "year": 2026, "url": "https://github.com/FrankSuperG/electrochemical-battery-parameters/blob/main/docs/HAIDI_REHM2025.md",
        "role": "Curated factual evidence from original paper and publisher catalogs, with response hashes and explicit access/quality gaps."}
    curves = extract(pins, review)
    catalog["records"] = [r for r in catalog["records"] if r["cell_link"]["cell_id"] != CID]+curves
    cell = {"manufacturer": "HAIDI Energy Group", "model": "HDCF18650-1800", "display_name": "HAIDI HDCF18650-1800 | Rehm2025 LFP/graphite",
        "format": "18650 cylindrical; harvested electrodes in CR2032 half-cells", "chemistry": "LFP/graphite", "nominal_capacity_Ah": 1.8,
        "identity_level": "explicit_commercial_model", "source_ids": [SID, PAPER, "rehm-2026"],
        "curation_guide": "docs/HAIDI_REHM2025.md",
        "supporting_asset_ids": ["haidi-rights-quality-review", "haidi-haidi18650-cathode-delithiation-0c05"],
        "model_context": "Partial source-specific measured pseudo-OCP package", "match_level": "same_model_same_study",
        "match_evidence": "Paper LIBHE is HAIDI HDCF18650-1800. Author half-cell notice cites the same paper as the deposited whole-cell tests; exact donor/serial chain unresolved.",
        "coverage": {"ocp": "Seven admitted author-processed branches: four graphite and three LFP, at 25 C and 0.02/0.05C. One 0.05C cathode branch quarantined for protocol-inconsistent low potentials.",
            "diffusion": "No same-study intrinsic diffusivity admitted; relaxed OCV/GITT observations alone are not D estimates.",
            "kinetics": "No same-study intrinsic kinetic law admitted; GEIS alone is not a defined kinetic coefficient.",
            "full_cell_tests": "Same-study dataset/paper links: 10/20/25/30/35/45 C OCV, multi-rate CC/CP and GEIS. Individual original file names and measured channels remain unverified; no new payload packaged."},
        "quarantined_source_files": [review["quarantine"]],
        "note": "Source LIBHE subset only. No A123 match, no sodium-ion material import, no shared specimen assertion or automatic parameter transfer."}
    audit_links({CID: cell}, catalog["records"], load("parameters")["records"], [])
    cell["missing_items"] += ["Exact harvested donor and full-cell serial mapping unresolved", "Original provider full-cell file inventory and observation headers unavailable",
        "Absolute stoichiometric endpoints, half-cell Ah and exact MAT filtering/cycle history unresolved", "Same-study intrinsic diffusion and kinetic coefficients not located",
        "0.05C cathode delithiation held: nine source nodes below the paper's 2 V cutoff", "Dynamic road-cycle profiles and longitudinal ageing series not established"]
    cells[CID] = cell
    audit["cell_matches"][CID] = {"display_name": cell["display_name"], "match_level": cell["match_level"], "components": cell["evidence_matrix"], "missing_items": cell["missing_items"]}
    audit["checked_date"] = "2026-10-24"
    for r in curves:
        materials[r["material_id"]] = {"label": r["material"], "cell_id": CID, "note": "Source-specific harvested HAIDI electrode; branch endpoints are not absolute stoichiometry."}
    for material in ["LFP", "graphite"]:
        selected = [r for r in curves if r["material"] == material]
        aid = selected[0]["provenance"]["asset_ids"][0]
        experiments[f"haidi-rehm2025-{material}-halfcell"] = {"source_id": SID, "asset_id": aid,
            "asset_ids": [r["provenance"]["asset_ids"][0] for r in selected], "configuration": "Harvested single-side-coated HAIDI electrode, 14 mm disk, CR2032 half-cell against metallic lithium; 80 uL LP57",
            "protocol": "0.02C main protocol with earlier 0.05C cycles and 1 h pauses; graphite 0.01-1.5 V, LFP 2-4 V vs Li. Exact supplied MAT cycle indices unresolved.",
            "temperature_K": 298.15, "cycle_selected": None, "known_issues": ["One 0.05C cathode branch quarantined separately; original retained"] if material == "LFP" else []}
    for name, value in [("catalog", catalog), ("sources", sources), ("assets", assets), ("cells", cells), ("materials", materials), ("experiments", experiments), ("matching_audit", audit)]:
        write_json(name+".json", value)
    print("HAIDI: 7 pseudo-OCP branches / 98,695 original nodes; 1 branch quarantined. Full-cell data remain external.")


if __name__ == "__main__":
    extend()
