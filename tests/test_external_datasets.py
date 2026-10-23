"""External links preserve dataset grain, licensing gaps and conservative joins."""

import copy
import json
import socket

import pytest

from ebp import Catalog
from ebp.cli import main


def test_external_search_is_offline_and_does_not_invent_parameter_matches(monkeypatch):
    def reject_network(*args, **kwargs):
        raise AssertionError("External registry search must not download observations")

    monkeypatch.setattr(socket, "create_connection", reject_network)
    catalog = Catalog()
    us06 = catalog.search_datasets(material="nmc", test_type="dynamic", profile="us06")
    assert {r["id"] for r in us06} == {
        "calb-l148n58a-2025", "calce-samsung-20r-dynamic", "malaya-three-chemistries-2022"
    }
    assert not catalog.search_datasets(profile="US06-extra")
    assert not catalog.search_datasets(cell_id="kim2011-nca-nominal-design")
    assert not catalog.search_datasets(cell_id="lg-m50")
    linked = catalog.search_datasets(cell_id="lg-m50lt-hallemans2025", test_type="eis")
    assert [r["id"] for r in linked] == ["hallemans-m50lt-eis-2025"]
    assert linked[0]["parameter_link"]["match_level"] == "same_model_same_study"
    assert catalog.cell_material_family("kokam-slpb75106100-ecker2015") == "NCO"
    assert len(catalog.full_cell_tests) == 61
    with pytest.raises(KeyError):
        catalog.full_cell_data(us06[0]["id"])


def test_external_cli_filters_combine_and_keep_dataset_grain(capsys):
    assert main(["datasets", "--material", "NCA", "--profile", "US06", "--json"]) == 0
    records = json.loads(capsys.readouterr().out)
    assert len(records) == 1
    assert records[0]["material_families"] == ["LFP", "NMC", "NCA"]
    assert records[0]["parameter_link"]["cell_ids"] == []
    assert main(["datasets", "--material", "LFP", "--test-type", "cccv", "--json"]) == 0
    records = json.loads(capsys.readouterr().out)
    assert [r["id"] for r in records] == ["uccs-a123-26650m1b-2021"]


@pytest.mark.parametrize("fault", ["duplicate", "missing_join", "unknown_cell", "wrong_material", "local_payload", "bad_date"])
def test_integrity_check_rejects_misleading_external_metadata(fault):
    catalog = Catalog()
    record = catalog.external_datasets[0]
    if fault == "duplicate":
        catalog.external_datasets.append(copy.deepcopy(record))
        expected = "Duplicate external dataset IDs"
    elif fault == "missing_join":
        record["parameter_link"]["match_level"] = "same_model_same_study"
        expected = "requires explicit cell links"
    elif fault == "unknown_cell":
        record["parameter_link"]["match_level"] = "same_model_same_study"
        record["parameter_link"]["cell_ids"] = ["unknown-model"]
        expected = "unknown external-dataset cell"
    elif fault == "wrong_material":
        record["parameter_link"]["match_level"] = "same_model_same_study"
        record["parameter_link"]["cell_ids"] = ["lg-m50"]
        expected = "material family disagrees"
    elif fault == "local_payload":
        record["storage"] = "local_csv"
        expected = "external datasets schema"
    else:
        record["review"]["checked_on"] = "2026-99-99"
        expected = "external datasets schema"
    assert any(expected in error for error in catalog.validate())
