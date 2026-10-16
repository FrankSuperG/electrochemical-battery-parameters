import json

from ebp import Catalog
from ebp.site import build_site


def test_viewer_downloads_and_embedded_data_are_consistent(tmp_path):
    catalog = Catalog()
    build_site(catalog, tmp_path)
    script = (tmp_path / "catalog.js").read_text()
    data = json.loads(script.removeprefix("window.EBP_DATA = ").removesuffix(";\n"))
    assert len(data["records"]) == 10
    assert len(data["parameters"]) == 38
    assert len(data["full_cell_tests"]) == 3
    for record in data["records"]:
        downloaded = json.loads((tmp_path / "downloads" / f"{record['id']}.json").read_text())
        assert downloaded["record"]["id"] == record["id"]
        assert (tmp_path / "downloads" / f"{record['id']}.csv").exists()
    for test in data["full_cell_tests"]:
        assert len(test["preview_segments"]) == 4
        assert {s["C_rate"] for s in test["preview_segments"]} == {0.1, 0.5, 1.0, 1.5}
        assert (tmp_path / "downloads" / test["path"].split("/")[-1]).read_bytes() == (
            catalog.root / test["path"]
        ).read_bytes()
    for filename in ["index.html", "app.js", "style.css"]:
        assert "cdn." not in (tmp_path / filename).read_text()
    assert (tmp_path / "licenses/PyBaMM-BSD-3-Clause.txt").exists()
    assert (tmp_path / "licenses/CC-BY-4.0.txt").exists()
