# LFP 2.3 Ah | Prada2013 implementation | part unresolved

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `prada2013-lfp-nominal-design`. Match level: `parameter_set_only`.

One published implementation dictionary. Its LFP OCP is borrowed from Afshar2017 and negative OCP from Chen2020. No identified commercial cell or original same-study half-cell pair is established.

Do not infer A123 18650M1A, AMP20, 26650 m1b or the undisclosed BPX 2 Ah cell from chemistry/capacity; this is a separate nominal parameter set.

## Parameters

[All 50 parameter records (CSV)](../parameters/prada2013-lfp-nominal-design.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/prada2013-lfp-nominal-design.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

### Diffusion parameters

[3 diffusion records (CSV)](../parameters/prada2013-lfp-nominal-design--diffusion.csv)

Two source scalar solid diffusivities; no cell-specific measurement claim.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Kinetics parameters

[6 kinetics records (CSV)](../parameters/prada2013-lfp-nominal-design--kinetics.csv)

Two source exchange-current laws; original convention retained.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `prada2013-negative-borrowed-ocp` | negative / graphite | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/prada2013-negative-borrowed-ocp-sampled.csv) | [JSON](../ocp/prada2013-negative-borrowed-ocp.json) |
| `prada2013-positive-borrowed-ocp` | positive / LFP | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/prada2013-positive-borrowed-ocp-sampled.csv) | [JSON](../ocp/prada2013-positive-borrowed-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Commercial part number unresolved
- Matching full-cell charge/discharge observations not imported

## Sources and reuse

- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
