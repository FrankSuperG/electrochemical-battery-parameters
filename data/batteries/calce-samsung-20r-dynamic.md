# Samsung INR18650-20R / CALCE

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| Not extracted | Not extracted | Not extracted |


## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [calce-samsung-20r-dynamic](../full-cell/calce-samsung-20r-dynamic.md#file-locations) | Not separately verified | 0/25/45 | US06, DST, FUDS, BJDST | [Not reported](../full-cell/calce-samsung-20r-dynamic.md#ageing-data) | Not reported | unmatched |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- **calce-samsung-20r-dynamic**: Samsung INR18650-20R has no electrode-characterization parameter package in this catalog. LG M50/M50LT and Mohtat NMC cells are different models/studies.
  [Missing items, source terms and review limits](../full-cell/calce-samsung-20r-dynamic.md#missing-items-and-limits)
