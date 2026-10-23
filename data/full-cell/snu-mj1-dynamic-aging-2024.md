# LG MJ1 dynamic operating-sequence ageing (80 cells)

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `snu-mj1-dynamic-aging-2024`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. LG Chem INR18650-MJ1 3.5 Ah NMC811/Gr-SiOx. SNU ageing cells are a different study/batch from catalog DLR-SINTEF harvested-electrode half cells.

[Open the original dataset](https://data.mendeley.com/datasets/h2y7mj4kt7/2) · Version: `2`

DOI: 10.17632/h2y7mj4kt7.2. Checked: 2026-10-23.

## Electrode OCP anchor

**Cross-study catalog half-cell reference**. Commercial MJ1 model matches the catalog DLR-SINTEF half-cell study, but paper, specimens, manufacturing batch and ageing state differ. Four existing finite-current half-cell OCP branches are a same-model, different-study reference only; no same-study D/i0 transfer or performance claim.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: Use the cited catalog curves/source evidence; no verified external half-cell member path.

OCP evidence: [Source 1](https://zenodo.org/records/15497193) · [Source 2](https://data.mendeley.com/datasets/h2y7mj4kt7/2)

## Tests and channels

Types: dynamic. Profiles: No named drive profile verified.

Source reports 72 cells across 24 staged 600-cycle operating sequences and eight cells with conditions changed every 25 cycles. This is staged cycle ageing, not an identified US06/WLTP road-current profile.

Reported temperature labels / degC: [25]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Observation headers and units were not independently read; source conditions remain distinct from measured channels.

## Ageing data

**Yes (cycle)**. Primary source identifies an 80-cell cycle-ageing campaign and one raw ZIP. Availability is source-documented; inner per-cell paths, cycle counts and channels remain unread.

[Ageing coverage evidence](https://data.mendeley.com/datasets/h2y7mj4kt7/2). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `same_model_different_study`. Commercial MJ1 model matches the catalog DLR-SINTEF half-cell study, but paper, specimens, manufacturing batch and ageing state differ. Four existing finite-current half-cell OCP branches are a same-model, different-study reference only; no same-study D/i0 transfer or performance claim.

[LG MJ1 &#124; DLR-SINTEF harvested-electrode characterization](../cells/lg-mj1-dlr-sintef.md)

Components without a native catalog join: diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `same_model_different_study` / `electrode_ocp` | `mj1-negative-ocp-charging`, `mj1-negative-ocp-discharging`, `mj1-positive-ocp-charging`, `mj1-positive-ocp-discharging` | Commercial MJ1 model matches the catalog DLR-SINTEF half-cell study, but paper, specimens, manufacturing batch and ageing state differ. Four existing finite-current half-cell OCP branches are a same-model, different-study reference only; no same-study D/i0 transfer or performance claim. Missing: No same-study or serialized-specimen match; cross-study reuse does not establish transferable aged-cell parameters. |
| diffusion | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |
| kinetics | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| multi_rate_discharge | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| US06 | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| EIS | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |

## File locations

Selected confirmed source paths and parameter evidence. Counts describe locators, not independent experiments or a complete cell-by-temperature matrix.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `Battery raw data.zip` | LG INR18650-MJ1 / No sample ID | ;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/h2y7mj4kt7/files/deb660ea-9d02-441b-9b04-edda17ea32fc/file_downloaded) |

File notes:

- `Battery raw data.zip`: Single source-listed ageing ZIP. Automated HEAD access returned 403; inner paths, channels and per-cell phase mapping remain unverified. Dataset-level dynamic claims are not assigned to unidentified archive members.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://data.mendeley.com/datasets/h2y7mj4kt7/2). Public source UI states CC BY 4.0. A single source-listed raw ZIP is linked; no data redistributed.

Review level: `source_file_listing`. Normal public UI confirms archive name/UUID and CC BY 4.0. Inner ZIP directory remains uninspected after HTTP 403; no trace, column or completeness claim.

- [Battery raw data.zip](https://data.mendeley.com/public-files/datasets/h2y7mj4kt7/files/deb660ea-9d02-441b-9b04-edda17ea32fc/file_downloaded)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ocp-first-expansion-review.json)


## Missing items and limits

- No half-cell OCP from the SNU ageing study itself; current DLR-SINTEF curves are a cross-study reference only.
- Raw ZIP members, measured I/V/T fields and per-cell rates are unverified; HTTP 403 is an access limitation, not absence of data.
- No matched diffusion/kinetics, multi-temperature matrix, EIS or named road-current cycle established. Dynamic operating sequences are not relabelled US06/WLTP.

## Evidence

- [Primary source 1](https://data.mendeley.com/datasets/h2y7mj4kt7/2)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
