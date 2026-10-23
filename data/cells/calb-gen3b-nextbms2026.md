# CALB generation 3b | NEXTBMS2026

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `calb-gen3b-nextbms2026`. Match level: `same_model_same_study`.

Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.

Other studies sharing a model name are separate sources, not a single measured parameter set.

## Parameters

No non-OCP parameters imported for this entry. No placeholder parameter values are supplied.

[Cell package: OCP, tests, sources and missing items (JSON)](../parameters/calb-gen3b-nextbms2026.json)

### Diffusion parameters

Not extracted for this cell/study.

### Kinetics parameters

Not extracted for this cell/study.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `nextbms-calb-negative-charge` | negative / graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/nextbms-calb-negative-charge.csv) | [JSON](../ocp/nextbms-calb-negative-charge.json) |
| `nextbms-calb-negative-discharge` | negative / graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/nextbms-calb-negative-discharge.csv) | [JSON](../ocp/nextbms-calb-negative-discharge.json) |
| `nextbms-calb-positive-charge` | positive / NMC532 | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/nextbms-calb-positive-charge.csv) | [JSON](../ocp/nextbms-calb-positive-charge.json) |
| `nextbms-calb-positive-discharge` | positive / NMC532 | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/nextbms-calb-positive-discharge.csv) | [JSON](../ocp/nextbms-calb-positive-discharge.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

### External full-cell datasets

These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.

- [CALB generation 3b 58 Ah: harvested half-cell OCP, multi-temperature tests and ageing](../full-cell/nextbms-calb-nmc532-2026.md)

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Commercial part number unresolved
- Matching full-cell charge/discharge observations not imported
- Half-cell measurement temperature and identical donor/full-cell serial mapping unresolved

## Sources and reuse

- [NEXTBMS CALB generation 3b NMC532 half-cell and full-cell dataset](<https://zenodo.org/records/22301764>) (`nextbms-calb-2026-data`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
