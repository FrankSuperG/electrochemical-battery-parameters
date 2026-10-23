# A123 AMP20M1HD-A | 20 Ah LFP pouch

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| Not extracted | [6 records](../parameters/a123-amp20m1hd-a--diffusion.csv) | [6 records](../parameters/a123-amp20m1hd-a--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/a123-amp20m1hd-a.md)

[Machine-readable package (JSON)](../parameters/a123-amp20m1hd-a.json)

- **OCP:** C/25 full-cell pseudo-OCV reported in Methods; no downloadable electrode-resolved OCP points located in the selected deposit
- **Diffusion:** Fitted shared diffusion times at three SOCs; effective D derived using the model's assumed radius
- **Kinetics:** Fitted volumetric exchange-current density and activation energy at three SOCs

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

[1 existing packaged test files with per-file conditions](../cells/a123-amp20m1hd-a.md#full-cell-tests)

Cell I 4C full-discharge voltage/current/thermal grid available

No external full-cell dataset curated for this entry.

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Methods names AMP20M1HD-A; paper links the ORA dataset; archive filename identifies Cell I. Table 1 is for one cell but its letter is not explicitly established here, so a same-specimen parameter claim is withheld.
