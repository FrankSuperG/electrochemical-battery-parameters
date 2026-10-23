# Electrochemical model parameter scope

E-BatP curates electrochemical model parameters for DFN/P2D, SPM and SPMe.
Electrode OCP, solid-state diffusion and reaction kinetics are the admission
anchors. Geometry, transport, thermal properties and associated experiments
provide context for those parameters.

## Admission rule

Each active cell/study package must have at least one stored electrode OCP,
diffusion or kinetics record. Each external supporting source must explicitly
reference at least one such native record with cell ownership, per-component
matching evidence and missing items. A source URL or a promise to extract values
later does not satisfy this rule. `ebp validate` enforces it.

A partial parameter set is useful. M50LT remains admitted through its grouped
diffusion and kinetic quantities; NCR18650B remains admitted through four native
pseudo-OCP branches. Grouped quantities, borrowed expressions, model-derived
curves and finite-current pseudo-OCP retain their stated definitions. Admission
does not establish a complete measured parameter set or transferable parameters.

Whole-cell OCV, cycling curves, EIS spectra, GITT observations and thermal or
geometry values alone do not qualify. Intrinsic D or kinetics must not be
inferred merely because an electrochemical experiment is available.

Full-cell charge/discharge, multiple temperatures, drive cycles, ageing and EIS
are supporting references for admitted parameters. New full-cell payloads remain
at their providers. Same-model cross-study links remain qualified; a shared
chemistry or capacity is insufficient. Source leads can be proposed in issues
without becoming active catalog entries.

## Excluded in v0.16 — 2026-10-24

All three admission components were empty for the entries below. The six
external records and their 79 locators are removed from the active registry,
README/model/material indexes, CLI and viewer. Historical source reviews and
Git history retain the investigation; they are not active data packages.

| Excluded entry | Original source | Reason |
|---|---|---|
| A123 26650 M1B: multi-rate charging and UDDS | [Provider](https://data.mendeley.com/datasets/p8kf893yv3/1) | No stored or explicitly matched electrode OCP, diffusion or kinetics records. |
| CALCE Samsung INR18650-20R: OCV and dynamic profiles | [Provider](https://calce.umd.edu/data) | No stored or explicitly matched electrode OCP, diffusion or kinetics records. |
| CALCE A123 LFP: OCV, DST and FUDS | [Provider](https://calce.umd.edu/data) | No stored or explicitly matched electrode OCP, diffusion or kinetics records. |
| CALB L148N58A: characterization, US06 and EIS | [Provider](https://data.mendeley.com/datasets/ycx459r5c3/2) | No stored or explicitly matched electrode OCP, diffusion or kinetics records. |
| University of Malaya: LFP, NCA and NMC dynamic tests | [Provider](https://data.mendeley.com/datasets/29kw38kzwj/1) | No stored or explicitly matched electrode OCP, diffusion or kinetics records. |
| 600 mAh LFP cells: SOC-dependent EIS | [Provider](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1) | No stored or explicitly matched electrode OCP, diffusion or kinetics records. |
| A123 high-power 9 Ah pouch, part undisclosed | [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:fe9bad3e-8a72-4e3b-8f01-fec3324b6758) | Parameter/workbook reuse unresolved; whole-cell pseudo-OCV is not measured electrode OCP. Ten packaged CC files and the unsupported cell package were removed. |

The 90 OCP/fit records and 1,041 other parameter records remain unchanged.
The active inventory has 19 cell/study packages, 51 supporting legacy test
files and 11 parameter-associated external sources / 357 selected locators.
Material-only electrode curves remain useful without a commercial-cell match.

[Battery model index](../data/batteries/README.md) ·
[Final review](FINAL_REVIEW.md) · [Contribution rules](../CONTRIBUTING.md)
