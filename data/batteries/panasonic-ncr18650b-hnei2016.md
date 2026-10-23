# Panasonic NCR18650B | HNEI2016

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NCA**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [4 pseudo-OCP](../cells/panasonic-ncr18650b-hnei2016.md#ocp-curves) | Not extracted | Not extracted |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/panasonic-ncr18650b-hnei2016.md)

[Machine-readable package (JSON)](../parameters/panasonic-ncr18650b-hnei2016.json)

- **OCP:** Four extracted finite-current half-cell branches, with original coordinates and source rows retained.
- **Diffusion:** No matched diffusivity values imported.
- **Kinetics:** No matched intrinsic kinetic values imported.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [hnei-ncr18650b-2016](../full-cell/hnei-ncr18650b-2016.md#file-locations) | [Source rates / limits](../full-cell/hnei-ncr18650b-2016.md#requested-test-coverage) | Unverified | Not reported | [Not reported](../full-cell/hnei-ncr18650b-2016.md#ageing-data) | Not reported | same_model_same_study |
| [bayreuth-ncr18650b-2023](../full-cell/bayreuth-ncr18650b-2023.md#file-locations) | [Source rates / limits](../full-cell/bayreuth-ncr18650b-2023.md#requested-test-coverage) | 25 | Not reported | [Not reported](../full-cell/bayreuth-ncr18650b-2023.md#ageing-data) | Located / source-listed | same_model_different_study |
| [virtual-vehicle-ncr18650b-aging-2023](../full-cell/virtual-vehicle-ncr18650b-aging-2023.md#file-locations) | [Source rates / limits](../full-cell/virtual-vehicle-ncr18650b-aging-2023.md#requested-test-coverage) | 0/5/15/20/25/30/35/40/45 | Unnamed / staged | [Yes (cycle, calendar)](../full-cell/virtual-vehicle-ncr18650b-aging-2023.md#ageing-data) | Not reported | same_model_different_study |
| [stanford-ncr18650b-rates-2021](../full-cell/stanford-ncr18650b-rates-2021.md#file-locations) | [Source rates / limits](../full-cell/stanford-ncr18650b-rates-2021.md#requested-test-coverage) | 5/25/35 | Not reported | [Not reported](../full-cell/stanford-ncr18650b-rates-2021.md#ageing-data) | Not reported | same_model_different_study |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Source names this cell/model within one study; full-cell observations stay externally linked and same-specimen mapping remains unresolved.
- **hnei-ncr18650b-2016**: Native extracted OCP/parameter records and external full-cell tests are linked by explicit study/model identity. No identical serialized specimen is asserted.
  [Missing items, source terms and review limits](../full-cell/hnei-ncr18650b-2016.md#missing-items-and-limits)
- **bayreuth-ncr18650b-2023**: Explicit Panasonic NCR18650B identity permits a cross-study reference to HNEI half-cell curves. No shared specimen, batch, ageing state or transferable D/kinetics is established.
  [Missing items, source terms and review limits](../full-cell/bayreuth-ncr18650b-2023.md#missing-items-and-limits)
- **virtual-vehicle-ncr18650b-aging-2023**: Explicit Panasonic NCR18650B identity permits a cross-study reference to HNEI half-cell curves. No shared specimen, batch, ageing state or transferable D/kinetics is established.
  [Missing items, source terms and review limits](../full-cell/virtual-vehicle-ncr18650b-aging-2023.md#missing-items-and-limits)
- **stanford-ncr18650b-rates-2021**: Explicit Panasonic NCR18650B identity permits a cross-study reference to HNEI half-cell curves. No shared specimen, batch, ageing state or transferable D/kinetics is established.
  [Missing items, source terms and review limits](../full-cell/stanford-ncr18650b-rates-2021.md#missing-items-and-limits)
