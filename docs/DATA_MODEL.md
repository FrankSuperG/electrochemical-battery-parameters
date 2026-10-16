# Data model

The authoritative catalog is `src/ebp/data/`, distributed inside the Python package. JSON references and checksums are validated by `ebp validate`. A stored record is not necessarily an independent experiment or directly measured material property.

## Entities

| Entity | File | Meaning |
|---|---|---|
| OCP record | `catalog.json` | One electrode curve or expression, with coordinate, domain, conditions, representation, provenance and limitations |
| Model parameter | `parameters.json` | One scalar or multivariable function, its unit, definition, model-specific origin and conditions |
| Cell / family | `cells.json` | Identity evidence, model context, linked record IDs, coverage and gaps |
| Experiment | `experiments.json` | Half-cell specimen, protocol, cycle/branch selection and extraction rule |
| Full-cell test | `full_cell_tests.json` | One source file/member, normalized rows, test protocol and relationship to parameters |
| Source | `sources.json` | A paper, data deposit or software distribution with its particular role |
| Asset | `assets.json` | A versioned source URL and SHA-256; optional packaged evidence path |
| Material | `materials.json` | Electrode composition and supplier information without inventing a commercial full-cell identity |

## Coordinates and representations

- `stoichiometry`: electrode lithium fraction θ. BPX bounds are the exact example's operating minimum/maximum; the older PyBaMM formulas retain their mathematical 0..1 domain without claiming independently verified fit validity.
- `normalized_branch_capacity`: cumulative charge throughput over the selected branch, normalized to 0..1. It follows test progress and does not establish absolute lithium fraction or whole-cell SOC.
- Table CSVs retain potential, capacity, current, time and upstream row coordinates. Linear interpolation is default; PCHIP is optional. Formula CSVs are generated samples and remain labeled as such.
- Unknown numeric temperatures are `null`. A model reference temperature is distinguished from a verified measurement temperature.

Parameters use `representation.kind=scalar` or a restricted expression with named inputs. `conditions` records cell SOC and derivation assumptions where known. `definition` preserves distinctions such as volumetric versus surface kinetics, effective versus intrinsic transport, and heat-transfer velocity versus a heat-transfer coefficient.

## Matching levels

| Level | Required evidence / interpretation |
|---|---|
| `material_only` | Material/electrode identity; no commercial cell link |
| `unmatched` | A parameter example exists, but commercial model and raw-test match are unresolved |
| `same_study_cell_family` | Explicit study association and manufacturer/capacity/format; part number unresolved |
| `same_model_same_study` | Exact model named in the paper and linked experiment deposit; does not imply identical specimen |

OCP `cell_link.relationship=same_parameter_set` means a fit is stored in the same BPX example. It does not establish a commercial-model identity. Read the cell's `identity_level` and `match_level` together. No record currently establishes an identical characterization/validation specimen or independent validation by this project.

## Normalized full-cell observations

Standard columns are `time_s`, `current_charge_positive_A`, `voltage_V`, `cell_temperature_K`, `ambient_temperature_K`, `cycle`, `step` and `mode`. Original Maccor row/record references remain in LG files. Oxford files use zero-based `source_record` and `original_member` for ZIP provenance. A synthetic cycle=0/step=1 groups each Oxford trace; it does not assert an instrument-recorded cycle or step.

Current is charge positive. LG originals contain magnitude + mode, so normalization explicitly applies the sign. Oxford signed current is retained and checked against the source protocol. Source NaNs become empty fields; mode `U` denotes unknown current. No rows are discarded and no values are imputed. `missing_values` records counts. Ambient temperature stays empty when absent. One-second Oxford relative time follows the deposited documentation; no absolute timestamp is inferred.

For external MAT/ZIP originals, `path=null`; `asset_id` identifies the source download and checksum. `normalized_path` identifies the packaged CSV and `normalized_sha256` verifies it. For packaged Maccor originals, `path` and the asset checksum verify the original bytes as well. A local curated evidence asset's `digest_scope` explicitly names the transcription; its hash does not claim to hash publisher HTML.

Cell package downloads are scoped by `cell_id`. They contain that cell's OCP metadata, parameters and test links, their source records and relevant assets. Empty packages expose gaps rather than silently substituting another model's data.
