# Malaya three-model archive / per-model files unverified

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP/NMC/NCA**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| Not extracted | Not extracted | Not extracted |


## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [malaya-three-chemistries-2022](../full-cell/malaya-three-chemistries-2022.md#file-locations) | Not separately verified | Unverified | US06, DST, FUDS, UDDS, WLTP | [Unverified](../full-cell/malaya-three-chemistries-2022.md#ageing-data) | Not reported | unmatched |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- **malaya-three-chemistries-2022**: Named models and archived per-model test matrix remain separate from catalog studies. Panasonic NCR18650B is not the unidentified Kim2011 nominal design; generic NCA or NMC tags are not joins.
  [Missing items, source terms and review limits](../full-cell/malaya-three-chemistries-2022.md#missing-items-and-limits)
