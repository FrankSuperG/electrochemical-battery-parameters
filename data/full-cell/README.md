# Full-cell tests by material

[All data](../README.md) · [How to use external links](../../docs/FULL_CELL_DATASETS.md)

61 existing packaged branch/test files and 7 external dataset-link records. External records are not imported files or independent specimens. One multi-chemistry dataset can appear under several materials.

Large observations remain with the original provider. [Dataset metadata CSV](datasets.csv) · [Complete metadata JSON](datasets.json) · [82 selected file/container locators (CSV)](files.csv). No automatic download occurs.

| Material family | Packaged test files | External datasets | Browse |
|---|---:|---:|---|
| LFP | 46 | 4 | [LFP](LFP.md) |
| NMC | 9 | 4 | [NMC](NMC.md) |
| NCA | 0 | 1 | [NCA](NCA.md) |
| LCO | 4 | 0 | [LCO](LCO.md) |
| NCO | 2 | 0 | [NCO](NCO.md) |

Test types: `constant_current`, `cccv`, `pulse`, `dynamic`, `eis`, `ocv`. Named profiles can be searched at dataset level with `ebp datasets --profile US06`, or at inspected-file level with `ebp datasets --files --profile US06`. Dataset declarations are not automatically inherited by file locators. `ocv` refers to whole-cell characterization, never an automatically inferred electrode OCP.
