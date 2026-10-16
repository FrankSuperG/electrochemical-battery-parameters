# Changelog

## Unreleased

- Added a reproducible prepublication audit and a separate, source-backed data-candidate ledger; candidate observations are not counted as imported records.
- Fixed LG M50 solid diffusivity classification so both electrode values appear under the diffusion filter; values, units and source evidence are unchanged, with record versions advanced to 2.
- Included GitHub navigation exports, contribution templates and issue/PR files in source distributions.
- Corrected license file patterns and historical Mohtat no-import wording; made access instructions work with either public or restricted repository visibility.

## 0.5.0 — 2026-10-16

- Retrieved ten official Mohtat author files under CC BY 4.0 and retained five charge-capacity/voltage/temperature series: 6,474 observations, with current and original time explicitly absent.
- Added 33 author inputs and two OCP expressions alongside, rather than replacing, the PyBaMM variant; documented the graphite-offset and other model differences.
- Reached 49 OCP records, 337 other parameters, 25 full-cell files, 9 cell/model entries and 11 material families.
- Added offline cell ZIPs, parameter-variant selection, GitHub data navigation and scoped CSV/JSON downloads, with executable usage examples.
- Added contribution templates, source-suggestion and PR templates, maintainer contact details, and an initial CPG-SPMT integration audit without claiming a new model-validation result.

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
- Full-cell model validation and complete parameter sets remain future work.
