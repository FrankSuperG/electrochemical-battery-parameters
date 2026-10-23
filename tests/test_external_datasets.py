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


def test_file_search_does_not_inherit_uninspected_dataset_profile_claims(capsys):
    catalog = Catalog()
    assert catalog.search_datasets(material="NCA", profile="US06")
    assert not catalog.search_dataset_files(material="NCA", profile="US06")
    assert main(["datasets", "--files", "--material", "NMC", "--profile", "US06", "--json"]) == 0
    rows = json.loads(capsys.readouterr().out)
    assert {r["dataset_id"] for r in rows} == {"calce-samsung-20r-dynamic", "calb-l148n58a-2025"}
    assert len(rows) == 6
    assert all(r["content_review"] == "not_read" for r in rows)


def test_charge_rates_and_combined_us06_workbooks_keep_source_labels():
    catalog = Catalog()
    files = catalog.search_dataset_files(material="LFP", test_type="cccv")
    assert len(files) == 5
    assert {r["nominal_rate_C"] for r in files} == {1, 2, 3, 4}
    assert all(r["temperature_C"] == 25 and r["source_sample_id"] == "A002" for r in files)
    a123 = [r for r in catalog.search_dataset_files(material="LFP", profile="US06")
            if r["kind"] == "archive_member"]
    assert {r["source_sample_id"] for r in a123} == {"A1-007", "A1-008"}
    assert all("DST-US06-FUDS" in r["source_path"] for r in a123)
    assert all(r["parameter_match"] == "unmatched" for r in a123)


def test_archive_directory_counts_do_not_become_measurement_or_specimen_claims():
    catalog = Catalog()
    evidence = catalog._load("evidence/external-archive-directory-review.json")
    rar = next(r for r in evidence["checks"] if r["source_url"].endswith("41673360"))
    eis = [f for f in rar["files"] if "/EIS measurements/" in f["path"] and f["path"].endswith(".csv")]
    assert len(eis) == 440
    assert len({f["path"].split("/")[1] for f in eis}) == 11
    assert rar["complete"] and rar["bytes_transferred"] < rar["archive_size_bytes"]
    r = next(r for r in catalog.external_datasets if r["id"] == "milano-lfp-eis-2023")
    assert not r["parameter_link"]["cell_ids"]
    assert all(item["content_review"] == "not_read" for item in r["file_links"])


@pytest.mark.parametrize("fault", ["wrong_component", "intrinsic_group", "member_size", "duplicate_path"])
def test_file_and_component_associations_require_specific_evidence(fault):
    catalog = Catalog()
    matched = next(r for r in catalog.external_datasets if r["id"] == "hallemans-m50lt-eis-2025")
    if fault == "wrong_component":
        matched["parameter_components"]["kinetics"]["record_ids"] = ["hallemans2025-tau-d-p"]
        expected = "invalid kinetics component record"
    elif fault == "intrinsic_group":
        matched["parameter_components"]["diffusion"]["quantity_kind"] = "intrinsic_diffusivity"
        expected = "time scale cannot be intrinsic diffusivity"
    elif fault == "member_size":
        r = next(r for r in catalog.external_datasets if r["id"] == "milano-lfp-eis-2023")
        r["file_links"][1]["size_bytes"] += 1
        expected = "archive member lacks matching directory evidence"
    else:
        catalog.external_datasets[0]["file_links"].append(copy.deepcopy(catalog.external_datasets[0]["file_links"][0]))
        expected = "duplicate external source paths"
    assert any(expected in error for error in catalog.validate())


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
