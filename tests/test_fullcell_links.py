"""Experimental source fidelity and conservative parameter/test matching."""

import csv
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest

from ebp import Catalog

CACHE = Path(__file__).resolve().parents[1] / ".cache/upstream"
ECKER = "kokam-slpb75106100-ecker2015"
ENERTECH = "enertech-lco-pouch-ai2020"


def test_matching_preserves_identity_borrowing_and_capacity_scale():
    c = Catalog()
    kokam = c.cells[ECKER]
    assert kokam["model"] == "SLPB75106100"
    assert kokam["nominal_capacity_Ah"] == 7.5
    assert kokam["implementation_capacity_Ah"] == 0.15625
    assert kokam["match_level"] == "same_model_same_study"
    assert len(c.linked_tests(ECKER)) == 2
    assert c.cells[ENERTECH]["model"] is None
    for category in ["diffusion", "kinetics"]:
        row = c.cells[ENERTECH]["evidence_matrix"][category]
        assert row["match_level"] == "borrowed_model_input"
        assert "dualfoil-attribution" in row["source_ids"]
    assert c.cells[ENERTECH]["match_level"] == "same_study_cell_family"
    assert not c.linked_tests("kokam-slpb78205130h-marquis2019")
    assert len(c.linked_tests("mohtat2020-nmc532-pouch")) == 5
    lead = c.matching_audit["research_leads"][0]
    assert lead["doi"] == "10.7302/wwma-hx25"
    assert "official_files_imported" in lead["status"]
    unlinked = {
        rid
        for row in c.matching_audit["unmatched_material_records"]
        for rid in row["record_ids"]
    }
    assert unlinked == {
        r.id for r in c.search() if r.record["cell_link"]["cell_id"] is None
    }


@pytest.mark.parametrize("fault", ["cross_cell", "channel_count", "stale_audit"])
def test_validation_rejects_misleading_link_or_channel_metadata(fault):
    c = Catalog()
    if fault == "cross_cell":
        c.cells[ECKER]["evidence_matrix"]["ocp"]["record_ids"].append(
            c.cells[ENERTECH]["ocp_record_ids"][0]
        )
        expected = "crosses cell ownership"
    elif fault == "channel_count":
        c.linked_tests(ECKER)[0]["channel_availability"]["current_charge_positive_A"][
            "present_rows"
        ] = 1
        expected = "Channel availability mismatch"
    else:
        c.matching_audit["cell_matches"][ECKER]["missing_items"] = []
        expected = "matching audit disagrees"
    assert any(expected in error for error in c.validate())


def test_discharge_rows_preserve_source_pairs_without_invented_current():
    c = Catalog()
    for cid in [ECKER, ENERTECH]:
        for test in c.linked_tests(cid):
            source = c.root / test["original_download_path"]
            assert (
                hashlib.sha256(source.read_bytes()).hexdigest()
                == c.assets[test["asset_id"]]["sha256"]
            )
            native = np.loadtxt(source, delimiter="," if cid == ECKER else None)
            rows = c.full_cell_data(test["id"], normalized=True)
            np.testing.assert_array_equal(
                [float(r["time_s"]) for r in rows], native[:, 0]
            )
            np.testing.assert_array_equal(
                [float(r["voltage_V"]) for r in rows], native[:, 1]
            )
            assert all(
                r["current_charge_positive_A"] == r["cell_temperature_K"] == ""
                for r in rows
            )
            assert [int(r["source_record"]) for r in rows] == list(
                range(1, len(rows) + 1)
            )
            assert test["basic_test"]["current_measurement"] == "not_supplied"
            assert (
                test["channel_availability"]["current_charge_positive_A"][
                    "present_rows"
                ]
                == 0
            )
            if cid == ECKER:
                assert test["observation_kind"] == "published_figure_digitization"


def test_temperature_rise_stays_on_separate_native_timebase():
    c = Catalog()
    sidecars = [(t, s) for t in c.linked_tests(ENERTECH) for s in t["sidecars"]]
    assert len(sidecars) == 3
    for test, side in sidecars:
        original = np.loadtxt(c.root / side["original_download_path"])
        with (c.root / side["path"]).open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        np.testing.assert_array_equal(
            [float(r["time_s"]) for r in rows], original[:, 0]
        )
        np.testing.assert_array_equal(
            [float(r["temperature_rise_K"]) for r in rows], original[:, 1]
        )
        assert (
            len(rows) != test["row_count"]
        )  # Actual source clocks have different lengths.
        assert "not interpolated" in side["processing"]
        assert c.full_cell_data(test["id"])[0]["cell_temperature_K"] == ""


def test_published_ocp_tables_keep_native_nodes_and_remove_only_named_guard():
    c = Catalog()
    for curve in c.search(cell_id=ENERTECH):
        r = curve.record
        aid = r["provenance"]["asset_ids"][0]
        path = CACHE / c.assets[aid]["filename"]
        if not path.exists():
            pytest.skip("Pinned source cache absent")
        assert hashlib.sha256(path.read_bytes()).hexdigest() == c.assets[aid]["sha256"]
        values = np.loadtxt(path, delimiter=",", comments="#")
        if r["material"] == "graphite":
            np.testing.assert_array_equal(values[0], [0, 3.5])
            values = values[1:]
        x, y = curve.points()
        np.testing.assert_array_equal(x, values[:, 0])
        np.testing.assert_array_equal(y, values[:, 1])
        assert r["measurement"] == "literature_table"
        assert r["x"]["domain"] == [float(x[0]), float(x[-1])]
        with pytest.raises(ValueError):
            curve(x[0] - 1e-6)


@pytest.mark.parametrize("name,cid", [("Ecker2015", ECKER), ("Ai2020", ENERTECH)])
def test_new_parameter_math_matches_pinned_source(name, cid):
    pybamm = pytest.importorskip("pybamm")
    c = Catalog()
    path = CACHE / f"{name}-v25.4.2.py"
    if not path.exists():
        pytest.skip("Pinned source cache absent")
    asset = c.assets[f"pybamm-{name.lower()}-code"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
    spec = importlib.util.spec_from_file_location("checked_fullcell_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    upstream = module.get_parameter_values()
    for p in [p for p in c.search_parameters(cell_id=cid) if not p.id.startswith("model-completion-")]:
        if p.record["representation"]["kind"] == "scalar":
            assert p.value == upstream[p.record["name"]]
        else:
            for temperature in [283.15, 298.15, 313.15]:
                kwargs = (
                    {"sto": 0.413, "T": temperature}
                    if p.record["category"] == "diffusion"
                    else {
                        "c_e": 1100,
                        "c_s_surf": 12345,
                        "c_s_max": 32100,
                        "T": temperature,
                    }
                )
                expected = upstream[p.record["name"]](**kwargs)
                if isinstance(expected, pybamm.Symbol):
                    expected = expected.evaluate()
                assert p(**kwargs) == pytest.approx(float(expected), rel=1e-9)
    if cid == ECKER:
        x = np.array([0.0037, 0.1231, 0.4997, 0.8103, 0.9971])
        for curve in c.search(cell_id=cid):
            function = getattr(
                module, curve.record["representation"]["source_function"]
            )
            np.testing.assert_allclose(curve(x), function(x), atol=2e-13, rtol=2e-13)
