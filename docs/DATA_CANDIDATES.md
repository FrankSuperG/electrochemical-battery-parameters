# Candidate data sources — review of 2026-10-16

These are reviewed leads, **not imported catalog records**. Downloading an
original file does not establish a validated parameter set. Catalog counts stay
at 49 OCP records, 337 other parameters and 25 full-cell files. Licensing, model
definitions and specimen matching must be resolved separately for each import.

## Priorities

| Priority | Candidate | Evidence available | Matching boundary / missing items |
|---|---|---|---|
| 1 — LFP | [ISU–UConn LFP/graphite](https://digitalcommons.lib.uconn.edu/reil_datasets/6/) and [author repository](https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics) | Low-rate half-cell and full-cell voltage/capacity workbook; CC BY 4.0 data | Same-study laboratory electrode/cell family; no commercial model. No diffusion/kinetic characterization or complete measured I/t/T input established. |
| 2 — LFP | [A123 18650M1A hysteresis study](https://doi.org/10.1038/s44172-024-00221-4), [data](https://zenodo.org/records/10852930) | Pseudo-OCV, pulse/path-dependency files and electrode-model arrays; CC BY 4.0 | Same paper/model; exact serial mapping and OCP-array derivation need review. ECM quantities are not intrinsic DFN diffusivity or reaction-rate constants. |
| 3 — same-paper parameter/test chain | [Hallemans2025 LG M50LT](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES) | OCP tables, fitted grouped-SPMe vector, impedance data and measured drive cycle; repository BSD-3-Clause notice | LG M50LT must remain separate from existing LG M50. Review third-party OCP attribution/reuse scope, current sign, group definitions and absent temperature trace before redistribution/import. |
| 4 — electrode characterization | [LG MJ1 characterization collection](https://zenodo.org/records/15407849) | Linked OCP, kinetics, geometry, GITT and model-dependent diffusion products; CC BY 4.0 | Same named cell/project; component-specific specimen evidence. No matching intact-cell time/current/voltage/temperature validation file located in reviewed records. |
| 5 — characterization tables | [O'Regan temperature-dependent characterization](https://zenodo.org/records/5171874) | 58 CSV tables: diffusivity, exchange current, entropy, conductivity and thermal properties; CC BY 4.0 | LG M50 context; existing Chen2020 tests are another study. No same-study full-cell validation trace in the inspected ZIP. |

## 1. ISU–UConn LFP/graphite

The [primary deposit](https://digitalcommons.lib.uconn.edu/reil_datasets/6/)
describes 15 half-cells and 35 laboratory CR2032 full-cells using MTI electrodes.
The [author code repository](https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics)
explicitly identifies its workbook as this CC BY 4.0 dataset; its code is MIT.
The workbook was downloaded successfully at commit
`1188c371e5836df4a7e5f5acf336a34ffd4027e6`; earlier failures at university
download endpoints no longer prevent access to an author-hosted copy.

Container inspection found 19 named sheets, including separate LFP/graphite
half-cell and full-cell configurations. Sheet count is not cell count. The
author loader consumes capacity/voltage pairs; newest-data selection, blank
delimiters, cycles and specimen columns need a dedicated extraction review.
Byte identity with the university-hosted original has not been established.
Best first import: low-rate electrode branches plus explicitly associated
laboratory full-cell V–Q tests. Do not infer commercial identity or measured I/t/T.

## 2. A123 18650M1A / probability-distributed ECM

The [paper's methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC11139865/)
identify an A123 18650M1A, testing at 25 °C, and harvested-electrode tests after
intact-cell experiments. The [deposit](https://zenodo.org/records/10852930)
contains pseudo-OCV and power-test CSVs plus `param_ocpn_lfp.mat` and
`param_ocpn_graphite.mat`. Downloaded pulse files have time, capacity, current and
voltage columns; no temperature channel is present in those CSV headers.

The MATs contain `pot`/`pot_dol` arrays of 399 and 602 values. The paper
distinguishes measured electrode responses from an approximated non-monotone
single-string potential. Determine which representation the arrays encode
before classifying them as measured OCP. Chamber setting is not a measured cell
temperature trace. No solid diffusivity/Butler–Volmer parameter import is proposed.

## 3. LG M50LT / Hallemans2025

Pinned author commit: `3308a34396b8b56cd614291dd151c3405577c068` in
[Battery-Intelligence-Lab/Hallemans-2025-JES](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES).
The stored drive-cycle MAT has 164,953 entries per `t`, `i`, `u`, `v` array.
Its `i` input is used with a sign flip by the author's model script. The fitted
MAT contains 18 grouped parameters and a 65-frequency / seven-SOC fitted
impedance matrix; the raw impedance file has nine SOCs. Review the selection.
No temperature array was found. `u` must not be assumed to mean voltage.

The OCP PDF attributes inputs to About:Energy and separates measured thickness,
estimated active fraction and an assumed pure-graphite/NMC811 description.
Retain that attribution and clarify third-party data reuse before importing.
Grouped diffusion/charge-transfer times need geometry and model conventions
before conversion into intrinsic transport/kinetic quantities. The separate
`timeDomainSimulation` file is synthetic; it must not be substituted for the
measured `DrivecycleMeasurement` file. The reviewed `Fig11` script plots/saves
simulated voltage after applying the drive current; it does not compare the
stored `v` channel. A later importer must establish that measured channel's
semantics and compute its own comparison, rather than relabel a simulation as
experimental validation. No author Python was executed in review.

## 4. LG MJ1 / DLR–SINTEF characterization

Reviewed [complete continuum inputs](https://zenodo.org/records/15496570),
[direct characterization](https://zenodo.org/records/15497193),
[anode GITT raw observations](https://zenodo.org/records/15519535),
[structured GITT](https://zenodo.org/records/15520717),
[OCP fitting](https://zenodo.org/records/15527995) and
[diffusion fits](https://zenodo.org/records/15528177). API metadata specify
CC BY 4.0 and explicit parent/processing relationships.

The parameter Python file was inspected as text. It contains substitutions,
reference-electrode context and placeholder initial states, so a direct scalar
scrape would be unsafe. Diffusion fits are separated by direction and by SPM,
SPMe or DFN formulation; preserve these alternatives. Direct-characterization
metadata name harvested cell #001, which does not establish every linked test's
specimen identity. Large raw CSV/HDF5 payloads were not downloaded; complete
numeric validation and intact-cell test matching remain open.

## 5. O'Regan / LG M50 characterization tables

The [Zenodo API](https://zenodo.org/api/records/5171874) specifies CC BY 4.0.
The 479,705-byte ZIP was downloaded and inspected: 58 CSVs cover two electrode
specimens, direction and temperature-dependent diffusivities, exchange-current
densities and thermal/entropy properties. Example headers retain m²/s, K,
stoichiometry and exchange current in **mA/cm²**, requiring explicit conversion.
The LG M50 context is also documented by the
[official PyBaMM example](https://docs.pybamm.org/en/v23.5_a/source/examples/notebooks/models/simulating-ORegan-2022-parameter-set.html).

Create a distinct O'Regan variant/source package. Linking these inputs to existing
Chen2020 tests would be a same-commercial-model, cross-study comparison, not
same-study validation or a same-specimen match. The ZIP has no full-cell I/V/T
series; keep that gap explicit. Preserve measured/fitted/derived origins per
quantity. Non-OCP tables require a supported table representation and an explicit
interpolation policy rather than an unreported fitted formula.

## Files actually retrieved and pinned

Copies remain in ignored review caches; the table below records provenance,
not permission to treat them as curated data. The original university XLSX and
author-hosted XLSX have not been compared byte-for-byte.

| Source file | SHA-256 |
|---|---|
| ISU–UConn author `LFP_Data.xlsx` | `fd50e09542be7adb2270963d65a6e7b5ccae1473a512f68462c2dd419d620ee1` |
| O'Regan `ORegan 2021 Data Repository.zip` | `1c5052e8af198429c29b6784681e7b1b7d8a4e48dfca03c6fc23df639ce084de` |
| A123 `20230125_Hys_A123_01_25deg_pOCV.csv` | `da6e14f79fe0e16d528780f6a5bacf725778c1390593d689bc6ad54a7517bda0` |
| A123 `20230125_HysPowerTest_A123_01_25deg_SOC100.csv` | `009c2fb085e219c7b20afaa050ac9e69d848cf04fc6e9165ce2bbd1282357feb` |
| M50LT `DrivecycleMeasurement_80to20.mat` | `981e5b045556a226ad7c08ed1401004f980d7983cafa45592f291833bfd9e0d0` |
| M50LT `LG_M50LT_Uneg.csv` | `23795944237357f8d8f656ed10b26eab0df6841e07510d7d9ef275359a1445ba` |
| M50LT `LG_M50LT_Upos.csv` | `012bde7b805908274f2661a4a260f6faa61b4b9e03925db194a3fd63744f7791` |

## Leads not ready for a data import

- [60 Ah graphite/LFP model comparison](https://doi.org/10.1016/j.est.2024.112326):
  useful published model parameterization; the article states data are available
  on request, so a public raw-test download is not established.
- [105 Ah LFP positive-OCP identification](https://www.sciencedirect.com/science/article/pii/S2352152X25029251):
  relevant electrode/full-cell association described in the paper; an accessible
  reusable original test deposit was not verified in this search.

No author has been contacted. Use the [contribution template](../templates/data-contribution.md)
for a future import, and update source hashes, representation labels, reuse
notices and matching evidence before increasing catalog counts.
