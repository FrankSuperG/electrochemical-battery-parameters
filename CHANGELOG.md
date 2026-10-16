# Changelog

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
