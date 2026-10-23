# Panasonic NCR18650B multi-rate discharge and surface-temperature data

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `stanford-ncr18650b-rates-2021`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NCA. Panasonic NCR18650B 3350 mAh NCA/graphite; only the NCA section of the three-model Stanford source is curated here. Its LG INR21700-M50 and A123 ANR26650m1-B sections are separate cells, not NCR18650B data.

[Open the original dataset](https://data.mendeley.com/datasets/kxsbr4x3j2/2) · Version: `2 (NCA section only)`

DOI: 10.17632/kxsbr4x3j2.2. Checked: 2026-10-23.

## Electrode OCP anchor

**Not identified**. No matched electrode half-cell file was verified for this external source in this review. Whole-cell OCV, EIS or chemistry alone does not supply electrode OCP.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: Use the cited catalog curves/source evidence; no verified external half-cell member path.

OCP evidence: [Source 1](https://data.mendeley.com/datasets/kxsbr4x3j2/2)

## Tests and channels

Types: constant_current, cccv. Profiles: No named drive profile verified.

NCA discharge rates C/20, 1C, 2C, 3C and 5C at source temperatures 5/25/35 degC after standard CCCV charge. The LFP source range up to 20C must not be assigned to NCR18650B. Charging preparation is not a multi-rate charge sweep.

Reported temperature labels / degC: [5, 25, 35]. These are source conditions, not measured temperature channels.

Reported time-series channels: time, voltage, current, cell_surface_temperature.

Reported frequency-domain channels: Not verified / not applicable.

The primary paper describes Excel time, current, voltage and thermocouple surface-temperature data. Workbook contents/units were not read. Source directory names are 05degC/25degC/35degC; preserve these actual names rather than the schematic T_amb folders in the paper.

## Ageing data

**Not reported**. The source describes initial characterization, not a longitudinal ageing series.

[Ageing coverage evidence](https://data.mendeley.com/datasets/kxsbr4x3j2/2). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set.

Components without a native catalog join: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |
| diffusion | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |
| kinetics | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |
| multi_rate_discharge | `file_located` | Actual NCA/k1 XLSX links are listed at 0.05/1/2/3/5C in each of 05degC, 25degC and 35degC. Only selected paths, not all specimens or raw columns, are checked. |
| US06 | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |
| EIS | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |

## File locations

Fifteen selected source-listed NCA k1 workbooks (five rates by three temperatures). This is not a certified six-cell matrix or an import of the LFP/NMC source sections.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `galvanostatic_discharge_test/NCA/05degC/NCA_k1_0_05C_05degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 5 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/76f12d0e-917e-4221-b9ec-ae6feb2fa71f/file_downloaded) |
| `galvanostatic_discharge_test/NCA/05degC/NCA_k1_1C_05degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 5 degC; 1C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/9b67ee52-7a18-4477-9ae6-a36d0761f131/file_downloaded) |
| `galvanostatic_discharge_test/NCA/05degC/NCA_k1_2C_05degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 5 degC; 2C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/f73ad953-73d8-4924-ba04-d3cd5a00ba8f/file_downloaded) |
| `galvanostatic_discharge_test/NCA/05degC/NCA_k1_3C_05degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 5 degC; 3C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/73e4dee2-4237-4855-8f0e-1563d1c7fedb/file_downloaded) |
| `galvanostatic_discharge_test/NCA/05degC/NCA_k1_5C_05degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 5 degC; 5C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/ae639390-e7ab-4448-84b6-b0f66f4e0a2b/file_downloaded) |
| `galvanostatic_discharge_test/NCA/25degC/NCA_k1_0_05C_25degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 25 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/e4bf7e8e-f3ef-4e6d-be8c-751bdec075f1/file_downloaded) |
| `galvanostatic_discharge_test/NCA/25degC/NCA_k1_1C_25degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 25 degC; 1C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/9ed734d2-2589-42e3-8311-95204e3a79c7/file_downloaded) |
| `galvanostatic_discharge_test/NCA/25degC/NCA_k1_2C_25degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 25 degC; 2C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/ee70ffd8-1c8e-4255-918c-09bdd8ee9466/file_downloaded) |
| `galvanostatic_discharge_test/NCA/25degC/NCA_k1_3C_25degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 25 degC; 3C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/35e36e18-81d9-49de-a3ba-205af572a9c2/file_downloaded) |
| `galvanostatic_discharge_test/NCA/25degC/NCA_k1_5C_25degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 25 degC; 5C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/3e2dea20-3349-4c6b-8b3e-aae43c5deb26/file_downloaded) |
| `galvanostatic_discharge_test/NCA/35degC/NCA_k1_0_05C_35degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 35 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/d7d9aaf5-39a8-463a-b663-177595739e23/file_downloaded) |
| `galvanostatic_discharge_test/NCA/35degC/NCA_k1_1C_35degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 35 degC; 1C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/978ff2ea-e13a-47bc-8284-34f8779283bb/file_downloaded) |
| `galvanostatic_discharge_test/NCA/35degC/NCA_k1_2C_35degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 35 degC; 2C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/658f3d3c-b8e2-4d07-8bb3-0aa9bb8409d7/file_downloaded) |
| `galvanostatic_discharge_test/NCA/35degC/NCA_k1_3C_35degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 35 degC; 3C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/2ca08fdf-cb26-4a21-82b1-95905877917c/file_downloaded) |
| `galvanostatic_discharge_test/NCA/35degC/NCA_k1_5C_35degC.xlsx` | Panasonic NCR18650B / k1 | constant_current;  | 35 degC; 5C | `source_listing`; content `not_read` | [Open source file](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/2ff68215-d1ab-4163-9bba-998911fb11e4/file_downloaded) |

File notes:

- `galvanostatic_discharge_test/NCA/05degC/NCA_k1_0_05C_05degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/05degC/NCA_k1_1C_05degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/05degC/NCA_k1_2C_05degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/05degC/NCA_k1_3C_05degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/05degC/NCA_k1_5C_05degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/25degC/NCA_k1_0_05C_25degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/25degC/NCA_k1_1C_25degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/25degC/NCA_k1_2C_25degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/25degC/NCA_k1_3C_25degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/25degC/NCA_k1_5C_25degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/35degC/NCA_k1_0_05C_35degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/35degC/NCA_k1_1C_35degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/35degC/NCA_k1_2C_35degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/35degC/NCA_k1_3C_35degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.
- `galvanostatic_discharge_test/NCA/35degC/NCA_k1_5C_35degC.xlsx`: Actual source-listed NCA/k1 rate workbook. Discharge-rate and temperature tags follow filename plus primary paper; raw columns, thermal cutoff occurrence and charge phases are not independently read.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://data.mendeley.com/datasets/kxsbr4x3j2/2). Dataset landing page states CC BY 4.0. The associated paper has separate CC BY-NC-ND terms; do not substitute the paper license for dataset reuse terms. No workbook is redistributed.

Review level: `source_file_listing`. Primary paper, public Mendeley UI and NCA temperature folders inspected. Retained fifteen exact k1 workbook links across five rates and three temperatures. Automated landing-page HTTP access returned 403; normal public UI exposed links. No workbook downloaded.

- [galvanostatic_discharge_test/NCA/05degC/NCA_k1_0_05C_05degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/76f12d0e-917e-4221-b9ec-ae6feb2fa71f/file_downloaded)
- [galvanostatic_discharge_test/NCA/05degC/NCA_k1_1C_05degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/9b67ee52-7a18-4477-9ae6-a36d0761f131/file_downloaded)
- [galvanostatic_discharge_test/NCA/05degC/NCA_k1_2C_05degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/f73ad953-73d8-4924-ba04-d3cd5a00ba8f/file_downloaded)
- [galvanostatic_discharge_test/NCA/05degC/NCA_k1_3C_05degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/73e4dee2-4237-4855-8f0e-1563d1c7fedb/file_downloaded)
- [galvanostatic_discharge_test/NCA/05degC/NCA_k1_5C_05degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/ae639390-e7ab-4448-84b6-b0f66f4e0a2b/file_downloaded)
- [galvanostatic_discharge_test/NCA/25degC/NCA_k1_0_05C_25degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/e4bf7e8e-f3ef-4e6d-be8c-751bdec075f1/file_downloaded)
- [galvanostatic_discharge_test/NCA/25degC/NCA_k1_1C_25degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/9ed734d2-2589-42e3-8311-95204e3a79c7/file_downloaded)
- [galvanostatic_discharge_test/NCA/25degC/NCA_k1_2C_25degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/ee70ffd8-1c8e-4255-918c-09bdd8ee9466/file_downloaded)
- [galvanostatic_discharge_test/NCA/25degC/NCA_k1_3C_25degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/35e36e18-81d9-49de-a3ba-205af572a9c2/file_downloaded)
- [galvanostatic_discharge_test/NCA/25degC/NCA_k1_5C_25degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/3e2dea20-3349-4c6b-8b3e-aae43c5deb26/file_downloaded)
- [galvanostatic_discharge_test/NCA/35degC/NCA_k1_0_05C_35degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/d7d9aaf5-39a8-463a-b663-177595739e23/file_downloaded)
- [galvanostatic_discharge_test/NCA/35degC/NCA_k1_1C_35degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/978ff2ea-e13a-47bc-8284-34f8779283bb/file_downloaded)
- [galvanostatic_discharge_test/NCA/35degC/NCA_k1_2C_35degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/658f3d3c-b8e2-4d07-8bb3-0aa9bb8409d7/file_downloaded)
- [galvanostatic_discharge_test/NCA/35degC/NCA_k1_3C_35degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/2ca08fdf-cb26-4a21-82b1-95905877917c/file_downloaded)
- [galvanostatic_discharge_test/NCA/35degC/NCA_k1_5C_35degC.xlsx](https://data.mendeley.com/public-files/datasets/kxsbr4x3j2/files/2ff68215-d1ab-4163-9bba-998911fb11e4/file_downloaded)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ncr18650b-source-review.json)


## Missing items and limits

- No verified current-catalog OCP/D/kinetics association for NCR18650B; other same-model studies are different specimens.
- No US06, EIS or longitudinal ageing series reported in the reviewed source.
- Only representative k1 links retained; six samples per chemistry in the paper does not certify a complete six-by-five-by-three source matrix.
- Workbook phase boundaries, measured channel units and thermal cutoffs remain unchecked.

## Evidence

- [Primary source 1](https://data.mendeley.com/datasets/kxsbr4x3j2/2)
- [Primary source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC7941039/)
- [Primary source 3](https://doi.org/10.1016/j.dib.2021.106894)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
