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


def test_battery_model_index_covers_every_package_and_external_source(index):
    catalog = Catalog()
    root = index["README.md"].decode()
    overview = index["data/batteries/README.md"].decode()
    for cid in catalog.cells:
        assert f"data/batteries/{cid}.md" in index
        assert f"data/batteries/{cid}.md" in root
        for category in ["diffusion", "kinetics"]:
            params = [p for p in catalog.parameters if p["cell_id"] == cid and p["category"] == category]
            path = f"data/parameters/{cid}--{category}.csv"
            if params:
                rows = list(csv.DictReader(io.StringIO(index[path].decode())))
                assert {r["id"] for r in rows} == {p["id"] for p in params}
            else:
                assert path not in index
    hubs = {name: body.decode() for name, body in index.items() if name.startswith("data/batteries/") and name.endswith(".md") and not name.endswith("README.md")}
    for source in catalog.external_datasets:
        assert sum(f"{source['id']}.md#file-locations" in body for body in hubs.values()) == (2 if source["id"] in {"tec-lgm50-multitemperature-2021", "tum-p45b-halfcell-aging-2026"} else 1)
    ncr = hubs["data/batteries/panasonic-ncr18650b-hnei2016.md"]
    assert all(name in ncr for name in ["hnei-ncr18650b-2016", "bayreuth-ncr18650b-2023", "virtual-vehicle-ncr18650b-aging-2023", "stanford-ncr18650b-rates-2021"])
    assert "same_model_different_study" in ncr
    assert "kim2011" not in ncr
    assert "Not extracted" in ncr  # D and kinetics remain absent.
    p45b = hubs["data/batteries/molicel-p45b-aboutenergy2026.md"]
    assert "tum-p45b-halfcell-aging-2026" in p45b and "no native parameter join" in p45b
    assert "multi-T" in overview and "ageing" in overview and "EIS" in overview


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


def test_full_cell_material_index_preserves_grain_and_complete_file_links(index):
    catalog = Catalog()
    registry = json.loads(index["data/full-cell/datasets.json"])
    assert registry["records"] == catalog.external_datasets
    assert len(list(csv.DictReader(io.StringIO(index["data/full-cell/datasets.csv"].decode())))) == len(catalog.external_datasets)
    for test in catalog.full_cell_tests:
        family = catalog.cell_material_family(test["cell_id"])
        page = index[f"data/full-cell/{family}.md"].decode()
        assert test["normalized_path"] in page
        assert f"`{test['id']}`" in page
    assert not any(name.startswith("data/full-cell/") and name.endswith(".csv")
                   and name not in {"data/full-cell/datasets.csv", "data/full-cell/files.csv"} for name in index)
    files = list(csv.DictReader(io.StringIO(index["data/full-cell/files.csv"].decode())))
    assert len(files) == len(catalog.search_dataset_files())
    assert {(r["dataset_id"], r["source_path"]) for r in files} == {
        (r["dataset_id"], r["source_path"]) for r in catalog.search_dataset_files()
    }
    assert "No packaged full-cell file" in index["data/full-cell/NCA.md"].decode()
    for dataset in catalog.external_datasets:
        assert f"data/full-cell/{dataset['id']}.md" in index
        for family in dataset["material_families"]:
            assert dataset["id"] + ".md" in index[f"data/full-cell/{family}.md"].decode()


def test_aging_column_preserves_unreported_unknown_and_source_level_grain(index):
    rows = list(csv.DictReader(io.StringIO(index["data/full-cell/datasets.csv"].decode())))
    catalog = Catalog()
    assert {r["aging_data"] for r in rows} == {"available", "not_reported", "unverified"}
    for row, source in zip(rows, catalog.external_datasets):
        assert row["aging_data"] == source["aging_data"]["status"]
        assert row["aging_source_url"] == source["aging_data"]["source_url"]
    overview = index["data/full-cell/README.md"].decode()
    assert "| Dataset | Materials | OCP anchor | Ageing data | License |" in overview
    nca = index["data/full-cell/NCA.md"].decode()
    assert "Ageing data" in nca and "Yes (cycle, calendar)" in nca
    files = list(csv.DictReader(io.StringIO(index["data/full-cell/files.csv"].decode())))
    docs = [f for f in files if f["kind"] == "documentation"]
    assert docs and all(not f["test_types"] for f in docs)
    ageing_docs = [f for f in docs if f["dataset_id"] == "virtual-vehicle-ncr18650b-aging-2023"]
    assert len(ageing_docs) == 1 and ageing_docs[0]["dataset_aging_status"] == "available"
    for row, source in zip(rows, catalog.external_datasets):
        assert row["ocp_anchor"] == source["ocp_anchor"]["kind"]
        assert json.loads(row["half_cell_temperatures_C"]) == source["ocp_anchor"]["half_cell_temperatures_C"]
