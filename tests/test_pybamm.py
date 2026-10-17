import numpy as np
import pytest

pybamm = pytest.importorskip("pybamm")
from ebp import Catalog, StoichiometryMapping


@pytest.mark.parametrize(
    "rid",
    [
        "lfp-afshar2017-formula",
        "graphite-chen2020-formula",
        "bpx-lfp18650-lfp-ocp",
        "bpx-lfp18650-graphite-ocp",
        "nmc811-lgm50-chen2020-formula",
        "mohtat2020-nmc532-ocp",
        "marquis2019-lco-ocp",
        "nca-kim2011-nca-ocp",
    ],
)
def test_actual_pybamm_component_with_off_grid_stoichiometry(rid):
    curve = Catalog().get(rid)
    ocp = curve.to_pybamm(count=50001)
    parameter = pybamm.InputParameter("sto")
    symbolic = ocp(parameter)
    lo, hi = curve.record["x"]["domain"]
    x = lo + (hi - lo) * np.array([0.01503, 0.10607, 0.49993, 0.90003, 0.98607])
    actual = np.array(
        [
            float(np.asarray(symbolic.evaluate(inputs={"sto": float(value)})).item())
            for value in x
        ]
    )
    np.testing.assert_allclose(actual, curve(x), atol=1e-5, rtol=0)
    assert not ocp.ebp_metadata["independently_validated"]


def test_reverse_direction_mapping_retains_voltage_order():
    curve = Catalog().get("sintef-lfp-d07eb6-c3-delithiation")
    mapping = StoichiometryMapping(
        0.9, 0.1, "Synthetic test mapping, not a scientific balancing result"
    )
    function = curve.to_pybamm(mapping=mapping)
    symbol = function(pybamm.InputParameter("sto"))
    actual = float(np.asarray(symbol.evaluate(inputs={"sto": 0.5})).item())
    assert actual == pytest.approx(curve(0.5), abs=1e-12)
    assert function.ebp_metadata["mapping"]["evidence"] == mapping.evidence


@pytest.mark.parametrize("material", ["lfp", "graphite"])
def test_model_ocpn_explicit_mapping_keeps_model_label_and_native_values(material):
    curve = Catalog().get(f"jahn-a123-{material}-model-ocpn")
    mapping = StoichiometryMapping(.1, .9, "Hypothetical test-only mapping; not a scientific balancing result")
    function = curve.to_pybamm(mapping=mapping)
    symbol = function(pybamm.InputParameter("sto"))
    source_x = .4137
    actual = float(np.asarray(symbol.evaluate(inputs={"sto": .1+.8*source_x})).item())
    assert actual == pytest.approx(curve(source_x),abs=1e-12)
    assert function.ebp_metadata["measurement"] == "model_ocp"
    assert function.ebp_metadata["coordinate_kind"] == "model_soc"
    assert not function.ebp_metadata["independently_validated"]
