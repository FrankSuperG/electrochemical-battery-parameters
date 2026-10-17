"""Verify MJ1 observations against originals, not synthesized model inputs."""

import csv
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
import pytest

from ebp import Catalog
from ebp.site import build_site

CELL = "lg-mj1-dlr-sintef"
NS = {"s":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def test_lab_tables_use_workbook_blanks_not_parquet_zeros():
    c = Catalog()
    original = Path(__file__).resolve().parents[1] / ".cache/upstream" / c.assets["mj1-workbook"]["filename"]
    if not original.exists():
        pytest.skip("External source cache absent; provenance CI reconstructs with --download")
    with zipfile.ZipFile(original) as z:
        # Independent OOXML extraction; no importer helper or upstream code runs.
        for sheet, member, factor in [("di","sheet5.xml",1e-4),("i0","sheet4.xml",10)]:
            doc = ET.fromstring(z.read("xl/worksheets/"+member))
            rows = {int(r.attrib["r"]):{x.attrib["r"].rstrip("0123456789"):x for x in r} for r in doc.findall("s:sheetData/s:row",NS)}
            for column, side, direction in [("C","negative","discharging"),("D","negative","charging"),("E","positive","discharging"),("F","positive","charging")]:
                expected=[]
                for n in range(5,42):
                    row=rows[n];node=row.get(column)
                    if node is None or node.attrib.get("t","n")!="n" or node.find("s:v",NS) is None:continue
                    expected.append([float(row["B"].find("s:v",NS).text),float(node.find("s:v",NS).text)*factor])
                p=c.get_parameter(f"mj1-lab-{side}-{sheet}-{direction}")
                x,y=p.points();expected.sort()
                assert len(x)==36 and np.all(y>0)
                np.testing.assert_array_equal(np.column_stack([x,y]),expected)
                assert p.record["conditions"]["missing_source_rows"] in [[5],[41]]


def test_model_variants_preserve_all_values_and_source_error_bounds():
    c=Catalog();fits=[p for p in c.search_parameters(cell_id=CELL) if p.id.startswith("mj1-gitt-")]
    assert len(fits)==12
    for p in fits:
        a=c.assets[p.record["provenance"]["asset_id"]]
        d=json.loads((c.root/a["path"]).read_text());side=p.record["conditions"]["electrode"].title()
        xkey=f"{side} electrode SOC [-]";ykey=f"{side} electrode diffusivity [m2.s-1]"
        order=np.argsort(d[xkey]);x,y=p.points()
        np.testing.assert_array_equal(x,np.asarray(d[xkey])[order]);np.testing.assert_array_equal(y,np.asarray(d[ykey])[order])
        with (c.root/p.record["representation"]["path"]).open(newline="") as f:rows=list(csv.DictReader(f))
        b=np.array([[float(r["source_error_lower"]),float(r["source_error_upper"])] for r in rows])
        np.testing.assert_array_equal(b,np.asarray(d["error bounds of "+ykey])[order])
    assert {p.record["conditions"]["model"] for p in fits}=={"SPM","SPMe","DFN"}


def test_ocp_native_finite_nodes_and_first_occurrences_are_preserved():
    c=Catalog()
    for curve in c.search(cell_id=CELL):
        r=curve.record;a=c.assets[r["provenance"]["asset_ids"][0]]
        src=pd.read_parquet(c.root/a["path"])[["stoichiometry_unit_one","voltage_volt"]].to_numpy()
        with (c.root/r["representation"]["path"]).open(newline="") as f:rows=list(csv.DictReader(f))
        indices=np.array([int(r["source_parquet_row"])-1 for r in rows]);x,y=curve.points()
        np.testing.assert_array_equal(np.column_stack([x,y]),src[indices])
        good=np.flatnonzero(np.isfinite(src).all(axis=1));_,first=np.unique(src[good,0],return_index=True)
        np.testing.assert_array_equal(indices,good[first])
        assert r["x"]["kind"]=="source_reported_stoichiometry" and r["direction"]=="unspecified"
        with pytest.raises(ValueError,match="StoichiometryMapping"):curve.to_pybamm()
    assert c.get("mj1-positive-ocp-charging").record["provenance"]["processing"]["nonfinite_rows_omitted"]==1402


def test_table_evaluation_guards_coordinate_domain_and_integrity():
    c=Catalog();p=c.get_parameter("mj1-lab-negative-di-charging");x,y=p.points()
    np.testing.assert_array_equal(p(source_soc_percent=x),y)
    assert p(source_soc_percent=(x[0]+x[1])/2)==pytest.approx((y[0]+y[1])/2)
    for bad in [np.nan,np.inf,x[0]-1,x[-1]+1]:
        with pytest.raises(ValueError,match="domain"):p(source_soc_percent=bad)
    with pytest.raises(ValueError,match="Required variable"):p(sto=0.5)
    p.record["representation"]["sha256"]="0"*64
    assert any("Parameter table SHA-256" in s for s in c.validate())


def test_identity_license_and_exclusions_are_explicit():
    c=Catalog();cell=c.cells[CELL]
    assert not c.linked_tests(CELL)
    assert cell["evidence_matrix"]["full_cell_tests"]["match_level"]=="missing"
    assert len(c.search_parameters(cell_id=CELL))==42
    assert cell["nominal_capacity_Ah"]==3.5
    assert all(p.record["license"]=="CC-BY-4.0" for p in c.search_parameters(cell_id=CELL))
    assert c.get_parameter("mj1-original-separator-thickness").value==pytest.approx(12e-6)
    assert not any("initial concentration" in p.record["name"].lower() for p in c.search_parameters(cell_id=CELL))
    assert all("path" not in a for a in c.assets.values() if a.get("role")=="electrode_test_external")
    assert "path" not in c.assets["mj1-workbook"]
    selection=json.loads((c.root/c.assets["mj1-workbook-selection"]["path"]).read_text())
    assert set(selection["sheets"])=={"physical_quantities","cell_specifications","Di","i0"}
    assert selection["source_sha256"]==c.assets["mj1-workbook"]["sha256"]


def test_native_parameter_downloads_and_offline_package(tmp_path):
    c=Catalog();build_site(c,tmp_path)
    with zipfile.ZipFile(tmp_path/"downloads"/f"{CELL}-bundle.zip") as z:
        for p in c.search_parameters(cell_id=CELL):
            rep=p.record["representation"]
            if rep["kind"]=="table":
                name=rep["path"].split("/")[-1]
                assert z.read(name)==(c.root/rep["path"]).read_bytes()
                assert (tmp_path/"downloads"/name).read_bytes()==z.read(name)
        assert "licenses/CC-BY-4.0.txt" in z.namelist()
        assert "sources/mj1-workbook-cell-selection.json" in z.namelist()
        assert not any(n.lower().endswith(".xlsx") for n in z.namelist())
