# Full-cell tests by material

[All data](../README.md) · [How to use external links](../../docs/FULL_CELL_DATASETS.md)

61 existing packaged branch/test files and 11 external dataset-link records. External records are not imported files or independent specimens. One multi-chemistry dataset can appear under several materials.

Large observations remain with the original provider. [Dataset metadata CSV](datasets.csv) · [Complete metadata JSON](datasets.json) · [233 selected file/container locators (CSV)](files.csv). No automatic download occurs.

| Material family | Packaged test files | External datasets | Browse |
|---|---:|---:|---|
| LFP | 46 | 4 | [LFP](LFP.md) |
| NMC | 9 | 4 | [NMC](NMC.md) |
| NCA | 0 | 5 | [NCA](NCA.md) |
| LCO | 4 | 0 | [LCO](LCO.md) |
| NCO | 2 | 0 | [NCO](NCO.md) |

## External dataset availability

Ageing availability applies to a source, not every linked file. `Not reported` is not proof of absence. Formation, repeated initial tests and simulated degradation alone are not measured longitudinal ageing data.

| Dataset | Materials | Ageing data | License |
|---|---|---|---|
| [A123 26650 M1B: multi-rate charging and UDDS](uccs-a123-26650m1b-2021.md) | LFP | Not reported | CC-BY-4.0 |
| [CALCE Samsung INR18650-20R: OCV and dynamic profiles](calce-samsung-20r-dynamic.md) | NMC | Not reported | not-stated |
| [CALCE A123 LFP: OCV, DST and FUDS](calce-a123-dynamic.md) | LFP | Not reported | not-stated |
| [CALB L148N58A: characterization, US06 and EIS](calb-l148n58a-2025.md) | NMC | Not reported | CC-BY-4.0 |
| [University of Malaya: LFP, NCA and NMC dynamic tests](malaya-three-chemistries-2022.md) | LFP, NMC, NCA | Unverified | CC-BY-4.0 |
| [600 mAh LFP cells: SOC-dependent EIS](milano-lfp-eis-2023.md) | LFP | Not reported | CC-BY-4.0 |
| [LG M50LT: measured EIS and grouped parameters](hallemans-m50lt-eis-2025.md) | NMC | Not reported | BSD-3-Clause |
| [Panasonic NCR18650B formation, full-cell RPT and harvested half-cell tests](hnei-ncr18650b-2016.md) | NCA | Not reported | CC0-1.0 |
| [Panasonic NCR18650B beginning-of-life pseudo-OCV, pulses and EIS (92 cells)](bayreuth-ncr18650b-2023.md) | NCA | Not reported | not-stated |
| [Panasonic NCR18650B ageing and repeated reference tests (116 cells)](virtual-vehicle-ncr18650b-aging-2023.md) | NCA | Yes (cycle, calendar) | CC-BY-4.0 |
| [Panasonic NCR18650B multi-rate discharge and surface-temperature data](stanford-ncr18650b-rates-2021.md) | NCA | Not reported | CC-BY-4.0 |

Test types: `constant_current`, `cccv`, `pulse`, `dynamic`, `eis`, `ocv`. Named profiles can be searched at dataset level with `ebp datasets --profile US06`, or at inspected-file level with `ebp datasets --files --profile US06`. Dataset declarations are not automatically inherited by file locators. `ocv` refers to whole-cell characterization, never an automatically inferred electrode OCP. Use `ebp datasets --aging-status available` for sources with documented ageing data.
