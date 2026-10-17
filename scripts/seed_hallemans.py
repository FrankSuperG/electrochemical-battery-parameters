"""Curate the licensed M50LT grouped fit and measured drive cycle, not its OCPs.

Pinned author files are read as data/text; no upstream Python or MATLAB runs.
The paper's grouped quantities are never inverted into intrinsic properties.
"""

import argparse
import hashlib
import json
import re
import shutil

import numpy as np
from scipy.io import loadmat

from seed_v01 import CACHE, DATA, ROOT, obtain, write_json
from seed_fullcell import audit_links, write_csv

CELL = "lg-m50lt-hallemans2025"
SOURCE = "hallemans-2025-repository"
PAPER = "hallemans-2025-paper-v4"
COMMIT = "3308a34396b8b56cd614291dd151c3405577c068"
SCRIPT = "scripts/seed_hallemans.py"
# Order independently checked in both Fig10 and Fig11, then against v4 Table 5.
# (name, category, unit, paper symbol, paper definition, optimization bounds)
SPECS = [
    ("Series resistance [Ohm]", "transport", "Ohm", "R_0", "Lumped series resistance of the grouped SPMe; not an isolated contact resistance.", [0.0125, 0.016]),
    ("Positive particle diffusion time scale [s]", "diffusion", "s", "tau_d_p", "tau_d_p = R_p^2 / D_p", [500, 10000]),
    ("Negative particle diffusion time scale [s]", "diffusion", "s", "tau_d_n", "tau_d_n = R_n^2 / D_n", [500, 10000]),
    ("Cation transference number", "transport", "1", "t_plus", "Cation transference number in the fitted electrolyte model.", [0.2, 0.7]),
    ("Positive electrode electrolyte diffusion time scale [s]", "transport", "s", "tau_e_p", "tau_e_p = epsilon_sep * L^2 / (epsilon_p^b_p * D_e)", [100, 1000]),
    ("Negative electrode electrolyte diffusion time scale [s]", "transport", "s", "tau_e_n", "tau_e_n = epsilon_sep * L^2 / (epsilon_n^b_n * D_e)", [100, 1000]),
    ("Separator electrolyte diffusion time scale [s]", "transport", "s", "tau_e_sep", "tau_e_sep = L^2 / (epsilon_sep^(b_sep - 1) * D_e); paper Table 2 convention.", [100, 1000]),
    ("Positive electrode charge transfer time scale [s]", "kinetics", "s", "tau_ct_p", "tau_ct_p = F * R_p / (m_p * sqrt(c_e0)); m_p is the paper's reference exchange-current prefactor.", [10, 5000]),
    ("Negative electrode charge transfer time scale [s]", "kinetics", "s", "tau_ct_n", "tau_ct_n = F * R_n / (m_n * sqrt(c_e0)); m_n is the paper's reference exchange-current prefactor.", [10, 5000]),
    ("Positive electrode capacitance [F]", "kinetics", "F", "C_p", "C_p = 3 * alpha_p * Cdl_p * L_p * A / R_p; whole-electrode capacitance, not F/m^2.", [0, 2]),
    ("Negative electrode capacitance [F]", "kinetics", "F", "C_n", "C_n = 3 * alpha_n * Cdl_n * L_n * A / R_n; whole-electrode capacitance, not F/m^2.", [0, 2]),
    ("Positive electrode relative porosity", "electrode", "1", "zeta_p", "zeta_p = epsilon_p / epsilon_sep; ratio, not absolute porosity.", [0.5, 1.7]),
    ("Negative electrode relative porosity", "electrode", "1", "zeta_n", "zeta_n = epsilon_n / epsilon_sep; ratio, not absolute porosity.", [0.5, 1.7]),
    ("Reference electrolyte capacity [A.s]", "transport", "A.s", "Q_e", "Q_e = F * epsilon_sep * c_e0 * L * A; reference electrolyte inventory in charge units, not cell capacity.", [500, 2000]),
    ("Minimum positive stoichiometry", "initial_state", "1", "c_p_100", "c_p_100 = c_p_at_100_percent_SOC / c_p_max; positive electrode minimum occurs at full-cell 100% SOC.", [0.1897, 0.1899]),
    ("Maximum positive stoichiometry", "initial_state", "1", "c_p_0", "c_p_0 = c_p_at_0_percent_SOC / c_p_max; positive electrode maximum occurs at full-cell 0% SOC.", [0.982, 0.984]),
    ("Minimum negative stoichiometry", "initial_state", "1", "c_n_0", "c_n_0 = c_n_at_0_percent_SOC / c_n_max; negative electrode minimum occurs at full-cell 0% SOC.", [0.0014, 0.0015]),
    ("Maximum negative stoichiometry", "initial_state", "1", "c_n_100", "c_n_100 = c_n_at_100_percent_SOC / c_n_max; negative electrode maximum occurs at full-cell 100% SOC.", [0.8862, 0.8864]),
]
GAPS = ["About:Energy M50LT OCP redistribution permission unresolved; no OCP imported",
        "Intrinsic solid diffusivity and reaction-rate prefactors not identified separately",
        "Measured cell and ambient temperature traces absent",
        "Standalone CC charge/discharge observations not deposited in the reviewed file set",
        "Serialized specimen mapping between OCP half-cells, EIS cell and drive-cycle cell unresolved",
        "Independent full-cell model reproduction not performed"]


def extend(download=False):
    load = lambda name: json.loads((DATA / (name + ".json")).read_text())
    doc, params, tests = load("catalog"), load("parameters")["records"], load("full_cell_tests")["records"]
    cells, sources, assets, audit = [load(n) for n in ["cells", "sources", "assets", "matching_audit"]]
    params = [p for p in params if p["cell_id"] != CELL]
    tests = [t for t in tests if t["cell_id"] != CELL]
    pins = json.loads((ROOT / "scripts/hallemans_assets.json").read_text())
    CACHE.mkdir(parents=True, exist_ok=True)
    for aid, asset in pins.items():
        if asset.get("path"):
            local = DATA / asset["path"]
            if not local.exists():
                original = obtain(asset["filename"], asset["url"], sha256=asset["sha256"], download=download)
                shutil.copyfile(original, local)
            if hashlib.sha256(local.read_bytes()).hexdigest() != asset["sha256"]:
                raise ValueError(f"Source checksum mismatch: {aid}")
        assets[aid] = asset
    authors = ["Noel Hallemans", "Nicola E. Courtier", "Colin P. Please", "Brady Planden", "Rishit Dhoot", "Robert Timms", "S. Jon Chapman", "David Howey", "Stephen R. Duncan"]
    sources.update({
        SOURCE: {"kind": "dataset_and_software", "title": "Hallemans2025 LG M50LT author data and scripts", "authors": authors,
                 "year": 2025, "version": COMMIT, "url": f"https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/{COMMIT}",
                 "license": "BSD-3-Clause", "license_evidence": "Pinned root LICENSE, Copyright (c) 2025 authors of journal paper, retained verbatim. Applied to author-owned measured data/results; no inferred grant for About:Energy third-party OCP inputs.",
                 "role": "Measured whole-cell EIS and drive cycle; fitted grouped-SPMe vector. Source code inspected as text, not executed."},
        PAPER: {"kind": "paper", "title": "Physics-based battery model parametrisation from impedance data", "authors": authors,
                "year": 2025, "doi": "10.1149/1945-7111/add41b", "url": "https://arxiv.org/html/2412.10896v4", "version": "arXiv v4, 2025-04-23", "license": "CC-BY-4.0",
                "role": "Table 2 definitions, Tables 4/5 EIS conditions and rounded fit, Section 7.3 measured drive-cycle interpretation. Earlier v3 is a different experiment/fit and is not combined."},
        "pybop-25-6-grouped": {"kind": "software", "title": "PyBOP v25.6 grouped SPMe", "authors": ["PyBOP team"], "year": 2025,
                              "version": "v25.6", "url": "https://github.com/pybop-team/PyBOP/blob/v25.6/pybop/models/lithium_ion/basic_SPMe.py", "license": "BSD-3-Clause",
                              "role": "Definition cross-check only. Separator conversion-helper convention differs from paper Table 2; fitted time scale is retained without inversion."},
        "aboutenergy-m50lt-ocp-lead": {"kind": "external_data_lead", "title": "About:Energy LG M50LT OCP inputs (reuse scope unresolved)",
                                     "authors": ["About:Energy Ltd"], "year": 2024,
                                     "url": f"https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/blob/{COMMIT}/Data/LGM50LT/Notes%20on%20LG%20M50LT%20OCP.pdf",
                                     "license": "unresolved", "role": "Paper Section 7 identifies personal communication; notes attribute OCP to About:Energy without separate reuse terms. Official company's CC-BY-SA-4.0 BPX repository describes a different NMC111 pouch cell, not M50LT. No OCP arrays, notes PDF or derived samples redistributed."},
    })
    def mat(aid):
        return loadmat(DATA / pins[aid]["path"], squeeze_me=True)
    fit, raw, drive = mat("hallemans-fit-mat"), mat("hallemans-eis-mat"), mat("hallemans-drive-mat")
    theta = fit["thetahat"]
    if theta.shape != (18,) or not np.isfinite(theta).all():
        raise ValueError("Unexpected fit vector")
    for name, a, b in [("Z", raw["Z"][:, 1:8], fit["Z"]), ("f", raw["f"], fit["f"]), ("SOC", raw["SOC"][1:8] / 100, fit["SOC"])]:
        if not np.array_equal(a, b):
            raise ValueError(f"Measured/fitted EIS lineage mismatch: {name}")
    for script in ["hallemans-fig10", "hallemans-fig11"]:
        text = (DATA / pins[script]["path"]).read_text()
        start = text.index("parameters = pybop.Parameters(")
        names = re.findall(r'pybop.Parameter\(\s*"([^"]+)"', text[start:])
        if names[:18] != [s[0] for s in SPECS]:
            raise ValueError(f"Parameter ordering mismatch: {script}")
    new_params = []
    for index, (name, category, unit, symbol, definition, bounds) in enumerate(SPECS):
        near = abs(float(theta[index])-bounds[0]) <= 1e-4*(bounds[1]-bounds[0]) or abs(float(theta[index])-bounds[1]) <= 1e-4*(bounds[1]-bounds[0])
        new_params.append({"id": "hallemans2025-" + symbol.lower().replace("_", "-"), "version": "1", "cell_id": CELL,
                           "name": name, "category": category, "unit": unit, "representation": {"kind": "scalar", "value": float(theta[index])},
                           "source_ids": [SOURCE, PAPER], "license": "BSD-3-Clause", "independent_validation": False,
                           "definition": definition,
                           "provenance": {"asset_id": "hallemans-fit-mat", "location": f"Zhat3mV_SOC_SPMe_LGM50LT.mat::thetahat[{index}] (zero-based); ordering: Fig10/Fig11 pybop.Parameters",
                                          "origin_status": "joint_EIS_fitted_grouped_SPMe_parameter; not independent material characterization"},
                           "conditions": {"parameterization_variant": "hallemans2025-v4-grouped-spme", "paper_symbol": symbol, "theta_index_zero_based": index,
                                          "definition_source": "arXiv v4 Table 2 / Appendix C", "ambient_setpoint_K": 298.15, "ambient_setpoint_scope": "EIS Table 4; not a measured temperature channel or verified drive-cycle setting",
                                          "fitted_SOC_fraction": fit["SOC"].tolist(), "optimization_bounds": bounds, "near_bound": near, "near_bound_rule": "Within 1e-4 of bound span; computational flag, not an uncertainty estimate",
                                          "model": "Grouped SPMe with differential double-layer surface form and contact resistance", "fitted_together": 18},
                           "limitations": ["Retain as a jointly fitted grouped quantity; do not label as an independently measured intrinsic coefficient.",
                                           "Some parameters clip at bounds; paper reports poor low-frequency fits. No confidence intervals or uniqueness claim.",
                                           "Fit uses external About:Energy OCPs and a Chen2020 initialization; OCP permission is unresolved, so no ready-to-run complete model is supplied."] + (["PyBOP v25.6 physical-to-grouped helper uses L^2/(epsilon_sep^b_sep*D_e), unlike paper's exponent b_sep-1; retained fitted value is not converted."] if symbol == "tau_e_sep" else [])})
    params += new_params
    t, i, v = [np.asarray(drive[k], dtype=float) for k in ["t", "i", "v"]]
    if any(x.shape != (164953,) or not np.isfinite(x).all() for x in [t, i, v]) or not np.all(np.diff(t) > 0):
        raise ValueError("Unexpected measured drive-cycle channels")
    rid = "hallemans2025-m50lt-drive-80to20"
    columns = ["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K", "ambient_temperature_K", "cycle", "step", "mode", "source_record"]
    digest = write_csv(f"full_cell/{rid}-normalized.csv", columns,
                       ([tt, ii, vv, "", "", "", "", "C" if ii > 0 else "D" if ii < 0 else "R", row+1] for row, (tt, ii, vv) in enumerate(zip(t, i, v))))
    evidence = "Same explicit LG M50LT model and Hallemans2025 study: Fig11 loads this drive-cycle MAT and the same fitted vector; v4 Section 7.3 identifies measured terminal voltage and Fig11 validation. Exact serialized-specimen chain to harvested OCP half-cells is not supplied."
    test = {"id": rid, "cell_id": CELL, "sample_id": "LG M50LT; serial not supplied", "asset_id": "hallemans-drive-mat", "source_id": SOURCE,
            "path": None, "original_download_path": pins["hallemans-drive-mat"]["path"], "original_format": "MATLAB v5 MAT",
            "normalized_path": f"full_cell/{rid}-normalized.csv", "normalized_sha256": digest, "license": "BSD-3-Clause", "csv_header_rows": 0,
            "protocol": "Measured drive cycle, nominal 80 to 20% SOC; repeated excitation, 0.15 s sampling, 24742.8 s elapsed; paper v4 Section 7.3 / Figure 11.",
            "relationship_to_parameters": "same_model_same_study", "evidence": evidence, "independent_validation_by_this_project": False,
            "observation_kind": "published_experimental_series", "row_count": len(t), "columns": columns, "discharge_segments": [],
            "format": "Published measured t/i/v arrays, all rows and native precision retained; not instrument export or simulated model output.",
            "current_convention": "Source i retained: charge positive, discharge negative. Author Fig11 negates i to supply PyBaMM's discharge-positive current. u is not used as voltage or substituted for measured i.",
            "temperature_definition": "No cell/ambient temperature array. Paper Table 4 specifies 25 degC for EIS; this is not assigned to drive-cycle rows.",
            "basic_test": {"type": "drive_cycle", "current_measurement": "supplied source i", "charge_trace": "available dynamic segments", "discharge_trace": "available dynamic segments", "voltage_trace": "available"},
            "processing": {"script": SCRIPT, "source_fields": {"time_s": "t [s]", "current_charge_positive_A": "i [A]", "voltage_V": "v [V]"},
                           "source_position": "source_record is one-based MATLAB array index", "changes": "Extract t/i/v without resampling, smoothing or unit changes; classify mode from i sign. Blank T/cycle/step remain unavailable.",
                           "omitted_fields": {"u": "Current-like array; precise measured/commanded/processed meaning unresolved. Retained only in original MAT."}},
            "missing_items": list(GAPS),
            "supporting_asset_ids": ["hallemans-fit-mat", "hallemans-eis-mat", "hallemans-fig10", "hallemans-fig11", "hallemans-license"],
            "source_checks": {"sampling_period_s": 0.15, "net_charge_Ah_trapezoid": float(np.sum((i[1:]+i[:-1])*np.diff(t)/2)/3600),
                              "note": "Integrated current is a consistency check, not an inferred capacity or SOC measurement."}}
    # Frequency-domain evidence is not miscounted as a time-domain test file.
    erel = "evidence/hallemans2025-m50lt-eis.csv"
    rows = []
    for j, soc in enumerate(raw["SOC"]):
        for k, freq in enumerate(raw["f"]):
            z = raw["Z"][k, j]
            zh = fit["Zhat"][k, j-1] if 1 <= j <= 7 else None
            rows.append([soc/100, freq, z.real, z.imag, raw["OCV"][j], "true" if zh is not None else "false", "" if zh is None else zh.real, "" if zh is None else zh.imag, k+1, j+1])
    ehash = write_csv(erel, ["SOC_fraction", "frequency_Hz", "measured_Z_real_Ohm", "measured_Z_imag_Ohm", "full_cell_OCV_V", "used_for_fit", "fitted_Z_real_Ohm", "fitted_Z_imag_Ohm", "source_frequency_index", "source_SOC_index"], rows)
    cell = {"manufacturer": "LG Energy Solution", "model": "M50LT", "display_name": "LG M50LT | Hallemans2025 grouped SPMe", "format": "Cylindrical; dimensions not independently verified in this import", "chemistry": "NMC/graphite; About:Energy notes assume NMC811/pure graphite",
            "nominal_capacity_Ah": None, "identity_level": "explicit_commercial_model", "source_ids": [SOURCE, PAPER, "aboutenergy-m50lt-ocp-lead", "pybop-25-6-grouped"],
            "model_context": "Grouped SPMe with double-layer capacitance; eighteen jointly EIS-fitted values", "match_level": "same_model_same_study", "match_evidence": evidence,
            "note": "M50LT is separate from Chen2020 LG M50. No intrinsic D or exchange-current law is reconstructed. About:Energy OCP inputs remain external with unresolved reuse scope. Paper v4 values match this vector after rounding; v3 describes a different fit.",
            "curation_guide": "docs/HALLEMANS2025.md", "missing_items": list(GAPS),
            "supporting_files": [{"path": erel, "sha256": ehash, "license": "BSD-3-Clause", "description": "EIS: 65 frequencies x 9 SOCs; measured complex impedance, full-cell OCV and seven-SOC model fit; 585 rows. Imaginary part retains source sign, not -Im(Z)."}],
            "coverage": {"ocp": "Third-party About:Energy OCPs used by source model; no separate M50LT reuse grant established, no curves imported.",
                         "diffusion": "Two fitted R^2/D particle time scales; not independent solid diffusivities. EIS Z/f/SOC exactly matches fit MAT selection.",
                         "kinetics": "Two fitted F*R/(m*sqrt(c_e0)) groups and two electrode capacitances; no intrinsic k or exchange-current density law.",
                         "full_cell_tests": "One same-study measured drive-cycle t/i/v series (164953 rows), nominal 80-20% SOC. No measured T or standalone CC cycle."}}
    audit_links({CELL: cell}, doc["records"], params, [test])
    cell["missing_items"] = sorted(set(cell["missing_items"] + GAPS))
    for component in ["diffusion", "kinetics"]:
        cell["evidence_matrix"][component]["missing_items"] += ["Intrinsic coefficients not separable from grouped fit without additional assumptions"]
    cell["evidence_matrix"]["ocp"]["match_level"] = "external_only_license_unresolved"
    cell["evidence_matrix"]["ocp"]["source_ids"] = [PAPER, "aboutenergy-m50lt-ocp-lead"]
    cell["evidence_matrix"]["ocp"]["missing_items"] = [GAPS[0], "Verified OCP half-cell to intact-cell specimen chain"]
    cell["evidence_matrix"]["full_cell_tests"]["missing_items"] = list(test["missing_items"])
    cell["evidence_matrix"]["basic_charge_discharge"] = {"record_ids": [], "source_ids": [], "match_level": "missing", "evidence": "Dynamic charge/discharge segments are available in drive cycle; no standalone constant-current test imported.", "missing_items": [GAPS[3]]}
    cells[CELL] = cell
    tests.append(test)
    audit["checked_date"] = "2026-10-17"
    audit["cell_matches"][CELL] = {"display_name": cell["display_name"], "match_level": cell["match_level"], "components": cell["evidence_matrix"], "missing_items": cell["missing_items"]}
    for rejection in ["LG M50LT/Hallemans2025 is not Chen2020 LG M50; no cross-model OCP or CC data join.", "Hallemans2025 grouped times/relative porosity are not intrinsic diffusivity, reaction-rate constant or absolute porosity."]:
        if rejection not in audit["rejected_joins"]:
            audit["rejected_joins"].append(rejection)
    doc["release"] = "0.7.0"
    for name, value in [("catalog", doc), ("parameters", {"schema_version": "0.1", "records": params}), ("full_cell_tests", {"schema_version": "0.1", "records": tests}), ("cells", cells), ("sources", sources), ("assets", assets), ("matching_audit", audit)]:
        write_json(name+".json", value)
    print("Hallemans2025: 18 grouped fitted parameters; 164953 measured t/i/v rows; 585 EIS evidence rows; no OCP redistributed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    extend(parser.parse_args().download)
