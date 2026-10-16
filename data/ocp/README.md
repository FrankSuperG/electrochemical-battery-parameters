# OCP data by material

[All cells](../README.md) · [Download and use the data](../../docs/DATA_ACCESS.md)

Every CSV link below is available from the repository without installing E-BatP. Retained tables preserve all stored points and source columns; generated samples contain 2,001 calculated points rounded to 12 significant digits and have `-sampled.csv` filenames. Read the adjacent JSON for original formulas, provenance, licensing and coordinate definitions.

Material-level measurements are not automatically linked to a commercial cell. Whole-cell SOC, electrode stoichiometry and normalized branch capacity are different coordinates.

## LFP

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `lfp-afshar2017-formula` | positive / LFP | stoichiometry; [0.0, 1.0] | [Generated samples](lfp-afshar2017-formula-sampled.csv) | [JSON](lfp-afshar2017-formula.json) |
| `sintef-lfp-d07eb6-c3-delithiation` | positive / LFP | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lfp-d07eb6-c3-delithiation.csv) | [JSON](sintef-lfp-d07eb6-c3-delithiation.json) |
| `sintef-lfp-d07eb6-c3-lithiation` | positive / LFP | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lfp-d07eb6-c3-lithiation.csv) | [JSON](sintef-lfp-d07eb6-c3-lithiation.json) |
| `sintef-lfp-178617-c3-delithiation` | positive / LFP | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lfp-178617-c3-delithiation.csv) | [JSON](sintef-lfp-178617-c3-delithiation.json) |
| `sintef-lfp-178617-c3-lithiation` | positive / LFP | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lfp-178617-c3-lithiation.csv) | [JSON](sintef-lfp-178617-c3-lithiation.json) |
| `bpx-lfp18650-lfp-ocp` | positive / LFP | stoichiometry; [0.0875, 0.95038] | [Generated samples](bpx-lfp18650-lfp-ocp-sampled.csv) | [JSON](bpx-lfp18650-lfp-ocp.json) |

## graphite

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `graphite-chen2020-formula` | negative / graphite | stoichiometry; [0.0, 1.0] | [Generated samples](graphite-chen2020-formula-sampled.csv) | [JSON](graphite-chen2020-formula.json) |
| `sintef-graphite-1d5628-c3-lithiation` | negative / graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-graphite-1d5628-c3-lithiation.csv) | [JSON](sintef-graphite-1d5628-c3-lithiation.json) |
| `sintef-graphite-1d5628-c3-delithiation` | negative / graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-graphite-1d5628-c3-delithiation.csv) | [JSON](sintef-graphite-1d5628-c3-delithiation.json) |
| `sintef-graphite-4ccc47-c3-lithiation` | negative / graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-graphite-4ccc47-c3-lithiation.csv) | [JSON](sintef-graphite-4ccc47-c3-lithiation.json) |
| `sintef-graphite-4ccc47-c3-delithiation` | negative / graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-graphite-4ccc47-c3-delithiation.csv) | [JSON](sintef-graphite-4ccc47-c3-delithiation.json) |
| `bpx-lfp18650-graphite-ocp` | negative / graphite | stoichiometry; [0.0016261, 0.82258] | [Generated samples](bpx-lfp18650-graphite-ocp-sampled.csv) | [JSON](bpx-lfp18650-graphite-ocp.json) |
| `marquis2019-graphite-ocp` | negative / graphite | stoichiometry; [0.0, 1.0] | [Generated samples](marquis2019-graphite-ocp-sampled.csv) | [JSON](marquis2019-graphite-ocp.json) |
| `mohtat2020-graphite-ocp` | negative / graphite | stoichiometry; [0.0, 1.0] | [Generated samples](mohtat2020-graphite-ocp-sampled.csv) | [JSON](mohtat2020-graphite-ocp.json) |
| `nca-kim2011-graphite-ocp` | negative / graphite | stoichiometry; [0.0, 1.0] | [Generated samples](nca-kim2011-graphite-ocp-sampled.csv) | [JSON](nca-kim2011-graphite-ocp.json) |
| `ecker2015-graphite-ocp` | negative / graphite | stoichiometry; [0.0, 1.0] | [Generated samples](ecker2015-graphite-ocp-sampled.csv) | [JSON](ecker2015-graphite-ocp.json) |
| `ai2020-graphite-ocp` | negative / graphite | stoichiometry; [0.0005, 1.0] | [Retained table](../../src/ebp/data/curves/ai2020-graphite-ocp.csv) | [JSON](ai2020-graphite-ocp.json) |
| `mohtat-author-graphite-ocp` | negative / graphite | stoichiometry; [0.0017, 0.8332] | [Generated samples](mohtat-author-graphite-ocp-sampled.csv) | [JSON](mohtat-author-graphite-ocp.json) |

## LCO

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `marquis2019-lco-ocp` | positive / LCO | stoichiometry; [0.0, 1.0] | [Generated samples](marquis2019-lco-ocp-sampled.csv) | [JSON](marquis2019-lco-ocp.json) |
| `ai2020-lco-ocp` | positive / LCO | stoichiometry; [0.4, 0.998903136] | [Retained table](../../src/ebp/data/curves/ai2020-lco-ocp.csv) | [JSON](ai2020-lco-ocp.json) |

## LNMO

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `sintef-lnmo-59ceaa-c3-delithiation` | positive / LNMO | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lnmo-59ceaa-c3-delithiation.csv) | [JSON](sintef-lnmo-59ceaa-c3-delithiation.json) |
| `sintef-lnmo-59ceaa-c3-lithiation` | positive / LNMO | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lnmo-59ceaa-c3-lithiation.csv) | [JSON](sintef-lnmo-59ceaa-c3-lithiation.json) |
| `sintef-lnmo-f9bf3e-c3-delithiation` | positive / LNMO | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lnmo-f9bf3e-c3-delithiation.csv) | [JSON](sintef-lnmo-f9bf3e-c3-delithiation.json) |
| `sintef-lnmo-f9bf3e-c3-lithiation` | positive / LNMO | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-lnmo-f9bf3e-c3-lithiation.csv) | [JSON](sintef-lnmo-f9bf3e-c3-lithiation.json) |

## NCA

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `nca-kim2011-nca-ocp` | positive / NCA | stoichiometry; [0.0, 1.0] | [Generated samples](nca-kim2011-nca-ocp-sampled.csv) | [JSON](nca-kim2011-nca-ocp.json) |

## NCO

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `ecker2015-nco-ocp` | positive / NCO | stoichiometry; [0.0, 1.0] | [Generated samples](ecker2015-nco-ocp-sampled.csv) | [JSON](ecker2015-nco-ocp.json) |

## NMC111

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `sintef-nmc111-9d3ce5-c3-delithiation` | positive / NMC111 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc111-9d3ce5-c3-delithiation.csv) | [JSON](sintef-nmc111-9d3ce5-c3-delithiation.json) |
| `sintef-nmc111-9d3ce5-c3-lithiation` | positive / NMC111 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc111-9d3ce5-c3-lithiation.csv) | [JSON](sintef-nmc111-9d3ce5-c3-lithiation.json) |
| `sintef-nmc111-6115bb-c3-delithiation` | positive / NMC111 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc111-6115bb-c3-delithiation.csv) | [JSON](sintef-nmc111-6115bb-c3-delithiation.json) |
| `sintef-nmc111-6115bb-c3-lithiation` | positive / NMC111 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc111-6115bb-c3-lithiation.csv) | [JSON](sintef-nmc111-6115bb-c3-lithiation.json) |

## NMC532

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `sintef-nmc532-2a2be3-c3-delithiation` | positive / NMC532 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc532-2a2be3-c3-delithiation.csv) | [JSON](sintef-nmc532-2a2be3-c3-delithiation.json) |
| `sintef-nmc532-2a2be3-c3-lithiation` | positive / NMC532 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc532-2a2be3-c3-lithiation.csv) | [JSON](sintef-nmc532-2a2be3-c3-lithiation.json) |
| `sintef-nmc532-ee86d1-c3-delithiation` | positive / NMC532 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc532-ee86d1-c3-delithiation.csv) | [JSON](sintef-nmc532-ee86d1-c3-delithiation.json) |
| `sintef-nmc532-ee86d1-c3-lithiation` | positive / NMC532 | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-nmc532-ee86d1-c3-lithiation.csv) | [JSON](sintef-nmc532-ee86d1-c3-lithiation.json) |
| `mohtat2020-nmc532-ocp` | positive / NMC532 | stoichiometry; [0.0, 1.0] | [Generated samples](mohtat2020-nmc532-ocp-sampled.csv) | [JSON](mohtat2020-nmc532-ocp.json) |
| `mohtat-author-nmc532-ocp` | positive / NMC532 | stoichiometry; [0.0335, 0.8907] | [Generated samples](mohtat-author-nmc532-ocp-sampled.csv) | [JSON](mohtat-author-nmc532-ocp.json) |

## NMC811

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `nmc811-lgm50-chen2020-formula` | positive / NMC811 | stoichiometry; [0.0, 1.0] | [Generated samples](nmc811-lgm50-chen2020-formula-sampled.csv) | [JSON](nmc811-lgm50-chen2020-formula.json) |

## silicon

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `sintef-silicon-931301-c3-lithiation` | negative / silicon | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-931301-c3-lithiation.csv) | [JSON](sintef-silicon-931301-c3-lithiation.json) |
| `sintef-silicon-931301-c3-delithiation` | negative / silicon | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-931301-c3-delithiation.csv) | [JSON](sintef-silicon-931301-c3-delithiation.json) |
| `sintef-silicon-2c4b6a-c3-lithiation` | negative / silicon | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-2c4b6a-c3-lithiation.csv) | [JSON](sintef-silicon-2c4b6a-c3-lithiation.json) |
| `sintef-silicon-2c4b6a-c3-delithiation` | negative / silicon | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-2c4b6a-c3-delithiation.csv) | [JSON](sintef-silicon-2c4b6a-c3-delithiation.json) |

## silicon-graphite

| Record | Electrode / material | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|
| `sintef-silicon-graphite-70e745-c3-lithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-70e745-c3-lithiation.csv) | [JSON](sintef-silicon-graphite-70e745-c3-lithiation.json) |
| `sintef-silicon-graphite-70e745-c3-delithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-70e745-c3-delithiation.csv) | [JSON](sintef-silicon-graphite-70e745-c3-delithiation.json) |
| `sintef-silicon-graphite-1c492a-c3-lithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-1c492a-c3-lithiation.csv) | [JSON](sintef-silicon-graphite-1c492a-c3-lithiation.json) |
| `sintef-silicon-graphite-1c492a-c3-delithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-1c492a-c3-delithiation.csv) | [JSON](sintef-silicon-graphite-1c492a-c3-delithiation.json) |
| `sintef-silicon-graphite-f4569b-c3-lithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-f4569b-c3-lithiation.csv) | [JSON](sintef-silicon-graphite-f4569b-c3-lithiation.json) |
| `sintef-silicon-graphite-f4569b-c3-delithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-f4569b-c3-delithiation.csv) | [JSON](sintef-silicon-graphite-f4569b-c3-delithiation.json) |
| `sintef-silicon-graphite-0cf06a-c3-lithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-0cf06a-c3-lithiation.csv) | [JSON](sintef-silicon-graphite-0cf06a-c3-lithiation.json) |
| `sintef-silicon-graphite-0cf06a-c3-delithiation` | negative / silicon-graphite | normalized_branch_capacity; [0.0, 1.0] | [Retained table](../../src/ebp/data/curves/sintef-silicon-graphite-0cf06a-c3-delithiation.csv) | [JSON](sintef-silicon-graphite-0cf06a-c3-delithiation.json) |
