# LG M50 | O'Regan2022 characterization and model

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `lg-m50-oregan2022`. Match level: `same_model_same_study`.

Parameter tables and published model refer to LG M50. OCP functions are borrowed from Chen2020. TEC/Chen full-cell comparisons are separate studies; same serialized specimens are not established.

Do not merge experimental-table and published-model variants automatically; M50, M50T and M50LT are distinct identities.

## Parameters

[All 128 parameter records (CSV)](../parameters/lg-m50-oregan2022.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/lg-m50-oregan2022.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

**Choose one parameterization variant. Do not combine these alternatives. The all-record CSV is for inspection.**

| Variant | Records | CSV |
|---|---:|---|
| `oregan-experimental-tables` | 55 | [Download CSV](../parameters/lg-m50-oregan2022--oregan-experimental-tables.csv) |
| `oregan-pybamm-v25-4-2` | 73 | [Download CSV](../parameters/lg-m50-oregan2022--oregan-pybamm-v25-4-2.csv) |

### Diffusion parameters

[43 diffusion records (CSV)](../parameters/lg-m50-oregan2022--diffusion.csv)

40 experimental tables: two electrodes, two specimens, five temperatures, two directions; plus two separately labeled model laws and a borrowed electrolyte law.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Kinetics parameters

[14 kinetics records (CSV)](../parameters/lg-m50-oregan2022--kinetics.csv)

Eight experimental i0 tables at 15/25/35/45 C; two separate concentration/temperature model laws and source charge-transfer/double-layer inputs.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Native parameter tables

Linear interpolation is available only within each retained native domain. Source SOC and stoichiometry coordinates require explicit mapping before model use.

| Parameter | Native CSV | Axis / unit | Value unit | Variant |
|---|---|---|---|---|
| `oregan-data-electronic-conductivity-positive-electrode` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-electronic-conductivity-positive-electrode.csv) | T / K | S.m-1 | oregan-experimental-tables |
| `oregan-data-entropic-term-negative-electrode-cell-001` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-entropic-term-negative-electrode-cell-001.csv) | sto / 1 | V.K-1 | oregan-experimental-tables |
| `oregan-data-entropic-term-negative-electrode-cell-002` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-entropic-term-negative-electrode-cell-002.csv) | sto / 1 | V.K-1 | oregan-experimental-tables |
| `oregan-data-entropic-term-positive-electrode-cell-001` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-entropic-term-positive-electrode-cell-001.csv) | sto / 1 | V.K-1 | oregan-experimental-tables |
| `oregan-data-entropic-term-positive-electrode-cell-002` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-entropic-term-positive-electrode-cell-002.csv) | sto / 1 | V.K-1 | oregan-experimental-tables |
| `oregan-data-exchange-current-negative-electrode-15deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-negative-electrode-15deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-negative-electrode-25deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-negative-electrode-25deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-negative-electrode-35deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-negative-electrode-35deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-negative-electrode-45deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-negative-electrode-45deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-positive-electrode-15deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-positive-electrode-15deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-positive-electrode-25deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-positive-electrode-25deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-positive-electrode-35deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-positive-electrode-35deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-exchange-current-positive-electrode-45deg` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-exchange-current-positive-electrode-45deg.csv) | sto / 1 | A.m-2 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-15-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-15-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-15-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-15-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-25-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-25-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-25-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-25-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-35-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-35-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-35-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-35-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-45-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-45-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-45-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-45-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-5-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-5-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell001-5-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell001-5-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-15-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-15-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-15-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-15-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-25-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-25-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-25-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-25-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-35-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-35-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-35-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-35-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-45-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-45-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-45-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-45-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-5-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-5-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-negative-electrode-cell002-5-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-negative-electrode-cell002-5-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-15-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-15-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-15-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-15-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-25-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-25-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-25-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-25-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-35-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-35-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-35-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-35-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-45-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-45-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-45-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-45-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-5-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-5-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell001-5-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell001-5-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-15-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-15-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-15-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-15-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-25-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-25-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-25-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-25-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-35-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-35-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-35-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-35-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-45-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-45-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-45-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-45-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-5-degc-delit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-5-degc-delit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-diffusivity-positive-electrode-cell002-5-degc-lit` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-diffusivity-positive-electrode-cell002-5-degc-lit.csv) | sto / 1 | m2.s-1 | oregan-experimental-tables |
| `oregan-data-thermal-conductivity-negative-electrode` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-thermal-conductivity-negative-electrode.csv) | T / K | W.m-1.K-1 | oregan-experimental-tables |
| `oregan-data-thermal-conductivity-positive-electrode` | [Download CSV](../../src/ebp/data/parameter_tables/oregan-data-thermal-conductivity-positive-electrode.csv) | T / K | W.m-1.K-1 | oregan-experimental-tables |

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `oregan-model-negative-electrode-ocp-v` | negative / graphite | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/oregan-model-negative-electrode-ocp-v-sampled.csv) | [JSON](../ocp/oregan-model-negative-electrode-ocp-v.json) |
| `oregan-model-positive-electrode-ocp-v` | positive / NMC811 | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/oregan-model-positive-electrode-ocp-v-sampled.csv) | [JSON](../ocp/oregan-model-positive-electrode-ocp-v.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Matching full-cell charge/discharge observations not imported
- Three source Cp tables quarantined: physical definition/units unresolved
- Same-specimen full-cell mapping unresolved; linked comparisons are cross-study
- Original measured OCP points not deposited here; expressions are reused Chen2020 fits

## Sources and reuse

- [O'Regan thermal-electrochemical characterisation parameter tables](<https://zenodo.org/records/5171874>) (`oregan-2021-data`)
- [Thermal-electrochemical parameters of a high energy lithium-ion cylindrical battery](<https://doi.org/10.1016/j.electacta.2022.140700>) (`oregan-2022`)
- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
