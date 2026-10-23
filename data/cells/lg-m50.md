# LG M50 | 5 Ah NMC811/graphite-SiOx

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `lg-m50`. Match level: `same_model_same_study`.

Parameters and full-cell tests are linked at same-model/same-study level. No exact characterization-specimen match or independently reproduced full-cell fit is claimed. This is an intentionally partial parameter collection.

Parameters and full-cell tests are linked at same-model/same-study level. No exact characterization-specimen match or independently reproduced full-cell fit is claimed. This is an intentionally partial parameter collection.

## Parameters

[All 38 parameter records (CSV)](../parameters/lg-m50.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/lg-m50.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `graphite-chen2020-formula` | negative / graphite | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/graphite-chen2020-formula-sampled.csv) | [JSON](../ocp/graphite-chen2020-formula.json) |
| `nmc811-lgm50-chen2020-formula` | positive / NMC811 | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/nmc811-lgm50-chen2020-formula-sampled.csv) | [JSON](../ocp/nmc811-lgm50-chen2020-formula.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `chen-lgm50-cell02` — CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description) | `time_s` | [CSV](../../src/ebp/data/full_cell/LGM50_cell02-normalized.csv) | [CSV](../../src/ebp/data/full_cell/LGM50_cell02.csv) | 6313 / 6313 / 6313 / 6313 of 6313 |
| `chen-lgm50-cell03` — CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description) | `time_s` | [CSV](../../src/ebp/data/full_cell/LGM50_cell03-normalized.csv) | [CSV](../../src/ebp/data/full_cell/LGM50_cell03.csv) | 6315 / 6315 / 6315 / 6315 of 6315 |
| `chen-lgm50-cell04` — CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description) | `time_s` | [CSV](../../src/ebp/data/full_cell/LGM50_cell04-normalized.csv) | [CSV](../../src/ebp/data/full_cell/LGM50_cell04.csv) | 6307 / 6307 / 6307 / 6307 of 6307 |

### Test gaps and extra channels

- `chen-lgm50-cell02`: No missing measurement channels recorded; specimen and validation limits still apply.
- `chen-lgm50-cell03`: No missing measurement channels recorded; specimen and validation limits still apply.
- `chen-lgm50-cell04`: No missing measurement channels recorded; specimen and validation limits still apply.

### External full-cell datasets

These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.

- [LG M50 multi-temperature discharge with explicitly reused Chen2020 electrode OCP](../full-cell/tec-lgm50-multitemperature-2021.md)

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed

## Sources and reuse

- [Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models](<https://doi.org/10.1149/1945-7111/ab9050>) (`chen-2020`)
- [Experimental data for "Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models"](<https://zenodo.org/records/4032561>) (`chen-validation-2020`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
