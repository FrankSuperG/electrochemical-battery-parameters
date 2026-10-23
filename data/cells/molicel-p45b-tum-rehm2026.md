# Molicel P45B | TUM Rehm2026 measured half-cells

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `molicel-p45b-tum-rehm2026`. Match level: `same_model_same_study`.

Five harvested P45B half-cell branches and external serial23 checkups share paper/model; exact donor/serial identity unresolved. About:Energy P45B parameters are a separate study.

Laboratory graphite comparator is material-only; reconstructed silicon is not a measured pure-material half cell.

## Parameters

No non-OCP parameters imported for this entry. No placeholder parameter values are supplied.

[Cell package: OCP, tests, sources and missing items (JSON)](../parameters/molicel-p45b-tum-rehm2026.json)

### Diffusion parameters

Not extracted for this cell/study.

### Kinetics parameters

Not extracted for this cell/study.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `tum-rehm2026-p45b-cathode-delithiation-0c03` | positive / NCA | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/tum-rehm2026-p45b-cathode-delithiation-0c03.csv) | [JSON](../ocp/tum-rehm2026-p45b-cathode-delithiation-0c03.json) |
| `tum-rehm2026-p45b-anode-delithiation-0c02` | negative / silicon-graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/tum-rehm2026-p45b-anode-delithiation-0c02.csv) | [JSON](../ocp/tum-rehm2026-p45b-anode-delithiation-0c02.json) |
| `tum-rehm2026-p45b-anode-delithiation-0c03` | negative / silicon-graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/tum-rehm2026-p45b-anode-delithiation-0c03.csv) | [JSON](../ocp/tum-rehm2026-p45b-anode-delithiation-0c03.json) |
| `tum-rehm2026-p45b-anode-lithiation-0c02` | negative / silicon-graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/tum-rehm2026-p45b-anode-lithiation-0c02.csv) | [JSON](../ocp/tum-rehm2026-p45b-anode-lithiation-0c02.json) |
| `tum-rehm2026-p45b-anode-lithiation-0c03` | negative / silicon-graphite | pseudo_ocp / Li/Li+ | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/tum-rehm2026-p45b-anode-lithiation-0c03.csv) | [JSON](../ocp/tum-rehm2026-p45b-anode-lithiation-0c03.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

### External full-cell datasets

These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.

- [Molicel P45B harvested half-cell curves and 800-EFC checkup pseudo-OCV](../full-cell/tum-p45b-halfcell-aging-2026.md)

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Matching full-cell charge/discharge observations not imported
- Exact harvested donor to serial23 mapping unresolved
- Numeric half-cell temperature not established
- Absolute half-cell capacity and stoichiometric balancing not supplied
- Same-study intrinsic D and kinetic coefficients not located
- 0C03 filename rate is 0.03C; original paper protocol states 0.033C
- Full-cell tests are external links; 25 C is a paper condition, not a verified measured temperature channel

## Sources and reuse

- [How to determine the degradation modes of lithium-ion batteries with silicon-graphite blend electrodes](<https://doi.org/10.1016/j.jpowsour.2026.239418>) (`rehm-2026`)
- [First-party Rehm2026 half-cell tables bundled with DegradationModeAnalysis v2.0.0](<https://zenodo.org/records/19555109>) (`tum-rehm2026-v2`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
