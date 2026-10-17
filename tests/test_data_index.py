"""GitHub navigation must reach complete source files and preserve variants."""

import csv
import io
import json
from pathlib import Path
import re

import numpy as np
import pytest

from ebp import Catalog
from scripts.build_data_index import REPO, render_index


@pytest.fixture(scope="module")
def index():
    return render_index()


def test_navigation_links_reach_all_curves_and_tests(index):
    catalog = Catalog()
    markdown = {name: value.decode() for name, value in index.items()
                if name.endswith(".md")}
    for page, content in markdown.items():
        for target in re.findall(r"\]\(([^)]+)\)", content):
            target = target.strip("<>").split("#")[0]
            if not target or target.startswith(("https:", "http:", "mailto:")):
                continue
            absolute = (REPO / page).parent / target
            relative = absolute.resolve().relative_to(REPO).as_posix()
            assert relative in index or absolute.exists(), (page, target)
    material_index = markdown["data/ocp/README.md"]
    for curve in catalog.search():
        assert f"`{curve.id}`" in material_index
        assert f"data/ocp/{curve.id}.json" in index
        if curve.record["representation"]["kind"] == "table":
            assert curve.record["representation"]["path"] in material_index
            assert f"data/ocp/{curve.id}.csv" not in index
    for test in catalog.full_cell_tests:
        page = markdown[f"data/cells/{test['cell_id']}.md"]
        assert test["normalized_path"] in page
        assert test["id"] in page
        assert test["normalized_path"].startswith("full_cell/")
        assert not any(name.endswith(Path(test["normalized_path"]).name)
                       for name in index)
    assert "0 / 0 / 3561 / 3561" in markdown["data/cells/mohtat2020-nmc532-pouch.md"]


def test_parameter_exports_keep_source_values_and_separate_alternatives(index):
    catalog = Catalog()
    exported = []
    for cid in catalog.cells:
        parameters = [p for p in catalog.parameters if p["cell_id"] == cid]
        package = json.loads(index[f"data/parameters/{cid}.json"])
        assert package["parameters"] == parameters
        assert package["cell_id"] == cid
        assert {r["id"] for r in package["ocp_records"]} == {r.id for r in catalog.search(cell_id=cid)}
        assert {t["id"] for t in package["full_cell_tests"]} == {t["id"] for t in catalog.linked_tests(cid)}
        if not parameters:
            assert f"data/parameters/{cid}.csv" not in index
            continue
        rows = list(csv.DictReader(io.StringIO(index[f"data/parameters/{cid}.csv"].decode())))
        assert [r["id"] for r in rows] == [p["id"] for p in parameters]
        package = json.loads(index[f"data/parameters/{cid}.json"])
        assert package["parameters"] == parameters
        assert not package["independent_full_cell_validation"]
        for row, parameter in zip(rows, parameters):
            assert row["unit"] == parameter["unit"]
            assert json.loads(row["conditions_json"]) == parameter.get("conditions", {})
            assert row["origin_status"] == parameter["provenance"]["origin_status"]
        exported.extend(r["id"] for r in rows)
    assert set(exported) == {p["id"] for p in catalog.parameters}
    cid = "mohtat2020-nmc532-pouch"
    for variant in ["original_author_mpm", "pybamm_v25_4_2"]:
        rows = list(csv.DictReader(io.StringIO(index[f"data/parameters/{cid}--{variant}.csv"].decode())))
        assert {r["parameterization_variant"] for r in rows} == {variant}
        assert {r["id"] for r in rows} == {
            p["id"] for p in catalog.parameters
            if p["cell_id"] == cid and p.get("conditions", {}).get("parameterization_variant") == variant
        }


def test_formula_csvs_are_marked_as_calculated_and_match_metadata(index):
    catalog = Catalog()
    for curve in catalog.search(representation="expression"):
        metadata = json.loads(index[f"data/ocp/{curve.id}.json"])
        assert metadata["record"]["representation"]["kind"] == "expression"
        assert metadata["export"]["kind"] == "generated_formula_samples"
        points = np.genfromtxt(io.BytesIO(index[f"data/ocp/{curve.id}-sampled.csv"]),
                               delimiter=",", names=True)
        assert len(points) == metadata["export"]["sample_count"] == 2001
        np.testing.assert_allclose(points["potential_V"], curve(points["x"]),
                                   rtol=2e-9, atol=2e-9)
