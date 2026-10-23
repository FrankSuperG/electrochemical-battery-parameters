# Molicel P45B harvested half-cell curves and 800-EFC checkup pseudo-OCV

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `tum-p45b-halfcell-aging-2026`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NCA. Molicel P45B; harvested blend-anode and cathode source files with one serial23 ageing checkup table. Author input folder labels cathode NCA. Different study from About:Energy P45B; no shared specimen or transfer of fitted parameters asserted.

[Open the original dataset](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30) · Version: `402bab94d20258162ff059b8d5d51abe40ec1c30`

DOI: 10.1016/j.jpowsour.2026.239418. Checked: 2026-10-23.

## Electrode OCP anchor

**External half-cell files**. Four harvested SiGr-anode branches and one cathode branch are source-listed; measured blend OCP stays distinct from reconstructed silicon and other literature curves in the repository. Same study/model as serial23 checkups, different/unresolved donors.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: `input_data/NCA/P45B_Cathode_Delithiation_0C03.mat`; `input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat`; `input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat`; `input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat`; `input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat`

OCP evidence: [Source 1](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/README_additional_citations_necessary.txt) · [Source 2](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/README_test_data.txt)

## Tests and channels

Types: ocv. Profiles: No named drive profile verified.

Measured blend half-cell filenames use 0C02/0C03 = 0.02C/0.03C, not temperatures. Full-cell table contains charge/discharge pOCV checkups over a reported 800 EFC; it is not a complete 800-cycle I/V/T history.

Reported temperature labels / degC: Not verified. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Observation headers and units were not independently read; source conditions remain distinct from measured channels.

## Ageing data

**Yes (cycle)**. Source README identifies serial23 pOCV checkups through 800 EFC, one of the paper's four cycled cells. No full continuous cycling log or same-specimen half-cell donor is certified.

[Ageing coverage evidence](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/README_test_data.txt). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters.

Components without a native catalog join: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |
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
| `input_data/NCA/P45B_Cathode_Delithiation_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.03C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/NCA/P45B_Cathode_Delithiation_0C03.mat) |
| `input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.02C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat) |
| `input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.03C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat) |
| `input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.02C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat) |
| `input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.03C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat) |
| `input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat) |
| `input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat) |
| `input_data/test_data/P45B_serial23_aging_data_table.mat` | Molicel P45B / serial23 | ocv;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/P45B_serial23_aging_data_table.mat) |

File notes:

- `input_data/NCA/P45B_Cathode_Delithiation_0C03.mat`: Measured finite-current harvested-electrode curve according to source README; MAT arrays/coordinates/reference and temperature remain unread.
- `input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat`: Measured finite-current harvested-electrode curve according to source README; MAT arrays/coordinates/reference and temperature remain unread.
- `input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat`: Measured finite-current harvested-electrode curve according to source README; MAT arrays/coordinates/reference and temperature remain unread.
- `input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat`: Measured finite-current harvested-electrode curve according to source README; MAT arrays/coordinates/reference and temperature remain unread.
- `input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat`: Measured finite-current harvested-electrode curve according to source README; MAT arrays/coordinates/reference and temperature remain unread.
- `input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat`: Reconstructed silicon curve, not a measured pure-silicon half cell; excluded from measured-half-cell anchor.
- `input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat`: Reconstructed silicon curve, not a measured pure-silicon half cell; excluded from measured-half-cell anchor.
- `input_data/test_data/P45B_serial23_aging_data_table.mat`: Whole-cell ageing pOCV checkup table; source reports 800 EFC. Raw continuous cycling I/V/T not established.

## Reuse and access

License: **not-stated**. [Source terms](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/README.md). Root framework LICENSE is MIT, but the README requires checking licenses/attribution for input_data from published sources. No separate blanket measurement-data license was established; retain links and per-source citation context. Do not apply the PyDMA Python mirror BSD license to this MATLAB dataset.

Review level: `source_file_listing`. Primary metadata, source documentation and file locations reviewed. No observation payload imported or source code executed.

- [input_data/NCA/P45B_Cathode_Delithiation_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/NCA/P45B_Cathode_Delithiation_0C03.mat)
- [input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat)
- [input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat)
- [input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat)
- [input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat)
- [input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat)
- [input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat)
- [input_data/test_data/P45B_serial23_aging_data_table.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/P45B_serial23_aging_data_table.mat)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ocp-first-expansion-review.json)


## Missing items and limits

- Measurement reuse scope needs clarification; framework code license is not used as a blanket relicensing of input_data.
- No raw MAT numerical inspection, verified half-cell temperature, donor-to-serial23 mapping, intrinsic D/k or native catalog parameter association.
- Ageing table contains checkup curves, not a verified continuous current/voltage/temperature ageing log. No dynamic road cycle, EIS or multi-temperature matrix established.
- Reconstructed silicon and third-party literature curves are not counted as measured pure-material OCP.

## Evidence

- [Primary source 1](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30)
- [Primary source 2](https://doi.org/10.1016/j.jpowsour.2026.239418)
- [Primary source 3](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/README_additional_citations_necessary.txt)
- [Primary source 4](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/README_test_data.txt)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
