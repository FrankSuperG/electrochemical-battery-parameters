"""Material identity, source math and diffusivity interface verification."""

import hashlib
import importlib.util
from pathlib import Path

import numpy as np
import pytest

from ebp import Catalog

CACHE = Path(__file__).resolve().parents[1] / ".cache/upstream"


def test_material_families_specimens_and_cell_associations():
    c = Catalog()
    assert {r.record["material"] for r in c.search()} == {
        "LFP",
        "graphite",
        "NMC111",
        "NMC532",
        "NMC811",
        "NMC",
        "Graphite-SiOx",
        "LNMO",
        "silicon",
        "silicon-graphite",
        "LCO",
        "NCA",
        "NCO",
    }
    assert len(c.search()) == 83
    assert len(c.experiments) == 20
    assert len(c.search(representation="table")) == 64
    for material, role in [
        ("NMC111", "positive"),
        ("NMC532", "positive"),
        ("LNMO", "positive"),
        ("silicon", "negative"),
        ("silicon-graphite", "negative"),
    ]:
        for curve in c.search(material=material, representation="table"):
            r = curve.record
            assert r["electrode_role"] == role
            if not curve.id.startswith("sintef-"):
                continue  # Study-linked NEXTBMS/BPX nodes have separate source tests.
            assert r["cell_link"]["cell_id"] is None
            assert r["x"]["kind"] == "normalized_branch_capacity"
            assert c.experiments[r["experiment_id"]]["known_issues"] == []
    assert (
        len(
            {
                c.experiments[r.record["experiment_id"]]["electrode_metadata"][
                    "Public Labels"
                ]
                for r in c.search(material="silicon-graphite") if r.id.startswith("sintef-")
            }
        )
        == 2
    )
    assert len(c.search(cell_id="lg-m50")) == 2
    assert len(c.linked_tests("lg-m50")) == 3
    assert (
        c.get("marquis2019-lco-ocp").record["cell_link"]["relationship"] == "surrogate"
    )
    assert "dualfoil-attribution" in c.get("marquis2019-lco-ocp").record["source_ids"]
    assert c.cells["kim2011-nca-nominal-design"]["model"] is None
    assert (
        c.cells["kim2011-nca-nominal-design"]["identity_level"] == "nominal_design_only"
    )
    assert c.cells["mohtat2020-nmc532-pouch"]["match_level"] == "same_study_cell_family"
    for cid in [
        "kim2011-nca-nominal-design",
        "kokam-slpb78205130h-marquis2019",
    ]:
        assert len([p for p in c.search_parameters(cell_id=cid) if not p.id.startswith("model-completion-")]) == 38
        assert not c.linked_tests(cid)


def test_diffusivity_temperature_and_input_domain():
    p = Catalog().get_parameter("mohtat2020-positive-diffusivity")
    assert p(sto=0.5, T=298.15) == 8e-15
    assert p(sto=0.5, T=313.15) > p(sto=0.5, T=283.15)
    np.testing.assert_array_equal(p(sto=np.array([0.2, 0.8]), T=298.15), [8e-15, 8e-15])
    for sto, temperature in [
        (1.001, 298.15),
        (-0.01, 298.15),
        (0.5, 0),
        (np.nan, 298.15),
    ]:
        with pytest.raises(ValueError):
            p(sto=sto, T=temperature)
    with pytest.raises(ValueError):
        p(c_e=1000, c_s_surf=10000, c_s_max=30000, T=298.15)


@pytest.mark.parametrize(
    "name,cid",
    [
        ("Marquis2019", "kokam-slpb78205130h-marquis2019"),
        ("Mohtat2020", "mohtat2020-nmc532-pouch"),
        ("NCA_Kim2011", "kim2011-nca-nominal-design"),
        ("Chen2020", "lg-m50"),
    ],
)
def test_transcribed_ocp_and_functions_match_pinned_implementation(name, cid):
    pybamm = pytest.importorskip("pybamm")
    c = Catalog()
    path = CACHE / f"{name}-v25.4.2.py"
    if not path.exists():
        pytest.skip("Pinned source cache absent; run scripts/seed_v01.py --download")
    asset = next(a for a in c.assets.values() if a["filename"] == path.name)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
    spec = importlib.util.spec_from_file_location("checked_material_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    upstream = module.get_parameter_values()
    bindings = pybamm.ParameterValues(upstream)
    x = np.array([0.0037, 0.1231, 0.4997, 0.8103, 0.9971])
    for curve in c.search(cell_id=cid):
        if curve.id.startswith("mohtat-author-"):
            continue
        if curve.record["material"] == "graphite" and cid == "lg-m50":
            continue  # Existing Prada distribution is covered by test_sources.
        function = curve.record["representation"]["source_function"]
        np.testing.assert_allclose(
            curve(x), getattr(module, function)(x), rtol=2e-13, atol=2e-13
        )
    for p in c.search_parameters(cell_id=cid):
        if p.record["id"].startswith(("mohtat-author-", "model-completion-")):
            continue
        r = p.record
        if r["representation"]["kind"] == "scalar":
            assert p.value == upstream[r["name"]]
            continue
        if cid == "lg-m50":
            continue  # Existing kinetics already compared over three temperatures.
        function = getattr(module, r["provenance"]["location"].split("::")[-1])
        for temperature in [283.15, 298.15, 313.15]:
            kwargs = (
                {"sto": 0.43, "T": temperature}
                if r["category"] == "diffusion"
                else {
                    "c_e": 1200,
                    "c_s_surf": 12345,
                    "c_s_max": 32100,
                    "T": temperature,
                }
            )
            expected = function(**kwargs)
            if isinstance(expected, pybamm.Symbol):
                expected = bindings.process_symbol(expected).evaluate()
            assert p(**kwargs) == pytest.approx(float(expected), rel=1e-9)
