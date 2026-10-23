# Enertech | LCO/graphite | 2.28 Ah model input

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LCO**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 tables / fits](../cells/enertech-lco-pouch-ai2020.md#ocp-curves) | [6 records](../parameters/enertech-lco-pouch-ai2020--diffusion.csv) | [7 records](../parameters/enertech-lco-pouch-ai2020--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/enertech-lco-pouch-ai2020.md)

[Machine-readable package (JSON)](../parameters/enertech-lco-pouch-ai2020.json)

- **OCP:** Two published OCP tables; negative synthetic extrapolation guard removed
- **Diffusion:** Two borrowed Dualfoil Arrhenius diffusivity functions; not same-cell measured D
- **Kinetics:** Two borrowed Dualfoil exchange-current laws; not same-cell measured kinetics

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

[4 existing packaged test files with per-file conditions](../cells/enertech-lco-pouch-ai2020.md#full-cell-tests)

Four experimental voltage series: 0.1/0.5/1/2C; three separate temperature-rise sidecars; measured current absent

No external full-cell dataset curated for this entry.

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_study_cell_family`. Enertech observations and Ai2020 implementation share the Ai/Rieger study family. Exact commercial model and specimen remain unresolved; borrowed electrode functions do not become measurements through this link.
