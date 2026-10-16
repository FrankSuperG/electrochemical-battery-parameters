# Undisclosed LFP/graphite 18650, 2 Ah (BPX)

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `bpx-lfp-18650-2ah-undisclosed`. Match level: `unmatched`.

The example title specifies chemistry, capacity and format only. No raw tests can be assigned to an exact commercial model.

Do not match this example to another 2 Ah LFP cell using nominal capacity alone.

## Parameters

[All 46 parameter records (CSV)](../parameters/bpx-lfp-18650-2ah-undisclosed.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/bpx-lfp-18650-2ah-undisclosed.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

## OCP curves

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `bpx-lfp18650-lfp-ocp` | positive / LFP | stoichiometry; [0.0875, 0.95038] | [Generated samples](../ocp/bpx-lfp18650-lfp-ocp-sampled.csv) | [JSON](../ocp/bpx-lfp18650-lfp-ocp.json) |
| `bpx-lfp18650-graphite-ocp` | negative / graphite | stoichiometry; [0.0016261, 0.82258] | [Generated samples](../ocp/bpx-lfp18650-graphite-ocp-sampled.csv) | [JSON](../ocp/bpx-lfp18650-graphite-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Commercial part number unresolved
- Matching full-cell charge/discharge observations not imported

## Sources and reuse

- [BPX LFP/graphite 2 Ah 18650 example](<https://raw.githubusercontent.com/FaradayInstitution/BPX/0f591336937c2c57509f20ab23f9908e58f7a757/examples/lfp_18650_cell_BPX.json>) (`bpx-lfp-2022`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
