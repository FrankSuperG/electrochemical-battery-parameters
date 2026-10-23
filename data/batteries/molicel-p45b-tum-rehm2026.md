# Molicel P45B | TUM Rehm2026 measured half-cells

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NCA**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [5 pseudo-OCP](../cells/molicel-p45b-tum-rehm2026.md#ocp-curves) | Not extracted | Not extracted |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/molicel-p45b-tum-rehm2026.md)

[Machine-readable package (JSON)](../parameters/molicel-p45b-tum-rehm2026.json)

- **OCP:** Five native finite-current pseudo-OCP branches, original nodes retained; Li/Li+ reference confirmed in Section 2.4.
- **Diffusion:** No same-study intrinsic diffusivity admitted.
- **Kinetics:** No same-study intrinsic kinetic law admitted.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [tum-p45b-halfcell-aging-2026](../full-cell/tum-p45b-halfcell-aging-2026.md#file-locations) | Not separately verified | 25 | Not reported | [Yes (cycle)](../full-cell/tum-p45b-halfcell-aging-2026.md#ageing-data) | Not reported | same_model_same_study |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Five harvested P45B half-cell branches and external serial23 checkups share paper/model; exact donor/serial identity unresolved. About:Energy P45B parameters are a separate study.
- **tum-p45b-halfcell-aging-2026**: Five native harvested P45B pseudo-OCP branches and serial23 checkups share the Rehm2026 study/model. Same serialized donor is unresolved. About:Energy BPX is a separate study.
  [Missing items, source terms and review limits](../full-cell/tum-p45b-halfcell-aging-2026.md#missing-items-and-limits)
