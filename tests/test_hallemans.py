"""Independent fidelity checks against the pinned M50LT MATLAB and author scripts."""

import csv
import hashlib
import re
import zipfile

import numpy as np
from scipy.io import loadmat

from ebp import Catalog
from ebp.site import build_site

CELL = "lg-m50lt-hallemans2025"


def native(c, aid):
    a = c.assets[aid]
    p = c.root / a["path"]
    assert hashlib.sha256(p.read_bytes()).hexdigest() == a["sha256"]
    return loadmat(p, squeeze_me=True)


def test_grouped_fit_order_units_and_paper_conventions():
    c = Catalog()
    fit = native(c, "hallemans-fit-mat")
    records = [p.record for p in c.search_parameters(cell_id=CELL)]
    assert len(records) == 18
    text = (c.root / c.assets["hallemans-fig11"]["path"]).read_text()
    names = re.findall(r'pybop.Parameter\(\s*"([^"]+)"', text[text.index("parameters = pybop.Parameters("):])[:18]
    assert names == [p["name"] for p in records]
    np.testing.assert_array_equal([p["representation"]["value"] for p in records], fit["thetahat"])
    # Independent published v4 Table 5 values, compared only at printed precision.
    assert abs(fit["thetahat"][0] - 0.0145) < 0.000005
    np.testing.assert_allclose(fit["thetahat"][1:3], [8953, 7974], atol=0.5, rtol=0)
    assert round(fit["thetahat"][3], 2) == 0.70
    assert round(fit["thetahat"][11], 2) == 1.70
    assert c.get_parameter("hallemans2025-tau-d-p").record["unit"] == "s"
    assert "R_p^2 / D_p" in c.get_parameter("hallemans2025-tau-d-p").record["definition"]
    assert "epsilon_p / epsilon_sep" in c.get_parameter("hallemans2025-zeta-p").record["definition"]
    separator = c.get_parameter("hallemans2025-tau-e-sep").record
    assert "b_sep - 1" in separator["definition"]
    assert any("conversion" in x or "helper" in x for x in separator["limitations"])
    assert all(p["unit"] != "m2.s-1" for p in records)
    assert all(not p["independent_validation"] for p in records)


def test_measured_eis_and_fitted_slice_are_identical():
    c = Catalog()
    raw, fit = native(c, "hallemans-eis-mat"), native(c, "hallemans-fit-mat")
    np.testing.assert_array_equal(raw["Z"][:, 1:8], fit["Z"])
    np.testing.assert_array_equal(raw["f"], fit["f"])
    np.testing.assert_array_equal(raw["SOC"][1:8]/100, fit["SOC"])
    evidence = c.cells[CELL]["supporting_files"][0]
    with (c.root / evidence["path"]).open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 585
    assert sum(r["used_for_fit"] == "true" for r in rows) == 455
    np.testing.assert_array_equal([float(r["measured_Z_imag_Ohm"]) for r in rows], raw["Z"].T.imag.ravel())


def test_drive_cycle_is_original_measured_t_i_v_with_no_temperature_imputation():
    c = Catalog()
    raw = native(c, "hallemans-drive-mat")
    test = c.linked_tests(CELL)[0]
    rows = c.full_cell_data(test["id"], normalized=True)
    assert len(rows) == 164953
    for column, field in [("time_s", "t"), ("current_charge_positive_A", "i"), ("voltage_V", "v")]:
        np.testing.assert_array_equal([float(r[column]) for r in rows], raw[field])
    assert all(not r["cell_temperature_K"] and not r["ambient_temperature_K"] for r in rows)
    assert [rows[0]["source_record"], rows[-1]["source_record"]] == ["1", "164953"]
    assert test["basic_test"]["type"] == "drive_cycle"
    assert -2.94 < test["source_checks"]["net_charge_Ah_trapezoid"] < -2.91
    assert not np.array_equal(raw["u"], raw["v"])


def test_m50lt_is_separate_ocp_is_external_and_cc_remains_missing():
    c = Catalog()
    cell = c.cells[CELL]
    assert cell["model"] == "M50LT" and c.cells["lg-m50"]["model"] == "M50"
    assert not c.search(cell_id=CELL)
    assert cell["evidence_matrix"]["ocp"]["match_level"] == "external_only_license_unresolved"
    assert cell["evidence_matrix"]["basic_charge_discharge"]["match_level"] == "missing"
    assert any("OCP redistribution permission unresolved" in s for s in cell["missing_items"])
    assert any("Standalone CC" in s for s in cell["missing_items"])
    for aid, asset in c.assets.items():
        if aid.startswith("hallemans-ocp-"):
            assert asset["license"] == "unresolved" and "path" not in asset
    # Supporting evidence is covered by the same integrity check as test CSVs.
    cell["supporting_files"][0]["sha256"] = "0"*64
    assert any("supporting evidence SHA-256" in e for e in c.validate())


def test_offline_bundle_keeps_eis_sources_and_notice_but_no_ocp(tmp_path):
    c = Catalog()
    build_site(c, tmp_path)
    with zipfile.ZipFile(tmp_path / "downloads" / f"{CELL}-bundle.zip") as z:
        assert z.read("sources/hallemans2025-m50lt-eis.csv") == (c.root / c.cells[CELL]["supporting_files"][0]["path"]).read_bytes()
        assert "licenses/Hallemans2025-BSD-3-Clause.txt" in z.namelist()
        assert all("OCP_LGM50LT" not in n and "Uneg" not in n and "Upos" not in n for n in z.namelist())
