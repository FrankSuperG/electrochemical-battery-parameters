# Curation and evidence decisions

All source assets are pinned by URL/version and SHA-256. Reconstruct the complete catalog with `python scripts/seed_v01.py --download`. This runs the base extraction, LG M50 importer and LFP expansion. Cached originals are excluded from Git. Four openly licensed Oxford inputs also have byte-identical, attributed copies in the private `upstream-lfp-v0.2.0` source-cache release because ORA returns HTTP 403 to hosted CI runners. CI verifies those copies using the same primary-source SHA-256 values; mirror URLs are explicit in asset metadata. Published facts, implementation values and generated observations retain distinct provenance.

## SINTEF half-cell branches

Zenodo record 20086298 v3 supplies CC BY 4.0 measurements and electrode metadata. Four p-OCV Parquet files cover two LFP and two graphite specimens. The importer selects cycle 3 and its two constant-current branches, excludes rest, and retains the first occurrence of repeated capacity coordinates. It creates a branch-relative throughput coordinate without claiming absolute stoichiometry. Source row positions, voltages, current, time and capacity are retained; no voltage smoothing is applied.

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

The ISU–UConn LFP/graphite deposit was discovered previously, but its workbook/README endpoints returned HTTP 403. Unread files were not turned into records. LiionDB remains a discovery route rather than an imported source. Follow-up work should favor same-model LFP half-cell OCP, diffusion/kinetic experiments and reusable full-cell tests, recording licensing and exact identity before joining them.

Automated checks establish source-value fidelity, checksums, reference integrity, scoped downloads and adapter behavior. They do not replace electrochemical review or an independent prediction experiment.
