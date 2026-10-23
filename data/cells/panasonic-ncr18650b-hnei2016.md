# Panasonic NCR18650B | HNEI2016

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `panasonic-ncr18650b-hnei2016`. Match level: `same_model_same_study`.

Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.

Other studies sharing a model name are separate sources, not a single measured parameter set.

## Parameters

No non-OCP parameters imported for this entry. No placeholder parameter values are supplied.

[Cell package: OCP, tests, sources and missing items (JSON)](../parameters/panasonic-ncr18650b-hnei2016.json)

### Diffusion parameters

Not extracted for this cell/study.

### Kinetics parameters

Not extracted for this cell/study.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `hnei-ncr18650b-ne-lithiation` | negative / graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [-0.0, 1.0] | [Retained table](../../src/ebp/data/curves/hnei-ncr18650b-ne-lithiation.csv) | [JSON](../ocp/hnei-ncr18650b-ne-lithiation.json) |
| `hnei-ncr18650b-ne-delithiation` | negative / graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/hnei-ncr18650b-ne-delithiation.csv) | [JSON](../ocp/hnei-ncr18650b-ne-delithiation.json) |
| `hnei-ncr18650b-pe-lithiation` | positive / NCA | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [-0.0, 1.0] | [Retained table](../../src/ebp/data/curves/hnei-ncr18650b-pe-lithiation.csv) | [JSON](../ocp/hnei-ncr18650b-pe-lithiation.json) |
| `hnei-ncr18650b-pe-delithiation` | positive / NCA | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/hnei-ncr18650b-pe-delithiation.csv) | [JSON](../ocp/hnei-ncr18650b-pe-delithiation.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

### External full-cell datasets

These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.

- [Panasonic NCR18650B formation, full-cell RPT and harvested half-cell tests](../full-cell/hnei-ncr18650b-2016.md)
- [Panasonic NCR18650B beginning-of-life pseudo-OCV, pulses and EIS (92 cells)](../full-cell/bayreuth-ncr18650b-2023.md)
- [Panasonic NCR18650B ageing and repeated reference tests (116 cells)](../full-cell/virtual-vehicle-ncr18650b-aging-2023.md)
- [Panasonic NCR18650B multi-rate discharge and surface-temperature data](../full-cell/stanford-ncr18650b-rates-2021.md)

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Matching full-cell charge/discharge observations not imported
- Half-cell measurement temperature and identical donor/full-cell serial mapping unresolved

## Sources and reuse

- [Panasonic NCR18650B formation, RPT and half cell data set](<https://zenodo.org/records/60232>) (`hnei-ncr-2016-data`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
