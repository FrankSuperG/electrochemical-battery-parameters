# Data contribution templates

Use these files to propose electrochemical parameters and associated full-cell
tests. Partial packages and well-documented source leads are welcome.

## Copy and fill

1. Copy [data-contribution.md](data-contribution.md) into a working directory
   named after the study or cell, and fill the applicable sections in English.
2. Copy only the CSV templates you need. They contain headers only, with no
   example measurements. Add source-faithful observations or parameters; keep
   original files separate and unmodified where reuse allows.
3. Include the completed Markdown file, applicable CSVs, source links, licenses,
   source hashes and any extraction script in an issue or PR. For a private
   submission inquiry, contact [feng.guo@vito.be](mailto:feng.guo@vito.be).

These files organize a submission for review. They are not an automatic import
format, and `ebp validate` does not validate an unimported submission directory.
Maintainers must map accepted information to the catalog schemas and references.
Do not upload data you are not entitled to share. A source lead can remain a link
when redistribution terms or specimen identity are unresolved.

Use UTF-8 and comma-separated CSV. Quote fields that contain commas or line
breaks, including formulas and parameter definitions.

## Available files

| File | Contents / usage |
|---|---|
| [data-contribution.md](data-contribution.md) | Source, licenses, cell identity, component matching, conditions, processing and missing-item checklist |
| [ocp-points.csv](ocp-points.csv) | One electrode branch: `x,potential_V,source_record`. Define `x` and the potential reference in Markdown. Separate lithiation and delithiation branches. |
| [parameters.csv](parameters.csv) | One scalar or expression per row, including units, definition, inputs, conditions, origin and source location |
| [full-cell-time-series.csv](full-cell-time-series.csv) | Measured time-based current/voltage/temperature observations; current is charge positive and temperature is K |
| [full-cell-capacity-series.csv](full-cell-capacity-series.csv) | Native charge-capacity observations when no original time is available; leave time and unmeasured current blank |

## Column conventions

- **OCP:** `x` must be identified as electrode stoichiometry or normalized branch
  capacity with a documented normalization. Whole-cell SOC is not automatically
  electrode stoichiometry. Retain additional original coordinate columns when
  available. Tabulated values from a publication, digitized plots, measured
  points and sampled expressions must be labeled separately.
- **Parameters:** `representation_kind` is `scalar` or `expression`; fill the
  applicable `value` or `expression`. Define variables and their units in
  `independent_variables`, and specify the domain in `validity_domain`. A table
  can be submitted as a separate source-faithful CSV with its definitions in
  Markdown; the current non-OCP importer may need extension to support it.
  `category` should use an existing category from
  [the catalog schema](../src/ebp/data/schema/linked-data.schema.json) where
  applicable. `origin_status` is measured, fitted, derived, borrowed or assumed.
  `cell_soc` is a 0–1 whole-cell SOC only when explicitly known. Reference
  temperatures and measured temperatures must be distinguished in Markdown.
- **Full-cell tests:** current is in A and positive for charge, voltage in V,
  temperature in K and time in s. Document the original sign, units and all
  conversions. `mode` is `C` for charge, `D` for discharge, `R` for rest or `U`
  for unknown; do not infer a mode solely from an undocumented source code.
  Cycle and step identifiers may stay empty.
- **Capacity-only tests:** retain the source's capacity definition and origin.
  Use the supplied column only for a documented charge-capacity axis; for
  discharge or another coordinate, retain its own clearly named column and
  explain it. Do not manufacture measured time as `Q/I` or row index times a
  reported sampling interval. A nominal C-rate is protocol metadata, not a
  measured current channel.
- **Missing data:** blank numeric cells mean unavailable. Never fill them with
  zero, an assumed room temperature or an invented timestamp. Record gaps and
  source conflicts in Markdown. Keep the complete source row sequence.
- **Traceability:** define `source_record` indexing and link it to an original
  filename, archive member, sheet, cycle and branch as applicable. Retain separate
  timebases for independently recorded channels; do not merge arrays by row
  number unless their pairing is established.

For an unmodified original file, a SHA-256 can be obtained with:

```bash
shasum -a 256 path/to/original-file
```

Hash originals and normalized files separately and identify which bytes each
digest covers. See [CONTRIBUTING.md](../CONTRIBUTING.md) for import and review steps.

For a real example of source review, parameter variants and explicit test-data
gaps, see the [Mohtat2020 audit](../docs/MOHTAT2020.md).
