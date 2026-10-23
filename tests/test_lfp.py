"""Check source fidelity, identity limits and model-specific LFP definitions."""

import hashlib
import json
from pathlib import Path

import numpy as np
import pytest
from scipy.io import loadmat

from ebp import Catalog
from ebp.expression import evaluate

CACHE = Path(__file__).resolve().parents[1] / ".cache/upstream"


def cached(catalog, asset_id):
    asset = catalog.assets[asset_id]
    path = CACHE / asset["filename"]
    if not path.exists():
        pytest.skip("Source cache absent; run scripts/seed_v01.py --download")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
    return path


def test_lfp_coverage_and_match_limits():
    c = Catalog()
    assert len(c.parameters) == 1041
    assert len(c.full_cell_tests) == 51
    assert len(c.cells) == 19
    amp = c.cells["a123-amp20m1hd-a"]
    assert amp["model"] == "AMP20M1HD-A"
    assert amp["match_level"] == "same_model_same_study"
    assert len(c.search_parameters(cell_id="a123-amp20m1hd-a")) == 30
    assert len(c.linked_tests("a123-amp20m1hd-a")) == 1
    assert "a123-high-power-pouch-9ah" not in c.cells
    assert not c.linked_tests("a123-high-power-pouch-9ah")
    bpx = c.cells["bpx-lfp-18650-2ah-undisclosed"]
    assert bpx["manufacturer"] is bpx["model"] is None
    assert bpx["match_level"] == "unmatched"
    assert len(c.search(cell_id="bpx-lfp-18650-2ah-undisclosed")) == 2
    assert not c.linked_tests("bpx-lfp-18650-2ah-undisclosed")
    assert all(
        not t["independent_validation_by_this_project"] for t in c.full_cell_tests
    )


def test_amp20_table_units_derivation_and_evidence_hash():
    c = Catalog()
    for soc, td, ai0 in [(30, 552, 1.86e6), (50, 590, 1.80e6), (70, 622, 1.86e6)]:
        d = c.get_parameter(f"a123-amp20-effective-diffusivity-soc{soc}")
        assert d.value == (5e-6) ** 2 / td
        assert d.record["conditions"]["assumed_particle_radius_m"] == 5e-6
        assert d.record["conditions"]["cell_SOC_fraction"] == soc / 100
        assert (
            d.record["provenance"]["origin_status"]
            == "derived_from_fitted_time_and_assumed_radius"
        )
        assert (
            c.get_parameter(f"a123-amp20-volumetric-exchange-current-soc{soc}").value
            == ai0
        )
    assert c.get_parameter("a123-amp20-reaction-activation-energy-soc50").value == 29200
    assert c.get_parameter(
        "a123-amp20-heat-transfer-velocity-soc50"
    ).value == pytest.approx(5.06e-6, rel=1e-14)
    assert (
        c.get_parameter("a123-amp20-ionic-temperature-coefficient-soc30").value
        == 0.0024
    )
    asset = c.assets["lin2022-table1"]
    path = c.root / asset["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
    assert "transcription" in asset["digest_scope"]
    evidence = json.loads(path.read_text())
    assert len(evidence["rows"]) == 9


def test_bpx_operating_domains_and_scalar_fidelity():
    c = Catalog()
    bpx = json.loads(cached(c, "bpx-lfp-example").read_text())
    for material, component in [
        ("lfp", "Positive electrode"),
        ("graphite", "Negative electrode"),
    ]:
        group = bpx["Parameterisation"][component]
        curve = c.get(f"bpx-lfp18650-{material}-ocp")
        assert curve.record["representation"]["expression"] == group["OCP [V]"]
        assert curve.record["x"]["domain"] == [
            group["Minimum stoichiometry"],
            group["Maximum stoichiometry"],
        ]
        x = np.linspace(*curve.record["x"]["domain"], 1003)
        np.testing.assert_array_equal(curve(x), evaluate(group["OCP [V]"], x))
        assert np.isfinite(curve(x)).all()
        with pytest.raises(ValueError):
            curve(0)
    for p in c.search_parameters(cell_id="bpx-lfp-18650-2ah-undisclosed"):
        _, component, name = p.record["provenance"]["location"].split("/")
        original=bpx["Parameterisation"][component][name]
        if p.record["representation"]["kind"]=="scalar":
            assert p.value == original
        else:
            variable=next(iter(p.record["representation"]["variables"]))
            nodes=np.array([700.,1100.,1500.]) if variable=="c_e" else np.array([.1,.5,.9])
            np.testing.assert_allclose(p(**{variable:nodes}),evaluate(original,nodes),rtol=1e-14)
    positive = c.get_parameter(
        "bpx-lfp18650-positive-electrode-reaction-rate-constant-mol-m-2-s-1"
    )
    assert positive.record["unit"] == "mol.m-2.s-1"
    assert positive.value == 9.736e-7


def assert_column(rows, column, expected):
    actual = np.array([float(r[column]) if r[column] else np.nan for r in rows])
    np.testing.assert_array_equal(actual, expected)


def test_amp20_normalized_values_match_original_mat():
    c = Catalog()
    raw = loadmat(cached(c, "lin2022-full-discharge"), simplify_cells=True)
    test = c.linked_tests("a123-amp20m1hd-a")[0]
    rows = c.full_cell_data(test["id"], normalized=True)
    assert len(rows) == len(raw["V"]) == test["row_count"]
    assert_column(rows, "time_s", np.arange(len(rows)))
    assert_column(rows, "voltage_V", raw["V"])
    assert_column(rows, "current_charge_positive_A", raw["I"])
    assert_column(rows, "cell_temperature_K", np.mean(raw["A"], axis=(0, 1)) + 273.15)
    assert all(r["ambient_temperature_K"] == "" for r in rows)


def test_catalog_rejects_cross_cell_links_duplicate_tests_and_wrong_missing_counts():
    c = Catalog()
    c.cells["a123-amp20m1hd-a"]["full_cell_test_ids"].append(
        c.linked_tests("lg-m50")[0]["id"]
    )
    c.full_cell_tests.append(dict(c.full_cell_tests[0]))
    c.linked_tests("a123-amp20m1hd-a")[0]["missing_values"]["voltage_V"] = 1
    errors = c.validate()
    assert any("record ownership" in e for e in errors)
    assert any("Duplicate full-cell test IDs" in e for e in errors)
    assert any("Missing count mismatch for voltage_V" in e for e in errors)
