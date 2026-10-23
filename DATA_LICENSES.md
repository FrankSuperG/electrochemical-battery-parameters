# Data and third-party code licenses

The root MIT license applies to original project code and documentation, not to
third-party experimental observations or formula implementations.

Python distribution metadata lists `MIT AND BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0` for the
combined shipped contents. This does not relicense individual files: original
project software remains MIT and each data/implementation record keeps its
source-specific terms. Other external sources and their notices remain scoped
to the provenance identified below.

## HAIDI admission in v0.15

The seven HAIDI derived pseudo-OCP CSVs and all eight retained author MAT
originals keep **CC BY 4.0** data terms from the exact-DOI TUM publisher
catalog distribution in open.bydata/GovData. The generic `cc-by` URI resolves
to CC BY 4.0 through GovData and the official DCAT vocabulary; attribution and
conflicting incomplete metadata are recorded in the [source review](docs/HAIDI_REHM2025.md).
The framework root MIT notice is not the HAIDI data grant.

Attribute Mathias Rehm, Marco Fischer, Manuel Rubio-Gomez, Moritz Schuette,
Dirk Uwe Sauer and Andreas Jossen; cite original paper 10.1016/j.jpowsour.2025.236290,
dataset 10.14459/2024mp1762675 and the additionally requested Rehm2026 framework
paper. Changes are branch-coordinate normalization/orientation and ordering;
source capacity and one-based row columns preserve every admitted node. No
new smoothing, clipping, row removal or endpoint insertion. The entire 0.05C
cathode-delithiation original is quarantined, with no admitted OCP derivative.

The author folder notice retains framework MIT documentation terms and its
original attribution request. The project's factual rights/quality review is
original MIT curation text and includes source response hashes/URLs; these do
not relicense measurement data. The article PDF, full release ZIP and whole-cell
observation payloads are not redistributed. [Exact asset pins](scripts/haidi_assets.json).

## First-party TUM admission in v0.14

Seven original Rehm2026 half-cell MATs and derived tables retain **MIT**, scoped
to author-origin files in fixed Zenodo release 19555109. The release metadata,
Mathias Rehm notice, per-folder first-party attribution and original paper
provide the combined admission basis. The [rights review](docs/TUM_OCP_RIGHTS.md)
and [asset manifest](scripts/tum_ocp_assets.json) identify every admitted member.
The author copyright/permission notice is packaged unchanged. Original normalized
capacity and source-row columns preserve all nodes; only the uniform branch
coordinate and ordering change. No whole-cell payload is added.

This decision does not clear third-party literature digitizations, reconstructed
silicon as measured data, or M50LT personal-communication inputs. Article access
is not used as a blanket data license. Original publication attribution remains
required. Public [Zenodo metadata](https://about.zenodo.org/policies/) and
[DataCite metadata](https://support.datacite.org/docs/datacite-data-file-use-policy)
are retained under their CC0 metadata terms, separately from the MAT
data; an empty dataset rightsList does not acquire the metadata's reuse terms.

## Extraction follow-up in v0.13

O'Regan's 55 parameter-table derivatives and original parameter ZIP are **CC BY
4.0**, with original authors, DOI and fixed-record license metadata retained.
Three Cp CSVs remain unmodified in the archive but are excluded as physical Cp
tables because their definition is unresolved. Model formulas/scalars come
separately from **BSD-3-Clause PyBaMM v25.4.2**; the paper PDF is not redistributed.

The completed Chen, Marquis, Mohtat, Kim, Ai, Ecker and Prada implementation
inputs retain the existing PyBaMM BSD-3-Clause notice. Borrowed formulas and
optional SEI/plating/mechanics assumptions are not relabeled measured cell data.
The three BPX LFP reference-law expressions retain the original **MIT** terms.
P45B's seven additional custom-law/contact records and pinned author parser/helper
files retain **BSD-3-Clause**, with the About:Energy notice already packaged.
No new full-cell payload or unclear third-party OCP is redistributed.

## Extracted OCP and parameter sources in v0.12

Two original HNEI NCR18650B half-cell MAT members and four extracted branches
retain the dataset's **CC0 1.0** terms (Zenodo 60232). Packaged API metadata and
the fixed-record export identify the grant; the paper is cited separately.

Four NEXTBMS CALB half-cell sweep CSVs and the author half-cell README are
retained under **CC BY 4.0** from Zenodo 22301764. Changes: keep source voltage
and specific capacity; retain the last row at repeated capacity for a strictly
increasing normalized branch coordinate; store original row references. The
unmodified originals preserve the omitted startup voltages.

The pinned AEPyBaMM Molicel P45B BPX, five fitted OCP exports and 60 non-OCP
records retain **BSD-3-Clause**. The full About:Energy notice is retained in
`src/ebp/licenses/AEPyBaMM-BSD-3-Clause.txt` and in pinned evidence. OCP exports
select native nodes inside source particle bounds without numerical refitting.
Source-defined phases, units and model-input origins remain explicit.

These grants do not extend to TUM literature input data or M50LT third-party
OCP. Those remain external with unresolved reuse scope. No new full-cell payload
is redistributed. [Extraction details](docs/PARAMETER_STORAGE.md).

## NCR18650B external links in v0.10

HNEI Zenodo 60232 reports `cc-zero` in its API and CC0 1.0 in its record export.
Virtual Vehicle Zenodo 7896429 and Stanford Mendeley kxsbr4x3j2 v2 state CC BY 4.0
for their datasets. No license was found in the inspected page, API or export
for Bayreuth Zenodo 8369275; its observations remain links pending clarification.
Open access alone is not a reuse grant.

At v0.10, only metadata, directory evidence and external locators were packaged.
The v0.12 half-cell extraction is described above; other full-cell observations
and the author protocol PDF remain external.
Source MD5 values identify external objects, not independent payload verification.
Article terms remain distinct from dataset terms. See [the source guide](docs/NCR18650B.md)
for exact records, matching limits and reuse evidence.

## OCP-first external links in v0.11

NEXTBMS Zenodo 22301764 and P45B experimental release 19052626 state CC BY 4.0.
The P45B README retains copyright/liability notices; its separately linked BPX
parameter package is in the pinned BSD-3-Clause AEPyBaMM repository. TEC2021 data
and code are linked from the BSD-3-Clause author repository; its Zenodo record
uses the less-specific `other-open` label. LG MJ1 SNU v2 states CC BY 4.0.

TUM's MATLAB framework is MIT, but its README explicitly asks users to check
licenses and attribution for published input data. No blanket measurement-data
grant is imposed on that collection. The v0.14 first-party subset is cleared
separately above; the remaining literature inputs stay unresolved. The Python
mirror's BSD license is not substituted for it.
Third-party curves and reconstructed silicon retain their respective origins.

At v0.11, these additions were links and review metadata only. The v0.12
half-cell/BPX extraction is described above; full-cell observations stay external
and no author code is executed.
See [the OCP-first source ledger](docs/OCP_FIRST_EXPANSION.md).

## LG MJ1 / DLR-SINTEF addition in v0.8

Selected laboratory workbook cells, original Parquet, JSON/JSON-LD and Python evidence files are
from Yannick Kuhn, Bhawna Rana, Micha Philipp, Christina Schmitt, Roberto Scipioni,
Eibar Flores, Dennis Kopljar, Simon Clark, Arnulf Latz and Birger Horstmann.
The fixed Zenodo records under [collection 15407849](https://zenodo.org/records/15407849)
explicitly license these datasets CC BY 4.0. Packaged API metadata and
`scripts/mj1_assets.json` retain exact record/file URLs, license evidence,
published MD5 and pinned SHA-256. The existing CC BY 4.0 license text is retained.

Changes: extract finite pseudo-OCP nodes with original Parquet row indices;
retain first occurrence per duplicate coordinate and omit missing coordinates;
extract numeric workbook D/i0 cells, omitting source NA/blanks rather than
adopting processed zero substitutions; convert cm2/s to m2/s and mA/cm2 to A/m2;
retain model/direction-specific diffusion values and source error bounds; extract
an explicit scalar selection with units and origins. No voltage smoothing,
resampling, source-code execution or silent scientific correction is applied.
Sources have not endorsed this catalog.

The complete MJ1 workbook remains external because its OCV sheet also contains
separately attributed literature silicon curves. No CC BY 4.0 sublicense is
asserted for those columns. Only a scoped selected-cell JSON is redistributed;
its digest identifies our derivative, while embedded source MD5/SHA-256 and
Excel addresses identify the original. No silicon literature OCV samples are
curated or packaged by this addition.

The associated article DOI 10.1039/D5DD00247H is separately labeled CC BY 3.0.
Article images/text are not repackaged as datasets. The inspected electrode GITT
tests remain external source links and are not relabeled full-cell observations.
See [MJ1 review](docs/LG_MJ1.md) for source conflicts, assembly and matching limits.

## LG M50LT / Hallemans2025 addition in v0.7

Original whole-cell EIS and drive-cycle MATs, the fitted-result MAT and Fig10/Fig11
scripts are from the Hallemans2025 authors, pinned to author repository commit
`3308a34396b8b56cd614291dd151c3405577c068`, under its root BSD-3-Clause license.
The unchanged notice is packaged as `src/ebp/licenses/Hallemans2025-BSD-3-Clause.txt`.
Scientific authors, exact URLs and hashes are in `scripts/hallemans_assets.json`.
No upstream code is executed. The authors have not endorsed this project.

Changes: extract eighteen fitted scalar groups with definitions/units and original
vector indices; extract all measured t/i/v drive-cycle rows without resampling;
leave missing temperatures blank; classify mode by signed i; retain all measured
complex EIS components and distinguish seven-SOC fitted model components.
Original files remain unchanged. The EIS CSV is a derived table, not an instrument
export. Scalars are joint fit results, not newly measured intrinsic properties.

About:Energy M50LT electrode OCPs are **not redistributed**. The paper identifies
them as personal communication; separate reuse terms have not been established.
The company's separate BPX license is not transferred to this battery. External
URLs and hashes are provenance leads only. The review and implementation
boundaries are documented in [HALLEMANS2025.md](docs/HALLEMANS2025.md).

| Content | Attribution | License |
|---|---|---|
| `src/ebp/data/curves/sintef-*.csv` | Eibar Flores, Sridevi Krishnamurthi, Killian Stokes-Rodriguez, Julie Cathrine Guldahl, Charifa Hakim, Simon Clark, Nils Peter Wagner, Sergi Obrador, Andrés Bernabeu Santisteban; SINTEF and collaborators; Zenodo record 20086298 v3 | CC BY 4.0 |
| SINTEF experimental and electrode metadata | Same dataset and authors | CC BY 4.0 |
| `src/ebp/data/full_cell/LGM50_cell*.csv`, originals and normalized derivatives | Chang-Hui Chen, Ferran Brosa Planella, Kieran O'Regan, Dominika Gastol, W. Dhammika Widanage, Emma Kendrick; Zenodo record 4032561 | CC BY 4.0 |
| PyBaMM OCP expressions and their generated samples | Copyright (c) 2018–2025, the PyBaMM team; v25.4.2 pinned parameter modules | BSD-3-Clause |
| LG M50 non-OCP numeric parameters and kinetics expressions | Copyright (c) 2018–2025, the PyBaMM team; v25.4.2 `Chen2020.py`; Chen et al. 2020 and references therein | BSD-3-Clause |
| Original software, schemas and explanatory documentation | FrankSuperG | MIT |

SINTEF dataset: https://doi.org/10.5281/zenodo.20086298

Changes to SINTEF data: selected the third recorded cycle, selected the two
constant-current steps, excluded rest, removed repeated capacity values (first
point retained), added a branch-relative capacity coordinate, and retained source
row positions. No voltage smoothing or resampling is applied to distributed CSV
files. The browser graph samples values for display; CSV downloads preserve the
full extracted points. Detailed counts and transformation parameters are in each
record's provenance. The source authors have not endorsed this project.

Formula implementation: https://github.com/pybamm-team/PyBaMM/blob/v25.4.2/src/pybamm/input/parameters/lithium_ion/Prada2013.py

Formula changes: renamed `sto` to `x`, removed the NumPy namespace, and retained
the original coefficients. Scientific attribution is Afshar et al. (2017) for LFP
and Chen et al. (2020) for graphite, as stated in that upstream file. The original
papers' formula equations have not been independently audited in this release.

LG M50 full-cell data: https://doi.org/10.5281/zenodo.4032561

Original CSV files are copied byte-for-byte. Normalized derivatives skip the
instrument banner, use Md=C/D to interpret current magnitude as charge-positive
signed current, convert temperatures from degrees Celsius to kelvin, and retain
record numbers and zero-based original file-row positions. No smoothing or
resampling is applied to distributed test files. Source authors have not endorsed
this project. Browser plots select the four validation discharge steps and sample
them for display; original and normalized downloads preserve every observation.

The kinetics implementation fixes the gas constant to 8.314462618 J/mol/K and
retains the upstream Arrhenius law and concentration convention. Numeric parameters
are extracted without executing the source dictionary. No claim is made that each
entry is a directly measured property of the same physical specimen.

License texts are distributed in `src/ebp/licenses/` and copied into the local
viewer. Keep attribution, source links and change notices when redistributing
data or generated exports. Each record carries its own license identifier.

## LFP expansion in v0.2

| Content | Attribution / source | License |
|---|---|---|
| `a123-amp20-*.csv` and Table 1 evidence / parameters | Jie Lin, Howie N. Chu, David A. Howey, Charles W. Monroe; 2022 paper and Oxford ORA deposit, DOI 10.5287/bodleian:NGQkq49wG | CC BY 4.0 |
| Model radius provenance | University of Oxford and multiscale-coupling developers; pinned `Battery_model.m` | BSD-2-Clause |
| `a123-9ah-*.csv` | Oxford high-power pouch-cell researchers; ORA deposit, DOI 10.5287/ora-eonzaxjpm | CC BY 4.0 |
| BPX LFP example OCP expressions, scalar inputs and generated samples | Copyright (c) 2022 University of Oxford; About:Energy parameterization; pinned FaradayInstitution/BPX example | MIT |
| E-BatP companion logo | Original project identity generated with ImageGen; generation brief in `assets/README.md` | MIT |

The earlier full-cell CSV attribution to Chen applies specifically to `LGM50_cell*`
files, not to the Oxford additions above. Likewise, the PyBaMM parameter license
applies to LG M50 inputs, not every scalar in the expanded catalog.

Oxford changes: selected one AMP20 full-discharge MAT and ten 9 Ah CC MAT members;
retained signed current, voltage and all source time rows; converted temperatures
from Celsius to kelvin; expressed documented 1 Hz sample indices as relative
seconds; left absent ambient temperatures empty. Source NaNs become empty CSV
fields with missing counts. For AMP20, temperature is the arithmetic mean of the
provided thermal grid without an additional ROI. For the 9 Ah data, ambiguity in
the fourth column's sensor/ROI description is retained. Large MAT/ZIP originals
remain external, checksum-pinned downloads. No smoothing or imputation is applied.
The dataset copyright notices are preserved verbatim in
`Oxford-Lin2022-data-notice.txt` and `Oxford-9Ah-data-notice.txt`.

Table 1 changes: transcribed the nine This work rows at three SOCs, converted
units explicitly, and derived three conditional diffusivities from a fitted time
and the source model's assumed radius. The local transcription hash identifies
our evidence JSON, not the publisher HTML. These are effective model parameters,
not new independent measurements.

BPX changes: copied two expressions verbatim, limited them to supplied operating
stoichiometry bounds, and transcribed numeric scalar fields. Estimated thermal
properties and borrowed sources are disclosed. Other functional fields are not
imported. `BPX-MIT.txt` preserves its license; `Oxford-BSD-2-Clause.txt` preserves
the multiscale model license. Related 9 Ah OCP workbooks with unresolved reuse
licensing are linked as external references only. Source authors have not
endorsed this project.

The `upstream-lfp-v0.2.0` source-cache release mirrors four original Oxford files for CI
reproduction because ORA rejects hosted-runner downloads with HTTP 403. The files
are byte-identical, retain CC BY 4.0, and include both original dataset notices.
Release notes preserve authors, primary URLs, DOIs, license and SHA-256 values.
The source-cache release does not change the scientific attribution or license.

## Multi-material expansion in v0.3

The additional NMC111/NMC532/LNMO/silicon/silicon–graphite CSVs are selected
observations from the same SINTEF Zenodo v3 dataset and retain CC BY 4.0 and its
existing attribution. Processing follows the fixed cycle-3 C/50 branch rule,
with source coordinates, duplicate-capacity removal counts and no smoothing.
The two SiGr formulations are retained separately. No new independent study or
commercial-cell association is inferred from adding specimens or materials.

Additional OCP, diffusion and kinetic implementations are from PyBaMM v25.4.2
`Chen2020.py`, `Marquis2019.py`, `Mohtat2020.py` and `NCA_Kim2011.py`, under the
existing PyBaMM BSD-3-Clause notice. Scientific attributions are recorded per
module/function; Dualfoil borrowing is explicit for Marquis electrode functions.
AST-local substitution and constant folding preserve the source math; the gas
constant is fixed for portable evaluation. Source reference parameters used by
Kim kinetics are resolved from that same pinned parameter set. Native measured
points are not claimed for any implementation expression or its generated CSV.

## Matched full-cell expansion in v0.4

`Ecker2015.py` and `Ai2020.py` inputs retain the existing PyBaMM v25.4.2
BSD-3-Clause notice. Ecker scientific attribution is Ecker2015 I/II and
Richardson2020 / Simon O'Kane; Enertech attribution is Ai2020 and Rieger2016.
Borrowed Dualfoil diffusion/kinetics remain labeled for Ai2020. AST substitutions
fix R=8.314462618 J/mol/K and F=96485.33212331001 C/mol.

The six new voltage files, three temperature-rise channels and two published
Enertech OCP tables are redistributed by the PyBaMM team in
https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2 under BSD-3-Clause.
Its separate Copyright (c) 2024, PyBaMM Team notice is preserved verbatim in
`src/ebp/licenses/PyBaMM-data-BSD-3-Clause.txt`. Scientific authors and the
figure-history chain are recorded in `docs/FULL_CELL_MATCHING.md`.

Changes: original time/voltage and temperature-rise files are copied byte-for-byte
to `src/ebp/data/evidence/`. Normalized CSVs retain all numeric source pairs and row order
with one-based source positions; unavailable current and absolute temperatures
stay empty. Temperature rise stays in separate native-clock sidecars, without
interpolation, synchronization or assumed ambient temperature. Ecker points are
upstream figure digitizations, not instrument raw. Enertech tables omit comments
and the explicitly synthetic negative-OCP `(0,3.5)` guard; all other numeric points
and source line references are retained. No smoothing or extrapolation is added.

At v0.4 the Mohtat DOI was indexed as a lead only after automated access failed.
The v0.5 retrieval and attribution below supersede that no-import status.
Source authors have not endorsed this project.

## Official Mohtat2020 deposit in v0.5

Ten original files (five MATs, four MATLAB files and READ_ME.pdf), author-model
OCP expressions and scalar inputs are from Peyman Mohtat, Jason B. Siegel and
Anna G. Stefanopoulou, University of Michigan, dataset DOI 10.7302/wwma-hx25,
related paper DOI 10.1149/1945-7111/aba5d1. They retain CC BY 4.0; original author
copyright/license headers are preserved byte-for-byte in the packaged source
files. Source URLs and SHA-256 values are in scripts/mohtat_assets.json.

Changes: all paired Q_data/Vt_data/Temp_data observations retained; temperature
converted from Celsius to kelvin; one-based source row references added; no
smoothing or resampling. Missing current and time remain empty. Protocol current
and 10-second acquisition metadata are not fabricated measurements. MATLAB scalar
assignments and two OCP expressions were transcribed without execution; source
balancing limits are retained. PyBaMM variants keep their separate BSD license.
The author/PyBaMM crosswalk is original project documentation. Source authors
have not endorsed this project. The v0.4 no-import status is superseded by the
verified v0.5 official retrieval; no third-party paper-download link is included.

## LFP study packages in v0.6

| Content | Attribution / source | License |
|---|---|---|
| Original `isu-uconn-LFP_Data.xlsx`, `isu-uconn-*.csv` electrode/full-cell derivatives | Yifan Zhang, Tingkai Li, Shan Hu, Chao Hu; [ISU-UConn primary deposit](https://digitalcommons.lib.uconn.edu/reil_datasets/6/) and author-hosted workbook at commit `1188c371e5836df4a7e5f5acf336a34ffd4027e6` | CC BY 4.0 |
| ISU author notebook/loader/README referenced as evidence | [REIL-UConn repository](https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics); pinned URLs/hashes, not executed or included as project code | MIT for code; does not replace the workbook's separate CC BY 4.0 terms |
| Original `jahn-*` evidence, model OCPn tables and experimental derivatives | Leonard Jahn; [data v2](https://zenodo.org/records/11958572), [code](https://zenodo.org/records/10852695); associated [Jahn et al. paper](https://doi.org/10.1038/s44172-024-00221-4) | CC BY 4.0 for both deposits, verified in packaged API metadata |

All selected original bytes are retained under checksum pins. ISU pseudo-OCP
changes: select two author-used half-cell pairs, blocks 6/7, stop at the first
capacity maximum, retain the first repeated-capacity observation and normalize
branch throughput. Full-cell changes: select eleven configurations and available
following reverse branches, retain every numeric row in those blocks, and convert
mAh to Ah. One-based Excel addresses are retained. Reference/temperature details
not verified from accessible sources remain explicit gaps.

Jahn changes: copy native modeled OCPn nodes; export nine MAT loop arrays; split
incremental full-cell OCV at the first maximum Q with no row duplication/deletion;
retain original stored charge alongside per-branch passed capacity. Signed
current is retained where supplied. Missing current/time/temperature are never
synthesized. Model OCPn is not raw electrode OCP. No source code is executed and
no prediction accuracy is claimed. See [curation details](docs/LFP_STUDIES.md),
`scripts/lfp_study_assets.json`, `ISU-UConn-data-notice.txt` and
`Jahn2024-data-code-notice.txt`. Source authors have not endorsed E-BatP.

## External dataset links

`src/ebp/data/external_datasets.json` and the generated `data/full-cell/` index
contain authored discovery metadata and source links, not copies of the linked
raw observations. The linked datasets retain their provider licenses. Each
record states the observed terms and evidence; `not-stated` is not permission
to redistribute. The library, viewer and CI do not fetch these external payloads.
Previously packaged source data and supporting evidence retain the notices
listed above. See [the source review](docs/FULL_CELL_DATASETS.md).

## v0.16 scope removal

The ten `a123-9ah-*.csv` observations and their active cell/source records were
removed because no electrode OCP, diffusion or kinetics records were admitted.
The earlier Oxford 9 Ah attribution above and original notice are retained as
historical license documentation, not as a current data-inventory claim.
