# Changelog

## 0.11.0 — 2026-10-23

- Screened 21 source families using electrode half-cell OCP as the entry point; added five external sources and 194 locators, reaching sixteen sources / 427 locators without adding observation payloads or numeric curve/parameter records.
- Located NEXTBMS harvested graphite/NMC532 files, full-cell CC/dynamic histories, 41 ageing histories and multi-temperature EIS through bounded 7z header reads; retained disagreement between declared and directory EIS stage counts.
- Linked About:Energy P45B published composite BPX parameters to explicitly reused CC/GITT/WLTP tests at 10/25/40/60 degC and eVTOL at 25/40/60 degC. Kept fitted OCP, whole-cell pseudo-OCV and simulated columns distinct from raw half-cell observations.
- Linked TUM P45B measured blend/cathode sources with one ageing checkup table; reconstructed silicon and third-party literature inputs retain separate origins and reuse gaps.
- Added LG M50 TEC2021 discharge files at 0/10/25 degC with explicit Chen2020 OCP reuse, and LG MJ1 80-cell dynamic ageing with a same-model, different-study reference to existing DLR-SINTEF half-cell curves. No intrinsic-parameter transfer or shared-specimen join is inferred.
- Added required OCP-anchor metadata, separate half-cell temperature scope and GitHub/viewer/CSV presentation (schema 1.3). Extended the optional archive inspector to 7z through a task-specific extra; no automatic downloads or model simulation.

## 0.10.0 — 2026-10-23

- Added four Panasonic NCR18650B external source records: HNEI formation/full-cell and harvested half-cell RPT, Bayreuth beginning-of-life pseudo-OCV/pulse/EIS, Virtual Vehicle ageing/reference tests, and the NCA section of Stanford multi-rate discharge tests.
- Added 151 metadata-only locators, reaching 233 across eleven sources. Kept all new MAT/CSV/XLSX/H5 observations external; preserved source file names, publisher checksums, versioned links, license gaps and unmatched OCP/D/kinetics.
- Verified the HNEI ZIP directory and same-study half/full-cell file locations without extracting MAT data. No equilibrium OCP, intrinsic D/k or cross-study specimen join is inferred.
- Added an evidence-backed Ageing data column, viewer/API/CLI filtering and CSV fields. Available, not reported and unverified are distinct; formation, initial repeats and degradation emulations do not count as measured ageing series.
- Recorded 116 external H5 cell files and protocol-documentation limits, including project-end censoring and ambiguous profile-to-cell IDs. Retained CC0 1.0 / CC BY 4.0 source terms; the Bayreuth record has no stated license in the inspected metadata.
- Advanced external metadata schema to 1.2 for required ageing evidence and documentation-file review; packaged scientific observations and parameter values are unchanged.

## 0.9.1 — 2026-10-23

- Audited all seven external records at file/container level; added 82 selected locators, source paths, sample labels and review scope without importing observation payloads.
- Located A123 1–4C CCCV and UDDS MAT files, CALB processed/raw CC/US06/EIS files and source-table CALCE ZIP links. Verified representative CALCE inner filenames and a complete LFP EIS RAR directory using bounded range reads.
- Added CALCE A123 US06 coverage based on two combined DST-US06-FUDS workbook filenames, without asserting phase boundaries or exact commercial-cell identity.
- Recorded 440 EIS CSV paths across B01–B11, two runs and twenty SOC filename labels in the 600 mAh LFP source; IFR14500 remains a filename designation, not a verified manufacturer part.
- Linked M50LT EIS to six same-study diffusion/kinetic group records; preserved missing electrode OCP rights and intrinsic D/k. Other external sources remain unmatched to catalog parameters.
- Added per-component and requested-test coverage, file-level filtering (`ebp datasets --files`), a file-locator CSV and an optional archive-directory inspector. Dataset-level profile declarations are not inherited by uninspected file locators.

## 0.9.0 — 2026-10-23

- Added seven metadata-only external dataset links for multi-rate charging, dynamic profiles including US06/UDDS/WLTP, pulses and EIS, with explicit review levels, licenses, parameter matches and missing items. No new raw test files were imported.
- Added LFP/NMC/NCA/LCO/NCO full-cell navigation, machine-readable link exports, `Catalog.search_datasets()` and `ebp datasets` filters.
- Added viewer material, test-type and drive-profile filters. External links remain separate from the 61 existing packaged files; NCO retains its original label and multi-chemistry coverage stays at dataset grain.

- Focused the project on parameter and experimental-data curation, provenance,
  matching and export. Removed the CPG-SPMT validation plan and benchmark roadmap.
- Clarified that `ebp validate` checks catalog integrity and that optional
  PyBaMM support exports OCP components without running a cell model.
- Retained associated full-cell observations, source-reported model context,
  matching evidence, missing-item ledgers and per-source reuse terms.

## 0.8.0 — 2026-10-17

- Curated LG MJ1 / DLR-SINTEF: four finite-current pseudo-OCP tables, 22 scalar/specification records, eight laboratory D/i0 tables and twelve direction/model-specific GITT diffusion tables with original error bounds. No intact-cell full-cell trace was verified or imported.
- Preserved CC BY 4.0 source bytes/selected laboratory cells and metadata; kept the literature-containing full XLSX external and separated the paper's CC BY 3.0 license. Used original workbook values instead of Parquet zero substitutions for missing endpoints, with unit conversions and source rows explicit.
- Added native non-OCP table evaluation, bounded linear interpolation, CSV downloads and offline packaging. Source-reported electrode coordinates require explicit PyBaMM mapping.
- Recorded NMC composition, units, stoichiometry-label and geometry differences; excluded ambiguous concentrations/initial states and kept reassembled-cell settings separate from commercial-cell components.
- Reached 59 electrode curves, 397 other parameter records, 61 full-cell exports, 13 material labels and 13 cell/study entries. Refreshed public-release documentation and corrected stale candidate wording; repository visibility remains private.

## 0.7.0 — 2026-10-17

- Curated LG M50LT / Hallemans2025: 18 jointly EIS-fitted grouped-SPMe parameters, one measured t/I/V drive cycle (164,953 rows), and 585 frequency-domain evidence rows with measured/model components distinguished.
- Verified the seven-SOC measured EIS slice byte-for-value against the fit MAT; checked parameter ordering and v4 paper definitions, including relative porosity, stoichiometry orientation and the separator-group conversion-helper discrepancy.
- Retained BSD-3-Clause author data/scripts and notices. About:Energy OCP permission remains unresolved; OCP files stay external leads without redistributed data or samples.
- Added cell-scoped CSV/JSON links, original evidence, an English curation guide and offline bundle support. Temperature, standalone CC tests, intrinsic coefficients and exact specimen mapping remain explicit gaps.
- Catalog now holds 55 electrode curves, 355 other parameter records and 61 full-cell exports across 12 cell/study entries; no independent model-validation or public-deployment claim.

## 0.6.0 — 2026-10-17

- Curated ISU-UConn's author-selected two half-cell specimens into four finite-current pseudo-OCP branches and 21 full-cell V-Q branches from eleven configurations; retained workbook addresses, unknown reference details, and missing I/t/T.
- Curated A123 18650M1A / Jahn2024 data v2: two modeled PD-ECM OCPn arrays and fourteen full-cell branch/array exports (low-rate cycle, incremental OCV, power tests and nine hysteresis loops).
- Added original source bytes, hashes, license evidence, attribution/change notices and reproducible selection scripts without executing upstream code. Intrinsic diffusion/kinetic coverage remains missing for both additions.
- Reached 55 electrode-curve records, 337 other parameters and 60 full-cell exports across eleven cell/study entries. Modeled OCPn is labeled separately from measured pseudo-OCP and published tables.
- Added model-coordinate and unresolved-reference metadata, guarded PyBaMM adaptation, explicit viewer labels, and cell JSON packages even when no non-OCP values are available.

### Prepublication fixes included

- Added a reproducible prepublication audit and a separate, source-backed data-candidate ledger; candidate observations are not counted as imported records.
- Fixed LG M50 solid diffusivity classification so both electrode values appear under the diffusion filter; values, units and source evidence are unchanged, with record versions advanced to 2.
- Included GitHub navigation exports, contribution templates and issue/PR files in source distributions.
- Corrected license file patterns and historical Mohtat no-import wording; made access instructions work with either public or restricted repository visibility.

## 0.5.0 — 2026-10-16

- Retrieved ten official Mohtat author files under CC BY 4.0 and retained five charge-capacity/voltage/temperature series: 6,474 observations, with current and original time explicitly absent.
- Added 33 author inputs and two OCP expressions alongside, rather than replacing, the PyBaMM variant; documented the graphite-offset and other model differences.
- Reached 49 OCP records, 337 other parameters, 25 full-cell files, 9 cell/model entries and 11 material families.
- Added offline cell ZIPs, parameter-variant selection, GitHub data navigation and scoped CSV/JSON downloads, with executable usage examples.
- Added contribution templates, source-suggestion and PR templates, and maintainer contact details. The initial CPG-SPMT integration note was removed in the later data-only scope revision.

## 0.4.0 — 2026-10-16

- Reached 47 OCP records, 304 other parameters and 20 full-cell files across 9 cell/model entries and 11 material families.
- Added Ecker/Kokam and Enertech/Ai model inputs, two published electrode tables, six time/voltage series and three separate temperature-rise sidecars.
- Retained upstream figure-digitization history, implementation/commercial scaling, borrowed inputs and missing measured current/absolute-temperature channels.
- Added component-level matching evidence and an explicit ledger of missing full-cell and basic-test data.

## 0.3.0 — 2026-10-16

- Expanded to 43 OCP records across 10 material families, 228 other parameter records and 7 cell / parameter-set entries; retained 14 existing full-cell files.
- Added 24 native C/50 branches from 12 SINTEF NMC111, NMC532, LNMO, silicon and silicon–graphite specimens, including two distinct SiGr formulations.
- Added the LG M50 NMC811 positive OCP linked to the existing three same-model full-cell tests.
- Added NMC532, LCO and NCA model expressions, plus 114 scalar/function inputs with conservative identity and borrowing labels.
- Added stoichiometry/temperature diffusivity evaluation and source-value audits; made viewer materials and cell packages data-driven.
- Corrected this project's historical author/committer names and configured future commits as FrankSuperG using the GitHub no-reply identity. File trees were unchanged by the metadata correction.

## 0.2.0 — 2026-10-16

- Expanded to 12 OCP records, 114 other parameter records and 14 full-cell files.
- Added 27 AMP20 Table 1 values and 3 conditional effective diffusivities, linked to Cell I's 4C full discharge at same-model/same-study level.
- Added ten A123 9 Ah CC experiments; retained missing values and unresolved part/sensor identity.
- Added the official BPX LFP 18650 example's two OCP expressions and 46 scalars, without assigning an unsupported commercial cell or test match.
- Added cell-scoped packages, coverage and matching evidence in the viewer and exports.
- Converted documentation and viewer to English and added an Atlas companion logo.
- Preserved source-specific licenses and provenance; no independent full-cell model validation claimed.

## 0.1.0 — 2026-10-16

- Added 8 measured LFP/graphite pseudo-OCP branches and 2 attributed literature formulas.
- Added 38 non-OCP LG M50 parameter records, including two kinetic functions.
- Linked three original LG M50 full-cell datasets at the same-model/same-study level.
- Added explicit current-sign normalization, retained source rows, and checksum-pinned provenance.
- Added Python and CLI search/evaluation/export, optional PyBaMM OCP components,
  static local browsing, parameter inspection, comparison, and data downloads.
- Added schemas, provenance reproduction, package checks, tests, CI, and per-asset licensing.
- At that release, full-cell model validation and complete parameter sets were deferred. The current scope covers parameter and experimental-data curation.
