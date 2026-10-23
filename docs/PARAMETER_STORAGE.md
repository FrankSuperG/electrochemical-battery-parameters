# Parameter storage and battery-model navigation

[Battery model index](../data/batteries/README.md) · [NCR18650B extraction](NCR18650B.md)

## Storage rule

Reusable **electrode OCP and model parameters are extracted and stored in this
repository** after source definitions and reuse terms are checked. New
**full-cell tests remain external links**, with descriptions, test conditions,
exact file locations, licensing, matching and missing items. Existing packaged
full-cell files are retained for compatibility. A discovery link alone is not an
imported parameter record.

## Fixed representations

| Item | Authoritative representation | Download / interpretation |
|---|---|---|
| Measured finite-current half-cell branch | `src/ebp/data/curves/*.csv` plus `catalog.json` metadata | Required `x,potential_V`; preserve native capacity, source row and other verified fields. Normalized branch progress is not absolute lithium fraction. |
| Published fitted OCP table | Same curve CSV/JSON format, explicitly labeled `literature_table` with fitted origin | Retain native nodes and source validity bounds; never label it a new measurement. |
| Analytical OCP | Expression in `catalog.json`; generated `data/ocp/*-sampled.csv` for convenience | Generated points remain labeled formula samples. |
| Other scalar or expression parameter | `parameters.json`; generated per-cell and category CSVs | Keep unit, definition, independent variables, conditions, source and origin. |
| Tabulated model parameter | `src/ebp/data/parameter_tables/*.csv` plus parameter JSON | Preserve source coordinate, missingness, domain and any error bounds. |
| Large full-cell measurement set | `external_datasets.json`; linked source pages under `data/full-cell/` | Store links and verified metadata. No automatic observation download. |

The generated **battery-model index** places OCP, diffusion, kinetics and full-cell
links in one row. Every model hub separates source studies and lists CC/rates,
full-cell temperatures, named/unnamed dynamic tests, ageing, EIS and the parameter
relationship. Material-only records remain in the OCP material index. A shared
model name is not a shared batch, specimen or ageing state.

## v0.12 extraction scope (historical)

- **NCR18650B / HNEI:** four low-rate NE/PE branches, 11,854 source points. Two
  original MAT members are retained under CC0. Source columns have no headers;
  exact current/time charge integration and paper voltage windows corroborate
  units. PE's source rate denominator 39 differs from the paper's C/40 label.
  No diffusion or kinetic coefficients are inferred from rate tests.
- **CALB generation 3b / NEXTBMS:** four C/20 slow-sweep source branches, 11,831
  retained points. The author README confirms harvested Cell_96 electrodes
  against lithium and documents the specific-capacity units. Sixteen repeated
  zero-capacity rows per file are omitted from the interpolation table using
  the last source occurrence; all original CSV rows remain available. The
  source naming text is ambiguous about physical directions, so charge/discharge
  names are preserved and lithiation direction remains unspecified. GITT files
  do not automatically become intrinsic diffusivity values.
- **Molicel P45B / About:Energy:** five fitted phase/branch OCP tables, 5,047
  retained nodes, plus 60 BPX inputs (58 scalars and two entropy tables).
  Graphite, silicon additive and NCA remain separate. Each OCP keeps only native
  nodes inside its particle's configured stoichiometry bounds. The original BPX
  includes extreme endpoint extrapolations and is preserved unchanged; those
  extrapolations are outside catalog evaluation domains. Six diffusion records
  mean three D inputs plus three activation energies; the six kinetic records
  likewise include coefficients and activation energies. BPX coefficients in
  `mol.m-2.s-1` are not relabeled intrinsic k or A/m2 exchange current.

The complete P45B BPX is retained with the author BSD notice. Its five standard
electrolyte placeholder zeros are **not** imported as measured zero transport;
71 user-defined law coefficients were initially retained in the original BPX.
In v0.13 their checked definitions also produce seven native transport,
thermodynamic, kinetic and contact-resistance records; coefficient flags remain
source metadata. No upstream author
code is executed. Partial exports are not drop-in complete model inputs.

**At v0.12:** TUM P45B measurement inputs and M50LT third-party OCP were
external pending reuse checks. The seven-file TUM first-party subset is admitted
in v0.14 below; M50LT and other candidate sources retain documented gaps. Unknown half-cell temperature is never
filled from full-cell test setpoints.

## v0.13 completion

See the [per-model audit](PARAMETER_AUDIT.md) and [O'Regan review](OREGAN2022.md).
The native inventory is 76 OCP/fit records and 1,041 other parameters across
18 cell/study packages. The four added OCP records are explicitly reused
expressions for O'Regan and Prada model variants, not new measurements.
Seven PyBaMM dictionaries now have all numeric/analytic non-OCP inputs stored,
including labeled assumptions and optional submodel defaults. Three BPX LFP
reference laws and seven P45B extension inputs are also native.

O'Regan adds 55 experimental tables and 73 separate model inputs. Three suspect
Cp files remain quarantined in the original archive. Full-cell observations added
in this release remain descriptions and external links.

## Reproduce and check

`scripts/parameter_source_assets.json` pins original file/member URLs and hashes.
`scripts/seed_parameter_sources.py` reads packaged half-cell/BPX originals offline.
It is included in the normal catalog reconstruction, which leaves the manually
reviewed external-link registry intact. Tests compare each extracted voltage,
capacity and parameter to original rows or BPX pointers, check coordinate handling
and confirm that no new full-cell observations are packaged.

Packaged original README files preserve source-relative links unchanged; use the
project model/source pages for working navigation within this repository.

```bash
python scripts/seed_parameter_sources.py
ebp validate
python scripts/build_data_index.py
```

## v0.14 TUM admission

The native inventory is now 83 curves/fits and 1,041 other parameters across
19 cell/study packages. Seven first-party TUM branches retain 40,378 original
points under the fixed release MIT evidence: five harvested P45B and two
material-only laboratory graphite curves. Each CSV also retains the original
normalized capacity and one-based MAT row; branch progress is not stoichiometry.

See [rights, source definitions and holds](TUM_OCP_RIGHTS.md). Serial23 ageing
checkups remain external at same-model/same-study match, with exact donor and
measured temperature channels unresolved. At that v0.14 review, M50LT, HAIDI and third-party TUM
inputs remained held where permission or definitions cannot be established.

## v0.15 HAIDI follow-up

At the v0.15 review: 90 OCP/fit records, 1,041 non-OCP records and
20 cell/study packages. HAIDI adds seven author-processed pseudo-OCP branches
with 98,695 unchanged source nodes. One additional cathode original is
quarantined for a protocol mismatch. CC BY 4.0 data terms come from exact-DOI
publisher metadata; the framework MIT grant is not reused for those data.

The [HAIDI source review](HAIDI_REHM2025.md) distinguishes half-cell 25 C from
six whole-cell temperatures, source protocols from actual file/header checks,
and same-study association from identical specimen identity. All new whole-cell
observations stay external; no D/kinetic law is inferred from GITT or GEIS.

## v0.16 parameter admission rule

The active inventory is 90 OCP/fit records, 1,041 other parameters and 19
cell/study packages. Every cell and external supporting source has at least
one stored OCP, diffusion or kinetics record. Six unmatched test-only sources
and the A123 9 Ah package were removed. Its ten packaged CC files are no
longer included; 51 supporting legacy test files remain. New full-cell
observations stay external. [Scope and removal decisions](PROJECT_SCOPE.md).
