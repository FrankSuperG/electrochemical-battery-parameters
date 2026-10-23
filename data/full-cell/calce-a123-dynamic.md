# CALCE A123 LFP: OCV, DST and FUDS

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `calce-a123-dynamic`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP. A123 cylindrical LFP; exact commercial part unresolved. Page reports 1110 mAh and 25.4 mm diameter; do not infer a model number.

[Open the original dataset](https://calce.umd.edu/data) · Version: `unversioned page; reviewed 2026-10-23`

DOI: Not assigned in the inspected source. Checked: 2026-10-23.

## Tests and channels

Types: dynamic, ocv. Profiles: DST, FUDS, US06.

Low-current OCV and dynamic tests; no source-supported multi-rate CC sweep asserted.

Reported temperature labels / degC: [-10, 0, 10, 20, 25, 30, 40, 50]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Download table lists these temperature labels. They are not proof of measured per-row temperature channels.

## Ageing data

**Not reported**. The reviewed source coverage describes characterization tests; no longitudinal ageing series has been established for this record. This is not proof that no ageing data exist elsewhere.

[Ageing coverage evidence](https://calce.umd.edu/data). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. CALCE exact A123 part is unresolved; source specification and sample labels do not establish identity with catalog A123 entries. Same brand and LFP chemistry are insufficient.

Missing components: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | CALCE exact A123 part is unresolved; source specification and sample labels do not establish identity with catalog A123 entries. Same brand and LFP chemistry are insufficient. Missing: No verified same-study, same-model catalog record for this component. |
| diffusion | `missing` / `missing` | None | CALCE exact A123 part is unresolved; source specification and sample labels do not establish identity with catalog A123 entries. Same brand and LFP chemistry are insufficient. Missing: No verified same-study, same-model catalog record for this component. |
| kinetics | `missing` / `missing` | None | CALCE exact A123 part is unresolved; source specification and sample labels do not establish identity with catalog A123 entries. Same brand and LFP chemistry are insufficient. Missing: No verified same-study, same-model catalog record for this component. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| multi_rate_discharge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| US06 | `archive_member_located` | 25 degC ZIP directory contains two combined DST-US06-FUDS XLSX files. Exact internal phase boundaries were not read. |
| EIS | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |

## File locations

Selected verified file/container locators, not an exhaustive test matrix. Repeated basenames are distinct when source_path differs.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `A123_OCV-10-20120629.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | -10 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV-10-20120629.zip) |
| `A123_OCV0-20120618.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV0-20120618.zip) |
| `A123_OCV10-20120611.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 10 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV10-20120611.zip) |
| `A123_OCV20-20120614.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 20 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV20-20120614.zip) |
| `A123_OCV25-20120905.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV25-20120905.zip) |
| `A123_OCV30-20120625.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 30 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV30-20120625.zip) |
| `A123_OCV40-20120627.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 40 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV40-20120627.zip) |
| `A123_OCV50-20120702.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | ocv;  | 50 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_OCV50-20120702.zip) |
| `A123_DST-US06-FUDS-N10.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | -10 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-N10.zip) |
| `A123_DST-US06-FUDS-0.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 0 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-0.zip) |
| `A123_DST-US06-FUDS-10.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 10 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-10.zip) |
| `A123_DST-US06-FUDS-20.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 20 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-20.zip) |
| `A123_DST-US06-FUDS-25.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 25 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-25.zip) |
| `A123_DST-US06-FUDS-30.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 30 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-30.zip) |
| `A123_DST-US06-FUDS-40.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 40 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-40.zip) |
| `A123_DST-US06-FUDS-50.zip` | A123 LFP cylindrical cell; exact part unresolved / No sample ID | dynamic; US06, DST, FUDS | 50 degC | `source_listing`; content `not_read` | [Open source file](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-50.zip) |
| `A123_DST-US06-FUDS-25.zip::DST-US06-FUDS-25/A1-007-DST-US06-FUDS-25-20120827.xlsx` | A123 LFP cylindrical cell; exact part unresolved / A1-007 | dynamic; US06, DST, FUDS | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-25.zip) |
| `A123_DST-US06-FUDS-25.zip::DST-US06-FUDS-25/A1-008-DST-US06-FUDS-25-20120827.xlsx` | A123 LFP cylindrical cell; exact part unresolved / A1-008 | dynamic; US06, DST, FUDS | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-25.zip) |

File notes:

- `A123_OCV-10-20120629.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV0-20120618.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV10-20120611.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV20-20120614.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV25-20120905.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV30-20120625.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV40-20120627.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_OCV50-20120702.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-N10.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-0.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-10.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-20.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-25.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-30.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-40.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-50.zip`: Archive URL published in the source table; inner files not inspected except for separately listed representative members. Profile names here are archive-name evidence, not a verified full inner-file matrix.
- `A123_DST-US06-FUDS-25.zip::DST-US06-FUDS-25/A1-007-DST-US06-FUDS-25-20120827.xlsx`: Inner filename and uncompressed size verified from ZIP directory only. Link downloads the parent ZIP, not a separately hosted member. No workbook content read.
- `A123_DST-US06-FUDS-25.zip::DST-US06-FUDS-25/A1-008-DST-US06-FUDS-25-20120827.xlsx`: Inner filename and uncompressed size verified from ZIP directory only. Link downloads the parent ZIP, not a separately hosted member. No workbook content read.

## Reuse and access

License: **not-stated**. [Source terms](https://calce.umd.edu/data). CALCE provides open access and requests paper citations; no standard redistribution license identified. Link only.

Review level: `archive_directory_reviewed`. Source-table ZIP URLs inspected. A representative 25 degC archive directory was read with bounded HTTP Range requests, without downloading/extracting observation contents; other archive members remain unchecked.

- [A123_OCV-10-20120629.zip](https://web.calce.umd.edu/batteries/data/A123_OCV-10-20120629.zip)
- [A123_OCV0-20120618.zip](https://web.calce.umd.edu/batteries/data/A123_OCV0-20120618.zip)
- [A123_OCV10-20120611.zip](https://web.calce.umd.edu/batteries/data/A123_OCV10-20120611.zip)
- [A123_OCV20-20120614.zip](https://web.calce.umd.edu/batteries/data/A123_OCV20-20120614.zip)
- [A123_OCV25-20120905.zip](https://web.calce.umd.edu/batteries/data/A123_OCV25-20120905.zip)
- [A123_OCV30-20120625.zip](https://web.calce.umd.edu/batteries/data/A123_OCV30-20120625.zip)
- [A123_OCV40-20120627.zip](https://web.calce.umd.edu/batteries/data/A123_OCV40-20120627.zip)
- [A123_OCV50-20120702.zip](https://web.calce.umd.edu/batteries/data/A123_OCV50-20120702.zip)
- [A123_DST-US06-FUDS-N10.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-N10.zip)
- [A123_DST-US06-FUDS-0.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-0.zip)
- [A123_DST-US06-FUDS-10.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-10.zip)
- [A123_DST-US06-FUDS-20.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-20.zip)
- [A123_DST-US06-FUDS-25.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-25.zip)
- [A123_DST-US06-FUDS-30.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-30.zip)
- [A123_DST-US06-FUDS-40.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-40.zip)
- [A123_DST-US06-FUDS-50.zip](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-50.zip)
- [A1-007-DST-US06-FUDS-25-20120827.xlsx](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-25.zip)
- [A1-008-DST-US06-FUDS-25-20120827.xlsx](https://web.calce.umd.edu/batteries/data/A123_DST-US06-FUDS-25.zip)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/external-archive-directory-review.json)


## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Narrative temperature range differs from the download-table labels; listed values describe the table, not a verified complete test matrix.
- Do not join to an A123 model based on brand, dimensions or chemistry alone.
- EIS and continuous multi-rate charge/discharge sweeps not located in the reviewed source table.
- Only the representative 25 degC archive directory was inspected; other members, headers and units remain unverified.
- US06 occurs in combined DST-US06-FUDS workbook filenames; exact phase boundaries within each workbook were not read.
- A1-007/A1-008 are source filenames; mapping to OCV specimens or a commercial part remains unresolved.

## Evidence

- [Primary source 1](https://calce.umd.edu/data)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
