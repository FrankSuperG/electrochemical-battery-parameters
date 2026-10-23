# Molicel P45B | About:Energy2026 BPX

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NCA**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [5 tables / fits](../cells/molicel-p45b-aboutenergy2026.md#ocp-curves) | [7 records](../parameters/molicel-p45b-aboutenergy2026--diffusion.csv) | [8 records](../parameters/molicel-p45b-aboutenergy2026--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/molicel-p45b-aboutenergy2026.md)

[Machine-readable package (JSON)](../parameters/molicel-p45b-aboutenergy2026.json)

- **OCP:** Published BPX phase-specific fits; original measured half-cell points not located.
- **Diffusion:** Three phase-specific D inputs and three activation energies in BPX.
- **Kinetics:** BPX-native reaction coefficients/activation energies and two author-defined negative-phase i0 laws with explicitly checked F*k and modifier convention.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [aboutenergy-p45b-2026](../full-cell/aboutenergy-p45b-2026.md#file-locations) | [Source rates / limits](../full-cell/aboutenergy-p45b-2026.md#requested-test-coverage) | 10/25/40/60 | WLTP, eVTOL | [Not reported](../full-cell/aboutenergy-p45b-2026.md#ageing-data) | Not reported | same_model_same_study |
| [tum-p45b-halfcell-aging-2026](../full-cell/tum-p45b-halfcell-aging-2026.md#file-locations) | Not separately verified | 25 | Not reported | [Yes (cycle)](../full-cell/tum-p45b-halfcell-aging-2026.md#ageing-data) | Not reported | Same model; other study, no native parameter join |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.
- **aboutenergy-p45b-2026**: Native extracted OCP/parameter records and external full-cell tests are linked by explicit study/model identity. No identical serialized specimen is asserted.
  [Missing items, source terms and review limits](../full-cell/aboutenergy-p45b-2026.md#missing-items-and-limits)
- **tum-p45b-halfcell-aging-2026**: Five native harvested P45B pseudo-OCP branches and serial23 checkups share the Rehm2026 study/model. Same serialized donor is unresolved. About:Energy BPX is a separate study.
  [Missing items, source terms and review limits](../full-cell/tum-p45b-halfcell-aging-2026.md#missing-items-and-limits)
