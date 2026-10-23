# Public-release readiness review - v0.8.0

Reviewed 2026-10-17. **Suitable for publication as a traceable, partial parameter
and observation catalog**, with the source, coordinate, variant and missing-item
labels retained. This review does not change repository visibility. It does not
certify complete interchangeable parameter sets or new predictive model accuracy.

Scope at that review: **59 electrode curves, 397 other parameter records, 61 full-cell
exports, 13 material labels and 13 cell/study entries**. File, branch and parameter
counts are not independent-cell or independent-study counts. MJ1 adds no intact
full-cell test; existing test counts are unchanged.

For the current v0.14 inventory (83 curves/fits, 1,041 other parameters and
19 cell/study entries), see the [extraction and storage review](PARAMETER_STORAGE.md)
and [current battery-model index](../data/batteries/README.md). This dated v0.8
review is retained as history; current source-level gaps remain authoritative.

## Findings resolved in this revision

| Finding | Resolution and evidence |
|---|---|
| MJ1 processed tables turn missing workbook endpoints into zero. | Eight laboratory tables use numeric original workbook cells; missing row addresses and exact unit multipliers are retained. Original processed files remain evidence. [MJ1 review](LG_MJ1.md). |
| Model-derived diffusion differs by formulation and direction. | Twelve SPM/SPMe/DFN tables stay separate, with source coordinates and error bounds. No cross-model average or automatic parameter-set assembly. |
| MJ1 GITT is a harvested/reassembled three-electrode experiment. | Its working-versus-Li voltage is excluded from intact-cell test counts; intact CC and t/I/V/T matching remain missing. Replacement/original separators are distinguished. |
| Several MJ1 source fields disagree or have ambiguous units. | Generic NMC label; source-version differences disclosed; implausible nominal-voltage units, concentration units and initial/stoichiometric state fields excluded. |
| Full MJ1 workbook also includes third-party silicon literature curves. | Original XLSX stays external. Only a hash-pinned laboratory-cell selection is packaged, excluding the entire OCV sheet; no grant is inferred for literature columns. |
| Article and dataset licenses differ. | Dataset CC BY 4.0 retained with frozen metadata and notices; article CC BY 3.0 recorded separately. Article text/images are not redistributed as data. |
| Source electrode axes may start above zero. | OCP adaptation maps the native low/high coordinate endpoints explicitly and retains that domain in metadata; actual PyBaMM checks cover the MJ1 NMC 0.21..1 case. |
| Non-OCP tables previously had no native representation. | Added source-axis descriptors, positive source-node extraction, bounded arithmetic interpolation, hashes, native CSV links and offline package inclusion. Unknown axes are not silently called full-cell SOC. |
| Stale curation text still called imported ISU data a candidate. | Updated historical status and linked the actual LFP, M50LT and MJ1 curation records. README, navigation, version and citation metadata refreshed. |
| Python distribution metadata named only MIT despite shipping separately licensed data. | Metadata now describes the combined MIT/BSD-3-Clause/CC-BY-4.0 contents; individual source/file licenses and root software terms are unchanged. |
| Git text rules would normalize CRLF in two original MJ1 evidence files, breaking their source hashes after checkout. | Evidence files now bypass text normalization; release audit compares staged Git blob bytes with canonical working files. Source archives retain `.gitattributes` and `.gitignore`. |
| New CLI table-label syntax worked on Python 3.12 but failed on the declared Python 3.10 minimum. | Replaced the quoted expression with compatible branches; added a Python 3.10 grammar check for authored modules, alongside actual version-matrix CI. |

The [2026-10-16 baseline review](PREPUBLICATION_REVIEW.md) remains available as
history. Current coverage is defined by the catalog and the per-cell evidence
matrices rather than the historical baseline's counts.

## Rights and distribution boundary

The root MIT license covers original software/documentation. Per-record licenses
and original notices govern imported data and implementation-derived formulas.
Keep [DATA_LICENSES.md](../DATA_LICENSES.md) with exported files. Source URLs,
versions, hashes, author attribution and conversion/extraction changes are
preserved. A source's public availability alone is not used as a reuse grant.

Unresolved Oxford 9 Ah OCP workbooks, About:Energy M50LT OCPs and the full MJ1
workbook containing literature silicon OCV remain **external leads only**. Their original files and third-party sampled curves are not included in distributable
catalog records or offline bundles. Their unresolved permission does not imply
that reuse is forbidden. It prevents this project from asserting a grant.

Working caches, temporary PDFs, research downloads and local build directories
are ignored. Approved source originals under `src/ebp/data/evidence/` are deliberate,
licensed distribution content, not accidentally committed caches. The Oxford
source-cache release preserves licensed original bytes and notices for CI.

## Verification scope

The release checks cover:

- Source-value fidelity, native coordinates, unit conversions, NA handling,
  uncertainty columns and source/specimen/model association boundaries.
- Catalog schemas, owned-record links, local paths, hashes, missing-channel
  counts and consistency of the matching ledger.
- Python API behavior, extrapolation guards and actual PyBaMM OCP adaptation
  where supported; unresolved reference/coordinate cases remain guarded.
- Generated GitHub navigation, local Markdown targets, native CSV/JSON downloads
  and cell-scoped offline bundles, including source bytes and license notices.
- Cached full-catalog reconstruction, comparing every canonical file byte for
  byte; wheel/source archive completeness and import from an extracted wheel.
- Tracked files and reachable local Git history for common credential patterns,
  unwanted cache/private paths, plus exported series profiles. A clean pattern
  scan is not an exhaustive security guarantee.

Run the reproducible checks from the project root:

Stage intended canonical-data changes before the final release audit so it can
check the exact bytes proposed for publication as well as the working files.

```bash
ebp validate
python scripts/build_data_index.py --check
PYBAMM_DISABLE_TELEMETRY=true python -m pytest -q
python scripts/seed_v01.py --download
git diff --exit-code -- src/ebp/data
python -m build
python scripts/verify_distribution.py
python scripts/release_audit.py --output .cache/release-audit.json
```

Local source caches can reproduce the catalog without `--download`. GitHub CI
also reconstructs from pinned sources and runs Python 3.10/3.12 checks. See
[the workflow](../.github/workflows/ci.yml) and
[CI results](https://github.com/FrankSuperG/electrochemical-battery-parameters/actions).
The repository has no automatic public-site, package-publishing or visibility
change workflow. Tests build the optional viewer without deploying it.

Browser interaction and visual QA of the optional local viewer were not rerun
in this review; JavaScript syntax, generated files and download contents are
checked. Model simulation, fitting and validation are outside the catalog's
scope; this review covers data and software consistency.

## Remaining scientific coverage limits

- MJ1 lacks verified same-study intact-cell CC and t/I/V/T observations. Its
  coordinate calibration, kinetic area basis and complete concentration laws
  remain explicit limits.
- M50LT OCP permission remains unresolved; particle/charge-transfer groups are
  not independently identified intrinsic D/k or absolute porosities.
- ISU reference chemistry and measured I/t/T remain unresolved; the A123 OCPn
  tables are modeled PD-ECM inputs, not raw measured OCP.
- Other source packages retain their borrowing, scaling, missing-channel and
  specimen boundaries. Read the [cell index](../data/README.md) and matching
  matrix before assembling a model.

These are stated coverage limits of the public catalog, not hidden replacements
with invented data. The publication decision belongs to the owner; this task
keeps the repository private and prepares the reviewed content for that decision.
