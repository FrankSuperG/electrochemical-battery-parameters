# Contributing to E-BatP

Contributions are welcome: electrode OCP, diffusion, reaction kinetics, geometry,
transport, thermal properties and the full-cell experiments that help interpret
them. A useful contribution can be one well-documented curve or a source lead;
it does not need to be a complete model parameter set.

Open an issue or pull request when repository access permits. If access is
restricted, invited collaborators can use those routes and other researchers
can email [Feng Guo](mailto:feng.guo@vito.be) with a source link or contribution
inquiry. The same templates support either workflow.

## Choose a contribution route

| What you have | Where to start |
|---|---|
| A paper, dataset or author repository worth investigating | [Source suggestion issue](.github/ISSUE_TEMPLATE/source-suggestion.md); a link and a short explanation are enough |
| New measurements, published parameter values or linked full-cell tests | [Data contribution issue](.github/ISSUE_TEMPLATE/data-contribution.md) and the [submission template](templates/data-contribution.md) |
| Files and a reproducible importer ready for review | Submit a pull request using the [PR template](.github/pull_request_template.md) |
| Corrections to units, provenance, identity or matching | Open an issue or PR naming the affected record IDs and supporting evidence |
| Collaboration, unpublished data or access questions | Email [feng.guo@vito.be](mailto:feng.guo@vito.be) before sending data that cannot be shared |

See [templates/README.md](templates/README.md) for a copy-and-fill workflow and
CSV headers. The submission templates are staging aids, not catalog records and
not an automatic import format. Maintainers review and map them to the catalog.

## Minimum information for a data addition

1. **Source and reuse:** paper/dataset DOI or original URL, version or commit,
   exact table/figure/file/function location, reuse license and attribution.
   A public download alone does not establish permission to redistribute it.
   An unknown license is acceptable for a source lead; keep its files external
   until reuse terms are resolved.
2. **Identity and matching:** material, electrode role, study, manufacturer,
   commercial model and specimen where disclosed. State which parameters and
   tests belong together and why. Use a [defined match level](docs/DATA_MODEL.md#matching-levels)
   for each component; do not join by chemistry or nominal capacity alone.
3. **Conditions and definitions:** protocol, reference electrode, direction,
   temperature, SOC/stoichiometry, units, independent variables and validity
   domain. For kinetics, retain the full equation and area/concentration
   convention. Distinguish intrinsic, effective and grouped parameters.
4. **Originals and processing:** source hashes, original file/member and row
   references, every conversion or extraction step and a reproducible script
   when processing is needed. Keep unmodified source bytes where reuse permits.
5. **Evidence and gaps:** measured, fitted, derived, borrowed or assumed origin;
   missing channels and identity information; source conflicts; and whether any
   trace informed fitting. A parameter source's validation claim is distinct
   from an independent validation performed by this project.

Use `unknown` or `not reported` in the Markdown submission when information is
missing. In CSVs, leave unavailable measurements empty; zero is a measured value.
Treat original instrument points, digitized plots and formula samples as distinct
representations. Do not count multiple branches or representations as independent
studies. Keep source NaNs and gaps visible rather than silently imputing or
deleting them. Preserve per-source attribution and notices.

## For pull requests that import records

The authoritative data live in `src/ebp/data/`. Follow the existing files rather
than placing a submission CSV directly into the catalog:

- Add source and asset metadata with stable versions, checksums and notices.
- Add or reuse material, experiment and cell identities with supporting evidence.
- Add OCP to `catalog.json`, other inputs to `parameters.json`, and experiments
  to `full_cell_tests.json`, with their referenced files.
- Update cell coverage and `matching_audit.json`, including unresolved gaps.
- Run `python scripts/build_data_index.py` to refresh GitHub CSV/JSON exports,
  per-cell pages and README links. Include the generated `data/` changes in the
  PR; CI checks that navigation and exports match the authoritative catalog.
- Add extraction logic under `scripts/` and integrate it into reconstruction
  when generated catalog data are introduced. Never execute downloaded source
  code merely to extract its values.
- Keep changes scoped; explain affected record versions, hashes and
  interpretation. Update coverage documentation when the catalog changes.

Read the [data definitions](docs/DATA_MODEL.md),
[curation decisions](docs/CURATION.md) and
[source licenses](DATA_LICENSES.md). Structural definitions are in
`src/ebp/data/schema/catalog.schema.json` and `linked-data.schema.json`.
Automated extraction does not replace source review.

## Verification

For imported data or code changes, run:

```bash
ebp validate
PYBAMM_DISABLE_TELEMETRY=true python -m pytest -q
ebp build-site
```

When extraction changes, also reconstruct the catalog from pinned sources and
check that the generated files are identical to those included in the PR:

```bash
python scripts/seed_v01.py --download
git diff --exit-code -- src/ebp/data
```

Stage the intended generated data before this comparison so that the diff checks
reconstruction against your proposed records. Avoid unrelated staged changes.
Source downloads may need network access. Report checks not run and why. A
source-only issue or a documentation-only contribution does not require model
simulation or a full data reconstruction.
