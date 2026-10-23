"""Source fidelity of experimental tables and completed model dictionaries."""

import ast
import csv
import importlib.util
import io
import json
from pathlib import Path
import zipfile
import sys

import numpy as np
import pytest

from ebp import Catalog
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from seed_materials import read_module
from seed_model_completeness import SETS


def test_oregan_tables_preserve_every_row_units_specimen_and_quality():
    c=Catalog()
    tables=[p for p in c.search_parameters(cell_id="lg-m50-oregan2022") if p.record["representation"]["kind"]=="table"]
    assert len(tables)==55
    assert len([p for p in tables if p.record["category"]=="diffusion"])==40
    with zipfile.ZipFile(c.root/c.assets["oregan-data-archive"]["path"]) as z:
        for p in tables:
            r=p.record;cond=r["conditions"];member=r["provenance"]["location"]
            source=list(csv.reader(io.StringIO(z.read(member).decode(cond["source_encoding"]))))
            original=np.array([[float(v) for v in row[:5 if "Diffusivity" in member else 2]] for row in source[1:]])
            with (c.root/r["representation"]["path"]).open() as f: rows=list(csv.DictReader(f))
            indices=np.array([int(row["source_csv_row"])-2 for row in rows])
            assert set(indices)==set(range(len(original)))
            is_d="Diffusivity" in member
            x,y=p.points()
            np.testing.assert_array_equal(x,original[indices,1 if is_d else 0])
            np.testing.assert_array_equal(y,original[indices,2 if is_d else 1]*cond["conversion_factor_to_native"])
            if is_d:
                np.testing.assert_array_equal([float(row["source_R_squared"]) for row in rows], original[indices,3])
                assert set(original[:,4])=={cond["temperature_K"]}
                assert cond["specimen_id"] in {"001","002"}
                assert cond["direction"] in {"lithiation","delithiation"}
            elif r["category"]=="kinetics":
                assert cond["specimen_id"] is None and r["unit"]=="A.m-2"
                assert cond["conversion_factor_to_native"]==10
            with pytest.raises(ValueError): p(**{r["representation"]["x"]["variable"]:x[0]-1})
    q=c.cells["lg-m50-oregan2022"]["quarantined_source_files"]
    assert len(q)==3 and all(p["negative_values"]>0 for p in q)
    assert all("Specific Heat Capacity" not in p.record["provenance"]["location"] for p in tables)
    conductivity=next(p for p in tables if "electronic-conductivity" in p.id)
    assert conductivity.points()[0][0]==288.0  # Source K is not silently shifted to 288.15.


def test_all_seven_model_dictionaries_are_stored_without_duplicate_keys():
    c=Catalog()
    for name,cid in SETS.items():
        asset=next(a for a in c.assets.values() if a["filename"]==name+"-v25.4.2.py")
        _,values,_=read_module(c.root/asset["path"])
        params=[p for p in c.parameters if p["cell_id"]==cid and not p["id"].startswith("mohtat-author-")]
        keys={k for k in values if k not in {"chemistry","citations"} and not k.endswith("electrode OCP [V]")}
        assert {p["name"] for p in params}==keys
        assert len(params)==len(keys)
        assert len(c.search(cell_id=cid)) in {2,4}


@pytest.mark.parametrize("name,cid",list(SETS.items())+[("ORegan2022","lg-m50-oregan2022")])
def test_new_expressions_match_reviewed_pybamm_reference_over_inputs(name,cid,tmp_path):
    pybamm=pytest.importorskip("pybamm")
    c=Catalog()
    cache=Path(__file__).resolve().parents[1]/".cache/upstream"
    source=cache/(name+"-v25.4.2.py")
    if name=="ORegan2022":
        source=tmp_path/"ORegan2022.py"
        source.write_bytes((c.root/c.assets["oregan-pybamm-code"]["path"]).read_bytes())
    if not source.exists():pytest.skip("Pinned reference cache absent; offline source fidelity is checked separately")
    spec=importlib.util.spec_from_file_location("reviewed_parameter_reference_"+name,source)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    reference=module.get_parameter_values();bindings=pybamm.ParameterValues(reference)
    selected=[p for p in c.search_parameters(cell_id=cid) if p.id.startswith(("model-completion-","oregan-model-"))]
    assert selected
    for p in selected:
        r=p.record
        if r["representation"]["kind"]=="scalar":
            assert p.value==reference[r["name"]]
            continue
        for t in [283.15,298.15,318.15]:
            for sto in [.0873,.4321,.8123]:
                sample={"T":t,"sto":sto,"c_e":1173,"c_s_surf":sto*32100,"c_s_max":32100,"c_Li":321,"L_sei":7e-9}
                kwargs={k:sample[k] for k in r["representation"]["variables"]}
                aliases=r.get("conditions",{}).get("source_argument_aliases",{k:k for k in kwargs})
                expected=reference[r["name"]](**{original:kwargs[alias] for original,alias in aliases.items()})
                if isinstance(expected,pybamm.Symbol):expected=bindings.process_symbol(expected).evaluate()
                np.testing.assert_allclose(p(**kwargs),float(expected),rtol=2e-9,atol=2e-17,err_msg=p.id)
    if name in {"Prada2013","ORegan2022"}:
        for curve in c.search(cell_id=cid):
            side=curve.record["electrode_role"].title()
            x=np.array([.043,.317,.714,.981])
            np.testing.assert_allclose(curve(x),reference[side+" electrode OCP [V]"](x),rtol=1e-12,atol=1e-12)


def test_p45b_user_laws_use_actual_coefficients_and_faraday_convention():
    c=Catalog()
    b=json.loads((c.root/c.assets["aepy-p45b-bpx"]["path"]).read_text())["Parameterisation"]
    u=b["User-defined"]
    ps=[p for p in c.search_parameters(cell_id="molicel-p45b-aboutenergy2026") if p.id.startswith("aepy-p45b-user-")]
    assert len(ps)==7
    for p in ps:
        name=p.record["name"]
        if name=="Contact resistance [Ohm]":
            assert p.value==u[name];continue
        for temp in [283.15,298.15,318.15]:
            ce=1173.;cm=ce/1000
            kwargs={"c_e":ce,"T":temp}
            if "exchange-current" in name:
                phase=name.split(":")[0];particle=b["Negative electrode"]["Particle"][phase]
                x=.317;kwargs.update(c_s_surf=x*30000,c_s_max=30000)
                modifier=(.5*np.tanh(1000*(x-.005))-.5*np.tanh(1000*(x-.995))) if phase=="Graphite" else 1.1*x+.2
                expected=modifier*96485.33212331001*particle["Reaction rate constant [mol.m-2.s-1]"]*np.exp(particle["Reaction rate constant activation energy [J.mol-1]"]/8.314462618*(1/298.15-1/temp))
            elif name in {"Cation transference number","Thermodynamic factor"}:
                expected=sum(u[f"{name} poly.poly{i}.a"]*ce**u[f"{name} poly.poly{i}.m"]*temp**u[f"{name} poly.poly{i}.n"] for i in range(9))
            elif "diffusivity" in name:
                a,b1,c1,d=(u[name+f" p{i}"] for i in range(1,5))
                expected=a*np.exp(b1*cm)*np.exp(c1/temp)*np.exp(d*cm/temp)
            else:
                a,b1,c1,d,e,f=(u[name+f" p{i}"] for i in range(1,7))
                expected=a*(1+temp-b1)*cm*(1+c1*np.sqrt(cm)+d*cm*(1+e*np.exp(1000/temp)))/(1+cm**4*f*np.exp(1000/temp))
            assert p(**kwargs)==pytest.approx(expected,rel=1e-12,abs=1e-15)


def test_new_parameter_domains_do_not_assume_missing_temperature_or_solid_inputs():
    c=Catalog()
    entropy=c.get_parameter("model-completion-ai2020-negative-electrode-ocp-entropic-change-v-k-1")
    assert np.isfinite(entropy(sto=.8))
    electrolyte=c.get_parameter("model-completion-chen2020-electrolyte-diffusivity-m2-s-1")
    assert electrolyte(c_e=1000,T=298.15)>0
    with pytest.raises(ValueError):electrolyte(c_e=-1,T=298.15)
    with pytest.raises(ValueError):electrolyte(c_e=1000,T=0)
    decay=c.get_parameter("model-completion-ecker2015-dead-lithium-decay-rate-s-1")
    with pytest.raises(ValueError):decay(L_sei=0)
    assert decay(L_sei=1e-8)>0
