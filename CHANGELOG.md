# Changelog

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
