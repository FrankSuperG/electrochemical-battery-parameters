# Curation and evidence decisions

All source assets are pinned by URL/version and SHA-256. Reconstruct the complete catalog with `python scripts/seed_v01.py --download`. This runs the base extraction, LG M50 importer, LFP expansion and multi-material extension. Cached originals are excluded from Git. Four openly licensed Oxford inputs also have byte-identical, attributed copies in the `upstream-lfp-v0.2.0` source-cache release because ORA returns HTTP 403 to hosted CI runners. CI verifies those copies using the same primary-source SHA-256 values; mirror URLs are explicit in asset metadata. Published facts, implementation values and generated observations retain distinct provenance.

## SINTEF half-cell branches

Zenodo record 20086298 v3 supplies CC BY 4.0 measurements and electrode metadata. Sixteen p-OCV Parquet files cover two LFP, two graphite, two NMC111, two NMC532, two NMP-processed LNMO, two silicon and four silicon–graphite specimens. The SiGr specimens cover two source formulations (SiGr-AQ-1 and SiGr-AQ-2). The importer selects cycle 3 and its two constant-current branches, excludes rest, and retains the first occurrence of repeated capacity coordinates. It creates a branch-relative throughput coordinate without claiming absolute stoichiometry. Source row positions, voltages, current, time and capacity are retained; no voltage smoothing is applied.

Room temperature is recorded without inventing a numeric value. Commercial electrode suppliers do not establish commercial full-cell models. The two specimens support inspection of repeatability, not an inferred population distribution. Other protocols in the upstream deposit, including GITT, have not been imported.

## PyBaMM formulas and LG M50

Fixed PyBaMM v25.4.2 `Prada2013.py` explicitly borrows `LFP_ocp_Afshar2017` and `graphite_LGM50_ocp_Chen2020`. Scientific attribution is per function. Transcription changes variable naming and NumPy prefixes while preserving coefficients. These implementations are compared numerically to the pinned code; the original papers' fit points and equations have not been independently audited.

The fixed `Chen2020.py` contributes 36 numeric scalars and two exchange-current functions. The dictionary is inspected with AST rather than executed by the importer. Values are labeled upstream implementation inputs; individual measurement/fit/borrowing origins remain unaudited. SEI examples and borrowed Nyman electrolyte functions are excluded. The gas constant used for kinetics is explicitly 8.314462618 J/(mol·K).

Zenodo 4032561 v1 provides the three LG M50 validation CSVs under CC BY 4.0. Originals are byte-preserved. Normalization skips 13 instrument-banner lines, interprets magnitude current using `Md=C/D`, converts Celsius to K, and retains source coordinates. Duplicate timestamps remain. The viewer selects steps 7/12/17/22, excluding initial preconditioning step 2, and decimates only for display. The paper and deposit establish same model / same study, not same specimen.

## A123 AMP20M1HD-A: fitted parameters and full discharge

[Lin et al. (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/) explicitly names the A123 AMP20M1HD-A 20 Ah LFP/graphite pouch cell. Its [ORA deposit](https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513) and source notice permit reuse under CC BY 4.0. The selected full-discharge MAT contains synchronized voltage, signed current and a calibrated thermal grid on a documented 1 Hz timebase. Relative time starts at zero. The normalized temperature is the arithmetic mean of the entire supplied grid, with no additional ROI mask. It is not labeled as a thermocouple or separate ambient trace.

The importer transcribes the nine rows in Table 1's **This work** columns at 30/50/70% initial SOC into 27 records. Units are converted explicitly, including A/cm³ → A/m³, kJ/mol → J/mol and µm/s → m/s. The local JSON transcription, location and SHA-256 are separate evidence. The model's effective conductivity scaling and kinetics definitions remain attached. Table 1 results correspond to one cell; its letter is not established here, so matching to deposited Cell I stops at same-model/same-study.

Three derived diffusivities use the fitted shared time and the pinned implementation's assumed radius: `D = (5e-6 m)^2 / t_d`. They are conditional effective values shared by both electrodes, not three new measurements or independently identified intrinsic LFP coefficients. Radius and diffusivity are not independently identifiable from that time alone. `Main_Opt.m` starting guesses are deliberately excluded.

C/25 full-cell pseudo-OCV is described in Methods, but measured electrode OCP points were not located in the selected deposit. The model convention assigns full-cell OCV to one electrode and zero to the other; that does not turn full-cell observations into measured half-cell OCPs. Local OCV gradients in Table 1 are scalar slopes, not a complete curve. The full-discharge experiment requires SOC-dependent OCV/entropy inputs beyond those local fits; this release does not reproduce the paper's model validation.

## A123 high-power 9 Ah study family

[Kumtepeli et al. (2026)](https://doi.org/10.1016/j.jpowsour.2025.238764) identifies a 9 Ah A123 LFP/graphite power pouch. The [linked ORA archive](https://ora.ox.ac.uk/objects/uuid:fe9bad3e-8a72-4e3b-8f01-fec3324b6758) provides ten CC charge/discharge MAT files at 2/4/6/8/10C under CC BY 4.0. Exact part number and per-file cell serial are unresolved: match level is same-study cell family. It is a different entry from AMP20 and the BPX example.

`Expivium` supplies sample index, voltage, signed current and reported temperature. Time is the index minus its first value on the documented 1 Hz timebase. Current sign is checked against charge/discharge protocol. The fourth column is called reference temperature in the archived README and mean temperature in the related code README. Its exact sensor/ROI identity remains unresolved. Source NaNs, including trailing voltage/current gaps in two discharge files, become empty fields; every row is retained and missing values are counted. Browser previews use only valid voltage points; CSVs preserve missing rows.

This model assumes fast diffusion; no finite fitted diffusivity is invented. The code's pseudo-OCV workbooks are indexed at a pinned commit but not redistributed because an explicit reuse license was not located. Electrode potentials allocated conventionally from full-cell pseudo-OCV are not electrode-resolved measurements. Kinetic fits are not transcribed in this release.

## Official BPX LFP 18650 example

The [pinned BPX file](https://github.com/FaradayInstitution/BPX/blob/0f591336937c2c57509f20ab23f9908e58f7a757/examples/lfp_18650_cell_BPX.json) is MIT licensed. Its header describes an About:Energy December 2022 parameterization based on cycling and electrode teardown. It identifies chemistry, format and 2 Ah capacity but no commercial part number or matching raw test files. Match status is explicitly unmatched.

Two OCP expressions are transcribed verbatim and evaluated only inside the file's supplied operating stoichiometry limits. The positive expression has a large exponential coefficient; extrapolating it to θ=0 would be misleading. Forty-six numeric fields are imported with their BPX units and reference-temperature context. Rate constants in mol/(m²·s) keep the BPX definition and are not relabeled as exchange-current density. Thermal properties described as estimated remain marked. The header's borrowed electrolyte and entropy attributions are retained; non-OCP expressions and the entropy table are not yet imported. No complete BPX round-trip or full-cell prediction is claimed.

## Deferred sources and validation

The ISU–UConn LFP/graphite deposit's earlier workbook/README requests returned HTTP 403. On 2026-10-16, a pinned author GitHub copy was retrieved and inspected. The subsequent v0.6 import includes a documented subset of that workbook; see [LFP study selections](LFP_STUDIES.md). The earlier candidate status is superseded, while reference details and specimen-matching limits remain explicit. See [DATA_CANDIDATES.md](DATA_CANDIDATES.md). LiionDB remains a discovery route rather than an imported source. Follow-up work should favor same-model LFP half-cell OCP, diffusion/kinetic experiments and reusable full-cell tests, recording licensing and exact identity before joining them.

Automated checks establish source-value fidelity, checksums, reference integrity, scoped downloads and adapter behavior. They do not replace electrochemical review or an independent prediction experiment.

## Multi-material model inputs in v0.3

The fixed PyBaMM v25.4.2 Chen2020 positive OCP completes the existing LG M50 electrode pair. Its source names the same commercial model and study as the existing tests, without establishing identical specimens.

The pinned Marquis2019, Mohtat2020 and NCA_Kim2011 files each contribute two OCPs, 34 selected scalars, two particle-diffusivity functions and two exchange-current laws. The importer parses dictionaries and simple mathematical statements with an AST allowlist; it never executes upstream Python. Local variables are substituted, the gas constant is fixed at 8.314462618 J/(mol·K), and source coefficients are retained. Tests independently compare against the pinned functions at off-grid stoichiometries and three temperatures. Kim's kinetic reference electrolyte concentration is resolved from that same parameter dictionary and disclosed in conditions. Its positive OCP uses a fractional power of 136.4; the interpreter permits bounded constant powers up to 256, while rejecting variable or unbounded powers.

Marquis2019 names a Kokam SLPB78205130H configuration but attributes electrode OCP, diffusion and kinetics to Dualfoil. These are borrowed implementation functions, not direct measurements on that commercial specimen. Mohtat2020 identifies a graphite/NMC532 pouch configuration; the v0.3 discovery endpoint returned HTTP 403 and that release contained no imported experiments. The v0.5 retrieval below supersedes that historical status: original author files and five charge-capacity/voltage/temperature series are now included, with current/time and commercial identity still unresolved. Kim2011 is explicitly a nominal NCA/graphite design; thermal properties include borrowed and scaled Marquis inputs. The source positive OCP docstring's Graphite label is retained as a source issue; the dictionary association and set context identify NCA.

All new parameter packages retain raw-test coverage gaps. NMC532 chemistry alone does not associate the Mohtat model with SINTEF half-cells. LNMO is a distinct material from LMO. No LMO or LTO curve is fabricated to complete a list of chemistries; these remain discovery priorities. The new source files and checksums are pinned in `scripts/material_assets.json`.

## Full-cell association audit in v0.4

`scripts/seed_fullcell.py` adds two identified implementation contexts and six
voltage series from pinned PyBaMM data v1.0.2. Same-model joins require explicit
model/study evidence; Enertech remains a study-family join with an unresolved
part number. Same-material SINTEF electrodes remain unassigned. Ecker figures
and published Enertech tables have distinct observation types from instrument
records. C-rate metadata never manufactures a measured-current trace.

Ecker commercial 7.5 Ah and implementation 0.15625 Ah capacities are both kept.
Borrowed Ecker thermal properties and Enertech Dualfoil D/kinetics remain visible.
AST transcriptions resolve only numeric constants, including Faraday's constant;
no upstream Python is executed by the importer. Original source files and native
numeric rows are checked independently in tests. Temperature-rise sidecars retain
separate clocks without resampling or assumed ambient temperature.

At v0.4, the Mohtat same-paper DOI was a metadata lead because HTTP 403 prevented
file inspection. That status is historical and superseded by the v0.5 import
below. The component evidence matrix records current missing items and source IDs.
Full decisions and citations are in
[FULL_CELL_MATCHING.md](FULL_CELL_MATCHING.md).

## Mohtat retrieval correction in v0.5

Normal-browser access succeeded on 2026-10-16 and retrieved the original author
bundle. Earlier 403 observations apply to automated access, not dataset availability.
The v0.5 importer uses committed, hash-pinned originals and requires no repeated
browser download in CI. Five capacity-coordinate charging series and 33 author
scalar inputs were curated without executing MATLAB. See [MOHTAT2020.md](MOHTAT2020.md)
for missing current/time/discharge channels, a source rate conflict and the
non-identical PyBaMM graphite OCP. The NMC532 label remains implementation-attributed.

## MJ1 native tables in v0.8

The MJ1 source/workbook comparison, missing-value corrections, model alternatives
and intact-cell coverage gap are documented in [LG_MJ1.md](LG_MJ1.md). Original
files retain CC BY 4.0. The new parameter-table representation retains source
coordinates and error bounds, evaluates only within its native domain and does
not infer kinetics concentration laws or absolute electrode balancing.
