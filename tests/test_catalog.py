import copy
import hashlib
import json
from pathlib import Path
import shutil

import numpy as np
import pytest

from ebp import Catalog, StoichiometryMapping
from ebp.expression import evaluate


@pytest.fixture(scope="module")
def catalog():
    return Catalog()


def test_complete_catalog_and_link_integrity(catalog):
    assert catalog.validate() == []
    assert len(catalog.search(material="LFP")) == 9
    assert len(catalog.search(material="graphite")) == 20
    assert len(catalog.search(representation="table")) == 57
    assert len(catalog.search_parameters(cell_id="lg-m50")) == 38
    assert len(catalog.linked_tests("lg-m50")) == 3
    assert all(
        not c.record["quality"]["independent_validation"] for c in catalog.search()
    )


def test_provenance_does_not_conflate_paper_software_or_cell(catalog):
    lfp = catalog.get("lfp-afshar2017-formula").record
    assert lfp["source_ids"] == ["afshar-2017", "pybamm-25-4-2"]
    assert lfp["cell_link"]["cell_id"] is None
    for curve in catalog.search(representation="table"):
        if not curve.id.startswith("sintef-"):
            continue
        assert curve.record["x"]["kind"] == "normalized_branch_capacity"
        assert curve.record["temperature"]["value_K"] is None
        assert curve.record["cell_link"]["relationship"] == "material_only"


@pytest.mark.parametrize("method", ["linear", "pchip"])
def test_interpolation_preserves_observed_nodes(catalog, method):
    for curve in catalog.search(representation="table"):
        x, y = curve.points()
        selection = np.unique(np.linspace(0, len(x) - 1, 57, dtype=int))
        np.testing.assert_allclose(
            curve(x[selection], method=method), y[selection], atol=1e-13, rtol=0
        )


@pytest.mark.parametrize("bad", [-1e-8, 1.00000001, np.nan, np.inf, [0.5, np.nan]])
def test_no_silent_extrapolation_or_nonfinite_input(catalog, bad):
    for rid in ["lfp-afshar2017-formula", "sintef-lfp-d07eb6-c3-lithiation"]:
        with pytest.raises(ValueError):
            catalog.get(rid)(bad)


@pytest.mark.parametrize(
    "malicious",
    [
        "__import__('os').system('id')",
        "x.__class__",
        "[x][0]",
        "exp(x, x)",
        "x**9999",
        "x**x",
    ],
)
def test_formula_language_rejects_executable_syntax(malicious):
    with pytest.raises(ValueError):
        evaluate(malicious, 0.5)


def test_capacity_mapping_requires_evidence_and_correct_direction(catalog):
    curve = catalog.get("sintef-lfp-d07eb6-c3-delithiation")
    with pytest.raises(ValueError, match="unknown"):
        curve.to_pybamm()
    with pytest.raises(ValueError):
        StoichiometryMapping(0.2, 0.8, "")
    with pytest.raises(ValueError, match="direction"):
        curve.to_pybamm(StoichiometryMapping(0.2, 0.8, "test evidence"))


def test_integrity_reports_changed_data_and_invalid_records(catalog, tmp_path):
    shutil.copytree(catalog.root, tmp_path / "data")
    altered = Catalog(tmp_path / "data")
    curve = altered.get("sintef-lfp-d07eb6-c3-lithiation")
    with curve._path().open("a") as handle:
        handle.write("\n")
    assert any("SHA-256 mismatch" in e for e in altered.validate())
    altered.document["records"][0].pop("x")
    assert any("schema:" in e for e in altered.validate())


def test_export_preserves_native_table_and_json_cli(catalog, tmp_path, capsys):
    from ebp.cli import main

    curve = catalog.get("sintef-lfp-d07eb6-c3-lithiation")
    target = tmp_path / "curve.csv"
    curve.export_csv(target)
    assert (
        hashlib.sha256(target.read_bytes()).hexdigest()
        == curve.record["representation"]["sha256"]
    )
    metadata = tmp_path / "curve.json"
    assert (
        main(["export", curve.id, "--output", str(metadata), "--format", "json"]) == 0
    )
    document = json.loads(metadata.read_text())
    assert document["experiment"]["sample_id"] == "d07eb6"
    assert set(document["upstream_assets"]) == set(
        curve.record["provenance"]["asset_ids"]
    )


def test_nonocp_scalar_and_kinetic_function(catalog):
    diffusion = catalog.search_parameters(cell_id="lg-m50", category="diffusion")
    assert {p.record["name"] for p in diffusion} == {
        "Negative particle diffusivity [m2.s-1]",
        "Positive particle diffusivity [m2.s-1]",
    }
    parameter = catalog.search_parameters("Negative particle diffusivity")[0]
    assert parameter.value == 3.3e-14
    negative = catalog.get_parameter("lgm50-negative-exchange-current-density")
    expected = 6.48e-7 * np.sqrt(1000 * 10000 * 20000)
    assert negative(c_e=1000, c_s_surf=10000, c_s_max=30000, T=298.15) == pytest.approx(
        expected
    )
    with pytest.raises(ValueError):
        negative(c_e=1000, c_s_surf=31000, c_s_max=30000, T=298.15)
    with pytest.raises(ValueError):
        negative(c_e=1000, c_s_surf=10000, c_s_max=30000, T=0)
