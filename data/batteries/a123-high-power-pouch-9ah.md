# A123 high-power LFP pouch | 9 Ah | part undisclosed

[All battery models](README.md) · [Storage and reuse rules](../../docs/DATA_ACCESS.md)

Material grouping: **LFP**. This is a navigation group; studies and specimens remain separate.

## OCP and model parameters

OCP and reusable model parameters are extracted into versioned CSV/JSON records. Unresolved reuse or definitions remain explicit; full-cell OCV is not electrode OCP.

| OCP | Diffusion | Kinetics |
|---|---|---|
| Not extracted | Not extracted | Not extracted |

[Full cell/study package: definitions, all parameters, sources and gaps](../cells/a123-high-power-pouch-9ah.md)

[Machine-readable package (JSON)](../parameters/a123-high-power-pouch-9ah.json)

- **OCP:** Full-cell pseudo-OCP referenced in the paper; electrode potentials are conventionally allocated, not electrode-resolved measurements
- **Diffusion:** Fast-diffusion model assumption; no finite fitted diffusivity imported
- **Kinetics:** Not transcribed in this release; raw tests do not uniquely identify electrode kinetic laws

## Full-cell tests

New full-cell observations remain at their providers. Links below lead to descriptions, exact file locations, source licenses and missing channels. Existing packaged tests are retained for compatibility.

[10 existing packaged test files with per-file conditions](../cells/a123-high-power-pouch-9ah.md#full-cell-tests)

Ten CC charge/discharge files at 2, 4, 6, 8 and 10C

No external full-cell dataset curated for this entry.

Multi-temperature labels apply to full-cell source conditions, not a complete temperature × rate × profile matrix or to half-cell OCP. Source-listed coverage is distinct from checked file contents. Not reported does not prove absence.

## Matching and gaps

A shared commercial model permits discovery across studies; it does not establish shared batches, specimens, ageing state or transferable parameters. Grouped diffusion/kinetics and BPX phase coefficients retain their definitions.

- Native package match: `same_study_cell_family`. Paper identifies a 9 Ah A123 power pouch; the linked ORA archive supplies this study's CC tests. Exact part number and per-file cell serial are not disclosed.
