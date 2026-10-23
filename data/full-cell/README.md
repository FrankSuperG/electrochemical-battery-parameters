# Supporting full-cell tests by material

[All data](../README.md) · [How to use external links](../../docs/FULL_CELL_DATASETS.md)

51 existing packaged branch/test files and 11 external dataset-link records. External records are not imported files or independent specimens. One multi-chemistry dataset can appear under several materials.

Large observations remain with the original provider. [Dataset metadata CSV](datasets.csv) · [Complete metadata JSON](datasets.json) · [357 selected file/container locators (CSV)](files.csv). No automatic download occurs.

| Material family | Packaged test files | External datasets | Browse |
|---|---:|---:|---|
| LFP | 36 | 1 | [LFP](LFP.md) |
| NMC | 9 | 4 | [NMC](NMC.md) |
| NCA | 0 | 6 | [NCA](NCA.md) |
| LCO | 4 | 0 | [LCO](LCO.md) |
| NCO | 2 | 0 | [NCO](NCO.md) |

## External dataset availability

Ageing availability applies to a source, not every linked file. `Not reported` is not proof of absence. Formation, repeated initial tests and simulated degradation alone are not measured longitudinal ageing data.

| Dataset | Materials | OCP anchor | Ageing data | License |
|---|---|---|---|---|
| [LG M50LT: measured EIS and grouped parameters](hallemans-m50lt-eis-2025.md) | NMC | Reuse unresolved | Not reported | BSD-3-Clause |
| [Panasonic NCR18650B formation, full-cell RPT and harvested half-cell tests](hnei-ncr18650b-2016.md) | NCA | Imported half-cell branches | Not reported | CC0-1.0 |
| [Panasonic NCR18650B beginning-of-life pseudo-OCV, pulses and EIS (92 cells)](bayreuth-ncr18650b-2023.md) | NCA | Cross-study catalog half-cell reference | Not reported | not-stated |
| [Panasonic NCR18650B ageing and repeated reference tests (116 cells)](virtual-vehicle-ncr18650b-aging-2023.md) | NCA | Cross-study catalog half-cell reference | Yes (cycle, calendar) | CC-BY-4.0 |
| [Panasonic NCR18650B multi-rate discharge and surface-temperature data](stanford-ncr18650b-rates-2021.md) | NCA | Cross-study catalog half-cell reference | Not reported | CC-BY-4.0 |
| [CALB generation 3b 58 Ah: harvested half-cell OCP, multi-temperature tests and ageing](nextbms-calb-nmc532-2026.md) | NMC | Imported half-cell branches | Yes (cycle, calendar) | CC-BY-4.0 |
| [Molicel P45B: published DFN OCP/parameters and multi-temperature CC, WLTP and eVTOL](aboutenergy-p45b-2026.md) | NCA | Published fitted parameterisation | Not reported | CC-BY-4.0 |
| [Molicel P45B harvested half-cell curves and 800-EFC checkup pseudo-OCV](tum-p45b-halfcell-aging-2026.md) | NCA | Imported half-cell branches | Yes (cycle) | MIT |
| [LG M50 multi-temperature discharge with explicitly reused Chen2020 electrode OCP](tec-lgm50-multitemperature-2021.md) | NMC | Explicitly reused catalog expression | Not reported | BSD-3-Clause |
| [LG MJ1 dynamic operating-sequence ageing (80 cells)](snu-mj1-dynamic-aging-2024.md) | NMC | Cross-study catalog half-cell reference | Yes (cycle) | CC-BY-4.0 |
| [HAIDI HDCF18650-1800 &#124; Rehm2025 multi-temperature OCV, rate and GEIS source](haidi-lfp-rehm2025.md) | LFP | Imported half-cell branches | Not reported | CC-BY-4.0 |

Test types: `constant_current`, `cccv`, `pulse`, `dynamic`, `eis`, `ocv`. Named profiles can be searched at dataset level with `ebp datasets --profile US06`, or at inspected-file level with `ebp datasets --files --profile US06`. Dataset declarations are not automatically inherited by file locators. `ocv` refers to whole-cell characterization, never an automatically inferred electrode OCP. Use `ebp datasets --aging-status available` for sources with documented ageing data.
