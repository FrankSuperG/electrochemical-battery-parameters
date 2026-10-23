# NCA_Kim2011 | NCA/graphite | 0.43 Ah model input

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NCA**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 expressions](../cells/kim2011-nca-nominal-design.md#ocp-curves) | [6 records](../parameters/kim2011-nca-nominal-design--diffusion.csv) | [7 records](../parameters/kim2011-nca-nominal-design--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/kim2011-nca-nominal-design.md)

[Machine-readable package (JSON)](../parameters/kim2011-nca-nominal-design.json)

- **OCP:** Kim2011 nominal-design implementation
- **Diffusion:** Two Arrhenius particle-diffusivity functions, with source stoichiometry/temperature inputs retained
- **Kinetics:** Two concentration/temperature exchange-current laws; source area and concentration convention retained

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

No external full-cell dataset curated for this entry.

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `unmatched`. A nominal design, not an identified commercial cell. Upstream thermal properties combine Marquis2019 material inputs with effective-heat-capacity scaling; they are not independently measured NCA-cell material properties. No matching raw test is assigned.
