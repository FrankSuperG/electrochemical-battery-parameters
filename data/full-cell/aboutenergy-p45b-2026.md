# Molicel P45B: published DFN OCP/parameters and multi-temperature CC, WLTP and eVTOL

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `aboutenergy-p45b-2026`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NCA. Molicel INR21700-P45B 4.5 Ah, NCA/graphite-SiOx according to published BPX header. DFN paper explicitly reuses the earlier public ECM validation dataset; same model and declared reuse, not a demonstrated shared serialized specimen.

[Open the original dataset](https://zenodo.org/records/19052626) · Version: `fixed record 19052626; BPX at 188bd62ee2347cc486b66dc43e31fb9597759db1`

DOI: 10.5281/zenodo.19052626. Checked: 2026-10-23.

## Electrode OCP anchor

**Published fitted parameterisation**. Published composite/fitted BPX electrode OCPs are linked externally. The authors explicitly connect this DFN set to the released full-cell tests. This review does not establish access to the original harvested half-cell observation points or independently validate the fitted curves.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: `examples/params/Molicel_P45B_bpx.json`

OCP evidence: [Source 1](https://raw.githubusercontent.com/About-Energy-OpenSource/AEPyBaMM/188bd62ee2347cc486b66dc43e31fb9597759db1/examples/params/Molicel_P45B_bpx.json) · [Source 2](https://www.aboutenergy.io/post/molicel-p45b-electrochemical-model-open-source-dfn-parameter-set)

## Tests and channels

Types: constant_current, pulse, dynamic, ocv. Profiles: WLTP, eVTOL.

CC charge at C/30, 1C, 3C and discharge at C/30, 1C, 3C, 10C; GITT and WLTP at 10/25/40/60 degC. eVTOL is limited to 25/40/60 degC. Alternate -charge.csv files retain a charge-optimised model case, not independent experiments.

Reported temperature labels / degC: [10, 25, 40, 60]. These are source conditions, not measured temperature channels.

Reported time-series channels: t_s, I_exp_A, V_exp_V, T_exp_degC.

Reported frequency-domain channels: Not verified / not applicable.

Author format PDF defines these experimental columns, positive charge current and Peltier-controlled surface temperature. I_sim_A, V_sim_V, SOC_sim, E_OCV_V, T_sim_degC and Q_sim_W are simulated columns. E_OCV_V is predicted whole-cell OCV, not measured electrode OCP. CSV headers/numerical data remain unchecked.

## Ageing data

**Not reported**. The reviewed source reports characterization or validation tests without an established longitudinal ageing series.

[Ageing coverage evidence](https://zenodo.org/records/19052626). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters.

Components without a native catalog join: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | Published composite/fitted BPX electrode OCPs are linked externally. The authors explicitly connect this DFN set to the released full-cell tests. This review does not establish access to the original harvested half-cell observation points or independently validate the fitted curves. Missing: No verified current-catalog record for this component and study. |
| diffusion | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |
| kinetics | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `archive_member_located` | The ZIP explicitly contains C/30, 1C and 3C charge and C/30, 1C, 3C and 10C discharge filename cases across four temperatures. -charge alternates are not independent experiments. |
| multi_rate_discharge | `archive_member_located` | The ZIP explicitly contains C/30, 1C and 3C charge and C/30, 1C, 3C and 10C discharge filename cases across four temperatures. -charge alternates are not independent experiments. |
| US06 | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| EIS | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |

## File locations

Selected confirmed source paths and parameter evidence. Counts describe locators, not independent experiments or a complete cell-by-temperature matrix.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `molicel_p45b_data.zip` | Molicel INR21700-P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_1C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_3C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_3C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_3C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_10C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 10.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_Co30_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_Co30_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_GITT_Ch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 10 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_GITT_Dch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 10 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_WLTP.csv` | Molicel INR21700-P45B / No sample ID | dynamic; WLTP | 10 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_1C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_1C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_1C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_3C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_3C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_3C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_10C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 10.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_Co30_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_Co30_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 25 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_eVTOL.csv` | Molicel INR21700-P45B / No sample ID | dynamic; eVTOL | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_GITT_Ch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_GITT_Dch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_025degC_WLTP.csv` | Molicel INR21700-P45B / No sample ID | dynamic; WLTP | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_1C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_1C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_1C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_3C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_3C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_3C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_10C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 10.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_Co30_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_Co30_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 40 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_eVTOL.csv` | Molicel INR21700-P45B / No sample ID | dynamic; eVTOL | 40 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_GITT_Ch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 40 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_GITT_Dch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 40 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_040degC_WLTP.csv` | Molicel INR21700-P45B / No sample ID | dynamic; WLTP | 40 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_1C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_1C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_1C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_3C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_3C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_3C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 3.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_10C_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 10.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_Co30_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_Co30_Dch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 60 degC; 0.03333333333333333C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_eVTOL.csv` | Molicel INR21700-P45B / No sample ID | dynamic; eVTOL | 60 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_GITT_Ch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 60 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_GITT_Dch.csv` | Molicel INR21700-P45B / No sample ID | pulse;  | 60 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_060degC_WLTP.csv` | Molicel INR21700-P45B / No sample ID | dynamic; WLTP | 60 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_1C_Ch.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `molicel_p45b_data.zip::MOLICEL_P45B_010degC_1C_Ch-charge.csv` | Molicel INR21700-P45B / No sample ID | constant_current;  | 10 degC; 1.0C | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content) |
| `examples/params/Molicel_P45B_bpx.json` | Molicel INR21700-P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `parameter_metadata_reviewed` | [Open source file](https://raw.githubusercontent.com/About-Energy-OpenSource/AEPyBaMM/188bd62ee2347cc486b66dc43e31fb9597759db1/examples/params/Molicel_P45B_bpx.json) |
| `Molicel P45B Data Release Data Format Documentation.pdf` | Molicel INR21700-P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `documentation_reviewed` | [Open source file](https://zenodo.org/api/records/19052626/files/Molicel%20P45B%20Data%20Release%20Data%20Format%20Documentation.pdf/content) |
| `readme_Molicel_P45B_dataset_AE.txt` | Molicel INR21700-P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `documentation_reviewed` | [Open source file](https://zenodo.org/api/records/19052626/files/readme_Molicel_P45B_dataset_AE.txt/content) |

File notes:

- `molicel_p45b_data.zip`: Parent archive only; no observation payload downloaded.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_1C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_3C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_3C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_3C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_10C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_Co30_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_Co30_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_GITT_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_GITT_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_WLTP.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_1C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_1C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_1C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_3C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_3C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_3C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_10C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_Co30_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_Co30_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_eVTOL.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_GITT_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_GITT_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_025degC_WLTP.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_1C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_1C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_1C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_3C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_3C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_3C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_10C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_Co30_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_Co30_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_eVTOL.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_GITT_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_GITT_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_040degC_WLTP.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_1C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_1C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_1C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_3C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_3C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_3C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_10C_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_Co30_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_Co30_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_eVTOL.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_GITT_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_GITT_Dch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_060degC_WLTP.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_1C_Ch.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `molicel_p45b_data.zip::MOLICEL_P45B_010degC_1C_Ch-charge.csv`: Experimental and optional simulated columns coexist according to the author PDF. -charge.csv is an alternate model case. Whole-cell Co30 and E_OCV_V must not be labelled electrode OCP; no CSV content read.
- `examples/params/Molicel_P45B_bpx.json`: Published BPX 1.1 DFN parameter package with graphite/silicon-additive particle branches, cathode OCP, diffusion and kinetic entries. Fitted/tuned parameterisation, not independently measured pure-silicon OCP or a native E-BatP import. Structure/header inspected; numerical arrays/units not audited. BSD-3-Clause author repository.
- `Molicel P45B Data Release Data Format Documentation.pdf`: Author README or format documentation inspected; no experimental observations in this locator.
- `readme_Molicel_P45B_dataset_AE.txt`: Author README or format documentation inspected; no experimental observations in this locator.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://zenodo.org/api/records/19052626). Zenodo states CC BY 4.0 for the test release; its README retains copyright/all-rights-reserved and liability notices. BPX is separately in the BSD-3-Clause author repository. Do not transfer license scope between these objects; no source payload is redistributed.

Review level: `archive_directory_reviewed`. All 51 ZIP member names/sizes, release metadata, README and two-page format PDF reviewed; BPX header/structure inspected. No observation CSV read. Published model parameters and measured/raw data are not merged.

- [molicel_p45b_data.zip](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_1C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_3C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_3C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_3C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_10C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_Co30_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_Co30_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_GITT_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_GITT_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_WLTP.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_1C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_1C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_1C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_3C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_3C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_3C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_10C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_Co30_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_Co30_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_eVTOL.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_GITT_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_GITT_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_025degC_WLTP.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_1C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_1C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_1C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_3C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_3C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_3C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_10C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_Co30_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_Co30_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_eVTOL.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_GITT_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_GITT_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_040degC_WLTP.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_1C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_1C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_1C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_3C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_3C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_3C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_10C_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_Co30_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_Co30_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_eVTOL.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_GITT_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_GITT_Dch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_060degC_WLTP.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_1C_Ch.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [MOLICEL_P45B_010degC_1C_Ch-charge.csv](https://zenodo.org/api/records/19052626/files/molicel_p45b_data.zip/content)
- [examples/params/Molicel_P45B_bpx.json](https://raw.githubusercontent.com/About-Energy-OpenSource/AEPyBaMM/188bd62ee2347cc486b66dc43e31fb9597759db1/examples/params/Molicel_P45B_bpx.json)
- [Molicel P45B Data Release Data Format Documentation.pdf](https://zenodo.org/api/records/19052626/files/Molicel%20P45B%20Data%20Release%20Data%20Format%20Documentation.pdf/content)
- [readme_Molicel_P45B_dataset_AE.txt](https://zenodo.org/api/records/19052626/files/readme_Molicel_P45B_dataset_AE.txt/content)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ocp-first-expansion-review.json)


## Missing items and limits

- No native catalog OCP/D/kinetics records for P45B; BPX arrays and parameter origins/units remain externally reviewable leads.
- Original harvested half-cell observations and their temperature not independently located; composite/silicon fitted OCP is not a measured pure-material curve.
- No eVTOL at 10 degC in the checked ZIP, no US06/EIS or longitudinal ageing source in this release.
- No independent-cell count from 51 files; measured/model columns and alternate model cases must remain separate.

## Evidence

- [Primary source 1](https://zenodo.org/records/19052626)
- [Primary source 2](https://zenodo.org/api/records/19052626)
- [Primary source 3](https://doi.org/10.1149/1945-7111/aea1c1)
- [Primary source 4](https://www.aboutenergy.io/post/molicel-p45b-electrochemical-model-open-source-dfn-parameter-set)
- [Primary source 5](https://raw.githubusercontent.com/About-Energy-OpenSource/AEPyBaMM/188bd62ee2347cc486b66dc43e31fb9597759db1/examples/params/Molicel_P45B_bpx.json)
- [Primary source 6](https://github.com/About-Energy-OpenSource/AEPyBaMM/tree/188bd62ee2347cc486b66dc43e31fb9597759db1)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
