# ISU-UConn | laboratory LFP/graphite CR2032 family

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `isu-uconn-lfp-graphite-lab`. Match level: `same_study_cell_family`.

Author notebook cells 6 and 8 use the selected LFP/graphite half-cell pair for eleven full-cell configurations in the same laboratory study. Shared MTI electrode family, not an identified commercial model or proven identical harvested specimen.

Only a documented subset is curated. The deposit describes 50 cells; retained branches and configuration labels are not independent studies or 50 imported specimens.

## Parameters

No non-OCP parameters imported for this entry. No placeholder parameter values are supplied.

[Cell package: OCP, tests, sources and missing items (JSON)](../parameters/isu-uconn-lfp-graphite-lab.json)

### Diffusion parameters

Not extracted for this cell/study.

### Kinetics parameters

Not extracted for this cell/study.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `isu-uconn-lfp-s2-b6-delithiation` | positive / LFP | pseudo_ocp / unresolved | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/isu-uconn-lfp-s2-b6-delithiation.csv) | [JSON](../ocp/isu-uconn-lfp-s2-b6-delithiation.json) |
| `isu-uconn-lfp-s2-b7-lithiation` | positive / LFP | pseudo_ocp / unresolved | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/isu-uconn-lfp-s2-b7-lithiation.csv) | [JSON](../ocp/isu-uconn-lfp-s2-b7-lithiation.json) |
| `isu-uconn-graphite-s2-b6-lithiation` | negative / graphite | pseudo_ocp / unresolved | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/isu-uconn-graphite-s2-b6-lithiation.csv) | [JSON](../ocp/isu-uconn-graphite-s2-b6-lithiation.json) |
| `isu-uconn-graphite-s2-b7-delithiation` | negative / graphite | pseudo_ocp / unresolved | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/isu-uconn-graphite-s2-b7-delithiation.csv) | [JSON](../ocp/isu-uconn-graphite-s2-b7-delithiation.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `isu-uconn-fresh-b6-charge` — fresh: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-fresh-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1107 / 0 of 1107 |
| `isu-uconn-fresh-b7-discharge` — fresh: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-fresh-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1098 / 0 of 1098 |
| `isu-uconn-lli-1-b6-charge` — lli-1: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lli-1-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1070 / 0 of 1070 |
| `isu-uconn-lli-1-b7-discharge` — lli-1: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lli-1-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1060 / 0 of 1060 |
| `isu-uconn-lli-2-b6-charge` — lli-2: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lli-2-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 950 / 0 of 950 |
| `isu-uconn-lli-2-b7-discharge` — lli-2: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lli-2-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 940 / 0 of 940 |
| `isu-uconn-lam-pe-1-b7-charge` — lam-pe-1: C/20 charge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-pe-1-b7-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1341 / 0 of 1341 |
| `isu-uconn-lam-pe-1-b8-discharge` — lam-pe-1: C/20 discharge capacity branch, source block 8; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-pe-1-b8-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1319 / 0 of 1319 |
| `isu-uconn-lam-ne-1-b6-charge` — lam-ne-1: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-ne-1-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1596 / 0 of 1596 |
| `isu-uconn-lam-ne-1-b7-discharge` — lam-ne-1: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-ne-1-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1545 / 0 of 1545 |
| `isu-uconn-lam-pe-lli-1-b0-charge` — lam-pe-lli-1: C/20 charge capacity branch, source block 0; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-pe-lli-1-b0-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1079 / 0 of 1079 |
| `isu-uconn-lam-pe-lli-2-b0-charge` — lam-pe-lli-2: C/20 charge capacity branch, source block 0; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-pe-lli-2-b0-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1045 / 0 of 1045 |
| `isu-uconn-lam-pe-lli-2-b1-discharge` — lam-pe-lli-2: C/20 discharge capacity branch, source block 1; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-pe-lli-2-b1-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1014 / 0 of 1014 |
| `isu-uconn-lam-ne-lli-1-b6-charge` — lam-ne-lli-1: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-ne-lli-1-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1551 / 0 of 1551 |
| `isu-uconn-lam-ne-lli-1-b7-discharge` — lam-ne-lli-1: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-ne-lli-1-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1499 / 0 of 1499 |
| `isu-uconn-lam-ne-lli-2-b6-charge` — lam-ne-lli-2: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-ne-lli-2-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1487 / 0 of 1487 |
| `isu-uconn-lam-ne-lli-2-b7-discharge` — lam-ne-lli-2: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-lam-ne-lli-2-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1451 / 0 of 1451 |
| `isu-uconn-all-mode-1-b6-charge` — all-mode-1: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-all-mode-1-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 1009 / 0 of 1009 |
| `isu-uconn-all-mode-1-b7-discharge` — all-mode-1: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-all-mode-1-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 998 / 0 of 998 |
| `isu-uconn-all-mode-2-b6-charge` — all-mode-2: C/20 charge capacity branch, source block 6; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-all-mode-2-b6-charge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 872 / 0 of 872 |
| `isu-uconn-all-mode-2-b7-discharge` — all-mode-2: C/20 discharge capacity branch, source block 7; constant-capacity tail retained | `passed_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/isu-uconn-all-mode-2-b7-discharge-normalized.csv) | [XLSX](../../src/ebp/data/evidence/isu-uconn-LFP_Data.xlsx) | 0 / 0 / 860 / 0 of 860 |

### Test gaps and extra channels

- `isu-uconn-fresh-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-fresh-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lli-1-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lli-1-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lli-2-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lli-2-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-pe-1-b7-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-pe-1-b8-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-ne-1-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-ne-1-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-pe-lli-1-b0-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-pe-lli-2-b0-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-pe-lli-2-b1-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-ne-lli-1-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-ne-lli-1-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-ne-lli-2-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-lam-ne-lli-2-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-all-mode-1-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-all-mode-1-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-all-mode-2-b6-charge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells
- `isu-uconn-all-mode-2-b7-discharge`: Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Instrument cycle/step identifiers; Measured current trace; Original timestamps; Same-specimen file-to-electrode provenance unresolved; Verified numeric temperature and reference details for associated half-cells

## Cell-level gaps

- Absolute measured cell/ambient temperature traces
- Commercial part number unresolved
- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Intrinsic reaction kinetics not imported
- Intrinsic solid diffusivity not imported
- Measured current and timestamps
- Verified reference chemistry and numerical temperature for selected half-cells

## Sources and reuse

- [REIL-UConn half-cell fitting notebook and loader](<https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics/tree/1188c371e5836df4a7e5f5acf336a34ffd4027e6>) (`isu-uconn-2026-code`)
- [ISU-UConn LFP/Graphite Emulated Degradation Dataset](<https://digitalcommons.lib.uconn.edu/reil_datasets/6/>) (`isu-uconn-2026-data`)
- [Benchmarking half-cell model fitting approaches for lithium-ion battery degradation diagnostics](<https://doi.org/10.1016/j.etran.2026.100593>) (`li-2026-benchmarking`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
