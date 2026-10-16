# A123 AMP20M1HD-A | 20 Ah LFP pouch

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `a123-amp20m1hd-a`. Match level: `same_model_same_study`.

Methods names AMP20M1HD-A; paper links the ORA dataset; archive filename identifies Cell I. Table 1 is for one cell but its letter is not explicitly established here, so a same-specimen parameter claim is withheld.

Do not label the full-cell pseudo-OCV as an LFP half-cell OCP, or assign a shared effective diffusion coefficient to a specific material without the model assumptions.

## Parameters

[All 30 parameter records (CSV)](../parameters/a123-amp20m1hd-a.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/a123-amp20m1hd-a.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

## OCP curves

No electrode-resolved OCP record linked to this cell. Full-cell pseudo-OCV and unrelated same-chemistry curves do not fill this gap.

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `a123-amp20-cell-i-4c` — 4C full discharge after CCCV charging and 1 h rest; 1 Hz source timebase | `time_s` | [CSV](../../src/ebp/data/full_cell/a123-amp20-cell-i-4c-normalized.csv) | [Source download](<https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513/files/d0c483j73t>) | 827 / 827 / 827 / 827 of 827 |

### Test gaps and extra channels

- `a123-amp20-cell-i-4c`: Ambient temperature trace

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed

## Sources and reuse

- [Oxford multiscale-coupling COMSOL/MATLAB implementation](<https://github.com/Battery-Intelligence-Lab/multiscale-coupling/tree/dba3649f2eeb4228d2849e4d4e748c91ed6ad7a4>) (`lin-2022-code`)
- [Oxford experimental data for Lin et al. 2022](<https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513>) (`lin-2022-data`)
- [Multiscale coupling of surface temperature with solid diffusion in large lithium-ion pouch cells](<https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/>) (`lin-2022-paper`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
