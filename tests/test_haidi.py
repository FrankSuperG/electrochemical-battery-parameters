"""HAIDI data rights, all original nodes, quarantine and whole-cell link grain."""

import csv

import numpy as np
import pytest
from scipy.io import loadmat

from ebp import Catalog
from ebp.site import _ocp_license_url

CID = "haidi-hdcf18650-1800-rehm2025"


def test_haidi_rights_are_dataset_specific_and_conflicts_are_retained():
    c = Catalog()
    review = c._load("evidence/haidi-rehm2025/review.json")
    rights = review["license_decision"]
    assert rights["identifier"] == "CC-BY-4.0"
    assert rights["distribution_access_url"] == "https://mediatum.ub.tum.de/1762675"
    assert rights["bydata_catalog_id"] == "mediatum"
    assert rights["govdata_ui_license_url"] == "https://creativecommons.org/licenses/by/4.0/"
    assert len(rights["conflicts"]) == 3
    assert "Sch" in rights["attribution"] and "Rehm" in rights["attribution"]
    assert len(c.search(cell_id=CID)) == 7
    assert sum(r.record["representation"]["point_count"] for r in c.search(cell_id=CID)) == 98695
    assert all(r.record["license"] == "CC-BY-4.0" for r in c.search(cell_id=CID))
    # A framework citation cannot replace the record's data license/notice.
    assert _ocp_license_url({"source_ids": ["tum-rehm2026-v2"], "license": "CC-BY-4.0"}) == "licenses/CC-BY-4.0.txt"


@pytest.mark.parametrize("index", range(7))
def test_all_haidi_original_nodes_survive_branch_progress_conversion(index):
    c = Catalog()
    curve = c.search(cell_id=CID)[index]
    r = curve.record
    asset = c.assets[r["provenance"]["asset_ids"][0]]
    original = loadmat(c.root/asset["path"], simplify_cells=True)["batteryData"]
    q, potential = original["normalizedCapacity"], original["voltage"]
    with (c.root/r["representation"]["path"]).open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    source_row = np.array([int(row["source_mat_row"]) for row in rows])-1
    np.testing.assert_array_equal(np.sort(source_row), np.arange(len(q)))
    np.testing.assert_array_equal([float(row["source_normalized_capacity"]) for row in rows], q[source_row])
    x, voltage = curve.points()
    np.testing.assert_array_equal(voltage, potential[source_row])
    expected_x = (q-q.min())/(q.max()-q.min())
    if r["provenance"]["processing"]["reverse_normalized_axis"]:
        expected_x = 1-expected_x
    np.testing.assert_array_equal(x, expected_x[source_row])
    np.testing.assert_array_equal(curve(x), voltage)
    assert x[0] == 0 and x[-1] == 1 and np.all(np.diff(x)>0)
    assert np.sign(voltage[-1]-voltage[0]) == (-1 if r["direction"] == "lithiation" else 1)
    assert r["temperature"]["value_K"] == 298.15 and r["reference"] == "Li/Li+"
    assert r["electrode_role"] == ("positive" if r["material"] == "LFP" else "negative")
    assert r["quality"]["raw_data"] == "published_table_not_instrument_raw"
    assert r["quality"]["axis_status"] == "relative_capacity_only"
    assert not r["quality"]["independent_validation"]
    assert r["provenance"]["processing"]["omitted_rows"] == 0


def test_quarantined_cathode_is_not_silently_repaired_or_counted_as_ocp():
    c = Catalog()
    review = c._load("evidence/haidi-rehm2025/review.json")
    b = next(b for b in review["branch_reports"] if b["admission"].startswith("quarantined"))
    a = c.assets[b["asset_id"]]
    original = loadmat(c.root/a["path"], simplify_cells=True)["batteryData"]
    assert len(original["voltage"]) == 9224
    assert (np.flatnonzero(original["voltage"]<2)+1).tolist() == list(range(1,10))
    assert original["voltage"].min() == pytest.approx(1.54006766759693)
    assert not any(b["asset_id"] in r.record["provenance"]["asset_ids"] for r in c.search())
    assert not (c.root/"curves/haidi-rehm2025-cathode-delithiation-0c05.csv").exists()
    assert c.cells[CID]["quarantined_source_files"][0]["original_preserved"]


def test_haidi_same_study_conditions_do_not_become_verified_fullcell_files():
    c = Catalog()
    source = c.search_datasets(cell_id=CID)[0]
    assert source["parameter_link"]["match_level"] == "same_model_same_study"
    assert source["temperatures_C"] == [10,20,25,30,35,45]
    assert source["ocp_anchor"]["half_cell_temperatures_C"] == [25]
    assert len(source["ocp_anchor"]["source_paths"]) == 7
    assert len(source["file_links"]) == 9
    assert source["parameter_link"]["missing_components"] == ["diffusion", "kinetics"]
    assert source["aging_data"]["status"] == "not_reported"
    assert not source["profiles"] and not source["channels"]["time_series"] and not source["channels"]["frequency_domain"]
    for key in ["multi_rate_charge", "multi_rate_discharge", "EIS"]:
        assert source["test_coverage"][key]["status"] == "container_only"
    assert not any(f["dataset_id"] == source["id"] for f in c.search_dataset_files(test_type="eis"))
    assert not c.linked_tests(CID) and not c.search_parameters(cell_id=CID)
    assert len(c.full_cell_tests) == 61
