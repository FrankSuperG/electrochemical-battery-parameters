"""Generate the GitHub browsing index from the authoritative packaged catalog.

No downloads are performed. Large native OCP/test files are linked, not copied.
Run after catalog changes; --check detects stale exports and navigation links.
"""

import argparse
import csv
import io
import json
import os
from pathlib import Path
import re

from ebp import Catalog


REPO = Path(__file__).resolve().parents[1]
START = "<!-- DATA_QUICKLINKS_START -->"
END = "<!-- DATA_QUICKLINKS_END -->"
FORMULA_SAMPLES = 2001


def text_cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def aging_label(record):
    aging = record["aging_data"]
    return ("Yes (" + ", ".join(aging["kinds"]) + ")" if aging["status"] == "available"
            else {"not_reported": "Not reported", "unverified": "Unverified"}[aging["status"]])


def ocp_anchor_label(record):
    return {"external_half_cell_files": "External half-cell files",
            "catalog_half_cell": "Imported half-cell branches",
            "published_parameterisation": "Published fitted parameterisation",
            "reused_catalog_expression": "Explicitly reused catalog expression",
            "cross_study_catalog_half_cell": "Cross-study catalog half-cell reference",
            "model_derived_only": "Model-derived only", "reuse_unresolved": "Reuse unresolved",
            "not_identified": "Not identified", "full_cell_ocv_only": "Whole-cell OCV only"}[record["ocp_anchor"]["kind"]]


def eis_coverage_label(record):
    if "eis" not in record["test_types"]:
        return "Not reported"
    status = record["test_coverage"]["EIS"]["status"]
    if status == "container_only":
        return "Dataset link only; files unverified"
    if status in {"not_located", "not_established"}:
        return "Source claim; files unverified"
    return "Located / source-listed"


def csv_bytes(headers, rows):
    handle = io.StringIO(newline="")
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return handle.getvalue().encode("utf-8")


def json_bytes(value):
    return (json.dumps(value, indent=2, allow_nan=False) + "\n").encode("utf-8")


def parameter_csv(parameters):
    return csv_bytes(
        ["id", "cell_id", "name", "category", "value_or_expression", "unit",
         "conditions_json", "definition", "source_ids", "origin_status",
         "parameterization_variant"],
        [
            [p["id"], p["cell_id"], p["name"], p["category"],
             ("table:" + p["representation"]["path"] if p["representation"]["kind"] == "table" else p["representation"].get("value", p["representation"].get("expression"))),
             p["unit"], json.dumps(p.get("conditions", {}), sort_keys=True),
             p.get("definition", p["name"]), ";".join(p["source_ids"]),
             p["provenance"]["origin_status"],
             p.get("conditions", {}).get("parameterization_variant", "")]
            for p in parameters
        ],
    )


def battery_model_index(catalog):
    """Group explicit cell identities for navigation without changing scientific joins."""
    output, groups, assigned = {}, [], set()
    # Navigation may cross studies; scientific parameter joins remain separately explicit.
    extra = {"molicel-p45b-aboutenergy2026": ["tum-p45b-halfcell-aging-2026"],
             "lg-m50-oregan2022": ["tec-lgm50-multitemperature-2021"]}
    names = {}
    for cid, cell in catalog.cells.items():
        sources = [r for r in catalog.external_datasets
                   if cid in r["parameter_link"]["cell_ids"] or r["id"] in extra.get(cid, [])]
        assigned.update(r["id"] for r in sources)
        groups.append({"id": cid, "title": cell["display_name"], "family": catalog.cell_material_family(cid),
                       "cell": cell, "sources": sources})
    for r in catalog.external_datasets:
        if r["id"] not in assigned:
            groups.append({"id": r["id"], "title": names.get(r["id"], r["cell_identity"]),
                           "family": "/".join(r["material_families"]), "cell": None, "sources": [r]})

    def link(page, target, label):
        target, sep, anchor = str(target).partition("#")
        href = Path(os.path.relpath(target, page.parent)).as_posix()+(sep+anchor if sep else "")
        return f"[{text_cell(label)}]({href})"

    def component_links(group, page):
        cid, cell = group["id"], group["cell"]
        curves = catalog.search(cell_id=cid) if cell else []
        kinds = {r.record["measurement"] for r in curves}
        label = ("modeled OCPn" if kinds == {"model_ocp"} else "pseudo-OCP" if kinds == {"pseudo_ocp"} else
                 "tables / fits" if kinds == {"literature_table"} else "expressions" if kinds == {"literature_formula"} else "curve records")
        if cid in {"lg-m50-oregan2022","prada2013-lfp-nominal-design"}:
            label="reused expressions"
        ocp = (link(page, f"data/cells/{cid}.md#ocp-curves", f"{len(curves)} {label}") if curves else
               link(page, f"data/cells/{cid}.md#ocp-curves", "Reuse unresolved") if cell and cid == "lg-m50lt-hallemans2025" else "Not extracted")
        if not curves:
            leads = [r for r in group["sources"] if r["ocp_anchor"]["kind"] in {"external_half_cell_files", "published_parameterisation"}]
            if leads:
                ocp = "<br>".join(link(page, f"data/full-cell/{r['id']}.md#electrode-ocp-anchor", "External only; reuse/definition gap") for r in leads)
        values = [ocp]
        for category in ["diffusion", "kinetics"]:
            subset = [p for p in catalog.parameters if cell and p["cell_id"] == cid and p["category"] == category]
            label = f"{len(subset)} records"
            if cid == "lg-m50lt-hallemans2025":label += " (groups)"
            values.append(link(page, f"data/parameters/{cid}--{category}.csv", label) if subset else "Not extracted")
        return values

    def coverage(group):
        kinds = []
        sources = group["sources"]
        if any(len(r["temperatures_C"]) > 1 for r in sources):kinds.append("multi-T")
        local = catalog.linked_tests(group["id"]) if group["cell"] else []
        if any("dynamic" in r["test_types"] for r in sources) or any("drive" in t["protocol"].lower() for t in local):kinds.append("dynamic")
        if any(r["aging_data"]["status"] == "available" for r in sources):kinds.append("ageing")
        if any("eis" in r["test_types"] for r in sources):kinds.append("EIS")
        return ", ".join(kinds) if kinds else "See test conditions / gaps"

    for group in groups:
        page = Path(f"data/batteries/{group['id']}.md")
        cell = group["cell"]
        lines = [f"# {group['title']}", "", "[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)", "",
                 f"Material grouping: **{group['family']}**. This is a navigation group; studies and specimens remain separate.", "",
                 "## OCP and model parameters", "",
                 "OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.", "",
                 "| OCP | Diffusion | Kinetics |", "|---|---|---|", "| "+" | ".join(component_links(group, page))+" |", ""]
        if cell:
            cid = group["id"]
            lines += [link(page, f"data/cells/{cid}.md", "Full cell/study package: definitions, all parameters, sources and gaps"), "",
                      link(page, f"data/parameters/{cid}.json", "Machine-readable package (JSON)"), ""]
            for category in ["ocp", "diffusion", "kinetics"]:
                lines += [f"- **{category.upper() if category == 'ocp' else category.title()}:** {cell['coverage'][category]}"]
        lines += ["", "## Full-cell tests", "",
                  "New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.", ""]
        local = catalog.linked_tests(group["id"]) if cell else []
        if local:
            lines += [link(page, f"data/cells/{group['id']}.md#full-cell-tests", f"{len(local)} existing packaged test files with per-file conditions"), "", cell["coverage"]["full_cell_tests"], ""]
        if group["sources"]:
            lines += ["| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |", "|---|---|---|---|---|---|---|"]
            for r in group["sources"]:
                source = f"data/full-cell/{r['id']}.md"
                cc = link(page, source+"#requested-test-coverage", "Source rates / limits") if "constant_current" in r["test_types"] or "cccv" in r["test_types"] else "Not separately verified"
                dynamic = (", ".join(r["profiles"]) or "Unnamed / staged") if "dynamic" in r["test_types"] else "Not reported"
                assoc = r["parameter_link"]["match_level"]
                if group["id"] not in r["parameter_link"]["cell_ids"] and cell:assoc = "Same model; other study, no native parameter join"
                lines += ["| "+" | ".join([link(page, source+"#file-locations", r["id"]), cc,
                    "/".join(str(t) for t in r["temperatures_C"]) or "Unverified", text_cell(dynamic),
                    link(page, source+"#ageing-data", aging_label(r)), eis_coverage_label(r), text_cell(assoc)])+" |"]
        else:lines += ["No external full-cell dataset curated for this entry."]
        lines += ["", link(page,"docs/PARAMETER_AUDIT.md","Parameter extraction audit: stored records, unresolved reuse and definitions"), "",
                  "Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.", "",
                  "## Matching and gaps", "",
                  "A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.", ""]
        if cell:lines += [f"- Native package match: `{cell['match_level']}`. {cell['match_evidence']}"]
        for r in group["sources"]:
            lines += [f"- **{r['id']}**: {r['parameter_link']['evidence']}",
                      "  "+link(page, f"data/full-cell/{r['id']}.md#missing-items-and-limits", "Missing items, source terms and review limits")]
        lines += [""]
        output[str(page)] = "\n".join(lines).encode()

    def table(page, level):
        lines = ["OCP and parameter links open repository data. Every indexed package has stored OCP, diffusion or kinetics records; full-cell links are supporting references to source descriptions and downloads. **Not extracted** means no reusable native record is curated; it is not a claim that no measurement exists.", "",
                 "Coverage labels below are source-level discovery aids. Read each model page for study, temperature, profile, licence and specimen limits. Half-cell temperature is tracked separately.", "",
                 link(page,"docs/PARAMETER_AUDIT.md","Extraction audit for every battery/study: stored / reuse unresolved / definition unresolved / not located"), "",
                 "Record counts include published assumptions, borrowed functions, activation energies and optional submodel inputs, not a count of independent measurements or solid-electrode coefficients. Read parameter names and origin fields before selecting a model input.", ""]
        families = sorted({g["family"] for g in groups}, key=lambda f: (("LFP", "NMC", "NCA", "LCO", "NCO").index(f) if f in ("LFP", "NMC", "NCA", "LCO", "NCO") else 99, f))
        for family in families:
            lines += ["#"*level+" "+family, "", "| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |", "|---|---|---|---|---|---|"]
            for g in sorted((g for g in groups if g["family"] == family), key=lambda g: ("ncr18650b" not in g["id"], g["title"].casefold())):
                target=f"data/batteries/{g['id']}.md"
                count=len(catalog.linked_tests(g["id"])) if g["cell"] else 0
                n_sources=len(g["sources"])
                label=" + ".join(([f"{count} packaged"] if count else [])+([f"{n_sources} external {'source' if n_sources == 1 else 'sources'}"] if n_sources else [])) or "Not linked"
                tests=link(page, target+"#full-cell-tests", label)
                limits=link(page, target+"#matching-and-gaps", "Match / gaps")
                match = ("Cross-study / mixed sources" if g["cell"] and any(r["parameter_link"]["match_level"] != "same_model_same_study" for r in g["sources"]) else
                         g["cell"]["match_level"].replace("_", " ") if g["cell"] else "Parameters unmatched")
                lines += ["| "+" | ".join([link(page,target,g["title"]),*component_links(g,page),tests,coverage(g)+"<br>"+match+" · "+limits])+" |"]
            lines += [""]
        lines += ["Material-only curves without a verified battery model remain in "+link(page,"data/ocp/README.md","the OCP material index")+"; no commercial-cell assignment is inferred.", ""]
        return "\n".join(lines)

    page=Path("data/batteries/README.md")
    output[str(page)]=( "# Battery model index\n\n[Repository README](../../README.md) · [All data](../README.md)\n\n"+table(page,2)).encode()
    return output, table(Path("README.md"),3)


def full_cell_index(catalog):
    """Metadata-only external links plus source-preserving local test navigation."""
    output = {}
    root = Path("data/full-cell")

    def link(page, target, label):
        return f"[{text_cell(label)}]({Path(os.path.relpath(target, page.parent)).as_posix()})"

    families = sorted(set(catalog.cell_material_family(cid) for cid in catalog.cells)
                      | {m for r in catalog.external_datasets for m in r["material_families"]},
                      key=lambda m: (("LFP", "NMC", "NCA", "LCO", "NCO").index(m)
                                     if m in ("LFP", "NMC", "NCA", "LCO", "NCO") else 99, m))
    output[str(root / "datasets.json")] = json_bytes(catalog.external_document)
    output[str(root / "datasets.csv")] = csv_bytes(
        ["id", "material_families", "cell_identity", "test_types", "profiles", "rate_summary",
         "temperatures_C", "license", "parameter_match", "linked_cell_ids", "source_url",
         "doi", "source_version", "checked_on", "review_level", "missing_items",
         "aging_data", "aging_kinds", "aging_evidence", "aging_source_url",
         "ocp_anchor", "half_cell_temperatures_C", "ocp_anchor_evidence"],
        [[r["id"], ";".join(r["material_families"]), r["cell_identity"], ";".join(r["test_types"]),
          ";".join(r["profiles"]), r["rate_summary"], json.dumps(r["temperatures_C"]),
          r["license"]["identifier"], r["parameter_link"]["match_level"],
          ";".join(r["parameter_link"]["cell_ids"]), r["source"]["url"], r["source"]["doi"],
          r["source"]["version"], r["review"]["checked_on"], r["review"]["level"],
          "; ".join(r["missing_items"]), r["aging_data"]["status"],
          ";".join(r["aging_data"]["kinds"]), r["aging_data"]["evidence"],
          r["aging_data"]["source_url"], r["ocp_anchor"]["kind"],
          json.dumps(r["ocp_anchor"]["half_cell_temperatures_C"]),
          r["ocp_anchor"]["evidence"]] for r in catalog.external_datasets])
    file_rows = catalog.search_dataset_files()
    output[str(root / "files.csv")] = csv_bytes(
        ["dataset_id", "source_path", "kind", "cell_model", "material_family", "source_sample_id",
         "test_types", "profiles", "temperature_C", "nominal_rate_C", "verification", "content_review",
         "parameter_match", "url", "note", "dataset_aging_status"],
        [[r["dataset_id"], r["source_path"], r["kind"], r["cell_model"], r["material_family"], r["source_sample_id"],
          ";".join(r["test_types"]), ";".join(r["profiles"]), r["temperature_C"], r["nominal_rate_C"],
          r["verification"], r["content_review"], r["parameter_match"], r["url"], r["note"],
          r["dataset_aging_status"]] for r in file_rows])
    for r in catalog.external_datasets:
        page = root / (r["id"] + ".md")
        lines = [f"# {r['title']}", "", "[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)", "",
                 f"Dataset link ID: `{r['id']}`. Storage: **external link**. This entry is not an imported measurement file.", "",
                 f"Material families: {', '.join(r['material_families'])}. {r['cell_identity']}", "",
                 f"[Open the original dataset]({r['source']['url']}) · Version: `{r['source']['version']}`", "",
                 f"DOI: {r['source']['doi'] or 'Not assigned in the inspected source'}. Checked: {r['review']['checked_on']}.", "",
                 "## Electrode OCP anchor", "", f"**{ocp_anchor_label(r)}**. {r['ocp_anchor']['evidence']}", "",
                 f"Reported half-cell temperature labels / degC: {r['ocp_anchor']['half_cell_temperatures_C'] or 'Not independently verified'}. Full-cell temperatures below do not establish half-cell OCP temperature coverage.", "",
                 "Source paths: " + ("; ".join('`' + path + '`' for path in r['ocp_anchor']['source_paths']) or 'Use the cited catalog curves/source evidence; no verified external half-cell member path.'), "",
                 "OCP evidence: " + " · ".join(f"[Source {i+1}]({url})" for i, url in enumerate(r['ocp_anchor']['source_urls'])), "",
                 "## Tests and channels", "",
                 f"Types: {', '.join(r['test_types'])}. Profiles: {', '.join(r['profiles']) or 'No named drive profile verified'}.", "",
                 r["rate_summary"], "",
                 f"Reported temperature labels / degC: {r['temperatures_C'] or 'Not verified'}. These are source conditions, not measured temperature channels.", "",
                 f"Reported time-series channels: {', '.join(r['channels']['time_series']) or 'Raw headers not inspected'}.", "",
                 f"Reported frequency-domain channels: {', '.join(r['channels']['frequency_domain']) or 'Not verified / not applicable'}.", "",
                 r["channels"]["note"], "", "## Ageing data", "",
                 f"**{aging_label(r)}**. {r['aging_data']['evidence']}", "",
                 f"[Ageing coverage evidence]({r['aging_data']['source_url']}). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.", "",
                 "## Parameter association", "",
                 f"Match: `{r['parameter_link']['match_level']}`. {r['parameter_link']['evidence']}", ""]
        for cid in r["parameter_link"]["cell_ids"]:
            lines += [link(page, Path("data/cells") / f"{cid}.md", catalog.cells[cid]["display_name"]), ""]
        lines += [f"Components without a native catalog join: {', '.join(r['parameter_link']['missing_components'])}.", "",
                  "| Component | Match / quantity | Catalog record IDs | Evidence and missing items |",
                  "|---|---|---|---|"]
        for key, component in r["parameter_components"].items():
            lines += [f"| {key} | `{component['match_level']}` / `{component['quantity_kind']}` | {', '.join('`' + rid + '`' for rid in component['record_ids']) or 'None'} | {text_cell(component['evidence'])} Missing: {text_cell('; '.join(component['missing_items']))} |"]
        lines += ["", "## Requested-test coverage", "", "| Test class | Review result | Evidence / limits |", "|---|---|---|"]
        for key, coverage in r["test_coverage"].items():
            lines += [f"| {key} | `{coverage['status']}` | {text_cell(coverage['evidence'])} |"]
        lines += ["", "## File locations", "", r["inventory_scope"], "",
                  "An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.", "",
                  "| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |",
                  "|---|---|---|---|---|---|"]
        for item in r["file_links"]:
            conditions = f"{item['temperature_C']} degC" if item["temperature_C"] is not None else "Temperature unknown"
            if item["nominal_rate_C"] is not None:
                conditions += f"; {item['nominal_rate_C']}C"
            label = ("Parent archive" if item["kind"] == "archive_member" else
                     "Open dataset / documentation" if item["kind"] == "documentation" else "Open source file")
            lines += [f"| `{text_cell(item['source_path'])}` | {text_cell(item['cell_model'] or 'Unresolved')} / {text_cell(item['source_sample_id'] or 'No sample ID')} | {text_cell(', '.join(item['test_types']) + '; ' + ', '.join(item['profiles']))} | {conditions} | `{item['verification']}`; content `{item['content_review']}` | [{label}]({item['url']}) |"]
        lines += ["", "File notes:", ""]
        for item in r["file_links"]:
            lines += [f"- `{text_cell(item['source_path'])}`: {item['note']}"]
        lines += ["",
                  "## Reuse and access", "",
                  f"License: **{r['license']['identifier']}**. [Source terms]({r['license']['evidence_url']}). {r['license']['note']}", "",
                  f"Review level: `{r['review']['level']}`. {r['review']['note']}", ""]
        for item in r["file_links"]:
            lines += [f"- [{item['label']}]({item['url']})"]
            for algorithm in ("md5", "sha256"):
                if algorithm in item:
                    lines += [f"  Publisher/pinned {algorithm.upper()}: `{item[algorithm]}`."]
        for path in r.get("catalog_evidence_paths", []):
            lines += ["", link(page, Path("src/ebp/data") / path, "Supporting evidence (" + Path(path).suffix.lstrip('.').upper() + ")"), ""]
        lines += ["", "## Missing items and limits", ""] + [f"- {item}" for item in r["missing_items"]]
        lines += ["", "## Evidence", ""] + [f"- [Primary source {i + 1}]({url})" for i, url in enumerate(r["evidence_urls"])]
        lines += ["", "No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.", ""]
        output[str(page)] = "\n".join(lines).encode()
    overview = ["# Supporting full-cell tests by material", "", "[All data](../README.md) · [How to use external links](../../docs/FULL_CELL_DATASETS.md)", "",
                f"{len(catalog.full_cell_tests)} existing packaged branch/test files and {len(catalog.external_datasets)} external dataset-link records. External records are not imported files or independent specimens. One multi-chemistry dataset can appear under several materials.", "",
                f"Large observations remain with the original provider. [Dataset metadata CSV](datasets.csv) · [Complete metadata JSON](datasets.json) · [{len(file_rows)} selected file/container locators (CSV)](files.csv). No automatic download occurs.", "",
                "| Material family | Packaged test files | External datasets | Browse |", "|---|---:|---:|---|"]
    for family in families:
        local = [t for t in catalog.full_cell_tests if catalog.cell_material_family(t["cell_id"]) == family]
        external = catalog.search_datasets(material=family)
        overview += [f"| {family} | {len(local)} | {len(external)} | [{family}]({family}.md) |"]
        page = root / f"{family}.md"
        lines = [f"# {family} full-cell tests", "", "[All materials](README.md) · [Access, licenses and limits](../../docs/FULL_CELL_DATASETS.md)", "",
                 "Material grouping is a discovery aid, not evidence that tests and parameters belong together. NCO retains its source label and is not silently classified as NMC or NCA.", "",
                 "## External datasets", "", "| Dataset / cell | OCP anchor | Tests / profiles | Rates and temperatures | Ageing data | License | Parameter match |", "|---|---|---|---|---|---|---|"]
        for r in external:
            temperatures = str(r["temperatures_C"]) if r["temperatures_C"] else "not verified"
            lines += [f"| [{text_cell(r['title'])}]({r['id']}.md) | {ocp_anchor_label(r)} | {text_cell(', '.join(r['test_types']) + '; ' + ', '.join(r['profiles']))} | {text_cell(r['rate_summary'])} Source temperatures: {temperatures} | {aging_label(r)} | {r['license']['identifier']} | `{r['parameter_link']['match_level']}` |"]
        if not external:
            lines += ["", "No external dataset link curated for this family yet."]
        lines += ["", "## Existing packaged tests", "", "These CSVs already belong to the catalog; this index adds links without duplicating observations.", "",
                  "| Test | Cell / metadata | Source protocol | CSV | Parameter match |", "|---|---|---|---|---|"]
        for t in local:
            target = Path("src/ebp/data") / t["normalized_path"]
            lines += [f"| `{t['id']}` | {link(page, Path('data/cells') / (t['cell_id'] + '.md'), catalog.cells[t['cell_id']]['display_name'])} | {text_cell(t['protocol'])} | {link(page, target, 'Download')} | `{t['relationship_to_parameters']}` |"]
        if not local:
            lines += ["", "No packaged full-cell file for this family. External links do not fill missing parameter matches."]
        lines += [""]
        output[str(page)] = "\n".join(lines).encode()
    overview += ["", "## External dataset availability", "",
                 "Ageing availability applies to a source, not every linked file. `Not reported` is not proof of absence. Formation, repeated initial tests and simulated degradation alone are not measured longitudinal ageing data.", "",
                 "| Dataset | Materials | OCP anchor | Ageing data | License |", "|---|---|---|---|---|"]
    for r in catalog.external_datasets:
        overview += [f"| [{text_cell(r['title'])}]({r['id']}.md) | {', '.join(r['material_families'])} | {ocp_anchor_label(r)} | {aging_label(r)} | {r['license']['identifier']} |"]
    overview += ["", "Test types: `constant_current`, `cccv`, `pulse`, `dynamic`, `eis`, `ocv`. Named profiles can be searched at dataset level with `ebp datasets --profile US06`, or at inspected-file level with `ebp datasets --files --profile US06`. Dataset declarations are not automatically inherited by file locators. `ocv` refers to whole-cell characterization, never an automatically inferred electrode OCP. Use `ebp datasets --aging-status available` for sources with documented ageing data.", ""]
    output[str(root / "README.md")] = "\n".join(overview).encode()
    return output


def render_index(repo=REPO):
    """Return relative output paths and deterministic bytes; never mutate sources."""
    repo = Path(repo)
    catalog = Catalog(repo / "src/ebp/data")
    errors = catalog.validate()
    if errors:
        raise ValueError("; ".join(errors))
    output = {}
    output.update(full_cell_index(catalog))
    if __package__:
        from .parameter_audit import render as render_parameter_audit
    else:
        from parameter_audit import render as render_parameter_audit
    model_pages, model_table = battery_model_index(catalog)
    output["docs/PARAMETER_AUDIT.md"] = render_parameter_audit(catalog)
    output.update(model_pages)

    def relative(page, target):
        return Path(os.path.relpath(target, Path(page).parent)).as_posix()

    def link(page, target, label):
        return f"[{text_cell(label)}]({relative(page, target)})"

    def source_path(path):
        return Path("src/ebp/data") / path

    def ocp_table(page, curves):
        lines = [
            "| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |",
            "|---|---|---|---|---|---|",
        ]
        for curve in curves:
            r = curve.record
            is_formula = r["representation"]["kind"] == "expression"
            target = (Path("data/ocp") / f"{curve.id}-sampled.csv" if is_formula
                      else source_path(r["representation"]["path"]))
            label = "Generated samples" if is_formula else "Retained table"
            lines.append(
                f"| `{curve.id}` | {r['electrode_role']} / {r['material']} | {r['measurement']} / {r['reference']} | "
                f"{r['x']['kind']}; {r['x']['domain']} | "
                f"{link(page, target, label)} | "
                f"{link(page, Path('data/ocp') / f'{curve.id}.json', 'JSON')} |"
            )
        return "\n".join(lines)

    for curve in catalog.search():
        r = curve.record
        formula = r["representation"]["kind"] == "expression"
        if formula:
            x, y = curve.sample(FORMULA_SAMPLES)
            output[f"data/ocp/{curve.id}-sampled.csv"] = csv_bytes(
                ["x", "potential_V"],
                ((f"{a:.12g}", f"{b:.12g}") for a, b in zip(x, y)),
            )
        output[f"data/ocp/{curve.id}.json"] = json_bytes({
            "record": r,
            "sources": {sid: catalog.sources[sid] for sid in r["source_ids"]},
            "experiment": catalog.experiments.get(r["experiment_id"]),
            "upstream_assets": {aid: catalog.assets[aid] for aid in r["provenance"]["asset_ids"]},
            "export": {
                "kind": "generated_formula_samples" if formula else "retained_source_table",
                "sample_count": FORMULA_SAMPLES if formula else None,
                "significant_digits": 12 if formula else None,
                "canonical_data_root": "../../src/ebp/data",
                "note": "Formula samples are calculated, not measurements. Read the record's coordinate, direction, conditions and license.",
            },
        })

    cell_rows = []
    for cid, cell in catalog.cells.items():
        page = Path("data/cells") / f"{cid}.md"
        curves = catalog.search(cell_id=cid)
        parameters = [p for p in catalog.parameters if p["cell_id"] == cid]
        tests = catalog.linked_tests(cid)
        lines = [f"# {cell['display_name']}", "",
                 f"[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)", "",
                 f"Cell ID: `{cid}`. Match level: `{cell['match_level']}`.", "",
                 cell["match_evidence"], "", cell["note"], "",
                 "## Parameters", ""]
        if cell.get("curation_guide"):
            lines += [link(page, Path(cell["curation_guide"]), "Curation review: definitions, licensing and matching limits"), ""]
        csv_path = Path("data/parameters") / f"{cid}.csv"
        json_path = csv_path.with_suffix(".json")
        source_ids = set(cell["source_ids"])
        source_ids.update(s for p in parameters for s in p["source_ids"])
        source_ids.update(s for curve in curves for s in curve.record["source_ids"])
        source_ids.update(t["source_id"] for t in tests)
        asset_ids = {p["provenance"]["asset_id"] for p in parameters}
        asset_ids.update(a for curve in curves for a in curve.record["provenance"]["asset_ids"])
        asset_ids.update(t["asset_id"] for t in tests)
        asset_ids.update(a for t in tests for a in t.get("supporting_asset_ids", []))
        asset_ids.update(s["asset_id"] for t in tests for s in t.get("sidecars", []))
        asset_ids.update(cell.get("supporting_asset_ids", []))
        output[str(json_path)] = json_bytes({
                "cell_id": cid, "cell": cell, "parameters": parameters,
                "ocp_records": [c.record for c in curves], "full_cell_tests": tests,
                "external_datasets": catalog.search_datasets(cell_id=cid),
                "sources": {s: catalog.sources[s] for s in sorted(source_ids)},
                "upstream_assets": {a: catalog.assets[a] for a in sorted(asset_ids)},
                "canonical_data_root": "../../src/ebp/data",
                "independent_full_cell_validation": False,
        })
        if parameters:
            output[str(csv_path)] = parameter_csv(parameters)
            lines += [f"{link(page, csv_path, f'All {len(parameters)} parameter records (CSV)')} · "
                      f"{link(page, json_path, 'Definitions, sources and linked-test metadata (JSON)')}", "",
                      "CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.", ""]
            variants = sorted({p.get("conditions", {}).get("parameterization_variant") for p in parameters}
                              - {None, ""})
            if len(variants) > 1:
                lines += ["**Choose one parameterization variant. Do not combine these alternatives. The all-record CSV is for inspection.**", "",
                          "| Variant | Records | CSV |", "|---|---:|---|"]
                for variant in variants:
                    subset = [p for p in parameters if p.get("conditions", {}).get("parameterization_variant") == variant]
                    target = csv_path.with_name(f"{cid}--{variant}.csv")
                    output[str(target)] = parameter_csv(subset)
                    lines.append(f"| `{variant}` | {len(subset)} | {link(page, target, 'Download CSV')} |")
                lines.append("")
        else:
            lines += ["No non-OCP parameters imported for this entry. No placeholder parameter values are supplied.", "",
                      link(page, json_path, "Cell package: OCP, tests, sources and missing items (JSON)"), ""]
        for category in ["diffusion", "kinetics"]:
            subset = [p for p in parameters if p["category"] == category]
            lines += [f"### {category.title()} parameters", ""]
            if subset:
                target = Path("data/parameters") / f"{cid}--{category}.csv"
                output[str(target)] = parameter_csv(subset)
                lines += [link(page, target, f"{len(subset)} {category} records (CSV)"), "", cell["coverage"][category], "",
                          "Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.", ""]
            else:lines += ["Not extracted for this cell/study.", ""]
        tabulated = [p for p in parameters if p["representation"]["kind"] == "table"]
        if tabulated:
            lines += ["### Native parameter tables", "", "Linear interpolation is available only within each retained native domain. Source SOC and stoichiometry coordinates require explicit mapping before model use.", "",
                      "| Parameter | Native CSV | Axis / unit | Value unit | Variant |", "|---|---|---|---|---|"]
            for p in tabulated:
                rep = p["representation"]
                lines.append(f"| `{p['id']}` | {link(page, source_path(rep['path']), 'Download CSV')} | {rep['x']['variable']} / {rep['x']['unit']} | {p['unit']} | {p['conditions'].get('parameterization_variant', '')} |")
            lines.append("")
        lines += ["## OCP curves", ""]
        lines += [ocp_table(page, curves) if curves else "No electrode-resolved OCP record linked to this cell. Full-cell pseudo-OCV and unrelated same-chemistry curves do not fill this gap.", ""]
        lines += ["Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.", "",
                  "## Full-cell tests", ""]
        if tests:
            lines += ["CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.", "",
                      "| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |",
                      "|---|---|---|---|---|"]
            for test in tests:
                original = test.get("original_download_path") or test.get("path")
                original_link = (link(page, source_path(original), Path(original).suffix.lstrip(".").upper())
                                 if original else f"[Source download](<{catalog.assets[test['asset_id']]['url']}>)")
                coordinate = test.get("independent_variable", {}).get("column", "time_s")
                availability = test["channel_availability"]
                rows = catalog.full_cell_data(test["id"], normalized=True)
                counts = [sum(bool(r.get(key)) for r in rows) for key in
                          ["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K"]]
                # Existing metadata counts are checked against the exported rows.
                for key, count in zip(["time_s", "current_charge_positive_A", "voltage_V", "cell_temperature_K"], counts):
                    if key in availability and count != availability[key]["present_rows"]:
                        raise ValueError(f"Channel count mismatch: {test['id']} {key}")
                lines.append(f"| `{test['id']}` — {text_cell(test['protocol'])} | `{coordinate}` | "
                             f"{link(page, source_path(test['normalized_path']), 'CSV')} | {original_link} | "
                             f"{' / '.join(map(str, counts))} of {len(rows)} |")
            lines += ["", "### Test gaps and extra channels", ""]
            for test in tests:
                gaps = "; ".join(test["missing_items"]) or "No missing measurement channels recorded; specimen and validation limits still apply."
                lines.append(f"- `{test['id']}`: {gaps}")
                for side in test.get("sidecars", []):
                    lines.append(f"  - {link(page, source_path(side['path']), 'Separate temperature-rise CSV')}; its own timebase is retained, not absolute cell temperature.")
        else:
            lines += ["No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match."]
        linked_external = catalog.search_datasets(cell_id=cid)
        if linked_external:
            lines += ["", "### External full-cell datasets", "",
                      "These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.", ""]
            for dataset in linked_external:
                lines += ["- " + link(page, Path("data/full-cell") / (dataset["id"] + ".md"), dataset["title"])]
        if cell.get("supporting_files"):
            lines += ["", "### Additional study evidence", ""]
            for item in cell["supporting_files"]:
                lines.append(f"- {link(page, source_path(item['path']), 'Download CSV')}: {item['description']} License: {item['license']}.")
        lines += ["", "## Cell-level gaps", ""]
        lines += [f"- {item}" for item in cell["missing_items"]]
        lines += ["", "## Sources and reuse", ""]
        sources = set(cell["source_ids"])
        sources.update(t["source_id"] for t in tests)
        for sid in sorted(sources):
            source = catalog.sources[sid]
            lines.append(f"- [{source['title']}](<{source['url']}>) (`{sid}`)")
        lines += ["", "Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.", ""]
        output[str(page)] = "\n".join(lines).encode("utf-8")
        cell_rows.append((cid, cell, len(curves), len(parameters), len(tests)))

    def cells_table(page):
        lines = ["| Cell / study entry | OCP | Other parameters | Full-cell tests | Match level |",
                 "|---|---|---|---|---|"]
        for cid, cell, n_ocp, n_param, n_test in cell_rows:
            target = Path("data/cells") / f"{cid}.md"
            href = relative(page, target)
            ocp = f"[{n_ocp} records]({href}#ocp-curves)" if n_ocp else "Not linked"
            param = f"[{n_param} records]({href}#parameters)" if n_param else "Not imported"
            tests = f"[{n_test} {'file' if n_test == 1 else 'files'}]({href}#full-cell-tests)" if n_test else "Not imported"
            lines.append(f"| {link(page, target, cell['display_name'])} | {ocp} | {param} | {tests} | `{cell['match_level']}` |")
        return "\n".join(lines)

    page = Path("data/ocp/README.md")
    lines = ["# OCP data by material", "", "[All cells](../README.md) · [Download and use the data](../../docs/DATA_ACCESS.md)", "",
             "Every CSV link below is available from the repository without installing E-BatP. Retained tables preserve all stored points and source columns; generated samples contain 2,001 calculated points rounded to 12 significant digits and have `-sampled.csv` filenames. Read the adjacent JSON for original formulas, provenance, licensing and coordinate definitions.", "",
             "Material-level measurements are not automatically linked to a commercial cell. Whole-cell SOC, electrode stoichiometry, author model SOC/DOL and normalized branch capacity are different coordinates. Modeled OCPn and unresolved-reference half-cell voltage remain explicitly labeled.", ""]
    materials = sorted({curve.record["material"] for curve in catalog.search()}, key=lambda x: (x != "LFP", x.casefold()))
    for material in materials:
        lines += [f"## {material}", "", ocp_table(page, catalog.search(material=material)), ""]
    output[str(page)] = "\n".join(lines).encode("utf-8")

    page = Path("data/README.md")
    lines = ["# Browse and download the data", "",
             "Start here when browsing on GitHub. No Python installation or hosted website is required to find files.", "",
             "1. Choose a cell below, [browse OCP by material](ocp/README.md), or [find full-cell tests by material](full-cell/README.md).",
             "2. Open the linked **CSV** for data and **JSON** for definitions, source evidence and missing items.",
             "3. Use the file page's **Raw / download raw file** controls to save the complete file. GitHub previews may not display large files. Keep the metadata and source license with your copy.", "",
             "See [how to download, interpret and use files](../docs/DATA_ACCESS.md) for Excel, Python and model examples. If repository access is restricted, sign in with an account that has access.", "",
             f"Snapshot: {len(catalog.search())} OCP records, {len(catalog.parameters)} other parameter records, {len(catalog.full_cell_tests)} full-cell test files.", "",
             "## Choose a battery model", "", "[Battery model index: OCP, diffusion, kinetics and full-cell source coverage](batteries/README.md)", "",
             "## Native cell or study packages", "", cells_table(page), "",
             "## Find data by type", "",
             "| Need | Entry point |", "|---|---|",
             "| LFP or another material's OCP | [OCP index](ocp/README.md), with CSV and per-record JSON links |",
             "| Diffusion, kinetics, geometry, transport or thermal values | [Cell parameter CSV/JSON exports](parameters/); filter CSV by `name` / `category` and inspect `definition`, units, conditions and origin |",
             "| CC, multi-rate charging, US06/UDDS/WLTP, pulses or EIS | [Full-cell tests by material](full-cell/README.md), with external dataset links and existing packaged files |",
             "| Original Mohtat MATs and author files | [Packaged evidence](../src/ebp/data/evidence/) and [source audit](../docs/MOHTAT2020.md) |",
             "| Matching evidence and missing items | Cell pages above and the [matching audit](../src/ebp/data/matching_audit.json) |",
             "| Primary papers, datasets, versions and hashes | [Sources](../src/ebp/data/sources.json), [assets](../src/ebp/data/assets.json) and each export's metadata |", "",
             "## Where the files live", "",
             "`src/ebp/data/` is authoritative. This `data/` directory is a generated browsing view: parameter CSV/JSON exports, small formula samples, per-record OCP metadata and Markdown links. Large native OCP and full-cell observations are linked to their canonical files rather than duplicated.", "",
             "Paths inside JSON records are relative to `src/ebp/data/`; use each export's `canonical_data_root` when reading the export from a checkout. GitHub navigation does not change the observations, definitions or validation status.", "",
             "Maintainers: regenerate with `python scripts/build_data_index.py` after catalog updates. Check freshness with `python scripts/build_data_index.py --check`. Read [CONTRIBUTING.md](../CONTRIBUTING.md) before changing source data.", ""]
    output[str(page)] = "\n".join(lines).encode("utf-8")
    readme = (repo / "README.md").read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        raise ValueError("README data-navigation markers are missing")
    replacement = START + "\n\n" + model_table + "\n" + END
    output["README.md"] = re.sub(re.escape(START) + r".*?" + re.escape(END),
                                 lambda _: replacement, readme, flags=re.DOTALL).encode("utf-8")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render_index()
    stale = [name for name, value in expected.items()
             if not (REPO / name).exists() or (REPO / name).read_bytes() != value]
    extra = [str(p.relative_to(REPO)) for p in (REPO / "data").rglob("*")
             if p.is_file() and str(p.relative_to(REPO)) not in expected]
    if args.check:
        if stale or extra:
            parser.exit(1, "Stale data navigation; regenerate with python scripts/build_data_index.py.\n"
                        + "\n".join(stale + extra) + "\n")
        print(f"OK: {len(expected) - 1} generated data-navigation files and README links are current")
        return
    for name, value in expected.items():
        target = REPO / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_bytes() != value:
            target.write_bytes(value)
    if extra:
        parser.exit(1, "Obsolete generated files need review/removal:\n" + "\n".join(extra) + "\n")
    print(f"Generated {len(expected) - 1} data-navigation files and updated README links")


if __name__ == "__main__":
    main()
