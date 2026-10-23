"""Independent comparisons to original half-cell and BPX source observations."""

import csv
import hashlib
import json

import numpy as np
from scipy.io import loadmat

from ebp import Catalog


def pointer(document, path):
    for key in path.split("/"):
        document = document[key]
    return document


def test_hnei_every_native_row_matches_original_half_cell_and_units():
    c = Catalog()
    curves = c.search(cell_id="panasonic-ncr18650b-hnei2016")
    assert len(curves) == 4
    assert sorted(r.record["representation"]["point_count"] for r in curves) == [2651, 2692, 2929, 3582]
    for curve in curves:
        r = curve.record
        asset = c.assets[r["provenance"]["asset_ids"][0]]
        path = c.root/asset["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
        p = r["provenance"]["processing"]
        d = loadmat(path, simplify_cells=True)
        original = d[p["field"]][p["cell_array_row_zero_based"], 0]
        with (c.root/r["representation"]["path"]).open() as f:
            rows = list(csv.DictReader(f))
        assert [int(row["source_mat_row"]) for row in rows] == list(range(1, len(original)+1))
        for column, source_col in [("potential_V", 1), ("source_capacity_Ah", 0), ("source_time_s", 2), ("source_current_A", 3)]:
            np.testing.assert_array_equal([float(row[column]) for row in rows], original[:, source_col])
        q, v, t, current = original.T
        np.testing.assert_allclose(np.sum(np.diff(t)*(current[:-1]+current[1:])/7200), q[-1], rtol=1e-10)
        x, voltage = curve.points()
        np.testing.assert_array_equal(x, (q-q[0])/(q[-1]-q[0]))
        assert r["reference"] == "Li/Li+" and r["license"] == "CC0-1.0"
        assert r["measurement"] == "pseudo_ocp" and r["temperature"]["value_K"] is None
        assert p["source_rate_denominator"] == (39 if r["electrode_role"] == "positive" else 40)
    assert not c.search_parameters(cell_id="panasonic-ncr18650b-hnei2016")
    assert not c.linked_tests("panasonic-ncr18650b-hnei2016")


def test_nextbms_native_rows_preserve_specific_capacity_and_duplicate_policy():
    c = Catalog()
    curves = c.search(cell_id="calb-gen3b-nextbms2026")
    assert len(curves) == 4
    for curve in curves:
        r = curve.record
        asset = c.assets[r["provenance"]["asset_ids"][0]]
        with (c.root/asset["path"]).open() as f:
            original = list(csv.DictReader(f))
        with (c.root/r["representation"]["path"]).open() as f:
            retained = list(csv.DictReader(f))
        assert int(retained[0]["source_csv_row"]) == 18
        assert len(original)-len(retained) == 16
        for row in retained:
            source = original[int(row["source_csv_row"])-2]
            assert float(row["potential_V"]) == float(source["Voltage(V)"])
            assert float(row["source_specific_capacity_mAh_g"]) == float(source["Capacity(mAh/g)"])
        assert r["direction"] == "unspecified" and r["reference"] == "Li/Li+"
        assert r["x"]["kind"] == "normalized_branch_capacity"
    assert not c.search_parameters(cell_id="calb-gen3b-nextbms2026")


def test_p45b_fitted_nodes_obey_particle_bounds_and_keep_component_origin():
    c = Catalog()
    source = json.loads((c.root/c.assets["aepy-p45b-bpx"]["path"]).read_text())
    curves = c.search(cell_id="molicel-p45b-aboutenergy2026")
    assert len(curves) == 5
    assert sorted(r.record["representation"]["point_count"] for r in curves) == [509, 883, 942, 1140, 1573]
    for curve in curves:
        r = curve.record
        p = r["provenance"]["processing"]
        table = pointer(source, p["source_pointer"])
        particle = pointer(source, p["source_pointer"].rsplit("/", 1)[0])
        with (c.root/r["representation"]["path"]).open() as f:
            rows = list(csv.DictReader(f))
        indices = [int(row["source_bpx_index"]) for row in rows]
        assert indices == [i for i, x in enumerate(table["x"]) if particle["Minimum stoichiometry"] <= x <= particle["Maximum stoichiometry"]]
        x, y = curve.points()
        np.testing.assert_array_equal(x, [table["x"][i] for i in indices])
        np.testing.assert_array_equal(y, [table["y"][i] for i in indices])
        assert r["measurement"] == "literature_table" and r["license"] == "BSD-3-Clause"
        assert min(y) > 0 and max(y) < 5
    assert len(c.search(cell_id="molicel-p45b-aboutenergy2026", material="silicon")) == 3


def test_p45b_parameters_preserve_bpx_values_and_do_not_import_placeholders():
    c = Catalog()
    source = json.loads((c.root/c.assets["aepy-p45b-bpx"]["path"]).read_text())
    params = [p for p in c.search_parameters(cell_id="molicel-p45b-aboutenergy2026") if not p.id.startswith("aepy-p45b-user-")]
    assert len(params) == 60
    assert len([p for p in params if p.record["category"] == "diffusion"]) == 6
    assert len([p for p in params if p.record["category"] == "kinetics"]) == 6
    for p in params:
        r = p.record
        path = r["provenance"]["location"]
        assert not path.startswith(("Parameterisation/Electrolyte/", "Parameterisation/User-defined/"))
        original = pointer(source, path)
        if r["representation"]["kind"] == "scalar":
            assert p.value == original
        else:
            x, y = p.points()
            np.testing.assert_array_equal(x, original["x"])
            np.testing.assert_array_equal(y, original["y"])
        if "Reaction rate constant [" in path:
            assert r["unit"] == "mol.m-2.s-1"
    assert len(c.full_cell_tests) == 51
