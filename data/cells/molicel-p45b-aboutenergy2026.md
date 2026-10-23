# Molicel P45B | About:Energy2026 BPX

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `molicel-p45b-aboutenergy2026`. Match level: `same_model_same_study`.

Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.

Other studies sharing a model name are separate sources, not a single measured parameter set.

## Parameters

[All 67 parameter records (CSV)](../parameters/molicel-p45b-aboutenergy2026.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/molicel-p45b-aboutenergy2026.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

### Diffusion parameters

[7 diffusion records (CSV)](../parameters/molicel-p45b-aboutenergy2026--diffusion.csv)

Three phase-specific D inputs and three activation energies in BPX.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Kinetics parameters

[8 kinetics records (CSV)](../parameters/molicel-p45b-aboutenergy2026--kinetics.csv)

BPX-native reaction coefficients/activation energies and two author-defined negative-phase i0 laws with explicitly checked F*k and modifier convention.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Native parameter tables

Linear interpolation is available only within each retained native domain. Source SOC and stoichiometry coordinates require explicit mapping before model use.

| Parameter | Native CSV | Axis / unit | Value unit | Variant |
|---|---|---|---|---|
| `aepy-p45b-parameterisation-negative-electrode-particle-graphite-entropic-change-coefficient-v-k-1` | [Download CSV](../../src/ebp/data/parameter_tables/aepy-p45b-parameterisation-negative-electrode-particle-graphite-entropic-change-coefficient-v-k-1.csv) | sto / 1 | V.K-1 | aepy-bpx-1.1-dfn |
| `aepy-p45b-parameterisation-negative-electrode-particle-silicon-additive-entropic-change-coefficient-v-k-1` | [Download CSV](../../src/ebp/data/parameter_tables/aepy-p45b-parameterisation-negative-electrode-particle-silicon-additive-entropic-change-coefficient-v-k-1.csv) | sto / 1 | V.K-1 | aepy-bpx-1.1-dfn |

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `aepy-p45b-negative-graphite-ocp-v` | negative / graphite | literature_table / Li/Li+ | source_reported_stoichiometry; [0.0011125213468379, 0.880643398272419] | [Retained table](../../src/ebp/data/curves/aepy-p45b-negative-graphite-ocp-v.csv) | [JSON](../ocp/aepy-p45b-negative-graphite-ocp-v.json) |
| `aepy-p45b-negative-silicon-ocp-v` | negative / silicon | literature_table / Li/Li+ | source_reported_stoichiometry; [0.054504455, 0.840496595] | [Retained table](../../src/ebp/data/curves/aepy-p45b-negative-silicon-ocp-v.csv) | [JSON](../ocp/aepy-p45b-negative-silicon-ocp-v.json) |
| `aepy-p45b-negative-silicon-ocp-delithiation-v` | negative / silicon | literature_table / Li/Li+ | source_reported_stoichiometry; [0.0545609206432044, 0.84] | [Retained table](../../src/ebp/data/curves/aepy-p45b-negative-silicon-ocp-delithiation-v.csv) | [JSON](../ocp/aepy-p45b-negative-silicon-ocp-delithiation-v.json) |
| `aepy-p45b-negative-silicon-ocp-lithiation-v` | negative / silicon | literature_table / Li/Li+ | source_reported_stoichiometry; [0.0547977268563917, 0.84] | [Retained table](../../src/ebp/data/curves/aepy-p45b-negative-silicon-ocp-lithiation-v.csv) | [JSON](../ocp/aepy-p45b-negative-silicon-ocp-lithiation-v.json) |
| `aepy-p45b-positive-nca-ocp-v` | positive / NCA | literature_table / Li/Li+ | source_reported_stoichiometry; [0.216085984349077, 0.935944628026975] | [Retained table](../../src/ebp/data/curves/aepy-p45b-positive-nca-ocp-v.csv) | [JSON](../ocp/aepy-p45b-positive-nca-ocp-v.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

### External full-cell datasets

These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.

- [Molicel P45B: published DFN OCP/parameters and multi-temperature CC, WLTP and eVTOL](../full-cell/aboutenergy-p45b-2026.md)

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Matching full-cell charge/discharge observations not imported
- Half-cell measurement temperature and identical donor/full-cell serial mapping unresolved

## Sources and reuse

- [About:Energy Molicel P45B BPX 1.1 parameterisation](<https://github.com/About-Energy-OpenSource/AEPyBaMM/tree/188bd62ee2347cc486b66dc43e31fb9597759db1>) (`aepy-p45b-2026`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
