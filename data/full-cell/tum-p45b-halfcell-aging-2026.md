# Molicel P45B harvested half-cell curves and 800-EFC checkup pseudo-OCV

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `tum-p45b-halfcell-aging-2026`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NCA. Molicel P45B; harvested blend-anode and cathode source files with one serial23 ageing checkup table. Author input folder labels cathode NCA. Different study from About:Energy P45B; no shared specimen or transfer of fitted parameters asserted.

[Open the original dataset](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30) · Version: `402bab94d20258162ff059b8d5d51abe40ec1c30`

DOI: 10.1016/j.jpowsour.2026.239418. Checked: 2026-10-23.

## Electrode OCP anchor

**Imported half-cell branches**. Five harvested P45B pseudo-OCP branches are native under the scoped first-party MIT admission. Same paper/model as serial23 checkups; exact donor mapping unresolved. Laboratory graphite comparator remains material-only.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: `input_data/NCA/P45B_Cathode_Delithiation_0C03.mat`; `input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat`; `input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat`; `input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat`; `input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat`

OCP evidence: [Source 1](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/README_additional_citations_necessary.txt) · [Source 2](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/README_test_data.txt) · [Source 3](https://zenodo.org/records/19555109)

## Tests and channels

Types: ocv. Profiles: No named drive profile verified.

Half-cell filenames use 0C02/0C03 = 0.02C/0.03C; paper Section 2.4 writes 0.02C/0.033C. Full-cell ageing protocol: 1C CCCV charge, 1.5C CC discharge at 25 C; pOCV checkups 0.033C. Protocol descriptions do not certify a complete cycling I/V/T file.

Reported temperature labels / degC: [25]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

25 C is the original paper full-cell ageing condition, not a verified measured temperature channel. Full-cell MAT observation headers/units remain unread.

## Ageing data

**Yes (cycle)**. Source README identifies serial23 pOCV checkups through 800 EFC, one of the paper's four cycled cells. No full continuous cycling log or same-specimen half-cell donor is certified.

[Ageing coverage evidence](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/README_test_data.txt). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `same_model_same_study`. Five native harvested P45B pseudo-OCP branches and serial23 checkups share the Rehm2026 study/model. Same serialized donor is unresolved. About:Energy BPX is a separate study.

[Molicel P45B &#124; TUM Rehm2026 measured half-cells](../cells/molicel-p45b-tum-rehm2026.md)

Components without a native catalog join: diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `same_model_same_study` / `electrode_ocp` | `tum-rehm2026-p45b-cathode-delithiation-0c03`, `tum-rehm2026-p45b-anode-delithiation-0c02`, `tum-rehm2026-p45b-anode-delithiation-0c03`, `tum-rehm2026-p45b-anode-lithiation-0c02`, `tum-rehm2026-p45b-anode-lithiation-0c03` | Five finite-current harvested P45B half-cell branches, not equilibrium certification. Native source nodes, Li reference and branch-progress processing are documented. Missing: Numeric half-cell temperature; Absolute stoichiometric endpoints; Identical donor-to-serial23 mapping |
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
| `input_data/NCA/P45B_Cathode_Delithiation_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.03C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/NCA/P45B_Cathode_Delithiation_0C03.mat) |
| `input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.02C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat) |
| `input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.03C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat) |
| `input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.02C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat) |
| `input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown; 0.03C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat) |
| `input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat) |
| `input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat` | Molicel P45B / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat) |
| `input_data/test_data/P45B_serial23_aging_data_table.mat` | Molicel P45B / serial23 | ocv;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/P45B_serial23_aging_data_table.mat) |

File notes:

- `input_data/NCA/P45B_Cathode_Delithiation_0C03.mat`: Numerical MAT branch extracted to native catalog; relative capacity, Li reference and author direction checked. Numeric half-cell temperature unresolved. 0C03 filename says 0.03C; paper protocol says 0.033C.
- `input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat`: Numerical MAT branch extracted to native catalog; relative capacity, Li reference and author direction checked. Numeric half-cell temperature unresolved. 0C03 filename says 0.03C; paper protocol says 0.033C.
- `input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat`: Numerical MAT branch extracted to native catalog; relative capacity, Li reference and author direction checked. Numeric half-cell temperature unresolved. 0C03 filename says 0.03C; paper protocol says 0.033C.
- `input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat`: Numerical MAT branch extracted to native catalog; relative capacity, Li reference and author direction checked. Numeric half-cell temperature unresolved. 0C03 filename says 0.03C; paper protocol says 0.033C.
- `input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat`: Numerical MAT branch extracted to native catalog; relative capacity, Li reference and author direction checked. Numeric half-cell temperature unresolved. 0C03 filename says 0.03C; paper protocol says 0.033C.
- `input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat`: Reconstructed silicon curve, not a measured pure-silicon half cell; excluded from measured-half-cell anchor.
- `input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat`: Reconstructed silicon curve, not a measured pure-silicon half cell; excluded from measured-half-cell anchor.
- `input_data/test_data/P45B_serial23_aging_data_table.mat`: Source-listed ageing pOCV checkups. 25 C is paper ageing condition; measured temperature, raw current/time channels and continuous cycling history not inspected. Same half-cell donor unresolved.

## Reuse and access

License: **MIT**. [Source terms](https://zenodo.org/records/19555109). Scoped to first-party Rehm2026/P45B release data and the author serial23 example. Fixed v2.0.0 metadata, bundled Mathias Rehm MIT notice and per-folder own-measurement attribution provide the combined basis. Not a blanket license for third-party literature inputs or other-model curves. Seven half-cell originals only are packaged; full-cell observations remain external.

Review level: `existing_source_audit`. Seven allowlisted first-party half-cell MATs read numerically against fixed v2.0.0; paper definitions and release license reviewed. Full-cell table contents remain unread; no full-cell payload packaged or author code executed.

- [input_data/NCA/P45B_Cathode_Delithiation_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/NCA/P45B_Cathode_Delithiation_0C03.mat)
- [input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C02.mat)
- [input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Delithiation_0C03.mat)
- [input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C02.mat)
- [input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/P45B_Anode_Lithiation_0C03.mat)
- [input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Delithiation_Rehm2026_P45B_Anode_0C03.mat)
- [input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon/SiReconstr_Lithiation_Rehm2026_P45B_Anode_0C03.mat)
- [input_data/test_data/P45B_serial23_aging_data_table.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/P45B_serial23_aging_data_table.mat)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ocp-first-expansion-review.json)


[Supporting evidence (JSON)](../../src/ebp/data/evidence/tum-rehm2026/rights-review.json)


## Missing items and limits

- Exact harvested donor-to-serial23 chain, half-cell numeric temperature and absolute stoichiometric balancing unresolved.
- No same-study intrinsic D/k imported; About:Energy fitted parameters are not transferred.
- Ageing table is a source-listed checkup file, not an inspected continuous current/voltage/temperature ageing log. No dynamic road cycle, EIS or multi-temperature matrix established.
- Reconstructed silicon and third-party literature curves excluded from measured OCP admission.
- Filename 0.03C and paper 0.033C labels retained separately.

## Evidence

- [Primary source 1](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30)
- [Primary source 2](https://doi.org/10.1016/j.jpowsour.2026.239418)
- [Primary source 3](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/silicon-graphite/README_additional_citations_necessary.txt)
- [Primary source 4](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/test_data/README_test_data.txt)
- [Primary source 5](https://zenodo.org/records/19555109)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
