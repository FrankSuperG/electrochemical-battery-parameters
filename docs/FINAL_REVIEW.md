# Final project review — v0.16.0

Reviewed 2026-10-24. Repository visibility remains **private**. No Pages,
public deployment or model-performance release is created by this review.
The deliverable is a traceable, partial electrochemical parameter catalog.

Current inventory: **90 OCP/fit records, 1,041 non-OCP records, 19 native
cell/study packages, 13 material labels, 51 legacy supporting full-cell test files and
11 parameter-associated external sources / 357 selected locators**. Counts are records/branches,
not independent specimens, complete parameter sets or condition matrices.

[README battery index](../README.md#battery-model-index) ·
[Parameter admission rules](PROJECT_SCOPE.md) ·
[Source and extraction audit](PARAMETER_AUDIT.md) ·
[HAIDI review](HAIDI_REHM2025.md) · [Data licenses](../DATA_LICENSES.md)

## Scope and source decisions

- Electrochemical model parameters define admission: every cell/study package
  and supporting external source has stored OCP, diffusion or kinetics records.
  Six unmatched test-only sources and the A123 9 Ah package are removed from
  active data, indexes, CLI and viewer. Source leads remain historical evidence.

- Every native OCP/parameter record has source IDs, units/coordinates, provenance,
  license and explicit model/cell ownership. Relative branch capacity is not
  presented as absolute lithium stoichiometry or full-cell SOC.
- HAIDI: seven author-processed branches admitted under exact-DOI publisher
  CC BY 4.0 evidence; one cathode original quarantined for a protocol mismatch.
  Conflicting metadata and original-provider access failures remain inspectable.
- First-party Rehm2026/P45B data keep their separate MIT basis. Laboratory
  graphite comparators are not assigned to the P45B graphite phase.
- M50LT third-party OCP, other unresolved literature inputs and unreviewed
  reconstruction definitions remain excluded. O'Regan Cp anomalies remain
  quarantined. Historical dated review ledgers are not rewritten as raw evidence.
- New whole-cell observations remain introductions and external links. Existing
  packaged observations are retained only for admitted parameter packages. Source protocols,
  file listings, read contents and measured channels remain distinct.
- Study/model matches do not prove identical specimens. GEIS/GITT observations
  do not automatically establish intrinsic diffusion or kinetic coefficients.
  Borrowed expressions, grouped quantities, defaults and model variants remain
  separate. No electrochemical-model validation is claimed.

## Executed verification

| Check | Result / inspectable evidence |
|---|---|
| Local automated suite | 153 tests passed, including all 98,695 HAIDI admitted nodes and the nine-node quarantine diagnosis. |
| Catalog integrity | Schemas, ownership/source joins, finite ascending axes, representation domains and local evidence/CSV SHA-256 pass `ebp validate`. |
| Offline reconstruction | All 343 canonical files reproduce byte-for-byte with `scripts/seed_v01.py`. |
| Prior data preservation | All 90 OCP/fit and 1,041 non-OCP records are unchanged from v0.15. The 51 retained supporting test records and their 78 payload/sidecar files are unchanged. Ten unsupported 9 Ah test files are intentionally removed. |
| Navigation | 240 generated files and README index are current; authored documentation/navigation file targets resolve locally. Original upstream readmes retain their own upstream-relative paths. |
| Licensing and quality boundaries | Dataset-specific CC BY, first-party MIT, third-party holds, quarantines, processed/raw distinctions and grouped/model inputs remain explicit. |
| Presentation metadata | Authored docs are English, CFF schema/version valid, JavaScript syntax valid, and source author lists/record-specific notice links are checked. |
| Credential-pattern review | 360 source/document files checked for high-signal private-key, GitHub-token and AWS-key patterns; no findings. This is not a comprehensive secret-scanner certification. |
| Release artifacts | Wheel/source byte checks cover all 343 canonical files and the required source/documentation files, with notices retained and cache/runtime paths excluded. |

Static viewer generation, wheel/source builds and
[`verify_distribution.py`](../scripts/verify_distribution.py) cover packaged
canonical bytes, required source files, original notices and cache/runtime
exclusions. The final commit's [CI run](https://github.com/FrankSuperG/electrochemical-battery-parameters/actions)
also checks Python 3.10/3.12, Linux source reconstruction and the PyBaMM curve
adapter. This checks the data/component interface, not full-cell model accuracy.
The latest CI status is available at the linked Actions page; per-job skips can
differ with optional dependencies and source-cache availability.

## Remaining limits

The original HAIDI provider file inventory/headers, mirror-to-original raw-file
identity, exact donors, absolute half-cell Ah/stoichiometry, and exact MAT
cycle/filtering history remain unresolved. Six temperature labels are paper
conditions, not a verified six-temperature file grid. Road-cycle and longitudinal
ageing data are not established for this source.

Other source-specific gaps remain in the per-model audit and data pages. This
review does not certify that every external server/archive is currently reachable
or that every published electrochemical dataset has been found. Unsupported
source records are not redistributed to fill those gaps.
