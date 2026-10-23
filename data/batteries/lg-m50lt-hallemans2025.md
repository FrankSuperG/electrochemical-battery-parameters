# LG M50LT | Hallemans2025 grouped SPMe

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **NMC**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [Reuse unresolved](../cells/lg-m50lt-hallemans2025.md#ocp-curves) | [2 records (groups)](../parameters/lg-m50lt-hallemans2025--diffusion.csv) | [4 records (groups)](../parameters/lg-m50lt-hallemans2025--kinetics.csv) |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/lg-m50lt-hallemans2025.md)

[Machine-readable package (JSON)](../parameters/lg-m50lt-hallemans2025.json)

- **OCP:** Third-party About:Energy OCPs used by source model; no separate M50LT reuse grant established, no curves imported.
- **Diffusion:** Two fitted R^2/D particle time scales; not independent solid diffusivities. EIS Z/f/SOC exactly matches fit MAT selection.
- **Kinetics:** Two fitted F*R/(m*sqrt(c_e0)) groups and two electrode capacitances; no intrinsic k or exchange-current density law.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, available file locations, source licenses and missing channels. Existing packaged tests support admitted parameter packages.

[1 existing packaged test files with per-file conditions](../cells/lg-m50lt-hallemans2025.md#full-cell-tests)

One same-study measured drive-cycle t/i/v series (164953 rows), nominal 80-20% SOC. No measured T or standalone CC cycle.

| Source / files | CC / rate coverage | Full-cell temperatures / °C | Dynamic | Ageing | EIS | Parameter relationship |
|---|---|---|---|---|---|---|
| [hallemans-m50lt-eis-2025](../full-cell/hallemans-m50lt-eis-2025.md#file-locations) | Not separately verified | 25 | Unnamed / staged | [Not reported](../full-cell/hallemans-m50lt-eis-2025.md#ageing-data) | Located / source-listed | same_model_same_study |

[Parameter extraction audit: stored records, unresolved reuse and definitions](../../docs/PARAMETER_AUDIT.md)

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_model_same_study`. Same explicit LG M50LT model and Hallemans2025 study: Fig11 loads this drive-cycle MAT and the same fitted vector; v4 Section 7.3 identifies measured terminal voltage and Fig11 validation. Exact serialized-specimen chain to harvested OCP half-cells is not supplied.
- **hallemans-m50lt-eis-2025**: Pinned author Figure 10 script connects the measured EIS file to the same grouped SPMe fit. Exact specimen identity across EIS, drive-cycle and harvested-electrode characterization is not established.
  [Missing items, source terms and review limits](../full-cell/hallemans-m50lt-eis-2025.md#missing-items-and-limits)
