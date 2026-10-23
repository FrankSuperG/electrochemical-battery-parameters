# LG MJ1 | DLR-SINTEF harvested-electrode characterization

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [4 pseudo-OCP](../cells/lg-mj1-dlr-sintef.md#ocp-curves) | [18 records](../parameters/lg-mj1-dlr-sintef--diffusion.csv) | [6 records](../parameters/lg-mj1-dlr-sintef--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/lg-mj1-dlr-sintef.md)

[Machine-readable package (JSON)](../parameters/lg-mj1-dlr-sintef.json)

- **OCP:** Four laboratory pseudo-OCP tables, lithium reference; native reported coordinate requires explicit model balancing.
- **Diffusion:** Four workbook GITT tables, twelve model/direction-dependent GITT fit tables with source error bounds, and two SOC-specific activation energies.
- **Kinetics:** Four EIS-derived exchange-current tables and two SOC-specific activation energies; area-basis and concentration/temperature extension remain unresolved.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [snu-mj1-dynamic-aging-2024](../full-cell/snu-mj1-dynamic-aging-2024.md#file-locations) | Not separately verified | 25 | Unnamed / staged | [Yes (cycle)](../full-cell/snu-mj1-dynamic-aging-2024.md#ageing-data) | Not reported | same_model_different_study |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Explicit LG MJ1 model and common DLR/SINTEF collection. Direct characterization identifies harvested cell #001; fit records link to their GITT processing chain. No intact-cell validation specimen correspondence established.
- **snu-mj1-dynamic-aging-2024**: Commercial MJ1 model matches the catalog DLR-SINTEF half-cell study, but paper, specimens, manufacturing batch and ageing state differ. Four existing finite-current half-cell OCP branches are a same-model, different-study reference only; no same-study D/i0 transfer or performance claim.
  [Missing items, source terms and review limits](../full-cell/snu-mj1-dynamic-aging-2024.md#missing-items-and-limits)
