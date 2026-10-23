"""External links preserve dataset grain, licensing gaps and conservative joins."""

import copy
import json
import socket

import pytest

from ebp import Catalog
from ebp.cli import main


def test_external_search_is_offline_and_parameter_scoped(monkeypatch):
    def reject_network(*args, **kwargs):
        raise AssertionError("External registry search must not download observations")

    monkeypatch.setattr(socket, "create_connection", reject_network)
    catalog = Catalog()
    assert not catalog.search_datasets(material="nmc", test_type="dynamic", profile="us06")
    assert not catalog.search_datasets(cell_id="kim2011-nca-nominal-design")
    assert [r["id"] for r in catalog.search_datasets(cell_id="lg-m50")] == ["tec-lgm50-multitemperature-2021"]
    linked = catalog.search_datasets(cell_id="lg-m50lt-hallemans2025", test_type="eis")
    assert [r["id"] for r in linked] == ["hallemans-m50lt-eis-2025"]
    assert linked[0]["parameter_link"]["match_level"] == "same_model_same_study"
    assert catalog.cell_material_family("kokam-slpb75106100-ecker2015") == "NCO"
    assert len(catalog.full_cell_tests) == 51
    with pytest.raises(KeyError):
        catalog.full_cell_data(linked[0]["id"])


def test_external_cli_filters_combine_and_keep_parameter_associations(capsys):
    assert main(["datasets", "--material", "NCA", "--profile", "US06", "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == []
    assert main(["datasets", "--material", "LFP", "--test-type", "cccv", "--json"]) == 0
    records = json.loads(capsys.readouterr().out)
    assert [r["id"] for r in records] == ["haidi-lfp-rehm2025"]
    assert records[0]["parameter_components"]["ocp"]["record_ids"]


def test_file_search_does_not_inherit_uninspected_dataset_profile_claims(capsys):
    catalog = Catalog()
    assert catalog.search_datasets(cell_id="lg-mj1-dlr-sintef", test_type="dynamic")
    assert not catalog.search_dataset_files(cell_id="lg-mj1-dlr-sintef", test_type="dynamic")
    assert main(["datasets", "--files", "--material", "NMC", "--profile", "US06", "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == []


def test_historical_directory_evidence_does_not_reenter_active_parameter_catalog():
    catalog = Catalog()
    evidence = catalog._load("evidence/external-archive-directory-review.json")
    rar = next(r for r in evidence["checks"] if r["source_url"].endswith("41673360"))
    eis = [f for f in rar["files"] if "/EIS measurements/" in f["path"] and f["path"].endswith(".csv")]
    assert len(eis) == 440
    assert len({f["path"].split("/")[1] for f in eis}) == 11
    assert rar["complete"] and rar["bytes_transferred"] < rar["archive_size_bytes"]
    assert not catalog.search_datasets("milano-lfp-eis-2023")


def test_ncr18650b_sources_keep_parameter_and_half_cell_matching_limits():
    catalog = Catalog()
    ids = {"hnei-ncr18650b-2016", "bayreuth-ncr18650b-2023",
           "virtual-vehicle-ncr18650b-aging-2023", "stanford-ncr18650b-rates-2021"}
    records = [r for r in catalog.external_datasets if r["id"] in ids]
    assert len(records) == 4
    assert all(r["material_families"] == ["NCA"] for r in records)
    assert all(r["parameter_link"]["cell_ids"] == ["panasonic-ncr18650b-hnei2016"] for r in records)
    assert all(len(r["parameter_components"]["ocp"]["record_ids"]) == 4 for r in records)
    assert all(not r["parameter_components"][key]["record_ids"] for r in records for key in ["diffusion", "kinetics"])
    hnei = next(r for r in records if r["id"] == "hnei-ncr18650b-2016")
    half = [f for f in hnei["file_links"] if "/Half cell/" in f["source_path"]]
    assert {f["source_sample_id"] for f in half} == {"NE", "PE"}
    assert all(f["verification"] == "archive_directory" and f["content_review"] == "existing_source_audit" for f in half)
    assert hnei["license"]["identifier"] == "CC0-1.0"
    assert hnei["aging_data"]["status"] == "not_reported"
    bayreuth = next(r for r in records if r["id"] == "bayreuth-ncr18650b-2023")
    assert bayreuth["license"]["identifier"] == "not-stated"
    assert len(bayreuth["file_links"]) == 13
    assert "ocv" in bayreuth["test_types"]
    assert bayreuth["parameter_components"]["ocp"]["match_level"] == "same_model_different_study"
    assert bayreuth["ocp_anchor"]["kind"] == "cross_study_catalog_half_cell"


def test_ncr18650b_discharge_rates_do_not_inherit_other_chemistries():
    catalog = Catalog()
    rows = [f for f in catalog.search_dataset_files(material="NCA", test_type="constant_current")
            if f["dataset_id"] == "stanford-ncr18650b-rates-2021"]
    assert len(rows) == 15
    assert {(f["temperature_C"], f["nominal_rate_C"]) for f in rows} == {
        (t, c) for t in [5, 25, 35] for c in [0.05, 1, 2, 3, 5]
    }
    assert all(f["source_sample_id"] == "k1" and "/NCA/" in f["source_path"] for f in rows)
    assert not any(f["nominal_rate_C"] > 5 or f["profiles"] for f in rows)


def test_aging_filters_keep_source_scope_and_documentation_separate(capsys):
    catalog = Catalog()
    available = catalog.search_datasets("NCR18650B", material="NCA", aging_status="available")
    assert [r["id"] for r in available] == ["virtual-vehicle-ncr18650b-aging-2023"]
    record = available[0]
    h5 = [f for f in record["file_links"] if f["source_path"].endswith(".h5")]
    assert len(h5) == 116
    assert all(f["kind"] == "file" and f["content_review"] == "not_read" for f in h5)
    assert set(record["aging_data"]["file_paths"]) <= {f["source_path"] for f in h5}
    docs = [f for f in record["file_links"] if f["kind"] == "documentation"]
    assert len(docs) == 1 and docs[0]["content_review"] == "documentation_reviewed"
    assert not docs[0]["test_types"] and not docs[0]["profiles"]
    assert not catalog.search_dataset_files("NCR18650B", aging_status="available", test_type="eis")
    assert catalog.search_datasets("NCR18650B", aging_status="available", test_type="dynamic")
    assert not catalog.search_dataset_files("NCR18650B", aging_status="available", test_type="dynamic")
    assert main(["datasets", "NCR18650B", "--material", "NCA", "--aging-status", "available", "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == available
    assert main(["datasets", "NCR18650B", "--files", "--aging-status", "available", "--test-type", "constant_current", "--json"]) == 0
    rows = json.loads(capsys.readouterr().out)
    assert len(rows) == 116
    assert all(f["dataset_aging_status"] == "available" for f in rows)
    unverified = catalog.search_datasets(aging_status="unverified")
    assert not unverified


def test_ocp_first_sources_keep_half_cell_and_temperature_scope():
    catalog = Catalog()
    nextbms = next(r for r in catalog.external_datasets if r["id"] == "nextbms-calb-nmc532-2026")
    assert nextbms["ocp_anchor"]["kind"] == "catalog_half_cell"
    assert len(nextbms["ocp_anchor"]["source_paths"]) == 6
    assert all("2_HalfCell/" in p and "OCPDis_" not in p for p in nextbms["ocp_anchor"]["source_paths"])
    assert not nextbms["ocp_anchor"]["half_cell_temperatures_C"]
    assert nextbms["temperatures_C"] == [0, 5, 25, 45]
    assert nextbms["parameter_link"]["cell_ids"] == ["calb-gen3b-nextbms2026"]
    assert len(nextbms["parameter_components"]["ocp"]["record_ids"]) == 4
    spectra = [f for f in nextbms["file_links"] if "3_Characterization/" in f["source_path"] and f["test_types"] == ["eis"]]
    assert len(spectra) == 12
    assert {f["temperature_C"] for f in spectra} == {0, 5, 25, 45}
    assert any("25/16/20" in gap for gap in nextbms["missing_items"])


def test_p45b_measured_fitted_and_reconstructed_curves_stay_distinct():
    catalog = Catalog()
    ae = next(r for r in catalog.external_datasets if r["id"] == "aboutenergy-p45b-2026")
    assert ae["ocp_anchor"]["kind"] == "published_parameterisation"
    assert len(ae["parameter_components"]["ocp"]["record_ids"]) == 5
    assert ae["parameter_components"]["kinetics"]["quantity_kind"] == "kinetic_coefficient"
    assert {f["temperature_C"] for f in ae["file_links"] if "WLTP" in f["profiles"]} == {10, 25, 40, 60}
    assert {f["temperature_C"] for f in ae["file_links"] if "eVTOL" in f["profiles"]} == {25, 40, 60}
    assert "E_OCV_V" in ae["channels"]["note"]
    tum = next(r for r in catalog.external_datasets if r["id"] == "tum-p45b-halfcell-aging-2026")
    assert len(tum["ocp_anchor"]["source_paths"]) == 5
    assert all("SiReconstr_" not in p for p in tum["ocp_anchor"]["source_paths"])
    assert len([f for f in tum["file_links"] if "SiReconstr_" in f["source_path"]]) == 2
    half = [f for f in tum["file_links"] if f["source_path"] in tum["ocp_anchor"]["source_paths"]]
    assert {f["nominal_rate_C"] for f in half} == {0.02, 0.03}
    assert all(f["temperature_C"] is None for f in half)
    assert tum["license"]["identifier"] == "MIT"


def test_cross_study_ocp_references_do_not_become_same_study_parameter_sets():
    catalog = Catalog()
    tec = catalog.search_datasets(cell_id="lg-m50")[0]
    assert tec["ocp_anchor"]["kind"] == "reused_catalog_expression"
    assert tec["parameter_components"]["ocp"]["record_ids"] == ["graphite-chen2020-formula", "nmc811-lgm50-chen2020-formula"]
    rows = [f for f in tec["file_links"] if f["test_types"] == ["constant_current"]]
    assert len(rows) == 48
    assert {f["temperature_C"] for f in rows} == {0, 10, 25}
    assert {f["nominal_rate_C"] for f in rows} == {0.1, 0.5, 1, 2}
    assert not tec["profiles"]
    mj1 = catalog.search_datasets(cell_id="lg-mj1-dlr-sintef")[0]
    assert mj1["parameter_link"]["match_level"] == "same_model_different_study"
    assert len(mj1["parameter_components"]["ocp"]["record_ids"]) == 4
    assert mj1["parameter_components"]["diffusion"]["match_level"] == "missing"
    assert mj1["parameter_components"]["kinetics"]["match_level"] == "missing"
    assert len(mj1["file_links"]) == 1 and mj1["file_links"][0]["kind"] == "archive"
    assert not mj1["profiles"]


@pytest.mark.parametrize("fault", ["unknown_path", "empty_catalog_records"])
def test_ocp_anchor_requires_inspectable_sources(fault):
    catalog = Catalog()
    tec = catalog.search_datasets(cell_id="lg-m50")[0]
    if fault == "unknown_path":
        tec["ocp_anchor"]["source_paths"] = ["invented-half-cell.csv"]
        expected = "OCP anchor references an unknown external source path"
    else:
        tec["parameter_components"]["ocp"]["record_ids"] = []
        expected = "catalog OCP anchor requires explicit curve records"
    assert any(expected in error for error in catalog.validate())


@pytest.mark.parametrize("fault", ["orphan_path", "unsupported_availability", "boolean_status"])
def test_aging_availability_requires_concrete_evidence(fault):
    catalog = Catalog()
    record = next(r for r in catalog.external_datasets if r["aging_data"]["status"] == "available")
    if fault == "orphan_path":
        record["aging_data"]["file_paths"] = ["invented-history.h5"]
        expected = "ageing evidence references an unknown external source path"
    else:
        if fault == "unsupported_availability":
            record["aging_data"]["file_paths"] = []
        else:
            record["aging_data"]["status"] = False
        expected = "external datasets schema"
    assert any(expected in error for error in catalog.validate())


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
        r = next(r for r in catalog.external_datasets if r["id"] == "hnei-ncr18650b-2016")
        member = next(item for item in r["file_links"] if item["kind"] == "archive_member")
        member["size_bytes"] += 1
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
        record["parameter_link"]["match_level"] = "unmatched"
        expected = "requires explicit cell links"
    elif fault == "unknown_cell":
        record["parameter_link"]["match_level"] = "same_model_same_study"
        record["parameter_link"]["cell_ids"] = ["unknown-model"]
        expected = "unknown external-dataset cell"
    elif fault == "wrong_material":
        record["parameter_link"]["match_level"] = "same_model_same_study"
        record["parameter_link"]["cell_ids"] = ["a123-amp20m1hd-a"]
        expected = "material family disagrees"
    elif fault == "local_payload":
        record["storage"] = "local_csv"
        expected = "external datasets schema"
    else:
        record["review"]["checked_on"] = "2026-99-99"
        expected = "external datasets schema"
    assert any(expected in error for error in catalog.validate())
