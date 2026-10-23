# CALB generation 3b 58 Ah: harvested half-cell OCP, multi-temperature tests and ageing

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `nextbms-calb-nmc532-2026`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. CALB generation 3b 58 Ah prismatic NMC532/graphite. Half-cell donor Cell_96; characterization Cell_4/6/15; 41 ageing cells. Exact commercial part is not supplied; do not equate this with L148N58A by capacity/dimensions alone.

[Open the original dataset](https://zenodo.org/records/22301764) · Version: `fixed record 22301764`

DOI: 10.5281/zenodo.22301764. Checked: 2026-10-23.

## Electrode OCP anchor

**Imported half-cell branches**. Six harvested graphite/NMC532 slow-cycle and GITT CSV members are located from donor Cell_96. Same study and model as full-cell characterization/ageing, different specimens. Half-cell temperature and numerical OCP extraction remain unverified. Four finite-current branches are now extracted into the native catalog.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fCharge.csv`; `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fDischarge.csv`; `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-anode.csv`; `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fCharge.csv`; `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fDischarge.csv`; `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-cathode.csv`

OCP evidence: [Source 1](https://zenodo.org/records/22301764) · [Source 2](https://zenodo.org/api/records/22301764)

## Tests and channels

Types: constant_current, cccv, pulse, dynamic, eis, ocv. Profiles: No named drive profile verified.

Full-cell CC, GITT, dynamic cycles and HPPC plus calendar/cyclic ageing. Characterization EIS source labels: 0/5/25/45 degC. No complete same-state continuous rate-sweep matrix was checked.

Reported temperature labels / degC: [0, 5, 25, 45]. These are source conditions, not measured temperature channels.

Reported time-series channels: Time, Voltage [V], Current [A], Cell temp [degC], Chamber temp [degC].

Reported frequency-domain channels: frequency, real_impedance, imaginary_impedance.

Source-documented fields only. Time starts with one absolute timestamp, followed by incremental seconds; cumulative reconstruction is required. Characterization header has trailing whitespace. Source reports sub-second increments and isolated voltage spikes. Half-cell CSVs, time units, EIS segmentation and actual headers remain unread.

## Ageing data

**Yes (cycle, calendar)**. Primary source reports five calendar and 36 cyclic cells. Forty-one per-cell history filenames and overview files are located; stage-specific Cell_22 EIS paths also exist. Stage cohort counts in source prose and archive differ and are not reconciled.

[Ageing coverage evidence](https://zenodo.org/records/22301764). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `same_model_same_study`. Native extracted OCP/parameter records and external full-cell tests are linked by explicit study/model identity. No identical serialized specimen is asserted.

[CALB generation 3b &#124; NEXTBMS2026](../cells/calb-gen3b-nextbms2026.md)

Components without a native catalog join: diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `same_model_same_study` / `electrode_ocp` | `nextbms-calb-negative-charge`, `nextbms-calb-negative-discharge`, `nextbms-calb-positive-charge`, `nextbms-calb-positive-discharge` | Four finite-current half-cell branches extracted from the pinned same-study originals. Original source units and rows retained; no absolute lithium-fraction mapping inferred. Missing: Identical serialized specimen unresolved |
| diffusion | `missing` / `missing` | None | No intrinsic diffusion or kinetic coefficient transcribed from this study; GITT/rate capability alone does not uniquely identify a coefficient. Missing: No verified current-catalog record for this component and study. |
| kinetics | `missing` / `missing` | None | No intrinsic diffusion or kinetic coefficient transcribed from this study; GITT/rate capability alone does not uniquely identify a coefficient. Missing: No verified current-catalog record for this component and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| multi_rate_discharge | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| US06 | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| EIS | `archive_member_located` | Twelve characterization impedance CSVs across three source cells and four temperature labels; Cell_22 has all three ageing-stage impedance filenames. Raw spectra and SoC segments remain unread. |

## File locations

Selected confirmed source paths and parameter evidence. Counts describe locators, not independent experiments or a complete cell-by-temperature matrix.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `2_HalfCell.7z` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fCharge.csv` | CALB generation 3b 58 Ah / Cell_96 (harvested donor) | ;  | Temperature unknown | `archive_directory`; content `existing_source_audit` | [Parent archive](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fDischarge.csv` | CALB generation 3b 58 Ah / Cell_96 (harvested donor) | ;  | Temperature unknown | `archive_directory`; content `existing_source_audit` | [Parent archive](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-anode.csv` | CALB generation 3b 58 Ah / Cell_96 (harvested donor) | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fCharge.csv` | CALB generation 3b 58 Ah / Cell_96 (harvested donor) | ;  | Temperature unknown | `archive_directory`; content `existing_source_audit` | [Parent archive](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fDischarge.csv` | CALB generation 3b 58 Ah / Cell_96 (harvested donor) | ;  | Temperature unknown | `archive_directory`; content `existing_source_audit` | [Parent archive](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-cathode.csv` | CALB generation 3b 58 Ah / Cell_96 (harvested donor) | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content) |
| `3_Characterization.7z` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_2-GITT.csv` | CALB generation 3b 58 Ah / Cell_15 | pulse;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_3-CC_cycles.csv` | CALB generation 3b 58 Ah / Cell_15 | constant_current;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_4-DynamicCycles.csv` | CALB generation 3b 58 Ah / Cell_15 | dynamic;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_5-HPPC.csv` | CALB generation 3b 58 Ah / Cell_15 | pulse;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_0C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_15 | eis;  | 0 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_25C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_15 | eis;  | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_45C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_15 | eis;  | 45 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_5C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_15 | eis;  | 5 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_2-GITT.csv` | CALB generation 3b 58 Ah / Cell_4 | pulse;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_3-CC_cycles.csv` | CALB generation 3b 58 Ah / Cell_4 | constant_current;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_4-DynamicCycles.csv` | CALB generation 3b 58 Ah / Cell_4 | dynamic;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_5-HPPC.csv` | CALB generation 3b 58 Ah / Cell_4 | pulse;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_0C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_4 | eis;  | 0 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_25C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_4 | eis;  | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_45C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_4 | eis;  | 45 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_5C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_4 | eis;  | 5 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_2-GITT.csv` | CALB generation 3b 58 Ah / Cell_6 | pulse;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_3-CC_cycles.csv` | CALB generation 3b 58 Ah / Cell_6 | constant_current;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_4-DynamicCycles.csv` | CALB generation 3b 58 Ah / Cell_6 | dynamic;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_5-HPPC.csv` | CALB generation 3b 58 Ah / Cell_6 | pulse;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_0C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_6 | eis;  | 0 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_25C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_6 | eis;  | 25 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_45C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_6 | eis;  | 45 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_5C_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_6 | eis;  | 5 degC | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content) |
| `4_Ageing.7z` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_11/Cell_11.csv` | CALB generation 3b 58 Ah / Cell_11 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_26/Cell_26.csv` | CALB generation 3b 58 Ah / Cell_26 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_28/Cell_28.csv` | CALB generation 3b 58 Ah / Cell_28 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_45/Cell_45.csv` | CALB generation 3b 58 Ah / Cell_45 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_57/Cell_57.csv` | CALB generation 3b 58 Ah / Cell_57 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/OverviewCapacityData_5cell.csv` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Calendar_ageing_data/OverviewResistanceData_5cell.csv` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_1/Cell_1.csv` | CALB generation 3b 58 Ah / Cell_1 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_12/Cell_12.csv` | CALB generation 3b 58 Ah / Cell_12 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_16/Cell_16.csv` | CALB generation 3b 58 Ah / Cell_16 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_17/Cell_17.csv` | CALB generation 3b 58 Ah / Cell_17 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_22/Cell_22.csv` | CALB generation 3b 58 Ah / Cell_22 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_23/Cell_23.csv` | CALB generation 3b 58 Ah / Cell_23 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_25/Cell_25.csv` | CALB generation 3b 58 Ah / Cell_25 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_27/Cell_27.csv` | CALB generation 3b 58 Ah / Cell_27 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_29/Cell_29.csv` | CALB generation 3b 58 Ah / Cell_29 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_3/Cell_3.csv` | CALB generation 3b 58 Ah / Cell_3 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_30/Cell_30.csv` | CALB generation 3b 58 Ah / Cell_30 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_34/Cell_34.csv` | CALB generation 3b 58 Ah / Cell_34 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_35/Cell_35.csv` | CALB generation 3b 58 Ah / Cell_35 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_40/Cell_40.csv` | CALB generation 3b 58 Ah / Cell_40 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_42/Cell_42.csv` | CALB generation 3b 58 Ah / Cell_42 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_43/Cell_43.csv` | CALB generation 3b 58 Ah / Cell_43 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_46/Cell_46.csv` | CALB generation 3b 58 Ah / Cell_46 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_47/Cell_47.csv` | CALB generation 3b 58 Ah / Cell_47 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_49/Cell_49.csv` | CALB generation 3b 58 Ah / Cell_49 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_5/Cell_5.csv` | CALB generation 3b 58 Ah / Cell_5 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_50/Cell_50.csv` | CALB generation 3b 58 Ah / Cell_50 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_53/Cell_53.csv` | CALB generation 3b 58 Ah / Cell_53 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_56/Cell_56.csv` | CALB generation 3b 58 Ah / Cell_56 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_60/Cell_60.csv` | CALB generation 3b 58 Ah / Cell_60 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_63/Cell_63.csv` | CALB generation 3b 58 Ah / Cell_63 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_64/Cell_64.csv` | CALB generation 3b 58 Ah / Cell_64 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_66/Cell_66.csv` | CALB generation 3b 58 Ah / Cell_66 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_68/Cell_68.csv` | CALB generation 3b 58 Ah / Cell_68 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_70/Cell_70.csv` | CALB generation 3b 58 Ah / Cell_70 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_71/Cell_71.csv` | CALB generation 3b 58 Ah / Cell_71 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_72/Cell_72.csv` | CALB generation 3b 58 Ah / Cell_72 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_74/Cell_74.csv` | CALB generation 3b 58 Ah / Cell_74 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_8/Cell_8.csv` | CALB generation 3b 58 Ah / Cell_8 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_89/Cell_89.csv` | CALB generation 3b 58 Ah / Cell_89 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_9/Cell_9.csv` | CALB generation 3b 58 Ah / Cell_9 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_93/Cell_93.csv` | CALB generation 3b 58 Ah / Cell_93 | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/OverviewCapacityData_36cell.csv` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/OverviewResistanceData_36cell.csv` | CALB generation 3b 58 Ah / No sample ID | ;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/EIS_data/1_BOL_EIS/Cell_22_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_22 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/EIS_data/2_MOL_EIS/Cell_22_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_22 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |
| `4_Ageing.7z::4_Ageing/EIS_data/3_EOL_EIS/Cell_22_impedanceData.csv` | CALB generation 3b 58 Ah / Cell_22 | eis;  | Temperature unknown | `archive_directory`; content `not_read` | [Parent archive](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content) |

File notes:

- `2_HalfCell.7z`: Parent archive only; no observation payload downloaded.
- `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fCharge.csv`: Harvested half-cell slow cycle/GITT source. This is electrode evidence, not a full-cell test; numerical branches, reference, coordinates and temperature have not been independently read. Selected OCP/parameter values are now retained in native records with pinned original-source evidence.
- `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fDischarge.csv`: Harvested half-cell slow cycle/GITT source. This is electrode evidence, not a full-cell test; numerical branches, reference, coordinates and temperature have not been independently read. Selected OCP/parameter values are now retained in native records with pinned original-source evidence.
- `2_HalfCell.7z::2_HalfCell/OCP_data/Anode_Graphite/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-anode.csv`: Harvested half-cell slow cycle/GITT source. This is electrode evidence, not a full-cell test; numerical branches, reference, coordinates and temperature have not been independently read.
- `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fCharge.csv`: Harvested half-cell slow cycle/GITT source. This is electrode evidence, not a full-cell test; numerical branches, reference, coordinates and temperature have not been independently read. Selected OCP/parameter values are now retained in native records with pinned original-source evidence.
- `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fDischarge.csv`: Harvested half-cell slow cycle/GITT source. This is electrode evidence, not a full-cell test; numerical branches, reference, coordinates and temperature have not been independently read. Selected OCP/parameter values are now retained in native records with pinned original-source evidence.
- `2_HalfCell.7z::2_HalfCell/OCP_data/Cathode_NMC532/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-cathode.csv`: Harvested half-cell slow cycle/GITT source. This is electrode evidence, not a full-cell test; numerical branches, reference, coordinates and temperature have not been independently read.
- `3_Characterization.7z`: Parent archive only; no observation payload downloaded.
- `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_2-GITT.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_3-CC_cycles.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_4-DynamicCycles.csv`: Named DynamicCycles member; no road-cycle name (US06/WLTP) or phase boundaries inferred.
- `3_Characterization.7z::3_Characterization/Cell_15/Cell_15_5-HPPC.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_0C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_25C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_45C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_15/EIS/Test_5C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_2-GITT.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_3-CC_cycles.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_4-DynamicCycles.csv`: Named DynamicCycles member; no road-cycle name (US06/WLTP) or phase boundaries inferred.
- `3_Characterization.7z::3_Characterization/Cell_4/Cell_4_5-HPPC.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_0C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_25C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_45C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_4/EIS/Test_5C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_2-GITT.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_3-CC_cycles.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_4-DynamicCycles.csv`: Named DynamicCycles member; no road-cycle name (US06/WLTP) or phase boundaries inferred.
- `3_Characterization.7z::3_Characterization/Cell_6/Cell_6_5-HPPC.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_0C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_25C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_45C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `3_Characterization.7z::3_Characterization/Cell_6/EIS/Test_5C_impedanceData.csv`: Name/size verified from archive headers only; columns and payload checksum remain unverified.
- `4_Ageing.7z`: Parent archive only; no observation payload downloaded.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_11/Cell_11.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_26/Cell_26.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_28/Cell_28.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_45/Cell_45.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/Cell_57/Cell_57.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/OverviewCapacityData_5cell.csv`: Derived overview table of checkup capacity/resistance; not a raw voltage/current trace.
- `4_Ageing.7z::4_Ageing/Calendar_ageing_data/OverviewResistanceData_5cell.csv`: Derived overview table of checkup capacity/resistance; not a raw voltage/current trace.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_1/Cell_1.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_12/Cell_12.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_16/Cell_16.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_17/Cell_17.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_22/Cell_22.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_23/Cell_23.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_25/Cell_25.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_27/Cell_27.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_29/Cell_29.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_3/Cell_3.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_30/Cell_30.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_34/Cell_34.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_35/Cell_35.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_40/Cell_40.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_42/Cell_42.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_43/Cell_43.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_46/Cell_46.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_47/Cell_47.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_49/Cell_49.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_5/Cell_5.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_50/Cell_50.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_53/Cell_53.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_56/Cell_56.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_60/Cell_60.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_63/Cell_63.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_64/Cell_64.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_66/Cell_66.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_68/Cell_68.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_70/Cell_70.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_71/Cell_71.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_72/Cell_72.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_74/Cell_74.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_8/Cell_8.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_89/Cell_89.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_9/Cell_9.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/Cell_93/Cell_93.csv`: Per-cell ageing/history container. Source-documentation conditions are not assigned by filename; time increments, columns and within-file phases remain unchecked.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/OverviewCapacityData_36cell.csv`: Derived overview table of checkup capacity/resistance; not a raw voltage/current trace.
- `4_Ageing.7z::4_Ageing/Cyclic_ageing_data/OverviewResistanceData_36cell.csv`: Derived overview table of checkup capacity/resistance; not a raw voltage/current trace.
- `4_Ageing.7z::4_Ageing/EIS_data/1_BOL_EIS/Cell_22_impedanceData.csv`: Same source cell label at this BoL/MoL/EoL stage; spectrum columns and exact sampling conditions remain unread.
- `4_Ageing.7z::4_Ageing/EIS_data/2_MOL_EIS/Cell_22_impedanceData.csv`: Same source cell label at this BoL/MoL/EoL stage; spectrum columns and exact sampling conditions remain unread.
- `4_Ageing.7z::4_Ageing/EIS_data/3_EOL_EIS/Cell_22_impedanceData.csv`: Same source cell label at this BoL/MoL/EoL stage; spectrum columns and exact sampling conditions remain unread.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://zenodo.org/api/records/22301764). Primary metadata explicitly states CC BY 4.0 for data. Separate author analysis code is MIT. Only metadata and external links are packaged.

Review level: `existing_source_audit`. Complete 2_HalfCell, 3_Characterization and 4_Ageing 7z directories inspected with py7zr 1.1.0 via bounded HTTP ranges. Only 520/1405/7333 metadata bytes read respectively; no member extracted. Source/documented counts and directory counts are kept separate. Follow-up: selected half-cell/parameter originals were read, pinned and extracted by scripts/seed_parameter_sources.py. Full-cell observation payloads remain unread and external.

- [2_HalfCell.7z](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fCharge.csv](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [2_HalfCell/OCP_data/Anode_Graphite/anode_NExtBMS_fDischarge.csv](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [2_HalfCell/OCP_data/Anode_Graphite/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-anode.csv](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fCharge.csv](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [2_HalfCell/OCP_data/Cathode_NMC532/cathode_NExtBMS_fDischarge.csv](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [2_HalfCell/OCP_data/Cathode_NMC532/NEXTMBS-full-charge-discharge-GITT-full0charge-discharge-NMC-cathode.csv](https://zenodo.org/api/records/22301764/files/2_HalfCell.7z/content)
- [3_Characterization.7z](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/Cell_15_2-GITT.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/Cell_15_3-CC_cycles.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/Cell_15_4-DynamicCycles.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/Cell_15_5-HPPC.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/EIS/Test_0C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/EIS/Test_25C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/EIS/Test_45C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_15/EIS/Test_5C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/Cell_4_2-GITT.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/Cell_4_3-CC_cycles.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/Cell_4_4-DynamicCycles.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/Cell_4_5-HPPC.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/EIS/Test_0C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/EIS/Test_25C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/EIS/Test_45C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_4/EIS/Test_5C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/Cell_6_2-GITT.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/Cell_6_3-CC_cycles.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/Cell_6_4-DynamicCycles.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/Cell_6_5-HPPC.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/EIS/Test_0C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/EIS/Test_25C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/EIS/Test_45C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [3_Characterization/Cell_6/EIS/Test_5C_impedanceData.csv](https://zenodo.org/api/records/22301764/files/3_Characterization.7z/content)
- [4_Ageing.7z](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/Cell_11/Cell_11.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/Cell_26/Cell_26.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/Cell_28/Cell_28.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/Cell_45/Cell_45.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/Cell_57/Cell_57.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/OverviewCapacityData_5cell.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Calendar_ageing_data/OverviewResistanceData_5cell.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_1/Cell_1.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_12/Cell_12.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_16/Cell_16.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_17/Cell_17.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_22/Cell_22.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_23/Cell_23.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_25/Cell_25.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_27/Cell_27.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_29/Cell_29.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_3/Cell_3.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_30/Cell_30.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_34/Cell_34.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_35/Cell_35.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_40/Cell_40.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_42/Cell_42.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_43/Cell_43.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_46/Cell_46.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_47/Cell_47.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_49/Cell_49.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_5/Cell_5.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_50/Cell_50.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_53/Cell_53.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_56/Cell_56.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_60/Cell_60.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_63/Cell_63.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_64/Cell_64.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_66/Cell_66.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_68/Cell_68.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_70/Cell_70.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_71/Cell_71.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_72/Cell_72.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_74/Cell_74.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_8/Cell_8.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_89/Cell_89.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_9/Cell_9.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/Cell_93/Cell_93.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/OverviewCapacityData_36cell.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/Cyclic_ageing_data/OverviewResistanceData_36cell.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/EIS_data/1_BOL_EIS/Cell_22_impedanceData.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/EIS_data/2_MOL_EIS/Cell_22_impedanceData.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)
- [4_Ageing/EIS_data/3_EOL_EIS/Cell_22_impedanceData.csv](https://zenodo.org/api/records/22301764/files/4_Ageing.7z/content)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ocp-first-expansion-review.json)


## Missing items and limits

- Source prose lists 22/13/17 ageing-EIS cells at BoL/MoL/EoL; the archive has 25/16/20 impedance CSV names. The extra labels are not characterization Cell_4/6/15. No silent reconciliation or completeness claim.
- OCPDis_Cell_*.csv in cyclic ageing are whole-cell checkup extracts, not harvested-electrode OCP.
- No US06 name or complete multi-rate charge/discharge matrix verified. Gen3b is not equated to an existing CALB model by nominal capacity.
- Four slow-sweep half-cell branches imported; GITT rest-endpoint extraction and intrinsic D/kinetics remain absent.
- Half-cell reference versus lithium is established by packaged README; absolute stoichiometry, half-cell temperature and donor-to-characterization serial identity remain unresolved.

## Evidence

- [Primary source 1](https://zenodo.org/records/22301764)
- [Primary source 2](https://zenodo.org/api/records/22301764)
- [Primary source 3](https://arxiv.org/abs/2610.23049)
- [Primary source 4](https://github.com/robinson-medina/Analysis_Of_NMC_Dataset)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
