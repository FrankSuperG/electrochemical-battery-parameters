# Full-cell tests by material

[All data](../README.md) · [How to use external links](../../docs/FULL_CELL_DATASETS.md)

61 existing packaged branch/test files and 16 external dataset-link records. External records are not imported files or independent specimens. One multi-chemistry dataset can appear under several materials.

Large observations remain with the original provider. [Dataset metadata CSV](datasets.csv) · [Complete metadata JSON](datasets.json) · [427 selected file/container locators (CSV)](files.csv). No automatic download occurs.

| Material family | Packaged test files | External datasets | Browse |
|---|---:|---:|---|
| LFP | 46 | 4 | [LFP](LFP.md) |
| NMC | 9 | 7 | [NMC](NMC.md) |
| NCA | 0 | 7 | [NCA](NCA.md) |
| LCO | 4 | 0 | [LCO](LCO.md) |
| NCO | 2 | 0 | [NCO](NCO.md) |

## External dataset availability

Ageing availability applies to a source, not every linked file. `Not reported` is not proof of absence. Formation, repeated initial tests and simulated degradation alone are not measured longitudinal ageing data.

| Dataset | Materials | OCP anchor | Ageing data | License |
|---|---|---|---|---|
| [A123 26650 M1B: multi-rate charging and UDDS](uccs-a123-26650m1b-2021.md) | LFP | Whole-cell OCV only | Not reported | CC-BY-4.0 |
| [CALCE Samsung INR18650-20R: OCV and dynamic profiles](calce-samsung-20r-dynamic.md) | NMC | Whole-cell OCV only | Not reported | not-stated |
| [CALCE A123 LFP: OCV, DST and FUDS](calce-a123-dynamic.md) | LFP | Whole-cell OCV only | Not reported | not-stated |
| [CALB L148N58A: characterization, US06 and EIS](calb-l148n58a-2025.md) | NMC | Not identified | Not reported | CC-BY-4.0 |
| [University of Malaya: LFP, NCA and NMC dynamic tests](malaya-three-chemistries-2022.md) | LFP, NMC, NCA | Not identified | Unverified | CC-BY-4.0 |
| [600 mAh LFP cells: SOC-dependent EIS](milano-lfp-eis-2023.md) | LFP | Not identified | Not reported | CC-BY-4.0 |
| [LG M50LT: measured EIS and grouped parameters](hallemans-m50lt-eis-2025.md) | NMC | Reuse unresolved | Not reported | BSD-3-Clause |
| [Panasonic NCR18650B formation, full-cell RPT and harvested half-cell tests](hnei-ncr18650b-2016.md) | NCA | External half-cell files | Not reported | CC0-1.0 |
| [Panasonic NCR18650B beginning-of-life pseudo-OCV, pulses and EIS (92 cells)](bayreuth-ncr18650b-2023.md) | NCA | Whole-cell OCV only | Not reported | not-stated |
| [Panasonic NCR18650B ageing and repeated reference tests (116 cells)](virtual-vehicle-ncr18650b-aging-2023.md) | NCA | Not identified | Yes (cycle, calendar) | CC-BY-4.0 |
| [Panasonic NCR18650B multi-rate discharge and surface-temperature data](stanford-ncr18650b-rates-2021.md) | NCA | Not identified | Not reported | CC-BY-4.0 |
| [CALB generation 3b 58 Ah: harvested half-cell OCP, multi-temperature tests and ageing](nextbms-calb-nmc532-2026.md) | NMC | External half-cell files | Yes (cycle, calendar) | CC-BY-4.0 |
| [Molicel P45B: published DFN OCP/parameters and multi-temperature CC, WLTP and eVTOL](aboutenergy-p45b-2026.md) | NCA | Published fitted parameterisation | Not reported | CC-BY-4.0 |
| [Molicel P45B harvested half-cell curves and 800-EFC checkup pseudo-OCV](tum-p45b-halfcell-aging-2026.md) | NCA | External half-cell files | Yes (cycle) | not-stated |
| [LG M50 multi-temperature discharge with explicitly reused Chen2020 electrode OCP](tec-lgm50-multitemperature-2021.md) | NMC | Explicitly reused catalog expression | Not reported | BSD-3-Clause |
| [LG MJ1 dynamic operating-sequence ageing (80 cells)](snu-mj1-dynamic-aging-2024.md) | NMC | Cross-study catalog half-cell reference | Yes (cycle) | CC-BY-4.0 |

Test types: `constant_current`, `cccv`, `pulse`, `dynamic`, `eis`, `ocv`. Named profiles can be searched at dataset level with `ebp datasets --profile US06`, or at inspected-file level with `ebp datasets --files --profile US06`. Dataset declarations are not automatically inherited by file locators. `ocv` refers to whole-cell characterization, never an automatically inferred electrode OCP. Use `ebp datasets --aging-status available` for sources with documented ageing data.
