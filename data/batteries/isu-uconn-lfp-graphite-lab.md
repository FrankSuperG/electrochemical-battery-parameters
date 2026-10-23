# ISU-UConn | laboratory LFP/graphite CR2032 family

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| [4 pseudo-OCP](../cells/isu-uconn-lfp-graphite-lab.md#ocp-curves) | Not extracted | Not extracted |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/isu-uconn-lfp-graphite-lab.md)

[Machine-readable package (JSON)](../parameters/isu-uconn-lfp-graphite-lab.json)

- **OCP:** Four C/20 half-cell pseudo-OCP branches from the author-selected two specimens; reference electrode detail and temperature not verified.
- **Diffusion:** No matched solid diffusion characterization imported.
- **Kinetics:** No matched intrinsic reaction-rate or exchange-current characterization imported.

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

[21 existing packaged test files with per-file conditions](../cells/isu-uconn-lfp-graphite-lab.md#full-cell-tests)

Eleven author-selected charge branches and available following discharge branches; native capacity/voltage only.

No external full-cell dataset curated for this entry.

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_study_cell_family`. Author notebook cells 6 and 8 use the selected LFP/graphite half-cell pair for eleven full-cell configurations in the same laboratory study. Shared MTI electrode family, not an identified commercial model or proven identical harvested specimen.
