# Candidate data sources — review of 2026-10-16

This ledger began with the 2026-10-16 review. ISU-UConn and A123 18650M1A
were partially imported in v0.6.0; see [LFP curation](LFP_STUDIES.md).
**LG M50LT / Hallemans2025 is partially imported in v0.7.0**; see
[its reuse/definition review](HALLEMANS2025.md). OCP remains external only.
LG MJ1 is partially imported in v0.8.0; [its review](LG_MJ1.md) documents
four pseudo-OCP branches and 42 parameter records, without an intact-cell test.
O'Regan remains a candidate. Current counts are 72 electrode curves, 457 other
parameters and 61 full-cell exports. Licenses, model definitions and specimen
matching remain distinct from data availability.

## Priorities

| Priority | Candidate | Evidence available | Matching boundary / missing items |
|---|---|---|---|
| Imported subset — LFP | [ISU–UConn LFP/graphite](https://digitalcommons.lib.uconn.edu/reil_datasets/6/) and [author repository](https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics) | Four pseudo-OCP branches and 21 full-cell V-Q branches; CC BY 4.0 data | Same-study laboratory family; no commercial model. Reference details, I/t/T and diffusion/kinetics remain missing. |
| Imported subset — LFP | [A123 18650M1A hysteresis study](https://doi.org/10.1038/s44172-024-00221-4), [data v2](https://zenodo.org/records/11958572) | Two modeled OCPn tables and 14 full-cell exports; CC BY 4.0 | Same paper/model; exact serial mapping unresolved. OCPn is parameterized, not raw measured OCP. No intrinsic diffusion/kinetic values imported. |
| Imported subset — grouped SPMe | [Hallemans2025 LG M50LT](HALLEMANS2025.md) | 18 grouped fit values, measured drive cycle and EIS evidence; author repository BSD-3-Clause notice retained | Same named model/study, separate from LG M50. OCP permission, serial chain, intrinsic coefficients, measured T and standalone CC traces remain unresolved/missing. |
| Imported subset — harvested electrodes | [LG MJ1 characterization](LG_MJ1.md) | Four pseudo-OCP curves, 22 scalars/specifications, eight laboratory tables and twelve GITT model fits; CC BY 4.0 | Shared model/study; coordinates, model alternatives and original/reassembled cell configuration remain distinct. No intact-cell t/I/V/T test verified. |
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
The subsequent v0.6 importer uses two author-selected half-cell specimens and
eleven full-cell configurations, with explicit source addresses and derivative
rules. It does not infer commercial identity, reference chemistry or measured I/t/T.

## 2. A123 18650M1A / probability-distributed ECM

The [paper's methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC11139865/)
identify an A123 18650M1A, testing at 25 °C, and harvested-electrode tests after
intact-cell experiments. The [deposit](https://zenodo.org/records/10852930)
contains pseudo-OCV and power-test CSVs plus `param_ocpn_lfp.mat` and
`param_ocpn_graphite.mat`. Downloaded pulse files have time, capacity, current and
voltage columns; no temperature channel is present in those CSV headers.

The MATs contain `pot`/`pot_dol` arrays of 399 and 602 values. The subsequent paper
and MATLAB text review confirms these are parameterized single-string OCPn model
inputs. v0.6 retains them with `model_ocp` / `model_soc` labels and imports the
selected observation files from fixed data v2 (the original v1 file checksums
agree). Chamber setting remains distinct from measured temperature. No intrinsic
diffusivity/Butler–Volmer parameters are inferred.

## 3. LG M50LT / Hallemans2025

The v0.7 [curation review](HALLEMANS2025.md) supersedes the earlier candidate
status. Pinned author commit: `3308a34396b8b56cd614291dd151c3405577c068`.
The retained fit vector agrees with arXiv **v4** at printed precision; v3's
10 mV experiment and fitted values must not be combined with this 3 mV study.
The stored measured drive cycle has 164,953 t/i/v rows; its current sign and
same-study paper link are established. `u` remains unresolved in the original
MAT only. No measured temperature or standalone constant-current test is supplied.

OCP files and About:Energy notes remain checksum-pinned external leads:
no distinct M50LT reuse grant was found. Grouped diffusion/charge-transfer times
and relative porosities remain model quantities, not independently characterized
intrinsic coefficients or absolute porosity. The separate synthetic time-domain
simulation and Fig11's simulated voltage are not imported as observations.

## 4. LG MJ1 / DLR–SINTEF characterization

The v0.8 [source and matching review](LG_MJ1.md) supersedes the candidate
status. Selected original bytes, metadata, native tables and model-fit error
bounds are packaged under CC BY 4.0. The laboratory workbook resolves missing
endpoints that some Parquet exports turned into zero. The model script's
substitutions and placeholder initial states are not automatically imported.

Inspected structured anode GITT voltage is versus the lithium reference in a
reassembled three-electrode fixture. It is not original MJ1 terminal voltage.
No same-study intact-cell validation or standalone commercial CC trace was
verified; this remains an explicit gap rather than an inferred join.

## 5. O'Regan / LG M50 characterization tables

Follow-up on 2026-10-23: the primary O'Regan paper points to Zenodo 4864437 for
full-cell comparison data. Its v1.0 TEC2021 archive and author repository have
now been indexed at 0/10/25 degC with explicit Chen2020 OCP reuse. They remain a
separate experiment/parameter source; no shared specimen or new independent OCP
measurement is implied. See [the OCP-first review](OCP_FIRST_EXPANSION.md).

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

The original review downloaded these files into ignored caches. Selected
ISU/A123 originals are packaged with their v0.6 derivatives; selected M50LT
author measurements/results are packaged in v0.7. Its OCP files and the
remaining candidates stay external. The original university XLSX and
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
