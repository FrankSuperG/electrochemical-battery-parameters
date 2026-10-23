"""First-party TUM admission retains all nodes and conservative source matches."""

import csv
import json

import numpy as np
import pytest
from scipy.io import loadmat

from ebp import Catalog

CID = "molicel-p45b-tum-rehm2026"


def tum_curves(catalog):
    return catalog.search(source="tum-rehm2026-v2")


def test_tum_first_party_whitelist_and_scoped_rights():
    c = Catalog()
    curves = tum_curves(c)
    assert len(curves) == 7
    assert sum(r.record["representation"]["point_count"] for r in curves) == 40378
    assert len(c.search(cell_id=CID)) == 5
    assert not c.search_parameters(cell_id=CID)
    assert not c.linked_tests(CID)
    assert all(r.record["license"] == "MIT" for r in curves)
    assert all(r.record["measurement"] == "pseudo_ocp" for r in curves)
    review = c._load("evidence/tum-rehm2026/rights-review.json")
    assert len(review["admission"]["files"]) == 7
    assert {row["asset_id"] for row in review["admission"]["files"]} == {
        r.record["provenance"]["asset_ids"][0] for r in curves}
    metadata = c._load("evidence/tum-rehm2026/zenodo-19555109.json")
    assert metadata["metadata"]["license"]["id"] == "mit-license"
    notice = (c.root/"evidence/tum-rehm2026/LICENSE").read_text()
    assert "Copyright (c) 2025 Mathias Rehm" in notice
    assert "Permission is hereby granted" in notice
    mat_members = [a["archive_member"] for a in c.assets.values()
                   if a.get("source_id") == "tum-rehm2026-v2" and a.get("archive_member", "").endswith(".mat")]
    assert len(mat_members) == 7
    assert not any("SiReconstr" in m or "test_data" in m or "M35A" in m for m in mat_members)
    holds = {row["id"] for row in review["held_sources"]}
    assert {"m50lt-hallemans", "haidi-lfp-graphite", "tum-third-party-literature", "tum-reconstructed-silicon"} <= holds
    assert not c.search(cell_id="lg-m50lt-hallemans2025")


@pytest.mark.parametrize("index", range(7))
def test_every_tum_source_node_row_and_direction_is_preserved(index):
    c = Catalog()
    curve = tum_curves(c)[index]
    r = curve.record
    info = r["provenance"]["processing"]
    asset = c.assets[r["provenance"]["asset_ids"][0]]
    original = loadmat(c.root/asset["path"], simplify_cells=True)[info["source_variable"]]
    q, v = original["normalizedCapacity"], original["voltage"]
    with (c.root/r["representation"]["path"]).open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    source_row = np.array([int(row["source_mat_row"]) for row in rows])-1
    np.testing.assert_array_equal(np.sort(source_row), np.arange(len(q)))
    np.testing.assert_array_equal([float(row["source_normalized_capacity"]) for row in rows], q[source_row])
    x, potential = curve.points()
    np.testing.assert_array_equal(potential, v[source_row])
    normalized = (q-q.min())/(q.max()-q.min())
    if info["reverse_normalized_axis"]:
        normalized = 1-normalized
    np.testing.assert_array_equal(x, normalized[source_row])
    assert np.all(np.diff(x) > 0) and x[0] == 0 and x[-1] == 1
    expected_sign = -1 if r["direction"] == "lithiation" else 1
    assert np.sign(potential[-1]-potential[0]) == expected_sign
    np.testing.assert_array_equal(curve(x), potential)
    assert info["omitted_rows"] == 0
    assert r["reference"] == "Li/Li+"
    assert r["temperature"]["value_K"] is None
    assert r["quality"]["axis_status"] == "relative_capacity_only"
    assert r["quality"]["raw_data"] == "published_table_not_instrument_raw"
    assert not r["quality"]["independent_validation"]
    if "0C03" in asset["filename"]:
        assert info["nominal_rate_C"] == .03
        assert info["paper_protocol_rate_C"] == .033
    if r["material"] == "graphite":
        assert r["cell_link"]["cell_id"] is None
        assert r["cell_link"]["relationship"] == "material_only"
        assert info["source_variable"].endswith("Kuecher")


def test_tum_study_join_does_not_transfer_aboutenergy_parameters_or_channels():
    c = Catalog()
    source = c.search_datasets(cell_id=CID)
    assert len(source) == 1
    source = source[0]
    assert source["parameter_link"]["match_level"] == "same_model_same_study"
    assert source["ocp_anchor"]["kind"] == "catalog_half_cell"
    assert set(source["parameter_components"]["ocp"]["record_ids"]) == {r.id for r in c.search(cell_id=CID)}
    assert source["parameter_link"]["missing_components"] == ["diffusion", "kinetics"]
    assert not source["channels"]["time_series"]
    assert not source["ocp_anchor"]["half_cell_temperatures_C"]
    assert source["temperatures_C"] == [25]  # Paper condition, not a measured channel.
    whole = [f for f in source["file_links"] if f["source_sample_id"] == "serial23"]
    assert len(whole) == 1 and whole[0]["content_review"] == "not_read"
    assert source["storage"] == "external_link"
    assert all("aboutenergy" not in rid for rid in source["parameter_components"]["ocp"]["record_ids"])
    assert len(c.full_cell_tests) == 61
