# NCA full-cell tests

[All materials](README.md) · [Access, licenses and limits](../../docs/FULL_CELL_DATASETS.md)

Material grouping is a discovery aid, not evidence that tests and parameters belong together. NCO retains its source label and is not silently classified as NMC or NCA.

## External datasets

| Dataset / cell | OCP anchor | Tests / profiles | Rates and temperatures | Ageing data | License | Parameter match |
|---|---|---|---|---|---|---|
| [Panasonic NCR18650B formation, full-cell RPT and harvested half-cell tests](hnei-ncr18650b-2016.md) | Imported half-cell branches | constant_current, ocv;  | The paper reports multi-rate full-cell charge/discharge characterization and half-cell RPT. Exact rate-to-MAT-step mapping was not read; a member named RPT is not a standalone equilibrium-OCP table. Source temperatures: not verified | Not reported | CC0-1.0 | `same_model_same_study` |
| [Panasonic NCR18650B beginning-of-life pseudo-OCV, pulses and EIS (92 cells)](bayreuth-ncr18650b-2023.md) | Cross-study catalog half-cell reference | constant_current, ocv, pulse, eis;  | Whole-cell pseudo-OCV at 0.05C in both directions; 0.5C, 10 s charge/discharge pulses at 50% SOC. A single pulse rate is not a multi-rate continuous CC sweep. Source temperatures: [25] | Not reported | not-stated | `same_model_different_study` |
| [Panasonic NCR18650B ageing and repeated reference tests (116 cells)](virtual-vehicle-ncr18650b-aging-2023.md) | Cross-study catalog half-cell reference | constant_current, cccv, pulse, dynamic;  | 37 source-reported ageing load profiles plus repeated reference tests. RTP includes C/3 and 1C discharges, C/3 and C/2 CCCV charges and pulse sequences. Ageing-profile rates vary by cell; no complete same-state multi-rate characterization matrix is asserted. Source temperatures: [0, 5, 15, 20, 25, 30, 35, 40, 45] | Yes (cycle, calendar) | CC-BY-4.0 | `same_model_different_study` |
| [Panasonic NCR18650B multi-rate discharge and surface-temperature data](stanford-ncr18650b-rates-2021.md) | Cross-study catalog half-cell reference | constant_current, cccv;  | NCA discharge rates C/20, 1C, 2C, 3C and 5C at source temperatures 5/25/35 degC after standard CCCV charge. The LFP source range up to 20C must not be assigned to NCR18650B. Charging preparation is not a multi-rate charge sweep. Source temperatures: [5, 25, 35] | Not reported | CC-BY-4.0 | `same_model_different_study` |
| [Molicel P45B: published DFN OCP/parameters and multi-temperature CC, WLTP and eVTOL](aboutenergy-p45b-2026.md) | Published fitted parameterisation | constant_current, pulse, dynamic, ocv; WLTP, eVTOL | CC charge at C/30, 1C, 3C and discharge at C/30, 1C, 3C, 10C; GITT and WLTP at 10/25/40/60 degC. eVTOL is limited to 25/40/60 degC. Alternate -charge.csv files retain a charge-optimised model case, not independent experiments. Source temperatures: [10, 25, 40, 60] | Not reported | CC-BY-4.0 | `same_model_same_study` |
| [Molicel P45B harvested half-cell curves and 800-EFC checkup pseudo-OCV](tum-p45b-halfcell-aging-2026.md) | Imported half-cell branches | ocv;  | Half-cell filenames use 0C02/0C03 = 0.02C/0.03C; paper Section 2.4 writes 0.02C/0.033C. Full-cell ageing protocol: 1C CCCV charge, 1.5C CC discharge at 25 C; pOCV checkups 0.033C. Protocol descriptions do not certify a complete cycling I/V/T file. Source temperatures: [25] | Yes (cycle) | MIT | `same_model_same_study` |

## Existing packaged tests

These CSVs already belong to the catalog; this index adds links without duplicating observations.

| Test | Cell / metadata | Source protocol | CSV | Parameter match |
|---|---|---|---|---|

No packaged full-cell file for this family. External links do not fill missing parameter matches.
