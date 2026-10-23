# Enertech | LCO/graphite | 2.28 Ah model input

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `enertech-lco-pouch-ai2020`. Match level: `same_study_cell_family`.

Enertech observations and Ai2020 implementation share the Ai/Rieger study family. Exact commercial model and specimen remain unresolved; borrowed electrode functions do not become measurements through this link.

OCP tables have Ai/Rieger attribution. Diffusivity and kinetics functions explicitly use Dualfoil. Separate temperature-rise files are not merged into absolute temperature or assumed synchronized with voltage.

## Parameters

[All 38 parameter records (CSV)](../parameters/enertech-lco-pouch-ai2020.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/enertech-lco-pouch-ai2020.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

### Diffusion parameters

[2 diffusion records (CSV)](../parameters/enertech-lco-pouch-ai2020--diffusion.csv)

Two borrowed Dualfoil Arrhenius diffusivity functions; not same-cell measured D

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Kinetics parameters

[2 kinetics records (CSV)](../parameters/enertech-lco-pouch-ai2020--kinetics.csv)

Two borrowed Dualfoil exchange-current laws; not same-cell measured kinetics

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `ai2020-graphite-ocp` | negative / graphite | literature_table / Li/Li+ | stoichiometry; [0.0005, 1.0] | [Retained table](../../src/ebp/data/curves/ai2020-graphite-ocp.csv) | [JSON](../ocp/ai2020-graphite-ocp.json) |
| `ai2020-lco-ocp` | positive / LCO | literature_table / Li/Li+ | stoichiometry; [0.4, 0.998903136] | [Retained table](../../src/ebp/data/curves/ai2020-lco-ocp.csv) | [JSON](../ocp/ai2020-lco-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `enertech-0p1c-discharge` — 0.1C constant-current discharge; Enertech beginning-of-life observations | `time_s` | [CSV](../../src/ebp/data/full_cell/enertech-0p1c-discharge-normalized.csv) | [TXT](../../src/ebp/data/evidence/0.1C_discharge_U.txt) | 36880 / 0 / 36880 / 0 of 36880 |
| `enertech-0p5c-discharge` — 0.5C constant-current discharge; Enertech beginning-of-life observations | `time_s` | [CSV](../../src/ebp/data/full_cell/enertech-0p5c-discharge-normalized.csv) | [TXT](../../src/ebp/data/evidence/0.5C_discharge_U.txt) | 7310 / 0 / 7310 / 0 of 7310 |
| `enertech-1c-discharge` — 1C constant-current discharge; Enertech beginning-of-life observations | `time_s` | [CSV](../../src/ebp/data/full_cell/enertech-1c-discharge-normalized.csv) | [TXT](../../src/ebp/data/evidence/1C_discharge_U.txt) | 3615 / 0 / 3615 / 0 of 3615 |
| `enertech-2c-discharge` — 2C constant-current discharge; Enertech beginning-of-life observations | `time_s` | [CSV](../../src/ebp/data/full_cell/enertech-2c-discharge-normalized.csv) | [TXT](../../src/ebp/data/evidence/2C_discharge_U.txt) | 1773 / 0 / 1773 / 0 of 1773 |

### Test gaps and extra channels

- `enertech-0p1c-discharge`: Absolute measured temperature; Ambient temperature trace; Capacity channel; Charge trace; Exact specimen identifier; Measured current trace
- `enertech-0p5c-discharge`: Absolute measured temperature; Ambient temperature trace; Capacity channel; Charge trace; Exact specimen identifier; Measured current trace
  - [Separate temperature-rise CSV](../../src/ebp/data/full_cell/enertech-0p5c-discharge-temperature-rise.csv); its own timebase is retained, not absolute cell temperature.
- `enertech-1c-discharge`: Absolute measured temperature; Ambient temperature trace; Capacity channel; Charge trace; Exact specimen identifier; Measured current trace
  - [Separate temperature-rise CSV](../../src/ebp/data/full_cell/enertech-1c-discharge-temperature-rise.csv); its own timebase is retained, not absolute cell temperature.
- `enertech-2c-discharge`: Absolute measured temperature; Ambient temperature trace; Capacity channel; Charge trace; Exact specimen identifier; Measured current trace
  - [Separate temperature-rise CSV](../../src/ebp/data/full_cell/enertech-2c-discharge-temperature-rise.csv); its own timebase is retained, not absolute cell temperature.

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Commercial part number unresolved

## Sources and reuse

- [Electrochemical Thermal-Mechanical Modelling of Stress Inhomogeneity in Lithium-Ion Pouch Cells](<https://doi.org/10.1149/2.0122001JES>) (`ai-2020`)
- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)
- [PyBaMM experimental data release v1.0.2](<https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2>) (`pybamm-data-1-0-2`)
- [A new method to model the thickness change of a commercial pouch cell during discharge](<https://doi.org/10.1149/2.0441608jes>) (`rieger-2016`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
