# Data model

The authoritative catalog is `src/ebp/data/`, distributed inside the Python package. JSON references and checksums are validated by `ebp validate`. A stored record is not necessarily an independent experiment or directly measured material property.

## Entities

| Entity | File | Meaning |
|---|---|---|
| OCP record | `catalog.json` | One electrode curve or expression, with coordinate, domain, conditions, representation, provenance and limitations |
| Model parameter | `parameters.json` | One scalar, function or native one-dimensional table, its unit, definition, origin and conditions |
| Cell / family | `cells.json` | Identity evidence, model context, linked record IDs, coverage and gaps |
| Experiment | `experiments.json` | Half-cell specimen, protocol, cycle/branch selection and extraction rule |
| Full-cell test | `full_cell_tests.json` | One source file/member, normalized rows, test protocol and relationship to parameters |
| Source | `sources.json` | A paper, data deposit or software distribution with its particular role |
| Asset | `assets.json` | A versioned source URL and SHA-256; optional packaged evidence path |
| Material | `materials.json` | Electrode composition and supplier information without inventing a commercial full-cell identity |
| Matching audit | `matching_audit.json` | Component matches, missing items, unmatched records and unimported leads |

## Coordinates and representations

- `stoichiometry`: electrode lithium fraction θ. BPX bounds are the exact example's operating minimum/maximum; the older PyBaMM formulas retain their mathematical 0..1 domain without claiming independently verified fit validity.
- `normalized_branch_capacity`: cumulative charge throughput over the selected branch, normalized to 0..1. It follows test progress and does not establish absolute lithium fraction or whole-cell SOC.
- `model_soc`: author model SOC/DOL coordinate. The Jahn2024 single-string PD-ECM coordinate is not verified absolute stoichiometry and is kept separate from measured branch throughput.
- `source_reported_stoichiometry`: source-labeled electrode coordinate whose absolute calibration is not independently established. MJ1 retains this separately from branch progress and verified lithium fraction; PyBaMM adaptation requires an explicit mapping.
- Table CSVs retain potential, capacity, current, time and upstream row coordinates. Linear interpolation is default; PCHIP is optional. Formula CSVs are generated samples and remain labeled as such.
- Unknown numeric temperatures are `null`. A model reference temperature is distinguished from a verified measurement temperature.

Parameters use `representation.kind=scalar` or a restricted expression with named inputs. Kinetic expressions use `c_e`, `c_s_surf`, `c_s_max`, `T`; particle-diffusivity expressions use `sto`, `T`. Both retain source conventions and reject non-finite inputs; diffusivity requires 0≤sto≤1 and T>0. Numerical domains do not establish experimental validity. `conditions` records cell SOC and derivation assumptions where known. `definition` preserves distinctions such as volumetric versus surface kinetics, effective versus intrinsic transport, and heat-transfer velocity versus a heat-transfer coefficient.

## Matching levels

| Level | Required evidence / interpretation |
|---|---|
| `material_only` | Material/electrode identity; no commercial cell link |
| `unmatched` | A parameter example exists, but commercial model and raw-test match are unresolved |
| `same_study_cell_family` | Explicit study/electrode/configuration family association; commercial part may be unresolved or inapplicable to laboratory cells |
| `parameter_set_only` | Parameters and OCP share a named implementation; no matched raw test or same-specimen measurement claim |
| `same_model_same_study` | Exact model named in the paper and linked experiment deposit; does not imply identical specimen |

OCP `cell_link.relationship=same_parameter_set` means the curve is part of the same source model (for example BPX or Jahn2024). It does not by itself establish a commercial-model identity. `same_study_cell_family` is also available for electrode curves associated with laboratory full-cell configurations. Read the cell's `identity_level` and `match_level` together. No record currently establishes an identical characterization/validation specimen or independent validation by this project.

## Normalized full-cell observations

Standard columns are `time_s`, `current_charge_positive_A`, `voltage_V`, `cell_temperature_K`, `ambient_temperature_K`, `cycle`, `step` and `mode`. Original Maccor row/record references remain in LG files. Oxford files use zero-based `source_record` and `original_member` for ZIP provenance. A synthetic cycle=0/step=1 groups each Oxford trace; it does not assert an instrument-recorded cycle or step.

Current is charge positive. LG originals contain magnitude + mode, so normalization explicitly applies the sign. Oxford signed current is retained and checked against the source protocol. Source NaNs become empty fields; mode `U` denotes unknown current. No rows are discarded and no values are imputed. `missing_values` records counts. Ambient temperature stays empty when absent. One-second Oxford relative time follows the deposited documentation; no absolute timestamp is inferred.

For external MAT/ZIP originals, `path=null`; `asset_id` identifies the source download and checksum. `normalized_path` identifies the packaged CSV and `normalized_sha256` verifies it. For packaged Maccor originals, `path` and the asset checksum verify the original bytes as well. A local curated evidence asset's `digest_scope` explicitly names the transcription; its hash does not claim to hash publisher HTML.

Cell package downloads are scoped by `cell_id`. They contain that cell's OCP metadata, parameters and test links, their source records and relevant assets. Empty packages expose gaps rather than silently substituting another model's data.

In v0.4, `basic_test` distinguishes CC discharge, CC charge and CCCV-charge/CC-discharge protocols. `channel_availability` counts observed rows. `observation_kind` distinguishes instrument series, published experimental series with unresolved raw status, and figure digitizations. `missing_items` appears at test, cell and component level. `borrowed_model_input` and `missing` are component evidence statuses, not commercial identity levels.

For time/voltage-only files, `path=null` selects the normalized reader; `original_download_path` identifies a byte-identical packaged CSV/TXT verified by its asset hash. Blank current is unavailable, not zero. C-rate never populates a measured-current column. Source-row references are one-based and documented. Temperature-rise `sidecars` retain separate timebases, row counts, hashes and source assets; they never populate `cell_temperature_K` or increase the test-file count.

`literature_table` distinguishes published OCP tables from C/50 measured branches. Coordinates/domains follow supplied stoichiometry; the explicitly synthetic graphite guard is omitted. Instrument protocol and numerical measurement temperature remain unknown. NCO follows the upstream label without an inferred composition ratio. Ecker commercial and implementation capacities remain separate fields requiring scaling review.

## Material families and cell joins

The v0.3 families are LFP, graphite, NMC111, NMC532, NMC811, LNMO, silicon, silicon-graphite, LCO and NCA. Positive/negative electrode roles are explicit per record; material names alone do not determine the role. Different SiGr formulations retain separate material IDs and source labels.

A shared family such as NMC532 does not join a SINTEF half-cell to the Mohtat pouch model. Marquis2019 OCPs use `relationship=surrogate` because their function origin is borrowed Dualfoil data. The named Kokam model remains the implementation's model association, not proof of same-cell characterization. NCA is a nominal design with no commercial model assigned. The NCA source's positive-OCP docstring says Graphite; classification follows the positive dictionary entry and NCA set context, with that source issue retained in limitations.

## Capacity-coordinate exports and variants in v0.5

`independent_variable.column=charge_capacity_Ah` selects native capacity for the
Mohtat charge exports. `time_s` stays empty and is never reconstructed from Q/I or
a reported sampling interval. Measured V/T retain paired source rows. Nominal
charge-current magnitudes are protocol metadata only. Parameter conditions use
`parameterization_variant` to separate author MPM inputs from the pinned PyBaMM
implementation; same-study association does not mean identical coefficients.
Offline cell ZIPs include scoped data, available source bytes, metadata and notices.

## Electrode-model and laboratory branches in v0.6

`measurement=model_ocp` explicitly identifies the parameterized Jahn2024 PD-ECM
single-string OCPn tables. They are tabulated model inputs, not instrument OCP
or raw GITT. `x.kind=model_soc` preserves their author coordinate; an explicit
`StoichiometryMapping` is required for PyBaMM adaptation and its metadata retains
the model label. Original node values are unchanged; bounded catalog interpolation
does not reproduce the entire source model's spline/extrapolation/balancing.

`reference=unresolved` is used for the ISU half-cell records because accessible
workbook/notebook evidence does not verify reference construction. Their voltage
is not automatically labeled versus Li/Li+. The adapter rejects such records
until reference evidence is curated, even if mapping endpoints are supplied.
Plots separate reference and model-coordinate groups.

`independent_variable.column=passed_capacity_Ah` covers source branch capacity
in the ISU workbook and the explicit Q-Q_start / Q_start-Q transformation for
Jahn incremental whole-cell OCV. Original Q remains in a separate source column.
Time/current stay blank where missing. Repeated full-cell branch capacities and
constant-capacity tails are retained; half-cell interpolation tables use the
documented first-occurrence/cutoff rule. Full-cell exports may be individual
branches or MAT arrays, so file counts are not specimen counts.

`basic_test.type` additionally supports constant-current full cycles, current
steps, partial cycles and incremental whole-cell OCV. The latter is not a
continuous CC time series or electrode OCP. `source_record` is one-based Excel
row for ISU and zero-based CSV/array sample for Jahn; exact source locations and
original bytes are provided. Blank cycle IDs do not invent instrument cycles.
See [LFP study selections and missing items](LFP_STUDIES.md).

## Native non-OCP parameter tables in v0.8

`representation.kind=table` references a checksum-pinned CSV in
`parameter_tables/`. Its x descriptor records the column, required API variable,
unit, source coordinate meaning and native domain; `y_column` selects the value.
Extra columns preserve source row indices or original error bounds.
`Parameter.points()` returns all stored x/y nodes; `p(source_soc_percent=50)`
or `p(source_sto=0.5)` must use the record's exact variable. Arithmetic linear
interpolation is bounded by native endpoints and rejects non-finite inputs.
Neither error bounds nor missing endpoints are interpolated into new evidence.

Parameter summary CSVs use `table:parameter_tables/<id>.csv` in
`value_or_expression`; it is a catalog-relative file reference, not a formula.
Per-cell pages link the native CSVs directly, and offline bundles include them.
Source SOC percent and model-aligned electrode coordinates are not automatically
full-cell SOC or absolute lithium fraction. Changing a coordinate requires
external balancing evidence, not a simple name substitution.

For mapped OCPs, `StoichiometryMapping.theta_start/theta_end` are the lithium
fractions at the **low/high native coordinate endpoints**. The adapter uses
`theta = theta_start + (x-lo)/(hi-lo)*(theta_end-theta_start)` and records
`mapping_source_domain`. This matters for source axes such as MJ1 NMC 0.21..1;
a missing part of the native domain is not implicitly treated as observed.

## External full-cell datasets

`external_datasets.json` is an authored metadata-only registry governed by
`schema/external-datasets.schema.json`. Its records are dataset links, not
imported test files, independent specimens or fitted model inputs. Each record
retains source version/DOI, material families, cell identity, test/profile tags,
reported conditions, channel-review scope, reuse terms and missing items.
`parameter_link` holds explicit catalog cell IDs, evidence and match level. An
`unmatched` record has no cell join; a chemistry category alone cannot add one.

`Catalog.search_datasets()` and `ebp datasets` inspect this metadata offline.
`full_cell_tests.json`, `linked_tests()` and `full_cell_data()` retain their
packaged-observation meaning. No library, viewer, seed or CI step fetches
external-link payloads. Existing source reconstruction downloads remain separate.
The material index derives packaged-test families from the source chemistry
labels; NCO is preserved separately from NMC/NCA. A multi-material external
dataset can appear in multiple groups but remains one registry record.

Read [the full-cell link review](FULL_CELL_DATASETS.md) before using a linked
file. A source temperature setpoint is not a measured trace; a whole-cell OCV
curve is not electrode OCP; EIS belongs to the frequency domain.

External registry schema 1.1 adds source paths, inspection scope, per-component
record joins and requested-test coverage. File/container locators are keyed by
dataset ID plus complete source path. Archive members require matching persisted
directory evidence and sizes. `search_dataset_files()` filters file tags without
inheriting dataset declarations. `evidence/external-archive-directory-review.json`
contains directory metadata only, not extracted observations. Whole-schema JSON
exports preserve the authoritative registry version and description.
