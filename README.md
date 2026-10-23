<p align="center">
  <img src="assets/logo.png" width="640" alt="E-BatP — Electrochemical Battery Parameters">
</p>
<p align="center"><strong>Traceable electrochemical parameters, connected to the cells and experiments behind them.</strong></p>
<p align="center">
  <a href="https://github.com/FrankSuperG/electrochemical-battery-parameters/actions"><img src="https://github.com/FrankSuperG/electrochemical-battery-parameters/actions/workflows/ci.yml/badge.svg" alt="Catalog and package checks"></a>
  <img src="https://img.shields.io/badge/version-0.14.0-287b78" alt="Version 0.14.0">
  <img src="https://img.shields.io/badge/Python-3.10%2B-203c4c" alt="Python 3.10 or later">
  <a href="DATA_LICENSES.md"><img src="https://img.shields.io/badge/data-per--source%20licenses-758d89" alt="Per-source data licenses"></a>
</p>

E-BatP is a multi-material library of traceable lithium-ion battery parameters and experimental records for **Doyle-Fuller-Newman (DFN/P2D)**, **single-particle (SPM)** and **single-particle with electrolyte dynamics (SPMe)** models. It covers electrode **open-circuit potential (OCP)** curves, solid-state diffusion, reaction kinetics, geometry, transport and thermal parameters. Records keep their original definitions, conditions, processing history and cell-match evidence. Parameters with different model conventions are not automatically interchangeable.

Find **GITT** (galvanostatic intermittent titration) diffusion and exchange-current data, **EIS** (electrochemical impedance spectroscopy) evidence, and full-cell tests including **constant-current charge/discharge** and drive cycles. Start with [OCP by material](data/ocp/README.md) for LFP, NMC, graphite and other electrodes, or [cell and study entries](data/README.md) for model-specific records. Source licenses, match levels and missing channels are explicit; entries can be partial references.

**Project scope:** curate, document and export electrochemical parameters and associated experimental data. Model simulation, parameter fitting and model validation are outside this repository's scope. Full-cell tests are retained as source observations with matching evidence; no model-performance results are reported.

**v0.14.0: 83 electrode-curve records · 13 material labels · 1,041 other parameter records · 61 full-cell branch/test files · 19 cell or study entries.** Curves comprise 55 measured pseudo-OCP branches, 7 published tables/fits, 19 expressions and **2 modeled PD-ECM OCPn tables**. Exported branches/files are not independent cells. Three temperature-rise sidecars and the M50LT frequency-domain evidence table remain additional data. The viewer runs locally; no public hosting workflow is configured.

File-level follow-up: **[OCP-first search: 21 source families and five additions](docs/OCP_FIRST_EXPANSION.md)** · [Panasonic NCR18650B: four sources, tests and ageing](docs/NCR18650B.md) · [original seven-source review](docs/EXTERNAL_FILE_REVIEW.md) · [selected file/container locations](data/full-cell/files.csv). Source-listed filenames, archive-directory evidence and reviewed contents remain separate. OCP, diffusion and kinetics associations are recorded independently.

New full-cell discovery: **[LFP](data/full-cell/LFP.md) · [NMC](data/full-cell/NMC.md) · [NCA](data/full-cell/NCA.md) · [LCO](data/full-cell/LCO.md) · [NCO](data/full-cell/NCO.md)**. Sixteen external dataset-link records include 427 selected locators for electrode-source anchors and full-cell rate, temperature, dynamic, ageing and EIS data where verified. [The source table includes OCP anchor and Ageing data columns](data/full-cell/README.md). Large payloads stay with their providers; these links are separate from the 61 existing packaged test files. [Review sources, licenses and matching limits](docs/FULL_CELL_DATASETS.md).

New characterization package: [LG MJ1 / DLR-SINTEF](data/cells/lg-mj1-dlr-sintef.md): four pseudo-OCP branches, 22 scalar/specification records and 20 native parameter tables, including model/direction-specific GITT fits. Read the [MJ1 source and matching review](docs/LG_MJ1.md). **Same-study intact-cell test data remain missing.** The [public-release readiness review](docs/RELEASE_READINESS.md) records checked boundaries and remaining gaps.

Earlier matched study: [LG M50LT / Hallemans2025](data/cells/lg-m50lt-hallemans2025.md), with 18 grouped fitted values and 164,953 measured drive-cycle t/I/V rows. Read the [definitions, OCP reuse review and missing-item ledger](docs/HALLEMANS2025.md). OCP permission remains unresolved; no M50LT electrode curves are redistributed.

New LFP packages: [ISU-UConn laboratory half/full-cells](data/cells/isu-uconn-lfp-graphite-lab.md) and [A123 18650M1A / Jahn2024](data/cells/a123-18650m1a-jahn2024.md). Read the [selection, matching and missing-channel notes](docs/LFP_STUDIES.md), including ISU's unresolved reference details and A123's modeled OCPn representation.

## Battery model index

**[Browse by battery model](data/batteries/README.md) · [Browse all data](data/README.md) · [OCP by material](data/ocp/README.md) · [Full-cell tests by material](data/full-cell/README.md) · [How to download and use](docs/DATA_ACCESS.md)**

**Storage rule:** extract reusable OCP and model parameters into source-traceable CSV/JSON records in this repository; retain new full-cell tests as descriptions and external download links. Permission or definition gaps remain explicit. Existing packaged full-cell tests are retained. [Fixed formats and extraction scope](docs/PARAMETER_STORAGE.md).

No installation is needed to browse or download files from GitHub. Choose a battery below: OCP and category-specific diffusion/kinetics links open repository data; full-cell links open per-source conditions and file locations. For LFP and other material-level OCP measurements, use the **OCP by material** index. On a file page, use **Raw / download raw file** to save the complete file; keep its metadata and license. See the [download guide](docs/DATA_ACCESS.md) for examples.

<!-- DATA_QUICKLINKS_START -->

OCP and parameter links open repository data. Full-cell links open source descriptions and downloads. **Not extracted** means no reusable native record is curated; it is not a claim that no measurement exists.

Coverage labels below are source-level discovery aids. Read each model page for study, temperature, profile, licence and specimen limits. Half-cell temperature is tracked separately.

[Extraction audit for every battery/study: stored / reuse unresolved / definition unresolved / not located](docs/PARAMETER_AUDIT.md)

Record counts include published assumptions, borrowed functions, activation energies and optional submodel inputs, not a count of independent measurements or solid-electrode coefficients. Read parameter names and origin fields before selecting a model input.

### LFP

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [A123 18650M1A &#124; Jahn2024 LFP/graphite](data/batteries/a123-18650m1a-jahn2024.md) | [2 modeled OCPn](data/cells/a123-18650m1a-jahn2024.md#ocp-curves) | Not extracted | Not extracted | [14 packaged](data/batteries/a123-18650m1a-jahn2024.md#full-cell-tests) | See test conditions / gaps<br>same model same study · [Match / gaps](data/batteries/a123-18650m1a-jahn2024.md#matching-and-gaps) |
| [A123 26650 m1b / UCCS](data/batteries/uccs-a123-26650m1b-2021.md) | Not extracted | Not extracted | Not extracted | [1 external source](data/batteries/uccs-a123-26650m1b-2021.md#full-cell-tests) | multi-T, dynamic<br>Parameters unmatched · [Match / gaps](data/batteries/uccs-a123-26650m1b-2021.md#matching-and-gaps) |
| [A123 AMP20M1HD-A &#124; 20 Ah LFP pouch](data/batteries/a123-amp20m1hd-a.md) | Not extracted | [6 records](data/parameters/a123-amp20m1hd-a--diffusion.csv) | [6 records](data/parameters/a123-amp20m1hd-a--kinetics.csv) | [1 packaged](data/batteries/a123-amp20m1hd-a.md#full-cell-tests) | See test conditions / gaps<br>same model same study · [Match / gaps](data/batteries/a123-amp20m1hd-a.md#matching-and-gaps) |
| [A123 cylindrical LFP / part unresolved](data/batteries/calce-a123-dynamic.md) | Not extracted | Not extracted | Not extracted | [1 external source](data/batteries/calce-a123-dynamic.md#full-cell-tests) | multi-T, dynamic<br>Parameters unmatched · [Match / gaps](data/batteries/calce-a123-dynamic.md#matching-and-gaps) |
| [A123 high-power LFP pouch &#124; 9 Ah &#124; part undisclosed](data/batteries/a123-high-power-pouch-9ah.md) | Not extracted | Not extracted | Not extracted | [10 packaged](data/batteries/a123-high-power-pouch-9ah.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](data/batteries/a123-high-power-pouch-9ah.md#matching-and-gaps) |
| [ISU-UConn &#124; laboratory LFP/graphite CR2032 family](data/batteries/isu-uconn-lfp-graphite-lab.md) | [4 pseudo-OCP](data/cells/isu-uconn-lfp-graphite-lab.md#ocp-curves) | Not extracted | Not extracted | [21 packaged](data/batteries/isu-uconn-lfp-graphite-lab.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](data/batteries/isu-uconn-lfp-graphite-lab.md#matching-and-gaps) |
| [LFP 2.3 Ah &#124; Prada2013 implementation &#124; part unresolved](data/batteries/prada2013-lfp-nominal-design.md) | [2 reused expressions](data/cells/prada2013-lfp-nominal-design.md#ocp-curves) | [3 records](data/parameters/prada2013-lfp-nominal-design--diffusion.csv) | [6 records](data/parameters/prada2013-lfp-nominal-design--kinetics.csv) | [Not linked](data/batteries/prada2013-lfp-nominal-design.md#full-cell-tests) | See test conditions / gaps<br>parameter set only · [Match / gaps](data/batteries/prada2013-lfp-nominal-design.md#matching-and-gaps) |
| [LFP IFR14500 labels / manufacturer unresolved](data/batteries/milano-lfp-eis-2023.md) | Not extracted | Not extracted | Not extracted | [1 external source](data/batteries/milano-lfp-eis-2023.md#full-cell-tests) | EIS<br>Parameters unmatched · [Match / gaps](data/batteries/milano-lfp-eis-2023.md#matching-and-gaps) |
| [Undisclosed LFP/graphite 18650, 2 Ah (BPX)](data/batteries/bpx-lfp-18650-2ah-undisclosed.md) | [2 expressions](data/cells/bpx-lfp-18650-2ah-undisclosed.md#ocp-curves) | [6 records](data/parameters/bpx-lfp-18650-2ah-undisclosed--diffusion.csv) | [4 records](data/parameters/bpx-lfp-18650-2ah-undisclosed--kinetics.csv) | [Not linked](data/batteries/bpx-lfp-18650-2ah-undisclosed.md#full-cell-tests) | See test conditions / gaps<br>unmatched · [Match / gaps](data/batteries/bpx-lfp-18650-2ah-undisclosed.md#matching-and-gaps) |

### NMC

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [CALB generation 3b &#124; NEXTBMS2026](data/batteries/calb-gen3b-nextbms2026.md) | [4 pseudo-OCP](data/cells/calb-gen3b-nextbms2026.md#ocp-curves) | Not extracted | Not extracted | [1 external source](data/batteries/calb-gen3b-nextbms2026.md#full-cell-tests) | multi-T, dynamic, ageing, EIS<br>same model same study · [Match / gaps](data/batteries/calb-gen3b-nextbms2026.md#matching-and-gaps) |
| [CALB L148N58A](data/batteries/calb-l148n58a-2025.md) | Not extracted | Not extracted | Not extracted | [1 external source](data/batteries/calb-l148n58a-2025.md#full-cell-tests) | multi-T, dynamic, EIS<br>Parameters unmatched · [Match / gaps](data/batteries/calb-l148n58a-2025.md#matching-and-gaps) |
| [LG M50 &#124; 5 Ah NMC811/graphite-SiOx](data/batteries/lg-m50.md) | [2 expressions](data/cells/lg-m50.md#ocp-curves) | [6 records](data/parameters/lg-m50--diffusion.csv) | [7 records](data/parameters/lg-m50--kinetics.csv) | [3 packaged + 1 external source](data/batteries/lg-m50.md#full-cell-tests) | multi-T<br>Cross-study / mixed sources · [Match / gaps](data/batteries/lg-m50.md#matching-and-gaps) |
| [LG M50 &#124; O'Regan2022 characterization and model](data/batteries/lg-m50-oregan2022.md) | [2 reused expressions](data/cells/lg-m50-oregan2022.md#ocp-curves) | [43 records](data/parameters/lg-m50-oregan2022--diffusion.csv) | [14 records](data/parameters/lg-m50-oregan2022--kinetics.csv) | [1 external source](data/batteries/lg-m50-oregan2022.md#full-cell-tests) | multi-T<br>Cross-study / mixed sources · [Match / gaps](data/batteries/lg-m50-oregan2022.md#matching-and-gaps) |
| [LG M50LT &#124; Hallemans2025 grouped SPMe](data/batteries/lg-m50lt-hallemans2025.md) | [Reuse unresolved](data/cells/lg-m50lt-hallemans2025.md#ocp-curves) | [2 records (groups)](data/parameters/lg-m50lt-hallemans2025--diffusion.csv) | [4 records (groups)](data/parameters/lg-m50lt-hallemans2025--kinetics.csv) | [1 packaged + 1 external source](data/batteries/lg-m50lt-hallemans2025.md#full-cell-tests) | dynamic, EIS<br>same model same study · [Match / gaps](data/batteries/lg-m50lt-hallemans2025.md#matching-and-gaps) |
| [LG MJ1 &#124; DLR-SINTEF harvested-electrode characterization](data/batteries/lg-mj1-dlr-sintef.md) | [4 pseudo-OCP](data/cells/lg-mj1-dlr-sintef.md#ocp-curves) | [18 records](data/parameters/lg-mj1-dlr-sintef--diffusion.csv) | [6 records](data/parameters/lg-mj1-dlr-sintef--kinetics.csv) | [1 external source](data/batteries/lg-mj1-dlr-sintef.md#full-cell-tests) | dynamic, ageing<br>Cross-study / mixed sources · [Match / gaps](data/batteries/lg-mj1-dlr-sintef.md#matching-and-gaps) |
| [Samsung INR18650-20R / CALCE](data/batteries/calce-samsung-20r-dynamic.md) | Not extracted | Not extracted | Not extracted | [1 external source](data/batteries/calce-samsung-20r-dynamic.md#full-cell-tests) | multi-T, dynamic<br>Parameters unmatched · [Match / gaps](data/batteries/calce-samsung-20r-dynamic.md#matching-and-gaps) |
| [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](data/batteries/mohtat2020-nmc532-pouch.md) | [4 expressions](data/cells/mohtat2020-nmc532-pouch.md#ocp-curves) | [9 records](data/parameters/mohtat2020-nmc532-pouch--diffusion.csv) | [12 records](data/parameters/mohtat2020-nmc532-pouch--kinetics.csv) | [5 packaged](data/batteries/mohtat2020-nmc532-pouch.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](data/batteries/mohtat2020-nmc532-pouch.md#matching-and-gaps) |

### NCA

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Panasonic NCR18650B &#124; HNEI2016](data/batteries/panasonic-ncr18650b-hnei2016.md) | [4 pseudo-OCP](data/cells/panasonic-ncr18650b-hnei2016.md#ocp-curves) | Not extracted | Not extracted | [4 external sources](data/batteries/panasonic-ncr18650b-hnei2016.md#full-cell-tests) | multi-T, dynamic, ageing, EIS<br>Cross-study / mixed sources · [Match / gaps](data/batteries/panasonic-ncr18650b-hnei2016.md#matching-and-gaps) |
| [Molicel P45B &#124; About:Energy2026 BPX](data/batteries/molicel-p45b-aboutenergy2026.md) | [5 tables / fits](data/cells/molicel-p45b-aboutenergy2026.md#ocp-curves) | [7 records](data/parameters/molicel-p45b-aboutenergy2026--diffusion.csv) | [8 records](data/parameters/molicel-p45b-aboutenergy2026--kinetics.csv) | [2 external sources](data/batteries/molicel-p45b-aboutenergy2026.md#full-cell-tests) | multi-T, dynamic, ageing<br>same model same study · [Match / gaps](data/batteries/molicel-p45b-aboutenergy2026.md#matching-and-gaps) |
| [Molicel P45B &#124; TUM Rehm2026 measured half-cells](data/batteries/molicel-p45b-tum-rehm2026.md) | [5 pseudo-OCP](data/cells/molicel-p45b-tum-rehm2026.md#ocp-curves) | Not extracted | Not extracted | [1 external source](data/batteries/molicel-p45b-tum-rehm2026.md#full-cell-tests) | ageing<br>same model same study · [Match / gaps](data/batteries/molicel-p45b-tum-rehm2026.md#matching-and-gaps) |
| [NCA_Kim2011 &#124; NCA/graphite &#124; 0.43 Ah model input](data/batteries/kim2011-nca-nominal-design.md) | [2 expressions](data/cells/kim2011-nca-nominal-design.md#ocp-curves) | [6 records](data/parameters/kim2011-nca-nominal-design--diffusion.csv) | [7 records](data/parameters/kim2011-nca-nominal-design--kinetics.csv) | [Not linked](data/batteries/kim2011-nca-nominal-design.md#full-cell-tests) | See test conditions / gaps<br>unmatched · [Match / gaps](data/batteries/kim2011-nca-nominal-design.md#matching-and-gaps) |

### LCO

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Enertech &#124; LCO/graphite &#124; 2.28 Ah model input](data/batteries/enertech-lco-pouch-ai2020.md) | [2 tables / fits](data/cells/enertech-lco-pouch-ai2020.md#ocp-curves) | [6 records](data/parameters/enertech-lco-pouch-ai2020--diffusion.csv) | [7 records](data/parameters/enertech-lco-pouch-ai2020--kinetics.csv) | [4 packaged](data/batteries/enertech-lco-pouch-ai2020.md#full-cell-tests) | See test conditions / gaps<br>same study cell family · [Match / gaps](data/batteries/enertech-lco-pouch-ai2020.md#matching-and-gaps) |
| [SLPB78205130H &#124; LCO/graphite &#124; 0.680616 Ah model input](data/batteries/kokam-slpb78205130h-marquis2019.md) | [2 expressions](data/cells/kokam-slpb78205130h-marquis2019.md#ocp-curves) | [6 records](data/parameters/kokam-slpb78205130h-marquis2019--diffusion.csv) | [7 records](data/parameters/kokam-slpb78205130h-marquis2019--kinetics.csv) | [Not linked](data/batteries/kokam-slpb78205130h-marquis2019.md#full-cell-tests) | See test conditions / gaps<br>parameter set only · [Match / gaps](data/batteries/kokam-slpb78205130h-marquis2019.md#matching-and-gaps) |

### NCO

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Kokam SLPB75106100 &#124; 7.5 Ah NCO/graphite](data/batteries/kokam-slpb75106100-ecker2015.md) | [2 expressions](data/cells/kokam-slpb75106100-ecker2015.md#ocp-curves) | [6 records](data/parameters/kokam-slpb75106100-ecker2015--diffusion.csv) | [6 records](data/parameters/kokam-slpb75106100-ecker2015--kinetics.csv) | [2 packaged](data/batteries/kokam-slpb75106100-ecker2015.md#full-cell-tests) | See test conditions / gaps<br>same model same study · [Match / gaps](data/batteries/kokam-slpb75106100-ecker2015.md#matching-and-gaps) |

### LFP/NMC/NCA

| Battery / study | OCP | Diffusion | Kinetics | Full-cell tests | Coverage / matching |
|---|---|---|---|---|---|
| [Malaya three-model archive / per-model files unverified](data/batteries/malaya-three-chemistries-2022.md) | Not extracted | Not extracted | Not extracted | [1 external source](data/batteries/malaya-three-chemistries-2022.md#full-cell-tests) | dynamic<br>Parameters unmatched · [Match / gaps](data/batteries/malaya-three-chemistries-2022.md#matching-and-gaps) |

Material-only curves without a verified battery model remain in [the OCP material index](data/ocp/README.md); no commercial-cell assignment is inferred.

<!-- DATA_QUICKLINKS_END -->

NCR18650B includes four extracted HNEI half-cell branches and four full-cell sources; [read the extraction notes](docs/NCR18650B.md). P45B includes separate About:Energy BPX fits/parameters and [TUM Rehm2026 measured half-cell branches](data/batteries/molicel-p45b-tum-rehm2026.md). [The TUM rights/definition review](docs/TUM_OCP_RIGHTS.md) admits seven first-party curves only; third-party literature inputs remain excluded.

Missing OCP or tests are marked explicitly. Mohtat has separate author and PyBaMM parameter variants; choose one. Generated formula samples are labeled and are not measurements.

**Get involved:** [Contribute data](templates/README.md) · [Suggest a source](.github/ISSUE_TEMPLATE/source-suggestion.md) · [Research collaboration](#maintainer-and-collaboration)

<details>
<summary>Detailed material coverage and cell-matching evidence</summary>

## Material coverage

| Material family | Measured branches | Published tables | Expressions | Modeled OCPn | Identity / interpretation |
|---|---:|---:|---:|---:|---|
| LFP | 6 | 0 | 3 | 1 | SINTEF and ISU laboratory electrodes; A123 PD-ECM model; Afshar and BPX expressions |
| Graphite | 12 | 2 | 9 | 1 | Distinct measured, modeled, figure-fitted and borrowed inputs; reference/coordinate labels retained |
| NMC111 | 4 | 0 | 0 | 0 | SINTEF specimens; commercial full-cell identity unresolved |
| NMC532 | 6 | 0 | 2 | 0 | SINTEF electrodes, NEXTBMS harvested CALB and Mohtat pouch remain separate sources |
| NMC811 | 0 | 0 | 2 | 0 | Chen2020 M50 positive OCP and its explicitly reused O'Regan model expression |
| NMC (MJ1 source label) | 2 | 0 | 0 | 0 | DLR-SINTEF MJ1 positive half-cell branches |
| Graphite-SiOx | 2 | 0 | 0 | 0 | DLR-SINTEF MJ1 negative half-cell branches |
| LNMO | 4 | 0 | 0 | 0 | High-voltage spinel specimens; distinct from LMO |
| Silicon | 4 | 3 | 0 | 0 | Si-AQ-1 laboratory specimens plus three P45B fitted silicon branches |
| Silicon–graphite | 12 | 0 | 0 | 0 | SINTEF SiGr-AQ-1/2 and four TUM P45B harvested branches remain separate |
| LCO | 0 | 1 | 1 | 0 | Enertech published table; separate borrowed Marquis/Dualfoil expression |
| NCA | 3 | 1 | 1 | 0 | HNEI NCR18650B and TUM P45B measured branches; About:Energy P45B fit; Kim2011 nominal design |
| NCO | 0 | 0 | 1 | 0 | Ecker/Kokam upstream label; no NMC/NCA composition ratio inferred |

LMO and LTO are deferred until a reusable source and its definitions can be verified; LNMO is not relabeled as LMO. All measured branches retain their own direction and relative-throughput coordinate. Formula domains describe numerical evaluation and do not establish experimental fit validity.

## Coverage and cell matches

Use the [battery model index](data/batteries/README.md) for OCP, diffusion,
kinetics and full-cell links together. The [per-model extraction audit](docs/PARAMETER_AUDIT.md)
shows all 19 native packages, remaining source-only leads and why a component
has not been admitted. Each cell page carries its definitions, provenance,
parameter variants, full-cell association and missing items.

Seven pinned PyBaMM dictionaries now have their complete numeric/analytic inputs
stored. Their values include borrowed laws, circuit/thermal defaults and optional
SEI/plating/mechanics assumptions; record counts are not a count of independent
measurements. O'Regan experimental tables and published model inputs are distinct
variants. The Prada nominal LFP package does not identify an A123 commercial part.
Seven first-party TUM branches are admitted; remaining TUM source gaps and
M50LT third-party OCP permission remain explicit.
These records do not establish an independently validated, drop-in full-cell model.

The strongest LFP association is [Lin et al. (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/) and its [Oxford experiment deposit](https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513). Its fitted diffusion time is shared by both electrodes. We expose `D = r²/t_d` using the implementation's **assumed 5 µm radius**, with that condition attached; it is not an independently measured intrinsic LFP diffusivity. The deposited full-discharge trace is retained as associated experimental data.

## Full-cell matching and basic tests

Each cell package now includes an **evidence matrix** for OCP, diffusion, kinetics, full-cell observations and basic charge/discharge tests. Each component has record IDs, source IDs, its own match level and missing items. Test metadata separately records available channels and whether the data are instrument series, published experimental series or figure digitizations. See the [matching ledger and remaining gaps](docs/FULL_CELL_MATCHING.md).

Existing **A123 9 Ah** files cover CC charge and discharge at 2/4/6/8/10C. **LG M50** files include CCCV charging and C/10, C/2, 1C and 1.5C CC discharge; preconditioning remains labeled. These measured-current files remain distinct from the new time/voltage-only files. A nominal C-rate never becomes a manufactured measured-current trace.

The [official PyBaMM release notes](https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.0) establish the experimental attribution and Ecker digitization history. Enertech temperature files contain **temperature rise**, not absolute temperature. Their own timebases are retained in sidecars; no alignment, interpolation or addition of an assumed ambient temperature is performed. The 25 test files are not 25 independently identified specimens.

**Mohtat data are now available in the catalog.** The [official open-access page](https://deepblue.lib.umich.edu/data/concern/data_sets/kp78gg60j) was accessible through a normal browser, and all ten original files were downloaded. Earlier HTTP 403 responses described an automated-access failure. The five charging exports contain measured voltage and temperature against capacity, but no exported current or original timestamps. Author/PyBaMM differences and source protocol conflicts are detailed in [the Mohtat audit](docs/MOHTAT2020.md).

</details>

## Install and browse

Use Python 3.10+; Python 3.12 is recommended.

```bash
git clone https://github.com/FrankSuperG/electrochemical-battery-parameters.git
cd electrochemical-battery-parameters
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
ebp validate
ebp serve
```

`ebp validate` checks data schemas, references, coordinates, values and checksums. It does not run an electrochemical model.

Run `ebp cells` to find stable cell IDs. Open [the local viewer](http://127.0.0.1:8765). Filter and compare OCPs, switch between cell packages, inspect coverage and parameter origins, and download data with metadata. Choose **Offline bundle ZIP** to download a cell's data, metadata, available originals and licenses together. Use the **Variant** filter to distinguish the Mohtat author model from PyBaMM inputs. The viewer uses local assets, without CDNs, analytics or remote fonts. `ebp serve` binds to `127.0.0.1`; `ebp build-site --output site` only writes static files.

Hosting is optional. Your existing personal GitHub site can coexist with a separate project site. For a private source repository, see [local/offline use and free hosting choices](docs/HOSTING.md); no public deployment has been enabled.

## Python and CLI

```python
from ebp import Catalog

catalog = Catalog()
curve = catalog.get("bpx-lfp18650-lfp-ocp")
voltage = curve(0.5)                         # V vs Li/Li+
x, voltage = curve.sample(501)              # generated samples, not measurements
curves = catalog.search(material="LFP")
linked_ocp = catalog.search(cell_id="bpx-lfp-18650-2ah-undisclosed")

parameters = catalog.search_parameters(
    cell_id="a123-amp20m1hd-a", category="diffusion"
)
for parameter in parameters:
    print(parameter.value, parameter.record["unit"], parameter.record["conditions"])

tests = catalog.linked_tests("a123-amp20m1hd-a")
rows = catalog.full_cell_data(tests[0]["id"], normalized=True)
```

```bash
ebp search --material LFP
ebp search --cell bpx-lfp-18650-2ah-undisclosed
ebp parameters --cell a123-amp20m1hd-a --category kinetics --json
ebp tests --cell a123-high-power-pouch-9ah
ebp datasets --material NMC --test-type dynamic --profile US06
ebp datasets --material LFP --test-type cccv
ebp datasets --test-type eis --json
ebp datasets --files --material NMC --profile US06
ebp datasets --files --material LFP --test-type cccv --json
ebp show a123-amp20-effective-diffusivity-soc50
ebp export bpx-lfp18650-lfp-ocp --output formula.csv --count 2001
```

Measured OCP tables support linear interpolation and PCHIP. `.points()` returns native retained points; `.export_csv()` preserves them unless a resampling count is explicit. Formulas use a restricted AST interpreter, without `eval` or arbitrary Python imports. Non-finite inputs and out-of-domain evaluation are rejected; no default extrapolation is allowed.

Original LG M50 CSVs encode current as a magnitude plus `Md=C/D`. Normalized files use **charge-positive current**, temperatures in K and source row/index references. Oxford MAT/ZIP originals stay at checksum-pinned URLs; normalized CSVs retain every time row. Source NaNs become empty fields and are counted in metadata. The 9 Ah temperature column has conflicting source descriptions, so its exact sensor/ROI identity remains unresolved. A model interface that uses discharge-positive current needs an explicit sign conversion.

Temperature-dependent particle diffusion retains both source inputs, even when the selected implementation is independent of stoichiometry:

```python
D = catalog.get_parameter("mohtat2020-positive-diffusivity")
print(D(sto=0.5, T=298.15))   # m²/s; source model function, not a new measurement
silicon = catalog.search(material="silicon", representation="table")
```

## Optional PyBaMM OCP export

```bash
python -m pip install -e '.[pybamm]'
PYBAMM_DISABLE_TELEMETRY=true python examples/pybamm_ocp.py
```

`curve.to_pybamm()` creates a linear `pybamm.Interpolant` with extrapolation disabled. Expressions are sampled for this conversion. Measured branch-throughput curves require an explicit `StoichiometryMapping(theta_start, theta_end, evidence)`: no absolute electrode balancing is inferred. The adapter supplies an OCP component, not a complete cell model.

## Data scope and interpretation

- **Electrode OCP, full-cell pseudo-OCV and loaded terminal voltage remain distinct.** Neither Oxford study's conventional allocation of full-cell OCV establishes measured half-cell OCPs.
- **Electrode lithium fraction, normalized branch throughput and whole-cell SOC remain distinct.** Plots group different coordinate types and directions separately.
- **Kinetic definitions travel with values.** AMP20 volumetric exchange current in A/m³, LG surface exchange-current laws, and BPX rate constants in mol/(m²·s) cannot be substituted directly.
- **Measured, fitted, derived, borrowed and assumed origins remain visible.** Optimizer initial guesses are not imported as fitted results. BPX's estimated thermal properties are labeled.
- **Unknown information stays unknown.** Room temperature does not become 298.15 K; nominal capacity does not create a commercial identity; a study link does not establish the same specimen.
- **Data checks establish catalog consistency.** Schema, source-value and export checks do not establish model-prediction accuracy.

PyBaMM's `Prada2013` file borrows its LFP OCP from Afshar2017 and its graphite OCP from Chen2020. Scientific attribution is recorded per function. BPX electrolyte and entropy sources are disclosed in its header; those non-OCP functions/tables are not yet imported.

## Reproduction and layout

```bash
python -m pip install -e '.[dev,pybamm]'
python scripts/seed_v01.py --download   # reconstructs all catalog expansions
ebp validate
PYBAMM_DISABLE_TELEMETRY=true python -m pytest -q
ebp build-site
python -m build
```

Upstream commits, URLs and SHA-256 hashes are pinned; Zenodo originals also retain source MD5 checks where supplied. Working source caches are ignored by Git; the small Mohtat author originals are committed and hash-pinned for reliable offline reconstruction. ORA returns HTTP 403 to GitHub-hosted runners, so CI restores the four Oxford inputs from an attributed [source-cache release](https://github.com/FrankSuperG/electrochemical-battery-parameters/releases/tag/upstream-lfp-v0.2.0) and verifies the same primary-source SHA-256 pins. Primary URLs remain authoritative. Only the selected observations, transcribed evidence, metadata and source notices are packaged. `requirements-lock-py312.txt` documents one Python 3.12 verification environment, not a universal lock.

```text
src/ebp/data/             Authoritative packaged catalog
  catalog.json           Electrode OCP records and representations
  parameters.json        Scalars and kinetic functions
  cells.json             Identities, coverage and match evidence
  full_cell_tests.json    Packaged-test metadata, channels, processing and links
  external_datasets.json Metadata-only links to large external full-cell datasets
  matching_audit.json     Component match matrix, open gaps and research leads
  sources.json           Papers, datasets and software roles
  assets.json            Original URLs, versions and checksums
  curves/                Retained OCP points and source coordinates
  full_cell/             Original CSVs / normalized observations
  evidence/              Published-table evidence and byte-identical TXT/CSV sources
  schema/                Structural constraints
src/ebp/web/              English static viewer and companion logo
src/ebp/licenses/         Upstream licenses and dataset notices
scripts/seed_lfp.py       LFP extraction and normalization
scripts/seed_materials.py Multi-material measurements and model functions
scripts/seed_fullcell.py  Ecker/Enertech links, basic tests and missing-item audit
scripts/seed_mohtat.py    Official author MATs, original parameters and crosswalk
scripts/mohtat_assets.json Original-author source URLs and SHA-256 pins
scripts/fullcell_assets.json Pinned parameter and experiment assets
scripts/material_assets.json Pinned multi-material source assets
scripts/lfp_assets.json   Pinned LFP source assets
```

See [data definitions](docs/DATA_MODEL.md), [curation and match decisions](docs/CURATION.md), [roadmap](docs/ROADMAP.md) and [contribution guide](CONTRIBUTING.md).

## Contribute data

Help extend the library with OCP curves, diffusion and kinetic parameters, other electrochemical inputs, and matching full-cell tests. **Partial datasets and source suggestions are welcome.** Start with the [data contribution template](templates/data-contribution.md) and [CSV templates](templates/README.md), or use the [short source suggestion template](.github/ISSUE_TEMPLATE/source-suggestion.md) to recommend a paper or dataset. The templates ask for sources, reuse terms, definitions, cell-match evidence and missing items; they do not require an already complete parameter set.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review and import workflow. Open an issue or pull request when repository access permits, or contact the maintainer by email with a contribution or source suggestion.

See the [prepublication review](docs/PREPUBLICATION_REVIEW.md) for the current audit scope and remaining limits, and [candidate data sources](docs/DATA_CANDIDATES.md) for newly reviewed leads. Candidate sources are separate from imported catalog records.

## Maintainer and collaboration

**Feng Guo** conducts battery research at VITO and UHasselt in Belgium as an FWO Senior Postdoctoral Fellow. He works on electrochemical models for battery management, with interests in parameter identification, state estimation, fault diagnosis and control. He develops [CPG-SPMT](https://github.com/FrankSuperG/CPG-SPMT) and maintains this parameter library and the [Electrochemical Battery Model Atlas](https://github.com/FrankSuperG/electrochemical-battery-model-atlas).

Collaboration is welcome on parameter curation, source matching, electrochemical testing, data sharing and open-source research tools. To discuss a contribution or research collaboration, contact **[feng.guo@vito.be](mailto:feng.guo@vito.be)**.

[Google Scholar](https://scholar.google.com/citations?user=z2SHUxkAAAAJ&hl=en) · [Academic homepage](https://franksuperg.github.io/feng-guo-academic/) · [GitHub](https://github.com/FrankSuperG)

## Attribution and licenses

Cite the scientific sources for the records you use and retain upstream notices. Project code, documentation and logo use MIT; experimental data and imported implementations keep their source licenses. See [DATA_LICENSES.md](DATA_LICENSES.md) and [CITATION.cff](CITATION.cff).

| Source | Role / license |
|---|---|
| [SINTEF / Zenodo v3](https://zenodo.org/records/20086298) | Half-cell measurements · CC BY 4.0 |
| [Afshar et al., 2017](https://arxiv.org/abs/1709.03970v1) | LFP OCP scientific attribution |
| [Chen et al., 2020](https://doi.org/10.1149/1945-7111/ab9050), [full-cell data](https://zenodo.org/records/4032561) | LG M50 parameter attribution / observations · CC BY 4.0 data |
| [PyBaMM v25.4.2](https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion) | Pinned OCP, diffusion and kinetic implementations · BSD-3-Clause |
| [Marquis et al., 2019](https://doi.org/10.1149/2.0341915jes) | LCO/graphite model context; electrode functions attributed to Dualfoil by upstream |
| [Mohtat et al., 2020](https://doi.org/10.1149/1945-7111/aba5d1) | NMC532/graphite parameter attribution via pinned implementation |
| [Kim et al., 2011](https://doi.org/10.1149/1.3597614) | NCA/graphite nominal-design parameter attribution via pinned implementation |
| [BPX example](https://github.com/FaradayInstitution/BPX/blob/0f591336937c2c57509f20ab23f9908e58f7a757/examples/lfp_18650_cell_BPX.json) | LFP parameter example · MIT |
| [O'Regan et al., 2022](https://doi.org/10.1016/j.electacta.2022.140700), [parameter tables](https://zenodo.org/records/5171874) | LG M50 experimental tables · CC BY 4.0; separate model implementation · BSD-3-Clause; three Cp files quarantined |
| [Lin et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/), [data](https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513), [code](https://github.com/Battery-Intelligence-Lab/multiscale-coupling/tree/dba3649f2eeb4228d2849e4d4e748c91ed6ad7a4) | AMP20 fitted parameters / observations · CC BY 4.0; code · BSD-2-Clause |
| [Kumtepeli et al., 2026](https://doi.org/10.1016/j.jpowsour.2025.238764), [Oxford data](https://ora.ox.ac.uk/objects/uuid:fe9bad3e-8a72-4e3b-8f01-fec3324b6758) | 9 Ah study family / observations · CC BY 4.0 data |
| [Ecker I](https://doi.org/10.1149/2.0551509jes), [Ecker II](https://doi.org/10.1149/2.0541509jes), [Richardson2020](https://doi.org/10.1016/j.electacta.2020.135862) | Kokam characterization, validation and fitted/digitized curve lineage |
| [Ai2020](https://doi.org/10.1149/2.0122001JES), [Rieger2016](https://doi.org/10.1149/2.0441608jes) | Enertech parameterization and experimental lineage; borrowing remains explicit |
| [PyBaMM data v1.0.2](https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2) | Versioned experimental redistribution and published OCP tables · BSD-3-Clause; separate notice retained |

The README identity is a companion to [Electrochemical Battery Model Atlas](https://github.com/FrankSuperG/electrochemical-battery-model-atlas); its generation brief is recorded in [assets/README.md](assets/README.md).
