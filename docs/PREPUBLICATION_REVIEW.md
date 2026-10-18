# Prepublication review — 2026-10-16

Historical baseline review. The current v0.8 release assessment is
[RELEASE_READINESS.md](RELEASE_READINESS.md). Later imports are documented in
[LFP study packages](LFP_STUDIES.md), [LG M50LT](HALLEMANS2025.md) and
[LG MJ1](LG_MJ1.md); current catalog counts supersede the baseline below.

Scope: repository content, data lineage and matching, distribution completeness,
GitHub data navigation, usage examples and a new source search. The reviewed
baseline was `a2916ae8aa67d8989cdc0aa4746b312cecc58b9e`. Visibility changes,
website deployment and independent electrochemical model validation are outside
this review. The repository remains restricted until its owner changes access.

## Assessment

The project is suitable for release as a **traceable, partial electrochemical
parameter and observation catalog**, with its existing evidence and missing-item
labels retained. It does not establish complete interchangeable parameter sets,
identical characterization/validation specimens or new model-prediction accuracy.
Newly discovered sources are [candidates](DATA_CANDIDATES.md), not imported data.

## Findings and fixes

| Severity / confidence | Finding and practical effect | Resolution |
|---|---|---|
| Medium / high | LG M50's two solid diffusivities were categorized as `electrode`; the diffusion filter missed both. | Seed classification corrected to `diffusion`; record versions advanced to 2. Numeric values, units, IDs and source evidence are unchanged. A regression assertion exercises the public filter. |
| Medium / high | Source-package manifest omitted generated GitHub data navigation, contribution templates and issue/PR files. Relative README links were incomplete outside a Git checkout. | Manifest includes these directories. `verify_distribution.py` checks their actual archived bytes and every packaged data file. CI runs this after building. |
| Low / high | LG M50 license documentation used `lg-m50-*`, while files are named `LGM50_cell*`; one evidence path omitted `src/ebp/`. | File patterns and paths corrected. Per-record licenses and source bytes retain their existing terms. |
| Low / high | Historical Mohtat sections could be read as current no-import claims. Changelog stopped at v0.3 while the package was v0.5. | Historical status explicitly scoped; v0.4/v0.5 history added. |
| Low / high | Unconditional private-repository wording would become misleading after publication. | Reader instructions now work with public or restricted access. No repository access setting was changed. |
| Informational / high | GitHub reports the repository license as `Other`, while the root file contains MIT plus a third-party scope note. | Original license terms and the explicit per-source exclusions are preserved. Readers should use `DATA_LICENSES.md` and record notices rather than infer one license for the entire data collection from GitHub's badge. |

## Data quality and grain

The review covers 49 OCP records with **548,973 retained table points**,
337 other parameter records and **84,103 rows in 25 full-cell files**.
These counts describe stored records/points, not independent studies or specimens.
Keys, source/cell references, hashes, scalar/function domains, normalized channels,
OCP coordinate order and complete native tables are checked by the catalog and
source tests plus the review script.

- No non-finite stored numeric channels, backwards native axes or duplicate
  source-record IDs were found in the full-cell profile.
- Each of three LG M50 files has two repeated timestamps. They are retained from
  the source. A time-domain solver needs an explicit event/resampling policy;
  source preservation is not a guarantee of strictly increasing sample time.
- Two A123 9 Ah discharge files each contain one missing current and voltage
  observation. Source gaps remain blank and are counted; no values were invented.
- Ecker current/absolute temperature, Enertech current/absolute temperature,
  Mohtat current/time and most ambient traces remain known missing channels.
  Separate temperature-rise channels never become absolute temperature records.
- Characterization implementations, fitted/effective quantities and borrowed
  inputs retain their source roles. Formula CSVs remain generated samples.
  No cell joins were strengthened on chemistry/capacity alone.

## Privacy and source notices

The baseline had 260 tracked files and 10 reachable commits. A read-only scan of
404 text Git objects found no configured common credential patterns; tracked
working files also had no matches. No source caches, virtual environments or
private key paths were tracked. This is a bounded pattern scan, not an exhaustive
security certification. The maintainer's public contact address is intentional.

MIT covers original project code/documentation; third-party records retain
CC BY 4.0, BSD or MIT source terms. The current upstream PyBaMM-data BSD notice
was fetched and matched the packaged notice byte-for-byte. Author Mohtat originals
retain headers and hashes. Reuse notices and primary attribution remain separate
from scientific evidence that any value was measured on a specific specimen.

## Reproduce the checks

Run from a checkout with the documented development dependencies:

```bash
python scripts/release_audit.py --output .cache/release-review/audit.json
python scripts/build_data_index.py --check
ebp validate
PYBAMM_DISABLE_TELEMETRY=true python -m pytest -q
ebp build-site
python -m build
python scripts/verify_distribution.py
```

Use a fresh output directory if old build versions remain, then pass it with
`verify_distribution.py --dist PATH`. The distribution check compares source
archive documents/navigation/templates and wheel data with checkout bytes,
including binary MAT/PDF evidence and all per-source license notices. It also
rejects cached/private paths in either archive. An isolated wheel-install check
exercises catalog loading and validation outside the checkout.

The source reconstruction was rerun from pinned cached originals. Only intended
diffusivity metadata and generated parameter exports changed; retained OCP and
full-cell observations were not modified. GitHub navigation checks cover file
links, formula labels, complete-data targets and parameter variant separation.

## Remaining boundaries

- Published OCP/functions are checked against pinned implementations; the
  project has not independently audited every original paper equation or fit.
- Same-model/same-study is not same specimen. Current per-cell gaps remain
  material to transferring a parameterization into a model.
- Model simulation, fitting and validation are outside this catalog's scope;
  this review covers data, source evidence and access.
- Browser interaction/visual QA was not repeated. The previously declined
  localhost browser origin was not retried. Static and file-export checks do
  not establish browser layout or interaction behavior.
- Automated source retrieval may fail at primary hosts. Attributed source-cache
  copies and hash pins support reproduction; the primary source stays authoritative.

Before a public release, retain the data-source notices and inspect the final CI
run. Public access itself is a separate owner action; no publication or external
message was sent during this review.
