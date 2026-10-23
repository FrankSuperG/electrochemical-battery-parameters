"""Render the extraction inventory from native records and reviewed source gaps."""


def render(catalog):
    lines=["# OCP and parameter extraction audit — 2026-10-23", "",
        "[Battery model index](../data/batteries/README.md) · [Formats and storage](PARAMETER_STORAGE.md) · [O'Regan source review](OREGAN2022.md)", "",
        "This audit covers every current native cell/study entry, every external-only model group, and the remaining half-cell leads from the earlier source screen. It checks what is actually stored, source reuse scope, definitions, coordinate/units, and test associations. It is not a claim to have found every published measurement.", "",
        f"**Current inventory: {len(catalog.search())} electrode curve/fit records, {len(catalog.parameters):,} non-OCP records, {len(catalog.cells)} cell/study entries.** Counts include borrowed expressions, assumptions, activation energies and optional model inputs, not independent experiments. v0.14 adds seven first-party TUM pseudo-OCP branches; the four v0.13 additions remain reused expressions, not measured curves.", "",
        "## Native inventory by battery or study", "",
        "Every nonzero count below links to actual versioned repository data. A zero means no admitted native record; it does not prove that no measurement exists. A stored OCP can still be a fitted, borrowed or modeled quantity: inspect its measurement/origin fields.", "",
        "| Battery / study | Stored OCP | Diffusion | Kinetics | All non-OCP inputs | Key remaining limit |", "|---|---|---|---|---|---|"]
    limits={"lg-m50lt-hallemans2025":"OCP third-party reuse unresolved; stored diffusion/kinetics are grouped quantities, not intrinsic coefficients.",
        "a123-high-power-pouch-9ah":"Author parameter code/workbooks have no reuse grant established. Workbooks are whole-cell pseudo-OCV, not measured electrode OCP.",
        "a123-amp20m1hd-a":"No measured electrode OCP source established. Effective D depends on an assumed radius; kinetics include volumetric fitted quantities.",
        "lg-m50-oregan2022":"Three Cp tables quarantined. OCP reused from Chen2020; linked TEC/Chen full-cell tests are cross-study.",
        "prada2013-lfp-nominal-design":"Borrowed Afshar/Chen OCP; exact commercial identity and matching tests unresolved.",
        "molicel-p45b-aboutenergy2026":"Stored fitted BPX/author laws; TUM measurements are a separate study, without parameter transfer.",
        "molicel-p45b-tum-rehm2026":"Five harvested pseudo-OCP branches; half-cell temperature, absolute stoichiometry, exact donor and D/k unresolved.",
        "panasonic-ncr18650b-hnei2016":"Four native half-cell branches; no matched D/kinetics found. Other full-cell datasets share only the commercial model.",
        "calb-gen3b-nextbms2026":"Four half-cell branches; direction ambiguous. GITT/raw observations alone do not define a diffusivity table.",
        "isu-uconn-lfp-graphite-lab":"Four pseudo-OCP branches; no confirmed D/kinetics or commercial part. Missing channels stay missing.",
        "a123-18650m1a-jahn2024":"Stored OCPn is model-derived, not measured electrode equilibrium OCP. No intrinsic D/kinetics admitted."}
    for cid,cell in catalog.cells.items():
        params=[p for p in catalog.parameters if p["cell_id"]==cid]
        counts=[len(catalog.search(cell_id=cid))]+[sum(p["category"]==kind for p in params) for kind in ["diffusion","kinetics"]]
        links=[]
        for count,component in zip(counts,["ocp","diffusion","kinetics"]):
            target=f"../data/cells/{cid}.md#ocp-curves" if component=="ocp" else f"../data/parameters/{cid}--{component}.csv"
            links.append(f"[{count}]({target})" if count else "0 — not admitted")
        links.append(f"[{len(params)}](../data/parameters/{cid}.json)")
        limit=limits.get(cid,"Published implementation inputs include borrowed/default values; same-specimen attribution is not established. See source/variant fields and the model's gaps.")
        lines.append("| "+" | ".join([f"[{cell['display_name'].replace('|','&#124;')}](../data/batteries/{cid}.md)",*links,limit])+" |")
    lines += ["", "## Confirmed additions in v0.13", "",
        "- O'Regan LG M50: 55 experimental CSV tables (40 solid diffusivity, 8 i0, 4 entropic, 1 electronic and 2 thermal conductivity); 73 separate published model inputs and 2 explicitly reused Chen OCP expressions. Original source archive, metadata and code are preserved.",
        "- Seven pinned PyBaMM dictionaries: all non-OCP numeric/analytic entries are now represented, including optional model defaults. This adds 446 records, of which 50 belong to the separately named Prada2013 nominal LFP set. Prada adds two borrowed OCP expressions. Original cell identities and all prior values are preserved.",
        "- MIT BPX LFP example: 3 previously skipped electrolyte/entropy expressions, retained as reference-temperature laws with separate activation-energy inputs.",
        "- About:Energy P45B: 7 additional native records reconstruct the four user-defined electrolyte/thermodynamic laws, two phase-specific negative i0 laws and contact resistance. The author parser and helpers are pinned; zero selector flags and standard placeholder zeros are not physical measured parameters.", "",
        "## Source leads that remain external or quarantined", "",
        "| Source / files | Decision | Reason and required next evidence |", "|---|---|---|",
        "| [M50LT / Hallemans author source](HALLEMANS2025.md) | Reuse unresolved for OCP | About:Energy personal-communication tables remain third-party inputs. The author's software notice does not establish their original redistribution permission. Grouped parameter records are already native. |",
        "| [TUM first-party source admission](TUM_OCP_RIGHTS.md) | Seven native pseudo-OCP branches; remaining inputs held | Fixed MIT release 19555109, bundled notice, first-party folder attribution and original paper jointly support five P45B and two material-only graphite branches. Reconstructed silicon and third-party literature curves are excluded. |",
        "| [TUM HAIDI LFP/graphite, M35A and LG M36 leads](TUM_OCP_RIGHTS.md) | Source-specific reuse/definition checks incomplete | HAIDI dataset DOI resolves in DataCite but rightsList is empty; provider returned 429/timeouts. M35A/M36 original protocol/reference and study mapping remain unresolved. No dataset grant or direction is inferred from article access or filenames. |",
        "| [Oxford A123 9 Ah author parameters](https://github.com/Battery-Intelligence-Lab/pouch-cell-thermal/tree/83054d013b288f01e1afa2da7935e0a6a67c6bc6/data/param) | Reuse unresolved for parameter code/workbooks | Pinned tree has no LICENSE file. calculate_param.py contains model constants, but its definitions/permission cannot be inferred from the separate CC BY full-cell deposit. The OCP workbooks represent whole-cell pseudo-OCV; do not split them into measured half-cell curves. |",
        "| O'Regan three Specific_Heat_Capacity CSVs | Definition unresolved; quarantined | Header states J/kg/K, but some values are negative and the magnitude is inconsistent with physical Cp. Original bytes stay in the licensed archive; no native physical Cp table or undocumented rescaling. Published model Cp laws are separate records. |",
        "| [NEXTBMS GITT files](../data/full-cell/nextbms-calb-nmc532-2026.md) | Observation links only | A current/voltage/time GITT trace is not itself a defined D(sto,T) estimate. Electrode geometry, analysis definition and derived coefficients must be established before conversion. |",
        "| [Other candidates from the 21-family source screen](OCP_FIRST_EXPANSION.md) | Not admitted where primary data/reuse/identity is unresolved | Sordi2024 deposit is documentation-only; Sordi2026 matching payload unresolved; Folkson P45B is request-only; confidential 49 Ah LFP does not supply reusable public electrode data. These decisions remain qualified leads, not imported measurements. |", "",
        "## External-only full-cell groups", "",
        "These sources remain descriptions and links. No same-study, reusable electrode OCP/D/kinetics package has been established for the identities below. Whole-cell OCV, EIS and a shared chemistry do not fill that gap.", ""]
    assigned={r["id"] for r in catalog.external_datasets if r["parameter_link"]["cell_ids"]}
    assigned.add("tum-p45b-halfcell-aging-2026")
    for r in catalog.external_datasets:
        if r["id"] not in assigned:
            lines.append(f"- [{r['cell_identity']}](../data/full-cell/{r['id']}.md): {r['ocp_anchor']['kind']}; D/kinetics not matched. Per-source files, multi-temperature, dynamic, ageing and EIS coverage remain in the linked description.")
    lines += ["", "## Material-only curves and verification", "",
        "Two Rehm2026 laboratory graphite comparators are material-only and are not assigned to P45B. SINTEF already contributes 32 cycle-3 slow half-cell branches from 16 specimens across graphite, LFP, NMC111, NMC532, LNMO, silicon and silicon-graphite labels; these are native and are not merely links. Sample-level metadata and known-issue filters remain available. Other protocols/cycles are not silently counted as independent material curves, and no commercial full cell is assigned by material alone.", "",
        "Reconstruction runs offline against pinned source bytes; tests compare all newly admitted experimental rows and conversions, dictionary key coverage, model expressions across temperatures/concentrations, and BPX custom-law conventions. The runtime keeps bounded expressions and rejects out-of-domain table requests. No new full-cell observation payload is imported. See the release notes for executed verification results.", ""]
    return ("\n".join(lines)).encode()
