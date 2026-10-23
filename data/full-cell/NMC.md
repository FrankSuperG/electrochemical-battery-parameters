# NMC full-cell tests

[All materials](README.md) · [Access, licenses and limits](../../docs/FULL_CELL_DATASETS.md)

Material grouping is a discovery aid, not evidence that tests and parameters belong together. NCO retains its source label and is not silently classified as NMC or NCA.

## External datasets

| Dataset / cell | Tests / profiles | Rates and temperatures | License | Parameter match |
|---|---|---|---|---|
| [CALCE Samsung INR18650-20R: OCV and dynamic profiles](calce-samsung-20r-dynamic.md) | dynamic, ocv, pulse; US06, DST, FUDS, BJDST | Source describes low-current and incremental-current OCV protocols; no multi-rate CC sweep asserted. Source temperatures: [0, 25, 45] | not-stated | `unmatched` |
| [CALB L148N58A: characterization, US06 and EIS](calb-l148n58a-2025.md) | constant_current, cccv, pulse, dynamic, eis, ocv; US06, UDDS, WLTP | C/20 charge/discharge characterization; HPPC at 1C and C/3. Pulse rates are not a standalone multi-rate continuous-discharge sweep. Source temperatures: [10, 25, 40] | CC-BY-4.0 | `unmatched` |
| [University of Malaya: LFP, NCA and NMC dynamic tests](malaya-three-chemistries-2022.md) | dynamic, pulse; US06, DST, FUDS, UDDS, WLTP | HPPC and pulse charge/discharge are described; numeric rates not verified. Source temperatures: not verified | CC-BY-4.0 | `unmatched` |
| [LG M50LT: measured EIS and grouped parameters](hallemans-m50lt-eis-2025.md) | eis, dynamic;  | 3 mV rms EIS; 9 SOC levels and 65 frequencies (585 measured rows). Source temperatures: [25] | BSD-3-Clause | `same_model_same_study` |

## Existing packaged tests

These CSVs already belong to the catalog; this index adds links without duplicating observations.

| Test | Cell / metadata | Source protocol | CSV | Parameter match |
|---|---|---|---|---|
| `chen-lgm50-cell02` | [LG M50 &#124; 5 Ah NMC811/graphite-SiOx](../cells/lg-m50.md) | CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description) | [Download](../../src/ebp/data/full_cell/LGM50_cell02-normalized.csv) | `same_model_same_study` |
| `chen-lgm50-cell03` | [LG M50 &#124; 5 Ah NMC811/graphite-SiOx](../cells/lg-m50.md) | CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description) | [Download](../../src/ebp/data/full_cell/LGM50_cell03-normalized.csv) | `same_model_same_study` |
| `chen-lgm50-cell04` | [LG M50 &#124; 5 Ah NMC811/graphite-SiOx](../cells/lg-m50.md) | CCCV charge; CC discharge at C/10, C/2, 1C and 1.5C (source description) | [Download](../../src/ebp/data/full_cell/LGM50_cell04-normalized.csv) | `same_model_same_study` |
| `mohtat-charge-0p1c` | [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](../cells/mohtat2020-nmc532-pouch.md) | Nominal 0.1C charge to 4.2 V; capacity-coordinate experimental export | [Download](../../src/ebp/data/full_cell/mohtat-charge-0p1c-normalized.csv) | `same_study_cell_family` |
| `mohtat-charge-0p2c` | [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](../cells/mohtat2020-nmc532-pouch.md) | Nominal 0.2C charge to 4.2 V; capacity-coordinate experimental export | [Download](../../src/ebp/data/full_cell/mohtat-charge-0p2c-normalized.csv) | `same_study_cell_family` |
| `mohtat-charge-0p5c` | [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](../cells/mohtat2020-nmc532-pouch.md) | Nominal 0.5C charge to 4.2 V; capacity-coordinate experimental export | [Download](../../src/ebp/data/full_cell/mohtat-charge-0p5c-normalized.csv) | `same_study_cell_family` |
| `mohtat-charge-1c` | [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](../cells/mohtat2020-nmc532-pouch.md) | Nominal 1C charge to 4.2 V; capacity-coordinate experimental export | [Download](../../src/ebp/data/full_cell/mohtat-charge-1c-normalized.csv) | `same_study_cell_family` |
| `mohtat-charge-2c` | [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](../cells/mohtat2020-nmc532-pouch.md) | Nominal 2C charge to 4.2 V; capacity-coordinate experimental export | [Download](../../src/ebp/data/full_cell/mohtat-charge-2c-normalized.csv) | `same_study_cell_family` |
| `hallemans2025-m50lt-drive-80to20` | [LG M50LT &#124; Hallemans2025 grouped SPMe](../cells/lg-m50lt-hallemans2025.md) | Measured drive cycle, nominal 80 to 20% SOC; repeated excitation, 0.15 s sampling, 24742.8 s elapsed; paper v4 Section 7.3 / Figure 11. | [Download](../../src/ebp/data/full_cell/hallemans2025-m50lt-drive-80to20-normalized.csv) | `same_model_same_study` |
