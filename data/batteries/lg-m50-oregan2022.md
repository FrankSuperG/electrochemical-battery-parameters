# LG M50 | O'Regan2022 characterization and model

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [2 reused expressions](../cells/lg-m50-oregan2022.md#ocp-curves) | [43 records](../parameters/lg-m50-oregan2022--diffusion.csv) | [14 records](../parameters/lg-m50-oregan2022--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/lg-m50-oregan2022.md)

[Machine-readable package (JSON)](../parameters/lg-m50-oregan2022.json)

- **OCP:** Two stored Chen2020 expressions explicitly reused by O'Regan; no new measured OCP table in this deposit.
- **Diffusion:** 40 experimental tables: two electrodes, two specimens, five temperatures, two directions; plus two separately labeled model laws and a borrowed electrolyte law.
- **Kinetics:** Eight experimental i0 tables at 15/25/35/45 C; two separate concentration/temperature model laws and source charge-transfer/double-layer inputs.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [tec-lgm50-multitemperature-2021](../full-cell/tec-lgm50-multitemperature-2021.md#file-locations) | [Source rates / limits](../full-cell/tec-lgm50-multitemperature-2021.md#requested-test-coverage) | 0/10/25 | Not reported | [Not reported](../full-cell/tec-lgm50-multitemperature-2021.md#ageing-data) | Not reported | Same model; other study, no native parameter join |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Parameter tables and published model refer to LG M50. OCP functions are borrowed from Chen2020. TEC/Chen full-cell comparisons are separate studies; same serialized specimens are not established.
- **tec-lgm50-multitemperature-2021**: Primary TEC2021 paper Table 1 attributes the LG M50 electrode OCP to Chen2020. Two existing catalog expressions therefore provide an explicit reused OCP anchor; full-cell experiments are a different study, without shared serials. This does not associate ORegan2022 diffusion/kinetic tables as same-study TEC measurements.
  [Missing items, source terms and review limits](../full-cell/tec-lgm50-multitemperature-2021.md#missing-items-and-limits)
