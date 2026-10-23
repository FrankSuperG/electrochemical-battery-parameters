"""Active packages require actual electrochemical parameter records."""

import copy

import pytest

from ebp import Catalog


def test_active_cells_and_supporting_links_have_electrochemical_parameters():
    c = Catalog()
    for cid in c.cells:
        assert c.search(cell_id=cid) or any(
            p.record["category"] in {"diffusion", "kinetics"}
            for p in c.search_parameters(cell_id=cid)
        ), cid
    for source in c.external_datasets:
        assert any(source["parameter_components"][k]["record_ids"]
                   for k in ("ocp", "diffusion", "kinetics")), source["id"]
    # Incomplete parameter packages remain useful; three empty components do not.
    assert not c.search(cell_id="lg-m50lt-hallemans2025")
    assert c.search_parameters(cell_id="lg-m50lt-hallemans2025", category="diffusion")
    assert c.search(cell_id="panasonic-ncr18650b-hnei2016")
    removed = {"uccs-a123-26650m1b-2021", "calce-a123-dynamic",
               "calce-samsung-20r-dynamic", "calb-l148n58a-2025",
               "milano-lfp-eis-2023", "malaya-three-chemistries-2022"}
    assert not removed.intersection(r["id"] for r in c.external_datasets)
    assert "a123-high-power-pouch-9ah" not in c.cells
    assert not list((c.root / "full_cell").glob("a123-9ah-*"))


@pytest.mark.parametrize("kind", ["cell", "external"])
def test_validation_rejects_full_cell_only_entries_even_with_coverage_prose(kind):
    c = Catalog()
    if kind == "cell":
        c.cells["unsupported-cell"] = copy.deepcopy(c.cells["a123-amp20m1hd-a"])
        expected = "active cell requires stored OCP, diffusion or kinetics records"
    else:
        source = c.external_datasets[0]
        for component in source["parameter_components"].values():
            component["record_ids"] = []
            component["match_level"] = "missing"
        expected = "active dataset requires stored OCP, diffusion or kinetics records"
    assert any(expected in error for error in c.validate())
