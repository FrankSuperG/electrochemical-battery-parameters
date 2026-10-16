# UMBL Mohtat2020 | 5 Ah NMC/graphite research pouch

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `mohtat2020-nmc532-pouch`. Match level: `same_study_cell_family`.

Original author model is bundled with these five experimental charging files in the same DOI deposit. Cell is fabricated by UMBL, not an identified commercial part. Exact specimen identity is not given.

Custom laboratory pouch. NMC532 label follows the PyBaMM implementation, not a composition assay in this deposit. Author and PyBaMM graphite OCP offsets, thermal geometry and temperature laws differ. Capacity-axis charge files have measured voltage/temperature but no exported current/time. Source Cover2 rate description conflicts are retained.

## Parameters

[All 71 parameter records (CSV)](../parameters/mohtat2020-nmc532-pouch.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/mohtat2020-nmc532-pouch.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

**Choose one parameterization variant. Do not combine these alternatives. The all-record CSV is for inspection.**

| Variant | Records | CSV |
|---|---:|---|
| `original_author_mpm` | 33 | [Download CSV](../parameters/mohtat2020-nmc532-pouch--original_author_mpm.csv) |
| `pybamm_v25_4_2` | 38 | [Download CSV](../parameters/mohtat2020-nmc532-pouch--pybamm_v25_4_2.csv) |

## OCP curves

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `mohtat2020-graphite-ocp` | negative / graphite | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/mohtat2020-graphite-ocp-sampled.csv) | [JSON](../ocp/mohtat2020-graphite-ocp.json) |
| `mohtat2020-nmc532-ocp` | positive / NMC532 | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/mohtat2020-nmc532-ocp-sampled.csv) | [JSON](../ocp/mohtat2020-nmc532-ocp.json) |
| `mohtat-author-graphite-ocp` | negative / graphite | stoichiometry; [0.0017, 0.8332] | [Generated samples](../ocp/mohtat-author-graphite-ocp-sampled.csv) | [JSON](../ocp/mohtat-author-graphite-ocp.json) |
| `mohtat-author-nmc532-ocp` | positive / NMC532 | stoichiometry; [0.0335, 0.8907] | [Generated samples](../ocp/mohtat-author-nmc532-ocp-sampled.csv) | [JSON](../ocp/mohtat-author-nmc532-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `mohtat-charge-0p1c` — Nominal 0.1C charge to 4.2 V; capacity-coordinate experimental export | `charge_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/mohtat-charge-0p1c-normalized.csv) | [MAT](../../src/ebp/data/evidence/mohtat2020-Cover10.mat) | 0 / 0 / 3561 / 3561 of 3561 |
| `mohtat-charge-0p2c` — Nominal 0.2C charge to 4.2 V; capacity-coordinate experimental export | `charge_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/mohtat-charge-0p2c-normalized.csv) | [MAT](../../src/ebp/data/evidence/mohtat2020-Cover5.mat) | 0 / 0 / 1745 / 1745 of 1745 |
| `mohtat-charge-0p5c` — Nominal 0.5C charge to 4.2 V; capacity-coordinate experimental export | `charge_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/mohtat-charge-0p5c-normalized.csv) | [MAT](../../src/ebp/data/evidence/mohtat2020-Cover2.mat) | 0 / 0 / 682 / 682 of 682 |
| `mohtat-charge-1c` — Nominal 1C charge to 4.2 V; capacity-coordinate experimental export | `charge_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/mohtat-charge-1c-normalized.csv) | [MAT](../../src/ebp/data/evidence/mohtat2020-Cover1.mat) | 0 / 0 / 330 / 330 of 330 |
| `mohtat-charge-2c` — Nominal 2C charge to 4.2 V; capacity-coordinate experimental export | `charge_capacity_Ah` | [CSV](../../src/ebp/data/full_cell/mohtat-charge-2c-normalized.csv) | [MAT](../../src/ebp/data/evidence/mohtat2020-2C.mat) | 0 / 0 / 156 / 156 of 156 |

### Test gaps and extra channels

- `mohtat-charge-0p1c`: Ambient temperature trace; C/20 OCV test; Discharge trace; Exact specimen identifier; Full CV/rest trace; Measured current trace; Original half-cell OCP points; Original timestamps
- `mohtat-charge-0p2c`: Ambient temperature trace; C/20 OCV test; Discharge trace; Exact specimen identifier; Full CV/rest trace; Measured current trace; Original half-cell OCP points; Original timestamps
- `mohtat-charge-0p5c`: Ambient temperature trace; C/20 OCV test; Discharge trace; Exact specimen identifier; Full CV/rest trace; Measured current trace; Original half-cell OCP points; Original timestamps
- `mohtat-charge-1c`: Ambient temperature trace; C/20 OCV test; Discharge trace; Exact specimen identifier; Full CV/rest trace; Measured current trace; Original half-cell OCP points; Original timestamps
- `mohtat-charge-2c`: Ambient temperature trace; C/20 OCV test; Discharge trace; Exact specimen identifier; Full CV/rest trace; Measured current trace; Original half-cell OCP points; Original timestamps

## Cell-level gaps

- Exact specimen identifier
- Measured current trace
- Original timestamps
- Discharge/CV/rest and C/20 files
- Raw electrode OCP points
- Independent full-cell model reproduction

## Sources and reuse

- [Differential Expansion and Voltage Model for Li-ion Batteries at Practical Charging Rates](<https://doi.org/10.1149/1945-7111/aba5d1>) (`mohtat-2020`)
- [UofM pouch cell voltage and expansion dataset and modeling code](<https://deepblue.lib.umich.edu/data/concern/data_sets/kp78gg60j>) (`mohtat-2020-data`)
- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
