# OCP-first expansion screen — 2026-10-23

**v0.11 screening snapshot.** See the [v0.13 comprehensive extraction audit](PARAMETER_AUDIT.md) for current decisions. The subsequent v0.12 follow-up extracted HNEI and
NEXTBMS half-cell branches plus P45B fitted OCP/model parameters. Read the
[current storage/extraction guide](PARAMETER_STORAGE.md) and
[battery model index](../data/batteries/README.md) for native records and updated
matches. The screening decisions below describe the earlier pass.

[Full-cell sources with OCP and ageing columns](../data/full-cell/README.md) · [NMC](../data/full-cell/NMC.md) · [NCA](../data/full-cell/NCA.md) · [Machine-readable evidence](../src/ebp/data/evidence/ocp-first-expansion-review.json)

This pass screened **21 source families** and added **five external records / 194 selected locators**. The registry now contains sixteen records and 427 locators. All new observations remain external. Native counts stay at 59 electrode-curve records, 397 other parameters and 61 packaged full-cell files. A locator is not an independent experiment.

## Admitted sources and OCP anchors

| Source | Electrode OCP anchor | Full-cell evidence / temperature | Matching and limits |
|---|---|---|---|
| [CALB generation 3b](../data/full-cell/nextbms-calb-nmc532-2026.md) | Six harvested graphite/NMC532 slow-cycle and GITT CSV paths from Cell_96 | CC/GITT/dynamic/HPPC; EIS at 0/5/25/45 degC; 41 calendar/cyclic histories and stage-specific EIS | Same study/model, different specimens. No link to the older L148N58A record by 58 Ah capacity alone. |
| [TUM P45B](../data/full-cell/tum-p45b-halfcell-aging-2026.md) | Four measured SiGr-anode and one cathode branch | One serial23 ageing pOCV checkup table, reported through 800 EFC | Same study/model; donor mapping and measurement-data reuse scope unresolved. Reconstructed silicon excluded from measured OCP anchor. |
| [About:Energy P45B](../data/full-cell/aboutenergy-p45b-2026.md) | Published BPX fitted/composite electrode OCP and D/kinetics entries | CC/GITT/WLTP at 10/25/40/60 degC; eVTOL at 25/40/60 degC | Author-declared reuse of public tests by the DFN paper. Original harvested half-cell points not independently located; BPX is not imported as measured data. |
| [LG M50 / TEC2021](../data/full-cell/tec-lgm50-multitemperature-2021.md) | Two explicitly reused catalog Chen2020 OCP expressions | 48 source-listed discharge CSVs: 0.1/0.5/1/2C at 0/10/25 degC | Same commercial model and explicit curve reuse; different parameterisation/experiment studies and unresolved serials. No WLTP found in this release. |
| [LG MJ1 / SNU2024](../data/full-cell/snu-mj1-dynamic-aging-2024.md) | Four existing DLR-SINTEF half-cell branches as cross-study references | 80-cell staged operating-sequence ageing at 25 degC; one listed raw ZIP | Same model, different study/batch. Inner paths unverified after HTTP 403. Staged ageing is not a named road-current profile. |

**Half-cell temperature is separate from full-cell temperature.** None of the new half-cell/source anchors is certified here as a multi-temperature OCP measurement series. Empty half-cell temperature lists mean unverified, not that the full-cell setpoints apply. New multi-temperature coverage belongs to full-cell tests; ORegan temperature-dependent D/i0/entropy tables are a separate parameter source.

## Evidence and parsing limits

- NEXTBMS: complete 7z directories were listed through bounded header ranges (520 / 1405 / 7333 bytes for half-cell / characterization / ageing). No CSV or compressed observation block was extracted. The optional inspector uses py7zr 1.1.0 only when explicitly invoked with `--kind 7z`; normal library, viewer and CI do not fetch these sources.
- NEXTBMS ageing EIS: source prose says 22/13/17 cells at BoL/MoL/EoL, while directory names contain 25/16/20 impedance CSVs. These are unresolved source/directory differences; the extra labels are not Cell_4/6/15. No values or cohort membership are silently corrected.
- NEXTBMS Time starts with a timestamp and continues as incremental seconds according to source documentation. Strip header whitespace; preserve fractional increments. Source-reported voltage spikes and absence of some stage/temperature combinations remain explicit. `OCPDis_Cell_*.csv` are whole-cell checkup extracts, not harvested-electrode OCP.
- P45B experimental columns are `t_s`, `I_exp_A`, `V_exp_V`, `T_exp_degC` according to the author format PDF. The temperature is Peltier-controlled cell-surface temperature. Simulated columns, including `E_OCV_V`, are not measured electrode data. `-charge.csv` denotes an alternate model case, not a new independent experiment.
- TUM filenames `0C02` / `0C03` mean 0.02C / 0.03C, not zero-degree tests. The serial23 file holds checkup pOCVs, not a verified continuous 800-cycle I/V/T log. Framework MIT and Python-mirror BSD licenses are not treated as a blanket grant for all literature input data.
- Primary links, exact paths, archive sizes, bytes read, source versions and published checksums are retained. Header listings do not independently certify raw columns, units, measurement values or full payload checksums.

## Full screening ledger

Included rows are link metadata, not numerical parameter imports. Remaining rows record concrete leads, existing coverage or admission gaps; they are not counted as downloadable matched packages.

| Source / material | Decision | Evidence / next missing item |
|---|---|---|
| [CALB generation 3b 58 Ah NMC532/graphite](https://zenodo.org/records/22301764) | `included` | Harvested half-cell files; same-study/model CC, dynamic, ageing and multi-temperature EIS; specimen sets differ. |
| [Molicel P45B harvested blend/cathode](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30) | `included` | Measured finite-current half-cell branches plus one 800-EFC checkup table; data reuse scope and half-cell temperature unresolved. |
| [Molicel P45B published BPX parameterisation](https://zenodo.org/records/19052626) | `included` | Public composite/fitted electrode OCP parameter package with explicitly reused multi-temperature CC/GITT/WLTP/eVTOL experiments; original half-cell points not independently located. |
| [LG M50 / TEC2021](https://zenodo.org/records/4864437) | `included` | Explicit reuse of catalog Chen2020 OCP expressions; 48 measured-data file paths at 0/10/25 degC. No named WLTP file in inspected release. |
| [LG MJ1 / SNU dynamic ageing](https://data.mendeley.com/datasets/h2y7mj4kt7/2) | `included` | 80-cell source at 25 degC; cross-study reference to existing DLR-SINTEF half-cell curves only; raw ZIP internals unverified. |
| [LG M50 / ORegan2022](https://zenodo.org/records/5171874) | `parameter_lead` | 58 previously reviewed diffusivity/kinetic/thermal CSVs; separate source from TEC2021. OCP reuse is not a new independent half-cell measurement. |
| [Undisclosed LG Energy Solution 49 Ah LFP pouch](https://www.nature.com/articles/s41524-024-01197-7) | `excluded_from_ocp_admission` | Paper reports harvested half-cell OCP but its Code availability explicitly lists OCP among confidential inputs. Public CC/GITT/EV full-cell data do not clear OCP access. |
| [Molicel P45B subzero pulses / Folkson2026](https://wrap.warwick.ac.uk/id/eprint/195594/7/Folkson_2026_J._Electrochem._Soc._173_010501.pdf) | `request_only` | Half-cell tests at 23 degC and subzero full-cell pulses are described, but the paper states data are available upon request; no open payload admitted. |
| [Sordi2026 field-aged LFP bus cells](https://doi.org/10.1016/j.est.2026.120653) | `unresolved_deposit` | Publisher describes half-cell, fresh/field-aged and EIS work and names Zenodo. Exact matching public deposit was not resolved in this pass. |
| [Sordi2024 low-temperature parameter diagnosis](https://zenodo.org/records/13905430) | `missing_payload` | Inspected fixed-record API lists README.docx only. No experimental observation payload is established from that record. |
| [HAIDI18650 LFP/graphite](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/LFP) | `half_cell_only_lead` | Eight source-listed low-rate electrode branches. Same-study full-cell files and per-source reuse scope not verified; no forced A123 join. |
| [LG M36 NMC cathode](https://github.com/tum-ees/DegradationModeAnalysis/tree/402bab94d20258162ff059b8d5d51abe40ec1c30/input_data/NMC) | `half_cell_only_lead` | Four source-listed cathode branches; matching negative-electrode/full-cell package and reuse terms remain unresolved. |
| [Molicel M35A NCA/SiGr](https://www.sciencedirect.com/science/article/pii/S2352152X24007357) | `half_cell_only_lead` | Measured OCP study and author-library paths located; complete same-study full-cell data/reuse scope not yet confirmed. |
| [SINTEF material-only half cells](https://zenodo.org/records/20086298) | `existing_material_source` | Metadata covers graphite, Si, SiGr, B/SiGr, LFP, NMC111, NMC532 and LNMO under several protocols. Current catalog imports selected LFP/graphite specimens; material labels do not identify a commercial full cell. |
| [NCR18650B / HNEI](https://zenodo.org/records/60232) | `existing_external_source` | Verified NE/PE and full-cell RPT member locations in one study; no numeric branch import or measured longitudinal ageing series. |
| [ISU-UConn LFP/graphite CR2032](https://digitalcommons.lib.uconn.edu/reil_datasets/6/) | `existing_catalog` | Existing measured half-cell branches and laboratory full-cell configurations; no universal commercial-cell identity or missing I/t/T filled. |
| [A123 18650M1A / Jahn2024](https://zenodo.org/records/11958572) | `existing_model_derived_source` | Catalog OCPn tables are modeled PD-ECM quantities. They remain distinct from measured half-cell OCP under this screen. |
| [LG M50 / Chen2020](https://doi.org/10.1149/1945-7111/ab9050) | `existing_catalog` | Existing half-cell-derived published OCP expressions and room-temperature full-cell tests. TEC adds external multi-temperature experiments through explicit reuse. |
| [LG MJ1 / DLR-SINTEF](https://zenodo.org/records/15497193) | `existing_catalog` | Existing finite-current harvested half-cell branches and GITT parameter sources; SNU ageing comparison is different study/batch. |
| [LG M50LT / Hallemans2025](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068) | `existing_reuse_gap` | Same-study EIS/groups/dynamic data exist, but third-party electrode OCP reuse rights remain unresolved. |
| [Samsung INR18650-30Q ageing/EIS](https://data.mendeley.com/datasets/g7ncmhrcrz/1) | `full_cell_only_lead` | Open eight-cell ageing/EIS source found. No same-model half-cell OCP anchor was established in this screen. |

## Use the links

```bash
ebp datasets --material NMC --test-type eis --json
ebp datasets --material NCA --profile WLTP --json
ebp datasets --cell lg-m50 --json
ebp datasets --cell lg-mj1-dlr-sintef --aging-status available --json
ebp datasets --files --material NCA --profile eVTOL --json
```

`ocp_anchor` distinguishes external half-cell measurements, published fitted parameterisation, explicitly reused expressions, cross-study references and unresolved reuse. `parameter_components` still describes joins to native catalog records: an external OCP lead does not create a numeric catalog record. No simulation or model-performance claim is added.
