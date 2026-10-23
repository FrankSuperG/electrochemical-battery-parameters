# HAIDI HDCF18650-1800 | Rehm2025 multi-temperature OCV, rate and GEIS source

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `haidi-lfp-rehm2025`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP. HAIDI Energy Group HDCF18650-1800, 1.8 Ah, LFP/graphite, 18650; paper LIBHE. Only this lithium-ion subset is indexed; two sodium-ion cell types in the source deposit are excluded.

[Open the original dataset](https://mediatum.ub.tum.de/1762675) · Version: `Published 2025-01-31; author half-cell mirror from fixed Zenodo 19555109. Original full-cell file inventory unresolved.`

DOI: 10.14459/2024mp1762675. Checked: 2026-10-24.

## Electrode OCP anchor

**Imported half-cell branches**. Seven native author-processed Li-reference half-cell branches at 25 C and 0.02/0.05C; preserved source capacity/rows. Same-study full-cell association, unresolved donor serials. Eighth original is quarantined and excluded from this admitted anchor.

Reported half-cell temperature labels / degC: [25]. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: `input_data/LFP/HAIDI18650_Anode_Delithiation_0C02.mat`; `input_data/LFP/HAIDI18650_Anode_Delithiation_0C05.mat`; `input_data/LFP/HAIDI18650_Anode_Lithiation_0C02.mat`; `input_data/LFP/HAIDI18650_Anode_Lithiation_0C05.mat`; `input_data/LFP/HAIDI18650_Cathode_Delithiation_0C02.mat`; `input_data/LFP/HAIDI18650_Cathode_Lithiation_0C02.mat`; `input_data/LFP/HAIDI18650_Cathode_Lithiation_0C05.mat`

OCP evidence: [Source 1](https://doi.org/10.1016/j.jpowsour.2025.236290) · [Source 2](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/README_additional_citations_necessary.txt)

## Tests and channels

Types: constant_current, cccv, pulse, eis, ocv. Profiles: No named drive profile verified.

Paper-defined full-cell protocol at 10/20/25/30/35/45 C: equal charge/discharge 0.1/0.2/0.33/0.5/0.67/1C; additional discharge 1.5/2/2.5C with charge held at 1C. CP load rates are E-rates, not C-rates. Quasi-OCV at 0.05C, relaxed OCV 0.1C pulses/rests; GEIS 0.01-100000 Hz, 15 points/decade, 0.1 A, eleven SOC levels. These are study conditions, not a verified file-by-temperature matrix.

Reported temperature labels / degC: [10, 20, 25, 30, 35, 45]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Original full-cell observation headers were not read. Paper conditions do not certify measured time/current/voltage/temperature or frequency/Z column availability.

## Ageing data

**Not reported**. Study characterizes fresh cells and uses new LIB cells per temperature to limit ageing effects. Repeated conditioning/rate cycles are not a longitudinal ageing dataset.

[Ageing coverage evidence](https://doi.org/10.1016/j.jpowsour.2025.236290). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `same_model_same_study`. The author HAIDI half-cell notice cites Rehm2025; the original paper identifies LIBHE as HDCF18650-1800 and points to this dataset. Exact serialized donors/test cells are not linked.

[HAIDI HDCF18650-1800 &#124; Rehm2025 LFP/graphite](../cells/haidi-hdcf18650-1800-rehm2025.md)

Components without a native catalog join: diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `same_model_same_study` / `electrode_ocp` | `haidi-rehm2025-anode-delithiation-0c02`, `haidi-rehm2025-anode-delithiation-0c05`, `haidi-rehm2025-anode-lithiation-0c02`, `haidi-rehm2025-anode-lithiation-0c05`, `haidi-rehm2025-cathode-delithiation-0c02`, `haidi-rehm2025-cathode-lithiation-0c02`, `haidi-rehm2025-cathode-lithiation-0c05` | Seven stored finite-current author-processed half-cell branches at 25 C: four graphite and three LFP. One additional LFP branch is quarantined; no equilibrium, absolute-stoichiometry or shared-specimen claim. Missing: Absolute stoichiometry/half-cell Ah; Exact donor/cycle/filtering history; One cathode branch held for protocol mismatch |
| diffusion | `missing` / `missing` | None | Same-study relaxed OCV/GITT traces do not define a reusable intrinsic diffusivity estimate. Missing: No same-study intrinsic D admitted |
| kinetics | `missing` / `missing` | None | GEIS observations do not independently define an intrinsic reaction-rate coefficient or i0 law. Missing: No same-study intrinsic kinetic law admitted |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `container_only` | Original paper describes 0.1-1C charge protocols at six temperatures; dataset links confirmed, individual original files not listed/read. |
| multi_rate_discharge | `container_only` | Original paper describes 0.1-2.5C discharge at six temperatures; charge stays 1C for the additional 1.5/2/2.5C discharge stages. Individual filenames unresolved. |
| EIS | `container_only` | GEIS in the paper and exact-DOI dataset description: six temperatures, eleven SOCs, 10 mHz-100 kHz, 0.1 A. File locations and frequency/Z headers not read. |
| US06 | `not_located` | No named road-cycle file found. Constant-power characterization is not relabeled US06 or a verified dynamic profile. |

## File locations

Eight real author-mirror half-cell paths plus one documentation-only original dataset access point. No whole-cell file name, archive format, cell serial or complete condition grid is invented. Counts are locators, not independent tests.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `input_data/LFP/HAIDI18650_Anode_Delithiation_0C02.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.02C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Delithiation_0C02.mat) |
| `input_data/LFP/HAIDI18650_Anode_Delithiation_0C05.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.05C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Delithiation_0C05.mat) |
| `input_data/LFP/HAIDI18650_Anode_Lithiation_0C02.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.02C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Lithiation_0C02.mat) |
| `input_data/LFP/HAIDI18650_Anode_Lithiation_0C05.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.05C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Lithiation_0C05.mat) |
| `input_data/LFP/HAIDI18650_Cathode_Delithiation_0C02.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.02C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Delithiation_0C02.mat) |
| `input_data/LFP/HAIDI18650_Cathode_Delithiation_0C05.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.05C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Delithiation_0C05.mat) |
| `input_data/LFP/HAIDI18650_Cathode_Lithiation_0C02.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.02C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Lithiation_0C02.mat) |
| `input_data/LFP/HAIDI18650_Cathode_Lithiation_0C05.mat` | HAIDI HDCF18650-1800 / No sample ID | ;  | 25 degC; 0.05C | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Lithiation_0C05.mat) |
| `Dataset landing page (not an observed filesystem path)` | HAIDI HDCF18650-1800 (LIBHE subset) / No sample ID | ;  | Temperature unknown | `source_documentation`; content `documentation_reviewed` | [Open dataset / documentation](https://mediatum.ub.tum.de/1762675) |

File notes:

- `input_data/LFP/HAIDI18650_Anode_Delithiation_0C02.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `input_data/LFP/HAIDI18650_Anode_Delithiation_0C05.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `input_data/LFP/HAIDI18650_Anode_Lithiation_0C02.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `input_data/LFP/HAIDI18650_Anode_Lithiation_0C05.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `input_data/LFP/HAIDI18650_Cathode_Delithiation_0C02.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `input_data/LFP/HAIDI18650_Cathode_Delithiation_0C05.mat`: Quarantined original: nine cathode nodes below the paper 2 V cutoff; no admitted CSV/record.
- `input_data/LFP/HAIDI18650_Cathode_Lithiation_0C02.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `input_data/LFP/HAIDI18650_Cathode_Lithiation_0C05.mat`: Native author-processed half-cell pseudo-OCP; all nodes and original capacity/row retained. 25 C and Li reference confirmed by original paper. Exact cycle/filtering history and raw-deposit byte identity unresolved.
- `Dataset landing page (not an observed filesystem path)`: Paper/catalog confirm same-study multi-temperature OCV, CC/CP and GEIS. This link is a dataset access point, not a verified file/ZIP or read observation. No individual full-cell filenames or headers established.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://data.gov.de/suche/daten/rate-capability-tests-ocv-measurements-impedance-and-half-cell-measurements-of-two-sodium-ion-b99db5). Exact-DOI TUM publisher record in open.bydata/GovData identifies CC-BY and author attribution; GovData license URL and official DCAT vocabulary resolve to CC BY 4.0. Empty DataCite rights and incomplete duplicate catalog records are documented. Framework MIT is not used to relicense the data. Full-cell observations remain external.

Review level: `existing_source_audit`. Original paper methods pages 3/4 visually checked; public publisher-catalog rights and eight author MATs reviewed, seven admitted and one quarantined. Original provider requests returned 429/timeouts; no full-cell payload/file inventory read or imported.

- [input_data/LFP/HAIDI18650_Anode_Delithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Delithiation_0C02.mat)
- [input_data/LFP/HAIDI18650_Anode_Delithiation_0C05.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Delithiation_0C05.mat)
- [input_data/LFP/HAIDI18650_Anode_Lithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Lithiation_0C02.mat)
- [input_data/LFP/HAIDI18650_Anode_Lithiation_0C05.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Anode_Lithiation_0C05.mat)
- [input_data/LFP/HAIDI18650_Cathode_Delithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Delithiation_0C02.mat)
- [input_data/LFP/HAIDI18650_Cathode_Delithiation_0C05.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Delithiation_0C05.mat)
- [input_data/LFP/HAIDI18650_Cathode_Lithiation_0C02.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Lithiation_0C02.mat)
- [input_data/LFP/HAIDI18650_Cathode_Lithiation_0C05.mat](https://raw.githubusercontent.com/tum-ees/DegradationModeAnalysis/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/HAIDI18650_Cathode_Lithiation_0C05.mat)
- [Original dataset landing page; full-cell file inventory unresolved](https://mediatum.ub.tum.de/1762675)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/haidi-rehm2025/review.json)


## Missing items and limits

- Exact harvested donor/full-cell serial mapping unresolved.
- Individual full-cell filenames, archive paths and observation headers unverified: provider landing/export requests unavailable; no payload imported.
- Absolute stoichiometry, half-cell Ah, exact MAT filtering and cycle selection history unresolved.
- One 0.05C cathode-delithiation MAT quarantined: nine nodes below the paper 2 V cutoff; no trimmed/repaired native curve.
- No same-study intrinsic D/kinetics admitted; relaxed OCV/GITT and GEIS observations are not automatically D or kinetic coefficients.
- Dynamic road profiles and longitudinal ageing series not established.
- Empty DataCite and incomplete duplicate GovData records retained in rights review; actual data grant comes from exact-DOI publisher distribution metadata.

## Evidence

- [Primary source 1](https://doi.org/10.1016/j.jpowsour.2025.236290)
- [Primary source 2](https://d-nb.info/1370379285/34)
- [Primary source 3](https://open.bydata.de/api/hub/search/datasets/10-14459-2024mp1762675)
- [Primary source 4](https://data.gov.de/suche/daten/rate-capability-tests-ocv-measurements-impedance-and-half-cell-measurements-of-two-sodium-ion-b99db5)
- [Primary source 5](https://www.dcat-ap.de/def/licenses/20260924)
- [Primary source 6](https://github.com/tum-ees/DegradationModeAnalysis/blob/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP/README_additional_citations_necessary.txt)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
