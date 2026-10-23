# CALB generation 3b | NEXTBMS2026

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [4 pseudo-OCP](../cells/calb-gen3b-nextbms2026.md#ocp-curves) | Not extracted | Not extracted |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/calb-gen3b-nextbms2026.md)

[Machine-readable package (JSON)](../parameters/calb-gen3b-nextbms2026.json)

- **OCP:** Four extracted finite-current half-cell branches, with original coordinates and source rows retained.
- **Diffusion:** No matched diffusivity values imported.
- **Kinetics:** No matched intrinsic kinetic values imported.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [nextbms-calb-nmc532-2026](../full-cell/nextbms-calb-nmc532-2026.md#file-locations) | [Source rates / limits](../full-cell/nextbms-calb-nmc532-2026.md#requested-test-coverage) | 0/5/25/45 | Unnamed / staged | [Yes (cycle, calendar)](../full-cell/nextbms-calb-nmc532-2026.md#ageing-data) | Located / source-listed | same_model_same_study |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.
- **nextbms-calb-nmc532-2026**: Native extracted OCP/parameter records and external full-cell tests are linked by explicit study/model identity. No identical serialized specimen is asserted.
  [Missing items, source terms and review limits](../full-cell/nextbms-calb-nmc532-2026.md#missing-items-and-limits)
