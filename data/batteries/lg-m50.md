# LG M50 | 5 Ah NMC811/graphite-SiOx

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 expressions](../cells/lg-m50.md#ocp-curves) | [6 records](../parameters/lg-m50--diffusion.csv) | [7 records](../parameters/lg-m50--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/lg-m50.md)

[Machine-readable package (JSON)](../parameters/lg-m50.json)

- **OCP:** Both electrode OCP expressions available; effective graphite-SiOx negative and NMC811 positive
- **Diffusion:** Two scalar particle diffusivities in upstream implementation
- **Kinetics:** Two exchange-current density laws

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

[3 existing packaged test files with per-file conditions](../cells/lg-m50.md#full-cell-tests)

Three same-model validation samples

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [tec-lgm50-multitemperature-2021](../full-cell/tec-lgm50-multitemperature-2021.md#file-locations) | [Source rates / limits](../full-cell/tec-lgm50-multitemperature-2021.md#requested-test-coverage) | 0/10/25 | Not reported | [Not reported](../full-cell/tec-lgm50-multitemperature-2021.md#ageing-data) | Not reported | same_model_different_study |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Parameters and full-cell tests are linked at same-model/same-study level. No exact characterization-specimen match or independently reproduced full-cell fit is claimed. This is an intentionally partial parameter collection.
- **tec-lgm50-multitemperature-2021**: Primary TEC2021 paper Table 1 attributes the LG M50 electrode OCP to Chen2020. Two existing catalog expressions therefore provide an explicit reused OCP anchor; full-cell experiments are a different study, without shared serials. This does not associate ORegan2022 diffusion/kinetic tables as same-study TEC measurements.
  [Missing items, source terms and review limits](../full-cell/tec-lgm50-multitemperature-2021.md#missing-items-and-limits)
