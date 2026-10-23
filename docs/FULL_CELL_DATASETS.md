# Full-cell dataset links and material groups

[Browse by material](../data/full-cell/README.md) · [Dataset metadata](../data/full-cell/datasets.json) · [File locators CSV](../data/full-cell/files.csv) · [File-review evidence](EXTERNAL_FILE_REVIEW.md)

Large observations stay with their original providers. E-BatP stores reviewed
source links, selected file/container paths, test tags, cell labels, source
versions, reuse terms, parameter associations and missing items. Catalog search,
exports, the viewer and CI do not fetch these external observations. The existing
61 packaged branch/test files remain unchanged.

The sixteen records describe dataset links, not sixteen tests or independent cells.
CALCE contributes two cell sections on one page; one multi-material deposit can
appear under LFP, NMC and NCA. The current file index has 427 selected locators,
including parent archives, named members, test files and parameter evidence.
These are not 427 imported measurement files or a complete test matrix.
The [NCR18650B source guide](NCR18650B.md) links four additions and their ageing,
half-cell and cross-study matching limits. The [OCP-first screen](OCP_FIRST_EXPANSION.md)
reviews 21 source families and five further additions.

## Choose material and test

- [LFP](../data/full-cell/LFP.md): A123 1–4C CCCV charging, UDDS, CALCE combined
  DST/US06/FUDS workbooks, EIS member paths and existing CC data.
- [NMC](../data/full-cell/NMC.md): CALB CC/US06/EIS locations, CALCE Samsung 20R
  US06 archives, M50LT same-study impedance/drive-cycle evidence, NEXTBMS harvested
  half cells with multi-temperature EIS/ageing, LG M50 three-temperature discharge
  files and cross-study LG MJ1 dynamic ageing.
- [NCA](../data/full-cell/NCA.md): NCR18650B full/half-cell RPT, initial
  pseudo-OCV/pulse/EIS, ageing and representative multi-rate discharge links.
  The Malaya RAR still has no verified NCA-specific US06 member. No NCR18650B
  source is joined to the Kim2011 nominal-design parameters. P45B adds published
  OCP/parameter links, four-temperature WLTP and a separate ageing-checkup source.
- [LCO](../data/full-cell/LCO.md) and [NCO](../data/full-cell/NCO.md): existing
  observations retain their source labels, digitization and missing channels.

```bash
ebp datasets --material NMC --profile US06
ebp datasets --files --material NMC --profile US06
ebp datasets --files --material LFP --test-type cccv --json
ebp datasets --files --test-type eis --json
ebp datasets --cell lg-m50lt-hallemans2025 --json
ebp datasets --material NCA --aging-status available --json
```

Dataset search uses provider-declared coverage. `--files` searches inspected
locators and does **not** inherit a dataset's profiles or per-model assignment.
Consequently NCA/US06 returns the multi-chemistry dataset but no confirmed
NCA-specific file locator. This is a source-review gap, not proof that no such
file exists. An archive-member link opens its parent ZIP/RAR/7z; extract the exact
named member yourself.

The **OCP anchor** column separates measured external half-cell sources, published
fitted parameterisation, explicit expression reuse and cross-study references.
Whole-cell OCV is not electrode OCP. `ocp_anchor.half_cell_temperatures_C` is
independent of full-cell source temperatures; unknown values remain empty.
`parameter_components` describes joins to native catalog curve/parameter records.
Imported OCP and parameter values are stored locally; other leads retain their
admission gaps. Read the [fixed storage/extraction rules](PARAMETER_STORAGE.md).

The **Ageing data** column distinguishes `available`, `not_reported` and
`unverified`. Available sources retain cycle/calendar kinds, evidence and linked
file paths. Formation, repeated initial tests and simulated degradation alone do
not count as measured ageing. Not reported is not proof of absence. Use
`--aging-status` (Python: `aging_status`); with `--files`, this filters the parent
source, not each file. The file CSV calls this `dataset_aging_status`.

```python
from ebp import Catalog

catalog = Catalog()
for item in catalog.search_dataset_files(material="NMC", profile="US06"):
    print(item["dataset_id"], item["source_path"], item["url"])
    print(item["verification"], item["content_review"], item["parameter_match"])
```

`full_cell_data()` reads existing packaged test IDs only. It does not download
an external dataset or convert a file locator into normalized observations.

## What the file review established

| Source | File/container location | Parameter association and remaining limits |
|---|---|---|
| [A123 26650 m1b / UCCS](../data/full-cell/uccs-a123-26650m1b-2021.md) | `CCCV/A002_CCCV_{1,2,3,4}C.mat`, a second 1C file, `Miscellaneous/A002_UDDS_P25.mat` / `P35.mat`, plus pulse/OCV representatives | Direct source-listed links; file contents not read. No US06/EIS located in reviewed folders. Different from catalog 18650M1A, AMP20 and 9 Ah pouch entries. |
| [CALCE Samsung 20R](../data/full-cell/calce-samsung-20r-dynamic.md) | Source-table OCV and dynamic ZIP URLs; 25 degC US06 ZIP contains separate 50SOC and 80SOC XLS files | ZIP member names/sizes verified. OCV source labels SP1/SP3 differ from dynamic SP2; identical-specimen matching is not established. License not stated. |
| [CALCE A123](../data/full-cell/calce-a123-dynamic.md) | `A123_DST-US06-FUDS-25.zip` contains `A1-007-...xlsx` and `A1-008-...xlsx` | Combined-profile filenames verified; phase boundaries, exact part and OCV specimen mapping unresolved. No catalog parameter join; license not stated. |
| [CALB L148N58A](../data/full-cell/calb-l148n58a-2025.md) | `Processed Data/Temperature_25C/{DV_US06,EIS_test,C20_charge,C20_discharge}/59294.mat`; representative raw workbooks under `Raw Data/Temperature_25C/59294/` | Actual source directories and selected download UUIDs verified. No electrode OCP/D/kinetics join. Pulse rates do not establish a continuous multi-rate CC sweep. Other cells/temperatures not exhaustively checked. |
| [University of Malaya](../data/full-cell/malaya-three-chemistries-2022.md) | One source-listed `Battery Test Data.rar` | LFP/NCA/NMC and US06 are collective source declarations. Inner paths and the per-model/profile matrix remain uninspected; direct automated header access returned 403. No parameter join. |
| [600 mAh LFP / Figshare](../data/full-cell/milano-lfp-eis-2023.md) | `Measurements.rar::Measurements/Bxx/EIS measurements/Test_n/Hioki/...csv` | Complete directory has 440 EIS CSV, 11 capacity CSV and 10 BMP. Eleven sample labels and IFR14500 filenames do not establish manufacturer/part, temperature or intrinsic parameters. CSV contents were not read. |
| [LG M50LT / Hallemans](../data/full-cell/hallemans-m50lt-eis-2025.md) | Pinned author EIS MAT, fitted-group MAT and unnamed drive-cycle MAT | Same model/study as six catalog diffusion/kinetic group records. OCP reuse permission, intrinsic D/k and serialized-specimen joins remain missing. Drive cycle is not labeled US06. |
| [NCR18650B / HNEI](../data/full-cell/hnei-ncr18650b-2016.md) | ZIP with harvested NE/PE and selected full-cell FORM/RPT members | Four low-rate native half-cell branches extracted under CC0 1.0; same-study full-cell FORM/RPT links remain external. D/kinetics and donor serial unresolved. |
| [NCR18650B / Bayreuth](../data/full-cell/bayreuth-ncr18650b-2023.md) | All 13 pseudo-OCV, pulse and EIS MAT/CSV links | Beginning-of-life characterization; whole-cell pseudo-OCV is not electrode OCP. Contents unread; license not stated. |
| [NCR18650B / Virtual Vehicle](../data/full-cell/virtual-vehicle-ncr18650b-aging-2023.md) | All 116 H5 cell files and protocol PDF | Ageing/RTP documented; H5 unread. Censoring and profile-ID conflicts retained; no cross-study specimen join. |
| [NCR18650B / Stanford](../data/full-cell/stanford-ncr18650b-rates-2021.md) | Fifteen NCA/k1 XLSX paths at 0.05/1/2/3/5C and 5/25/35 degC | Discharge sweep, not a multi-rate charge sweep. Other deposit chemistries are different models; no OCP/D/k join. |
| [CALB / NEXTBMS](../data/full-cell/nextbms-calb-nmc532-2026.md) | Harvested half-cell CSVs, full-cell characterization and ageing members in three 7z containers | Four half-cell branches now imported; same study/model, distinct specimens; full-cell EIS at four temperature labels. Declared and directory stage counts differ. |
| [About:Energy P45B](../data/full-cell/aboutenergy-p45b-2026.md) | Published BPX and four-temperature CC/GITT/WLTP ZIP; eVTOL at three temperatures | Five fitted OCP tables and 67 BPX/custom-law inputs imported; original raw half-cell points not independently located. Experimental/model columns and alternate reports remain separate. |
| [TUM P45B](../data/full-cell/tum-p45b-halfcell-aging-2026.md) | Five harvested finite-current branches, two reconstructed Si files and one 800-EFC pOCV checkup table | Measured blend/cathode, reconstructed Si and whole-cell checkups retain distinct origins; measurement-data reuse scope unresolved. |
| [LG M50 / TEC2021](../data/full-cell/tec-lgm50-multitemperature-2021.md) | 48 pinned CSV paths at 0/10/25 degC and 0.1/0.5/1/2C | Explicit reuse of existing Chen2020 OCP expressions; different study and unjoined specimen serials. No WLTP in inspected release. |
| [LG MJ1 / SNU2024](../data/full-cell/snu-mj1-dynamic-aging-2024.md) | One source-listed 80-cell staged-ageing ZIP | DLR-SINTEF half-cell OCP is a same-model cross-study reference. Inner paths and I/V/T unverified; not a named US06/WLTP trace. |

Open a source's row for the exact path, direct file or parent-container link,
per-file review level and all missing items. The [dated review](EXTERNAL_FILE_REVIEW.md)
records the original seven-source audit; the [NCR18650B guide](NCR18650B.md) and
[OCP-first screen](OCP_FIRST_EXPANSION.md) cover subsequent primary evidence,
protocol distinctions, temperature scope and source conflicts.

## Interpretation and reuse

A material family is a discovery category. It never establishes that a test and
a parameter belong together. Per-component `parameter_components` records keep
OCP, diffusion and kinetics associations separate. M50LT time scales/capacitances
remain grouped fitted quantities; EIS does not uniquely identify intrinsic D/k.

Whole-cell OCV/pseudo-OCV is distinct from electrode OCP. A source temperature
setpoint is not a measured trace. A file with EIS in its name is not proof of
complex-impedance columns; a raw workbook may contain conditioning logs. A pulse
rate is not a complete constant-current discharge rate. Source filenames and
sample labels are retained without inventing serial numbers or phase boundaries.

`source_listing` verifies a listed path/link. `archive_directory` verifies a
member name and size, not its contents. `existing_source_audit` refers to data
already reviewed in the catalog. `content_review=not_read` remains explicit.
`documentation_reviewed` applies to protocol documents, not observations.
`parameter_metadata_reviewed` identifies structure/header inspection of the
external BPX package, not a numerical-array or model-performance audit.
There is no automatic URL-health certification for every file.

Dataset licenses remain with the providers. CC BY 4.0 applies to the selected
Mendeley/Figshare sources; pinned author M50LT data use BSD-3-Clause and do not
clear third-party OCP rights. CALCE requests citations but no standard reuse
license was identified. HNEI NCR18650B data are CC0 1.0; the Bayreuth record has
no stated license in the inspected metadata. `not-stated` is not a permissive
redistribution grant.

Model simulation, fitting and validation remain outside this repository's scope.
This review adds access and matching evidence, not new model-performance results.

## Contribute an external source

Use [the JSON template](../templates/external-dataset.json) and retain the
schema-required per-component evidence and requested-test coverage. Add selected
`file_links` with `source_path`, source cell/sample labels, test/profile tags,
conditions, `verification`, `content_review` and notes. Leave unknown fields null;
never copy a mixed dataset's claims onto every file. Archive-member paths use
`container.zip::folder/member.xlsx` and must have directory evidence. A parent
archive link must not be presented as a standalone member download.
Include required `aging_data`: status, kinds, source URL/text and representative
paths already in `file_links`. Use empty kinds/paths for not-reported or unverified
coverage. Protocol PDFs use kind `documentation`, not experimental-test tags.
Include `ocp_anchor` with type, evidence/source URLs, verified paths and a separate
half-cell temperature list. Schema 1.4 also distinguishes imported half-cell branches, model diffusivity inputs and native kinetic coefficients. These quantity labels preserve source definitions and do not assert independent measurement.

```bash
ebp validate
python scripts/build_data_index.py
```

The registry is authored metadata and is not rewritten by source reconstruction.
An optional [archive-directory inspector](../scripts/inspect_external_archives.py)
performs bounded ZIP/RAR5 header reads, plus optional 7z listing with
`pip install '.[archive-review]'`, only when explicitly invoked by a reviewer. It is
not called by catalog search, viewer generation, normal reconstruction or CI.
