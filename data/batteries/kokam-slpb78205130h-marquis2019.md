# SLPB78205130H | LCO/graphite | 0.680616 Ah model input

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LCO**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 expressions](../cells/kokam-slpb78205130h-marquis2019.md#ocp-curves) | [2 records](../parameters/kokam-slpb78205130h-marquis2019--diffusion.csv) | [2 records](../parameters/kokam-slpb78205130h-marquis2019--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/kokam-slpb78205130h-marquis2019.md)

[Machine-readable package (JSON)](../parameters/kokam-slpb78205130h-marquis2019.json)

- **OCP:** Dualfoil1998 borrowed OCP implementation; no same-cell half-cell measurement match established
- **Diffusion:** Two Arrhenius particle-diffusivity functions, with source stoichiometry/temperature inputs retained
- **Kinetics:** Two concentration/temperature exchange-current laws; source area and concentration convention retained

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

No external full-cell dataset curated for this entry.

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `parameter_set_only`. The upstream set names a Kokam model but borrows Dualfoil electrode functions. Model association does not establish that the OCP, diffusion or kinetics were measured on that commercial specimen.
