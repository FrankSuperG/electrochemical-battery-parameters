# LG MJ1 | DLR-SINTEF harvested-electrode characterization

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `lg-mj1-dlr-sintef`. Match level: `same_model_same_study`.

Explicit LG MJ1 model and common DLR/SINTEF collection. Direct characterization identifies harvested cell #001; fit records link to their GITT processing chain. No intact-cell validation specimen correspondence established.

No same-study intact MJ1 full-cell trace imported. Three-electrode GITT is electrode-versus-Li voltage, with a 260 um replacement separator; it is not an original commercial-cell validation trace. Do not combine all diffusion variants.

## Parameters

[Curation review: definitions, licensing and matching limits](../../docs/LG_MJ1.md)

[All 42 parameter records (CSV)](../parameters/lg-mj1-dlr-sintef.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/lg-mj1-dlr-sintef.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

**Choose one parameterization variant. Do not combine these alternatives. The all-record CSV is for inspection.**

| Variant | Records | CSV |
|---|---:|---|
| `direct-laboratory` | 30 | [Download CSV](../parameters/lg-mj1-dlr-sintef--direct-laboratory.csv) |
| `gitt-dfn-delithiation` | 2 | [Download CSV](../parameters/lg-mj1-dlr-sintef--gitt-dfn-delithiation.csv) |
| `gitt-dfn-lithiation` | 2 | [Download CSV](../parameters/lg-mj1-dlr-sintef--gitt-dfn-lithiation.csv) |
| `gitt-spm-delithiation` | 2 | [Download CSV](../parameters/lg-mj1-dlr-sintef--gitt-spm-delithiation.csv) |
| `gitt-spm-lithiation` | 2 | [Download CSV](../parameters/lg-mj1-dlr-sintef--gitt-spm-lithiation.csv) |
| `gitt-spme-delithiation` | 2 | [Download CSV](../parameters/lg-mj1-dlr-sintef--gitt-spme-delithiation.csv) |
| `gitt-spme-lithiation` | 2 | [Download CSV](../parameters/lg-mj1-dlr-sintef--gitt-spme-lithiation.csv) |

### Native parameter tables

Linear interpolation is available only within each retained native domain. Source SOC and stoichiometry coordinates require explicit mapping before model use.

| Parameter | Native CSV | Axis / unit | Value unit | Variant |
|---|---|---|---|---|
| `mj1-lab-negative-di-discharging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-negative-di-discharging.csv) | source_soc_percent / % | m2.s-1 | direct-laboratory |
| `mj1-lab-negative-di-charging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-negative-di-charging.csv) | source_soc_percent / % | m2.s-1 | direct-laboratory |
| `mj1-lab-positive-di-discharging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-positive-di-discharging.csv) | source_soc_percent / % | m2.s-1 | direct-laboratory |
| `mj1-lab-positive-di-charging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-positive-di-charging.csv) | source_soc_percent / % | m2.s-1 | direct-laboratory |
| `mj1-lab-negative-i0-discharging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-negative-i0-discharging.csv) | source_soc_percent / % | A.m-2 | direct-laboratory |
| `mj1-lab-negative-i0-charging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-negative-i0-charging.csv) | source_soc_percent / % | A.m-2 | direct-laboratory |
| `mj1-lab-positive-i0-discharging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-positive-i0-discharging.csv) | source_soc_percent / % | A.m-2 | direct-laboratory |
| `mj1-lab-positive-i0-charging` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-lab-positive-i0-charging.csv) | source_soc_percent / % | A.m-2 | direct-laboratory |
| `mj1-gitt-negative-spme-delithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-negative-spme-delithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spme-delithiation |
| `mj1-gitt-negative-dfn-delithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-negative-dfn-delithiation.csv) | source_sto / 1 | m2.s-1 | gitt-dfn-delithiation |
| `mj1-gitt-negative-spm-delithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-negative-spm-delithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spm-delithiation |
| `mj1-gitt-negative-spme-lithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-negative-spme-lithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spme-lithiation |
| `mj1-gitt-negative-dfn-lithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-negative-dfn-lithiation.csv) | source_sto / 1 | m2.s-1 | gitt-dfn-lithiation |
| `mj1-gitt-negative-spm-lithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-negative-spm-lithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spm-lithiation |
| `mj1-gitt-positive-spme-lithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-positive-spme-lithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spme-lithiation |
| `mj1-gitt-positive-spme-delithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-positive-spme-delithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spme-delithiation |
| `mj1-gitt-positive-dfn-lithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-positive-dfn-lithiation.csv) | source_sto / 1 | m2.s-1 | gitt-dfn-lithiation |
| `mj1-gitt-positive-spm-lithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-positive-spm-lithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spm-lithiation |
| `mj1-gitt-positive-dfn-delithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-positive-dfn-delithiation.csv) | source_sto / 1 | m2.s-1 | gitt-dfn-delithiation |
| `mj1-gitt-positive-spm-delithiation` | [Download CSV](../../src/ebp/data/parameter_tables/mj1-gitt-positive-spm-delithiation.csv) | source_sto / 1 | m2.s-1 | gitt-spm-delithiation |

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `mj1-negative-ocp-charging` | negative / Graphite-SiOx | pseudo_ocp / Li/Li+ | source_reported_stoichiometry; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/mj1-negative-ocp-charging.csv) | [JSON](../ocp/mj1-negative-ocp-charging.json) |
| `mj1-negative-ocp-discharging` | negative / Graphite-SiOx | pseudo_ocp / Li/Li+ | source_reported_stoichiometry; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/mj1-negative-ocp-discharging.csv) | [JSON](../ocp/mj1-negative-ocp-discharging.json) |
| `mj1-positive-ocp-charging` | positive / NMC | pseudo_ocp / Li/Li+ | source_reported_stoichiometry; [0.21, 1.0] | [Retained table](../../src/ebp/data/curves/mj1-positive-ocp-charging.csv) | [JSON](../ocp/mj1-positive-ocp-charging.json) |
| `mj1-positive-ocp-discharging` | positive / NMC | pseudo_ocp / Li/Li+ | source_reported_stoichiometry; [0.21, 1.0] | [Retained table](../../src/ebp/data/curves/mj1-positive-ocp-discharging.csv) | [JSON](../ocp/mj1-positive-ocp-discharging.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

## Cell-level gaps

- Exact specimen chain between direct cell #001, GITT electrodes and an intact validation cell unresolved
- Exchange-current active/geometric area convention not independently established
- Identical characterization/validation specimen not established
- Independent electrochemical model validation not performed
- Independent full-cell model reproduction not performed
- Matching full-cell charge/discharge observations not imported
- No same-study intact commercial MJ1 full-cell I/V/T validation series verified
- No standalone intact-cell constant-current charge/discharge observations imported
- Source SOC/stoichiometry coordinates need explicit balancing before model use

## Sources and reuse

- [Workflows and principles for collaboration and communication in battery research](<https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00247h>) (`kuhn-2026-workflows`)
- [INR18650-LG-3500-MJ1 Lithium-Ion Battery Cell Characterization Data](<https://zenodo.org/records/15407849>) (`mj1-zenodo-15407849`)
- [INR18650-LG-3500-MJ1 Lithium-Ion Battery Cell Complete Continuum Simulation Parameters](<https://zenodo.org/records/15496570>) (`mj1-zenodo-15496570`)
- [INR18650-LG-3500-MJ1 Lithium-Ion Battery Cell Direct Characterization Data](<https://zenodo.org/records/15497193>) (`mj1-zenodo-15497193`)
- [INR18650-LG-3500-MJ1 Anode GITT Structured Data](<https://zenodo.org/records/15520717>) (`mj1-zenodo-15520717`)
- [INR18650-LG-3500-MJ1 Anode GITT Parameters](<https://zenodo.org/records/15528177>) (`mj1-zenodo-15528177`)
- [INR18650-LG-3500-MJ1 Cathode GITT Parameters](<https://zenodo.org/records/15538164>) (`mj1-zenodo-15538164`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
