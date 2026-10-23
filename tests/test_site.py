import json
import re

from ebp import Catalog
from ebp.site import build_site


def test_viewer_downloads_are_cell_scoped_and_source_faithful(tmp_path):
    c = Catalog()
    build_site(c, tmp_path)
    script = (tmp_path / "catalog.js").read_text()
    data = json.loads(script.removeprefix("window.EBP_DATA = ").removesuffix(";\n"))
    assert len(data["records"]) == 90
    assert len(data["parameters"]) == 1041
    assert len(data["full_cell_tests"]) == 61
    assert data["external_datasets"] == c.external_datasets
    assert data["cell_material_families"] == {cid: c.cell_material_family(cid) for cid in c.cells}
    assert json.loads((tmp_path / "downloads/external-datasets.json").read_text()) == c.external_document
    for record in data["records"]:
        license_url = record["license_url"]
        if license_url.startswith("licenses/"):
            assert (tmp_path/license_url).is_file()
        else:
            assert license_url == "https://creativecommons.org/publicdomain/zero/1.0/"
        if "tum-rehm2026-v2" in record["source_ids"] and record["license"] == "MIT":
            assert "Copyright (c) 2025 Mathias Rehm" in (tmp_path/license_url).read_text()
        if "aepy-p45b-2026" in record["source_ids"]:
            assert "About:Energy" in (tmp_path/license_url).read_text()
        downloaded = json.loads(
            (tmp_path / "downloads" / f"{record['id']}.json").read_text()
        )
        assert downloaded["record"]["id"] == record["id"]
        assert (tmp_path / "downloads" / f"{record['id']}.csv").exists()
    for cid in c.cells:
        package = json.loads(
            (tmp_path / "downloads" / f"{cid}-parameters.json").read_text()
        )
        assert package["cell_id"] == cid
        assert all(p["cell_id"] == cid for p in package["parameters"])
        assert all(t["cell_id"] == cid for t in package["full_cell_tests"])
        assert all(r["cell_link"]["cell_id"] == cid for r in package["ocp_records"])
        assert not package["independent_full_cell_validation"]
        assert package["external_datasets"] == c.search_datasets(cell_id=cid)
    for test in data["full_cell_tests"]:
        for relative in filter(
            None,
            [test.get("original_download_path")]
            + [
                path
                for side in test.get("sidecars", [])
                for path in [side["path"], side["original_download_path"]]
            ],
        ):
            assert (tmp_path / "downloads" / relative.split("/")[-1]).read_bytes() == (
                c.root / relative
            ).read_bytes()
        assert len(test["preview_segments"]) == (
            4 if test["cell_id"] == "lg-m50" else 1
        )
        for key in ("path", "normalized_path"):
            if test[key]:
                assert (
                    tmp_path / "downloads" / test[key].split("/")[-1]
                ).read_bytes() == (c.root / test[key]).read_bytes()
        if test["id"] == "a123-9ah-2c-ch":
            points = test["preview_segments"][0]["points"]
            assert points[-1][1] > points[0][1]
    for filename in ["index.html", "app.js", "style.css"]:
        source = (tmp_path / filename).read_text()
        assert "cdn." not in source
        assert not re.search(r"[\u4e00-\u9fff]", source)
    for source in data["sources"].values():
        assert isinstance(source["authors"], list)
    assert '<html lang="en">' in (tmp_path / "index.html").read_text()
    assert (
        json.loads((tmp_path / "downloads/matching-audit.json").read_text())
        == c.matching_audit
    )
    for name in [
        "PyBaMM-BSD-3-Clause.txt",
        "CC-BY-4.0.txt",
        "BPX-MIT.txt",
        "PyBaMM-data-BSD-3-Clause.txt",
        "Oxford-BSD-2-Clause.txt",
    ]:
        assert (tmp_path / "licenses" / name).exists()
    assert (tmp_path / "logo.png").read_bytes() == (
        c.root.parent / "web/logo.png"
    ).read_bytes()
