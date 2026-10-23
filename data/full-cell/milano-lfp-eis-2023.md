# 600 mAh LFP cells: SOC-dependent EIS

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `milano-lfp-eis-2023`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP. 600 mAh LFP per provider; IFR14500 appears in filenames. B01-B11 are source sample labels; manufacturer, exact commercial part and serial-number provenance remain unresolved.

[Open the original dataset](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1) · Version: `1`

DOI: 10.6084/m9.figshare.23736582.v1. Checked: 2026-10-23.

## Tests and channels

Types: eis. Profiles: No named drive profile verified.

Repeated EIS across SOC and charging cycles; no CC rate sweep verified.

Reported temperature labels / degC: Not verified. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: impedance.

Official metadata describes EIS, but archive columns, impedance sign, units and frequency range were not inspected.

## Ageing data

**Not reported**. The reviewed source coverage describes characterization tests; no longitudinal ageing series has been established for this record. This is not proof that no ageing data exist elsewhere.

[Ageing coverage evidence](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. Only 600 mAh LFP is disclosed. No manufacturer/part or electrode-characterization chain establishes a join to catalog LFP OCP, D or kinetics.

Missing components: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | Only 600 mAh LFP is disclosed. No manufacturer/part or electrode-characterization chain establishes a join to catalog LFP OCP, D or kinetics. Missing: No verified same-study, same-model catalog record for this component. |
| diffusion | `missing` / `missing` | None | Only 600 mAh LFP is disclosed. No manufacturer/part or electrode-characterization chain establishes a join to catalog LFP OCP, D or kinetics. Missing: No verified same-study, same-model catalog record for this component. |
| kinetics | `missing` / `missing` | None | Only 600 mAh LFP is disclosed. No manufacturer/part or electrode-characterization chain establishes a join to catalog LFP OCP, D or kinetics. Missing: No verified same-study, same-model catalog record for this component. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| multi_rate_discharge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| US06 | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| EIS | `archive_member_located` | 440 CSV member paths: source samples B01-B11, Test_1/Test_2, Hioki, SOC labels 5 to 100 percent in 5-percent steps. No frequency or impedance columns inspected. |

## File locations

Selected verified file/container locators, not an exhaustive test matrix. Repeated basenames are distinct when source_path differs.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `Measurements.rar` | Unresolved / No sample ID | eis;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B01/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_03-07-2023_20-49.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B01 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B02/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_28-04-2023_02-00.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B02 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B03/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_06-07-2023_00-12.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B03 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B04/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_07-06-2023_21-04.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B04 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B05/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_01-03-2023_22-27.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B05 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B06/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_22-03-2023_20-03.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B06 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B07/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_04-03-2023_02-41.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B07 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B08/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_23-03-2023_19-58.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B08 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B09/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_10-03-2023_20-32.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B09 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B10/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_15-03-2023_19-05.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B10 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B11/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_14-03-2023_19-25.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B11 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B01/EIS measurements/Test_2/Hioki/Hk_IFR14500_SoC_50_07-06-2023_21-04.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B01 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |
| `Measurements.rar::Measurements/B01/Capacity measurements/2023-5-16-12-17-17-EBD-A20H-1-1_BATT1.csv` | IFR14500 label in EIS filenames; manufacturer/part not established / B01 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://ndownloader.figshare.com/files/41673360) |

File notes:

- `Measurements.rar`: Official Figshare archive metadata confirmed. Publisher MD5 and size are not independently computed payload hashes.
- `Measurements.rar::Measurements/B01/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_03-07-2023_20-49.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B02/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_28-04-2023_02-00.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B03/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_06-07-2023_00-12.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B04/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_07-06-2023_21-04.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B05/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_01-03-2023_22-27.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B06/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_22-03-2023_20-03.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B07/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_04-03-2023_02-41.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B08/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_23-03-2023_19-58.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B09/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_10-03-2023_20-32.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B10/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_15-03-2023_19-05.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B11/EIS measurements/Test_1/Hioki/Hk_IFR14500_SoC_50_14-03-2023_19-25.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B01/EIS measurements/Test_2/Hioki/Hk_IFR14500_SoC_50_07-06-2023_21-04.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.
- `Measurements.rar::Measurements/B01/Capacity measurements/2023-5-16-12-17-17-EBD-A20H-1-1_BATT1.csv`: Directory header and byte size verified, not CSV content. Link opens the parent RAR; extract this member yourself. Filename SOC labels are not independently calibrated measurements.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1). Source dataset terms apply to downloaded files; cite the dataset and associated study.

Review level: `archive_directory_reviewed`. Complete RAR5 directory inspected with HTTP Range header reads: 539 entries, 461 files (440 EIS CSV, 11 capacity CSV, 10 BMP). Source compressed data skipped without extraction; CSV headers/units and full payload checksum not verified.

- [Measurements.rar](https://ndownloader.figshare.com/files/41673360)
  Publisher/pinned MD5: `94a817377b3f5148806e65d4bb68b29a`.
- [Hk_IFR14500_SoC_50_03-07-2023_20-49.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_28-04-2023_02-00.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_06-07-2023_00-12.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_07-06-2023_21-04.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_01-03-2023_22-27.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_22-03-2023_20-03.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_04-03-2023_02-41.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_23-03-2023_19-58.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_10-03-2023_20-32.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_15-03-2023_19-05.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_14-03-2023_19-25.csv](https://ndownloader.figshare.com/files/41673360)
- [Hk_IFR14500_SoC_50_07-06-2023_21-04.csv](https://ndownloader.figshare.com/files/41673360)
- [2023-5-16-12-17-17-EBD-A20H-1-1_BATT1.csv](https://ndownloader.figshare.com/files/41673360)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/external-archive-directory-review.json)


## Missing items and limits

- Manufacturer, exact commercial part and chain from source sample labels to physical serial numbers unresolved.
- IFR14500 is a filename designation, not a verified unique manufacturer model.
- CSV frequency range, complex-impedance units/sign, temperatures and measured-versus-derived capacity fields were not read.
- No source-supported US06 or numeric multi-rate CC sweep identified.
- No same-study electrode OCP, intrinsic D or reaction-kinetic record joined to catalog cells.

## Evidence

- [Primary source 1](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1)
- [Primary source 2](https://api.figshare.com/v2/articles/23736582)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
