# Kokam SLPB75106100 | 7.5 Ah NCO/graphite

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NCO**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 expressions](../cells/kokam-slpb75106100-ecker2015.md#ocp-curves) | [6 records](../parameters/kokam-slpb75106100-ecker2015--diffusion.csv) | [6 records](../parameters/kokam-slpb75106100-ecker2015--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/kokam-slpb75106100-ecker2015.md)

[Machine-readable package (JSON)](../parameters/kokam-slpb75106100-ecker2015.json)

- **OCP:** Two upstream figure-fitted expressions; same model/study lineage
- **Diffusion:** Two stoichiometry/temperature diffusivity fits; Ecker/Richardson lineage
- **Kinetics:** Two concentration/temperature exchange-current laws; Ecker/Richardson lineage

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

[2 existing packaged test files with per-file conditions](../cells/kokam-slpb75106100-ecker2015.md#full-cell-tests)

Two digitized CC discharges: 1C and 5C; time/voltage only

No external full-cell dataset curated for this entry.

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Ecker characterization and validation share the named Kokam SLPB75106100 model. Whole-cell voltage points are digitized from Richardson2020 Figure 8. Exact specimen match is not established.
