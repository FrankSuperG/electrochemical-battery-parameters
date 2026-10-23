"""Source evidence, implementation differences and no fabricated time/current."""

import csv
import hashlib
import io
import json
import zipfile

import numpy as np
from scipy.io import loadmat

from ebp import Catalog
from ebp.site import build_site

CID = "mohtat2020-nmc532-pouch"


def test_official_mat_arrays_keep_paired_capacity_voltage_temperature():
    c = Catalog()
    tests = c.linked_tests(CID)
    assert len(tests) == 5
    assert sum(t["row_count"] for t in tests) == 6474
    for test in tests:
        asset = c.assets[test["asset_id"]]
        source = c.root / asset["path"]
        assert hashlib.sha256(source.read_bytes()).hexdigest() == asset["sha256"]
        native = loadmat(source, simplify_cells=True)
        rows = c.full_cell_data(test["id"], normalized=True)
        np.testing.assert_array_equal(
            [float(r["charge_capacity_Ah"]) for r in rows], native["Q_data"]
        )
        np.testing.assert_array_equal(
            [float(r["voltage_V"]) for r in rows], native["Vt_data"]
        )
        np.testing.assert_array_equal(
            [float(r["cell_temperature_K"]) for r in rows], native["Temp_data"] + 273.15
        )
        assert all(r["time_s"] == r["current_charge_positive_A"] == "" for r in rows)
        assert test["independent_variable"]["column"] == "charge_capacity_Ah"
        assert not test["basic_test"]["sampling_interval_applied_to_time"]
    issue_test = next(t for t in tests if t["basic_test"]["nominal_C_rate"] == 0.5)
    assert any("C/2.5" in issue for issue in issue_test["source_issues"])


def test_author_parameterization_is_separate_from_pybamm_variant():
    c = Catalog()
    assert len(c.search_parameters(cell_id=CID, variant="original_author_mpm")) == 33
    assert len(c.search_parameters(cell_id=CID, variant="pybamm_v25_4_2")) == 105
    params = c.search_parameters(cell_id=CID)
    assert (
        len(
            [
                p
                for p in params
                if p.record["conditions"]["parameterization_variant"]
                == "original_author_mpm"
            ]
        )
        == 33
    )
    assert (
        len(
            [
                p
                for p in params
                if p.record["conditions"]["parameterization_variant"]
                == "pybamm_v25_4_2"
            ]
        )
        == 105
    )
    assert c.get_parameter("mohtat-author-ds-n").value == 5e-15
    assert c.get_parameter("mohtat-author-ds-p").value == 8e-15
    assert c.get_parameter("mohtat-author-k0-n").value == 1.1e-11
    assert c.get_parameter("mohtat-author-k0-p").value == 5e-11
    x = 0.01
    delta = c.get("mohtat-author-graphite-ocp")(x) - c.get("mohtat2020-graphite-ocp")(x)
    expected = 0.8 * (np.exp(-75 * (x + 0.007)) - np.exp(-75 * (x + 0.001)))
    np.testing.assert_allclose(delta, expected, atol=1e-15)
    crosswalk = json.loads(
        (c.root / "evidence/mohtat2020-parameter-crosswalk.json").read_text()
    )
    assert not crosswalk["identical_parameterization"]


def test_offline_bundle_keeps_native_axis_and_source_bytes(tmp_path):
    c = Catalog()
    build_site(c, tmp_path)
    with zipfile.ZipFile(tmp_path / "downloads" / f"{CID}-bundle.zip") as archive:
        package = json.loads(archive.read(f"{CID}-parameters.json"))
        assert all(t["cell_id"] == CID for t in package["full_cell_tests"])
        for test in package["full_cell_tests"]:
            original = test["original_download_path"]
            assert (
                archive.read("sources/" + c.assets[test["asset_id"]]["filename"])
                == (c.root / original).read_bytes()
            )
        assert "sources/main.m" in archive.namelist()
        assert "sources/READ_ME.pdf" in archive.namelist()
    data = json.loads(
        (tmp_path / "catalog.js")
        .read_text()
        .removeprefix("window.EBP_DATA = ")
        .removesuffix(";\n")
    )
    test = next(t for t in data["full_cell_tests"] if t["cell_id"] == CID)
    points = test["preview_segments"][0]["points"]
    source = c.full_cell_data(test["id"], normalized=True)
    assert points[-1][0] == float(source[-1]["charge_capacity_Ah"])
