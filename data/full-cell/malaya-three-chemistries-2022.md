# University of Malaya: LFP, NCA and NMC dynamic tests

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `malaya-three-chemistries-2022`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP, NMC, NCA. Source names an LFP 18650 3.3 V 1100 mAh cell, Panasonic NCR18650B 3400 mAh and Murata VTC6 18650 3000 mAh; per-model chemistry/profile matrix not independently inspected

[Open the original dataset](https://data.mendeley.com/datasets/29kw38kzwj/1) · Version: `1`

DOI: 10.17632/29kw38kzwj.1. Checked: 2026-10-23.

## Electrode OCP anchor

**Not identified**. No matched electrode half-cell file was verified for this external source in this review. Whole-cell OCV, EIS or chemistry alone does not supply electrode OCP.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: Use the cited catalog curves/source evidence; no verified external half-cell member path.

OCP evidence: [Source 1](https://data.mendeley.com/datasets/29kw38kzwj/1)

## Tests and channels

Types: dynamic, pulse. Profiles: US06, DST, FUDS, UDDS, WLTP.

HPPC and pulse charge/discharge are described; numeric rates not verified.

Reported temperature labels / degC: Not verified. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Source reports Neware BTS 4000 testing at four temperatures. Numeric setpoints and raw channel definitions were not verified.

## Ageing data

**Unverified**. The archive internals remain uninspected. The reviewed landing-page description does not establish longitudinal ageing coverage for any named model.

[Ageing coverage evidence](https://data.mendeley.com/datasets/29kw38kzwj/1). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. Named models and archived per-model test matrix remain separate from catalog studies. Panasonic NCR18650B is not the unidentified Kim2011 nominal design; generic NCA or NMC tags are not joins.

Components without a native catalog join: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | Named models and archived per-model test matrix remain separate from catalog studies. Panasonic NCR18650B is not the unidentified Kim2011 nominal design; generic NCA or NMC tags are not joins. Missing: No verified same-study, same-model catalog record for this component. |
| diffusion | `missing` / `missing` | None | Named models and archived per-model test matrix remain separate from catalog studies. Panasonic NCR18650B is not the unidentified Kim2011 nominal design; generic NCA or NMC tags are not joins. Missing: No verified same-study, same-model catalog record for this component. |
| kinetics | `missing` / `missing` | None | Named models and archived per-model test matrix remain separate from catalog studies. Panasonic NCR18650B is not the unidentified Kim2011 nominal design; generic NCA or NMC tags are not joins. Missing: No verified same-study, same-model catalog record for this component. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| multi_rate_discharge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| US06 | `container_only` | Dataset description names US06 collectively, but the only exposed file is a RAR. Per-cell US06 filenames not verified. |
| EIS | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |

## File locations

Selected verified file/container locators, not an exhaustive test matrix. Repeated basenames are distinct when source_path differs.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `Battery Test Data.rar` | Unresolved / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/29kw38kzwj/files/a221e3ba-df1d-4f46-aed9-f1222296baca/file_downloaded) |

File notes:

- `Battery Test Data.rar`: Only one 98 MB RAR listed in the source UI. Inner per-model files, profiles, rates and temperatures remain unresolved. Direct automated header request returned HTTP 403; no archive downloaded.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://data.mendeley.com/datasets/29kw38kzwj/1). Source dataset terms apply to downloaded files; cite the dataset and associated study.

Review level: `source_file_listing`. Source UI confirms the single archive filename and stable download link, not an exposed per-model directory. Dataset-level chemistry/profile declarations do not establish the archived cell-by-profile matrix.

- [Battery Test Data.rar](https://data.mendeley.com/public-files/datasets/29kw38kzwj/files/a221e3ba-df1d-4f46-aed9-f1222296baca/file_downloaded)

## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Raw file headers, units and sampling details require review before use.
- Material/profile coverage is dataset-level; no assertion that every named profile is available for every cell or temperature.
- Numeric temperatures, per-cell filenames and rates await source-file inspection.
- Not linked to Kim2011 nominal NCA parameters; chemistry alone does not establish a parameter match.

## Evidence

- [Primary source 1](https://data.mendeley.com/datasets/29kw38kzwj/1)
- [Primary source 2](https://doi.org/10.1016/j.est.2022.106049)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
