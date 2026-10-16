"""Compare extracted observations with original deposited files, when cached."""

from pathlib import Path
import csv
import hashlib
import importlib.util

import numpy as np
import pytest

from ebp import Catalog

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache/upstream"


def test_fullcell_originals_and_explicit_current_convention():
    catalog = Catalog()
    for test in catalog.linked_tests("lg-m50"):
        original = catalog.full_cell_data(test["id"])
        with (catalog.root / test["normalized_path"]).open(newline="") as handle:
            normalized = list(csv.DictReader(handle))
        assert len(original) == len(normalized) == test["row_count"]
        for index, (raw, norm) in enumerate(zip(original, normalized)):
            assert float(norm["voltage_V"]) == float(raw["Voltage [V]"])
            assert float(norm["time_s"]) == float(raw["Test Time [s]"])
            assert (
                float(norm["cell_temperature_K"])
                == float(raw["Temperature Cell [degC]"]) + 273.15
            )
            expected_sign = 1 if raw["Md"] == "C" else -1 if raw["Md"] == "D" else 0
            assert float(norm["current_charge_positive_A"]) == expected_sign * float(
                raw["Current [A]"]
            )
            assert int(norm["source_file_row"]) == index + 14
        assert test["relationship_to_parameters"] == "same_model_same_study"
        assert test["independent_validation_by_this_project"] is False


def test_every_retained_ocp_voltage_matches_source_row():
    pd = pytest.importorskip("pandas")
    catalog = Catalog()
    for curve in catalog.search(representation="table"):
        asset = catalog.assets[curve.record["provenance"]["asset_ids"][0]]
        path = CACHE / asset["filename"]
        if not path.exists():
            pytest.skip(
                "Raw cache absent; run scripts/seed_v01.py --download for provenance audit"
            )
        assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
        original = pd.read_parquet(path)
        derived = pd.read_csv(curve._path(), float_precision="round_trip")
        source = original.iloc[derived["source_row"].to_numpy()]
        np.testing.assert_array_equal(
            derived["potential_V"].to_numpy(), source["Voltage / V"].to_numpy()
        )
        np.testing.assert_array_equal(
            derived["capacity_Ah"].to_numpy(),
            source["Cumulative Capacity / Ah"].to_numpy(),
        )
        assert (source["Cycle Count / 1"] == 3).all()
        assert (
            source["Step Index / 1"] == curve.record["provenance"]["processing"]["step"]
        ).all()


def test_formulas_and_kinetics_match_pinned_upstream():
    pytest.importorskip("pybamm")
    code = CACHE / "Prada2013-v25.4.2.py"
    chen = CACHE / "Chen2020-v25.4.2.py"
    if not code.exists() or not chen.exists():
        pytest.skip("Pinned upstream source cache is absent")
    catalog = Catalog()
    modules = []
    for path, asset_id in [(code, "pybamm-prada-code"), (chen, "pybamm-chen-code")]:
        assert (
            hashlib.sha256(path.read_bytes()).hexdigest()
            == catalog.assets[asset_id]["sha256"]
        )
        spec = importlib.util.spec_from_file_location("checked_upstream", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    x = np.linspace(0, 1, 1003)
    for curve in catalog.search(representation="expression", source="pybamm-25-4-2"):
        if "pybamm-prada-code" not in curve.record["provenance"]["asset_ids"]:
            continue
        expected = getattr(
            modules[0], curve.record["representation"]["source_function"]
        )(x)
        np.testing.assert_allclose(curve(x), expected, atol=2e-15, rtol=1e-14)
    for side, function in [
        ("negative", "graphite_LGM50_electrolyte_exchange_current_density_Chen2020"),
        ("positive", "nmc_LGM50_electrolyte_exchange_current_density_Chen2020"),
    ]:
        parameter = catalog.get_parameter(f"lgm50-{side}-exchange-current-density")
        for temperature in [283.15, 298.15, 313.15]:
            expected = float(
                getattr(modules[1], function)(
                    1000, 10000, 30000, temperature
                ).evaluate()
            )
            assert parameter(
                c_e=1000, c_s_surf=10000, c_s_max=30000, T=temperature
            ) == pytest.approx(expected, rel=1e-9)
    upstream_values = modules[1].get_parameter_values()
    for parameter in catalog.search_parameters(cell_id="lg-m50"):
        if parameter.record["representation"]["kind"] == "scalar":
            assert parameter.value == upstream_values[parameter.record["name"]]
