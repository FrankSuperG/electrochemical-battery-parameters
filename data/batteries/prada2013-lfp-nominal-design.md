# LFP 2.3 Ah | Prada2013 implementation | part unresolved

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 reused expressions](../cells/prada2013-lfp-nominal-design.md#ocp-curves) | [3 records](../parameters/prada2013-lfp-nominal-design--diffusion.csv) | [6 records](../parameters/prada2013-lfp-nominal-design--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/prada2013-lfp-nominal-design.md)

[Machine-readable package (JSON)](../parameters/prada2013-lfp-nominal-design.json)

- **OCP:** Two explicitly borrowed OCP implementation expressions; not new measured points.
- **Diffusion:** Two source scalar solid diffusivities; no cell-specific measurement claim.
- **Kinetics:** Two source exchange-current laws; original convention retained.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

No external full-cell dataset curated for this entry.

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `parameter_set_only`. One published implementation dictionary. Its LFP OCP is borrowed from Afshar2017 and negative OCP from Chen2020. No identified commercial cell or original same-study half-cell pair is established.
