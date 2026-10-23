# LFP IFR14500 labels / manufacturer unresolved

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| Not extracted | Not extracted | Not extracted |


## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [milano-lfp-eis-2023](../full-cell/milano-lfp-eis-2023.md#file-locations) | Not separately verified | Unverified | Not reported | [Not reported](../full-cell/milano-lfp-eis-2023.md#ageing-data) | Located / source-listed | unmatched |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- **milano-lfp-eis-2023**: Only 600 mAh LFP is disclosed. No manufacturer/part or electrode-characterization chain establishes a join to catalog LFP OCP, D or kinetics.
  [Missing items, source terms and review limits](../full-cell/milano-lfp-eis-2023.md#missing-items-and-limits)
