# Final project review — v0.15.0

Reviewed 2026-10-24. Repository visibility remains **private**. No Pages,
public deployment or model-performance release is created by this review.
The deliverable is a traceable, partial electrochemical parameter catalog.

Current inventory: **90 OCP/fit records, 1,041 non-OCP records, 20 native
cell/study packages, 13 material labels, 61 legacy full-cell test files and
17 external sources / 436 selected locators**. Counts are records/branches,
not independent specimens, complete parameter sets or condition matrices.

[README battery index](../README.md#battery-model-index) ·
[Source and extraction audit](PARAMETER_AUDIT.md) ·
[HAIDI review](HAIDI_REHM2025.md) · [Data licenses](../DATA_LICENSES.md)

## Scope and source decisions

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
  packaged observations are retained for compatibility. Source protocols,
  file listings, read contents and measured channels remain distinct.
- Study/model matches do not prove identical specimens. GEIS/GITT observations
  do not automatically establish intrinsic diffusion or kinetic coefficients.
  Borrowed expressions, grouped quantities, defaults and model variants remain
  separate. No electrochemical-model validation is claimed.

## Executed verification

| Check | Result / inspectable evidence |
|---|---|
| Local automated suite | 152 tests passed, including all 98,695 HAIDI admitted nodes and the nine-node quarantine diagnosis. |
| Catalog integrity | Schemas, ownership/source joins, finite ascending axes, representation domains and local evidence/CSV SHA-256 pass `ebp validate`. |
| Offline reconstruction | All 353 canonical files reproduce byte-for-byte with `scripts/seed_v01.py`. |
| Prior data preservation | All prior 83 curve, 1,041 non-OCP and 61 full-cell records are unchanged; full-cell file bytes are unchanged. |
| Navigation | 255 generated files and README index are current; 1,803 authored documentation/navigation links resolve locally. |
| Licensing and quality boundaries | Dataset-specific CC BY, first-party MIT, third-party holds, quarantines, processed/raw distinctions and grouped/model inputs remain explicit. |
| Presentation metadata | Authored docs are English, CFF schema/version valid, JavaScript syntax valid, and source author lists/record-specific notice links are checked. |
| Credential-pattern review | 372 source/document files checked for high-signal private-key, GitHub-token and AWS-key patterns; no findings. This is not a comprehensive secret-scanner certification. |
| Release artifacts | Wheel/source byte checks cover all 353 canonical files and 706 required source files, with notices retained and cache/runtime paths excluded. |

Static viewer generation, wheel/source builds and
[`verify_distribution.py`](../scripts/verify_distribution.py) cover packaged
canonical bytes, required source files, original notices and cache/runtime
exclusions. The final commit's [CI run](https://github.com/FrankSuperG/electrochemical-battery-parameters/actions)
also checks Python 3.10/3.12, Linux source reconstruction and the PyBaMM curve
adapter. This checks the data/component interface, not full-cell model accuracy.

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
