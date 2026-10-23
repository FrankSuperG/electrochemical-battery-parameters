# CALCE Samsung INR18650-20R: OCV and dynamic profiles

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `calce-samsung-20r-dynamic`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. Samsung INR18650-20R, 2 Ah; LiNiMnCo/graphite as stated by CALCE

[Open the original dataset](https://calce.umd.edu/data) · Version: `unversioned page; reviewed 2026-10-23`

DOI: Not assigned in the inspected source. Checked: 2026-10-23.

## Tests and channels

Types: dynamic, ocv, pulse. Profiles: US06, DST, FUDS, BJDST.

Source describes low-current and incremental-current OCV protocols; no multi-rate CC sweep asserted.

Reported temperature labels / degC: [0, 25, 45]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Protocols are described on the source page. Per-file measured channel headers were not inspected.

## Ageing data

**Not reported**. The reviewed source coverage describes characterization tests; no longitudinal ageing series has been established for this record. This is not proof that no ageing data exist elsewhere.

[Ageing coverage evidence](https://calce.umd.edu/data). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. Samsung INR18650-20R has no electrode-characterization parameter package in this catalog. LG M50/M50LT and Mohtat NMC cells are different models/studies.

Missing components: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | Samsung INR18650-20R has no electrode-characterization parameter package in this catalog. LG M50/M50LT and Mohtat NMC cells are different models/studies. Missing: No verified same-study, same-model catalog record for this component. |
| diffusion | `missing` / `missing` | None | Samsung INR18650-20R has no electrode-characterization parameter package in this catalog. LG M50/M50LT and Mohtat NMC cells are different models/studies. Missing: No verified same-study, same-model catalog record for this component. |
| kinetics | `missing` / `missing` | None | Samsung INR18650-20R has no electrode-characterization parameter package in this catalog. LG M50/M50LT and Mohtat NMC cells are different models/studies. Missing: No verified same-study, same-model catalog record for this component. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| multi_rate_discharge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| US06 | `archive_member_located` | 25 degC SP2 ZIP directory lists distinct US06 50SOC and 80SOC XLS workbooks; 0/45 degC archive URLs listed but members not inspected. |
| EIS | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |

## File locations

Selected verified file/container locators, not an exhaustive test matrix. Repeated basenames are distinct when source_path differs.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `SP1_0C_LC_OCV_02_24_2016.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP1_0C_LC_OCV_02_24_2016.zip) |
| `SP1_25C_LC_OCV_11_5_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP1_25C_LC_OCV_11_5_2015.zip) |
| `SP1_45C_LC_OCV_11_21_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP1_45C_LC_OCV_11_21_2015.zip) |
| `SP3_0C_LC_OCV_03_03_2016.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP3_0C_LC_OCV_03_03_2016.zip) |
| `SP3_25C_LC_OCV_11_16_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP3_25C_LC_OCV_11_16_2015.zip) |
| `SP3_45C_LC_OCV_11_21_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP3_45C_LC_OCV_11_21_2015.zip) |
| `SP1_0C_IC_OCV_02_26_2016.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP1_0C_IC_OCV_02_26_2016.zip) |
| `SP1_25C_IC_OCV_12_2_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP1_25C_IC_OCV_12_2_2015.zip) |
| `SP1_45C_IC_OCV_12_09_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP1_45C_IC_OCV_12_09_2015.zip) |
| `SP3_0C_IC_OCV_03_09_2016.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP3_0C_IC_OCV_03_09_2016.zip) |
| `SP3_25C_IC_OCV_12_2_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP3_25C_IC_OCV_12_2_2015.zip) |
| `SP3_45C_IC_OCV_12_09_2015.zip` | Samsung INR18650-20R / No sample ID | ocv;  | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP3_45C_IC_OCV_12_09_2015.zip) |
| `SP2_0C_DST.zip` | Samsung INR18650-20R / No sample ID | dynamic; DST | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_0C_DST.zip) |
| `SP2_25C_DST.zip` | Samsung INR18650-20R / No sample ID | dynamic; DST | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_25C_DST.zip) |
| `SP2_45C_DST.zip` | Samsung INR18650-20R / No sample ID | dynamic; DST | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_45C_DST.zip) |
| `SP2_0C_FUDS.zip` | Samsung INR18650-20R / No sample ID | dynamic; FUDS | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_0C_FUDS.zip) |
| `SP2_25C_FUDS.zip` | Samsung INR18650-20R / No sample ID | dynamic; FUDS | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_25C_FUDS.zip) |
| `SP2_45C_FUDS.zip` | Samsung INR18650-20R / No sample ID | dynamic; FUDS | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_45C_FUDS.zip) |
| `SP2_0C_US06.zip` | Samsung INR18650-20R / No sample ID | dynamic; US06 | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_0C_US06.zip) |
| `SP2_25C_US06.zip` | Samsung INR18650-20R / No sample ID | dynamic; US06 | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip) |
| `SP2_45C_US06.zip` | Samsung INR18650-20R / No sample ID | dynamic; US06 | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_45C_US06.zip) |
| `SP2_0C_BJDST.zip` | Samsung INR18650-20R / No sample ID | dynamic; BJDST | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_0C_BJDST.zip) |
| `SP2_25C_BJDST.zip` | Samsung INR18650-20R / No sample ID | dynamic; BJDST | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_25C_BJDST.zip) |
| `SP2_45C_BJDST.zip` | Samsung INR18650-20R / No sample ID | dynamic; BJDST | 45 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/SP2_45C_BJDST.zip) |
| `SP2_25C_US06.zip::11_11_2015_SP20-2_US06_50SOC.xls` | Samsung INR18650-20R / SP20-2 | dynamic; US06 | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip) |
| `SP2_25C_US06.zip::11_11_2015_SP20-2_US06_80SOC.xls` | Samsung INR18650-20R / SP20-2 | dynamic; US06 | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip) |

File notes:

- `SP1_0C_LC_OCV_02_24_2016.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP1_25C_LC_OCV_11_5_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP1_45C_LC_OCV_11_21_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP3_0C_LC_OCV_03_03_2016.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP3_25C_LC_OCV_11_16_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP3_45C_LC_OCV_11_21_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP1_0C_IC_OCV_02_26_2016.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP1_25C_IC_OCV_12_2_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP1_45C_IC_OCV_12_09_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP3_0C_IC_OCV_03_09_2016.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP3_25C_IC_OCV_12_2_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP3_45C_IC_OCV_12_09_2015.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_0C_DST.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_25C_DST.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_45C_DST.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_0C_FUDS.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_25C_FUDS.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_45C_FUDS.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_0C_US06.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_25C_US06.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_45C_US06.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_0C_BJDST.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_25C_BJDST.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_45C_BJDST.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `SP2_25C_US06.zip::11_11_2015_SP20-2_US06_50SOC.xls`: Inner filename and uncompressed size verified from ZIP directory only. Link downloads the parent ZIP, not a separately hosted member. No workbook content read.
- `SP2_25C_US06.zip::11_11_2015_SP20-2_US06_80SOC.xls`: Inner filename and uncompressed size verified from ZIP directory only. Link downloads the parent ZIP, not a separately hosted member. No workbook content read.

## Reuse and access

License: **not-stated**. [Source terms](https://calce.umd.edu/data). CALCE provides open access and requests citation of the experiment papers; no standard redistribution license was identified on the page. Link only.

Review level: `archive_directory_reviewed`. Source-table ZIP URLs inspected. A representative 25 degC archive directory was read with bounded HTTP Range requests, without downloading/extracting observation contents; other archive members remain unchecked.

- [SP1_0C_LC_OCV_02_24_2016.zip](https://web.calce.umd.edu/batteries/data/SP1_0C_LC_OCV_02_24_2016.zip)
- [SP1_25C_LC_OCV_11_5_2015.zip](https://web.calce.umd.edu/batteries/data/SP1_25C_LC_OCV_11_5_2015.zip)
- [SP1_45C_LC_OCV_11_21_2015.zip](https://web.calce.umd.edu/batteries/data/SP1_45C_LC_OCV_11_21_2015.zip)
- [SP3_0C_LC_OCV_03_03_2016.zip](https://web.calce.umd.edu/batteries/data/SP3_0C_LC_OCV_03_03_2016.zip)
- [SP3_25C_LC_OCV_11_16_2015.zip](https://web.calce.umd.edu/batteries/data/SP3_25C_LC_OCV_11_16_2015.zip)
- [SP3_45C_LC_OCV_11_21_2015.zip](https://web.calce.umd.edu/batteries/data/SP3_45C_LC_OCV_11_21_2015.zip)
- [SP1_0C_IC_OCV_02_26_2016.zip](https://web.calce.umd.edu/batteries/data/SP1_0C_IC_OCV_02_26_2016.zip)
- [SP1_25C_IC_OCV_12_2_2015.zip](https://web.calce.umd.edu/batteries/data/SP1_25C_IC_OCV_12_2_2015.zip)
- [SP1_45C_IC_OCV_12_09_2015.zip](https://web.calce.umd.edu/batteries/data/SP1_45C_IC_OCV_12_09_2015.zip)
- [SP3_0C_IC_OCV_03_09_2016.zip](https://web.calce.umd.edu/batteries/data/SP3_0C_IC_OCV_03_09_2016.zip)
- [SP3_25C_IC_OCV_12_2_2015.zip](https://web.calce.umd.edu/batteries/data/SP3_25C_IC_OCV_12_2_2015.zip)
- [SP3_45C_IC_OCV_12_09_2015.zip](https://web.calce.umd.edu/batteries/data/SP3_45C_IC_OCV_12_09_2015.zip)
- [SP2_0C_DST.zip](https://web.calce.umd.edu/batteries/data/SP2_0C_DST.zip)
- [SP2_25C_DST.zip](https://web.calce.umd.edu/batteries/data/SP2_25C_DST.zip)
- [SP2_45C_DST.zip](https://web.calce.umd.edu/batteries/data/SP2_45C_DST.zip)
- [SP2_0C_FUDS.zip](https://web.calce.umd.edu/batteries/data/SP2_0C_FUDS.zip)
- [SP2_25C_FUDS.zip](https://web.calce.umd.edu/batteries/data/SP2_25C_FUDS.zip)
- [SP2_45C_FUDS.zip](https://web.calce.umd.edu/batteries/data/SP2_45C_FUDS.zip)
- [SP2_0C_US06.zip](https://web.calce.umd.edu/batteries/data/SP2_0C_US06.zip)
- [SP2_25C_US06.zip](https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip)
- [SP2_45C_US06.zip](https://web.calce.umd.edu/batteries/data/SP2_45C_US06.zip)
- [SP2_0C_BJDST.zip](https://web.calce.umd.edu/batteries/data/SP2_0C_BJDST.zip)
- [SP2_25C_BJDST.zip](https://web.calce.umd.edu/batteries/data/SP2_25C_BJDST.zip)
- [SP2_45C_BJDST.zip](https://web.calce.umd.edu/batteries/data/SP2_45C_BJDST.zip)
- [11_11_2015_SP20-2_US06_50SOC.xls](https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip)
- [11_11_2015_SP20-2_US06_80SOC.xls](https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/external-archive-directory-review.json)


## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Dynamic tests start at 80% and 50% battery level; exact specimen chain to OCV tests not verified.
- No standard reuse license verified; obtain terms from the provider before redistributing payloads.
- EIS and continuous multi-rate charge/discharge sweeps not located in the reviewed source table.
- Only the representative 25 degC archive directory was inspected; other members, headers and units remain unverified.

## Evidence

- [Primary source 1](https://calce.umd.edu/data)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
