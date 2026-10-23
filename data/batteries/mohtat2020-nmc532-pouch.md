# UMBL Mohtat2020 | 5 Ah NMC/graphite research pouch

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [4 expressions](../cells/mohtat2020-nmc532-pouch.md#ocp-curves) | [9 records](../parameters/mohtat2020-nmc532-pouch--diffusion.csv) | [12 records](../parameters/mohtat2020-nmc532-pouch--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/mohtat2020-nmc532-pouch.md)

[Machine-readable package (JSON)](../parameters/mohtat2020-nmc532-pouch.json)

- **OCP:** Two original author OCP expressions plus two PyBaMM variants; graphite x-offset differs (0.007 versus 0.001). Raw half-cell points absent.
- **Diffusion:** Original author D_n=5e-15 and D_p=8e-15 m2/s; PyBaMM same reference values with added Arrhenius dependence.
- **Kinetics:** Original k0_n=1.1e-11 and k0_p=5e-11 with source i0 definition; PyBaMM exchange-current prefactors are rounded/unit-converted and have added temperature dependence.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

[5 existing packaged test files with per-file conditions](../cells/mohtat2020-nmc532-pouch.md#full-cell-tests)

Five original charging MAT files, 0.1/0.2/0.5/1/2C by code/inventory. Measured voltage and temperature versus capacity; current, timestamps, discharge and C/20 files absent.

No external full-cell dataset curated for this entry.

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_study_cell_family`. Original author model is bundled with these five experimental charging files in the same DOI deposit. Cell is fabricated by UMBL, not an identified commercial part. Exact specimen identity is not given.
