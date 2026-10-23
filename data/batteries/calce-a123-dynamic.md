# A123 cylindrical LFP / part unresolved

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| Not extracted | Not extracted | Not extracted |


## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [calce-a123-dynamic](../full-cell/calce-a123-dynamic.md#file-locations) | Not separately verified | -10/0/10/20/25/30/40/50 | DST, FUDS, US06 | [Not reported](../full-cell/calce-a123-dynamic.md#ageing-data) | Not reported | unmatched |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- **calce-a123-dynamic**: CALCE exact A123 part is unresolved; source specification and sample labels do not establish identity with catalog A123 entries. Same brand and LFP chemistry are insufficient.
  [Missing items, source terms and review limits](../full-cell/calce-a123-dynamic.md#missing-items-and-limits)
