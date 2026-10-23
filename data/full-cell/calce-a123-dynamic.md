# CALCE A123 LFP: OCV, DST and FUDS

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `calce-a123-dynamic`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP. A123 cylindrical LFP; exact commercial part unresolved. Page reports 1110 mAh and 25.4 mm diameter; do not infer a model number.

[Open the original dataset](https://calce.umd.edu/data) · Version: `unversioned page; reviewed 2026-10-23`

DOI: Not assigned in the inspected source. Checked: 2026-10-23.

## Tests and channels

Types: dynamic, ocv. Profiles: DST, FUDS.

Low-current OCV and dynamic tests; no source-supported multi-rate CC sweep asserted.

Reported temperature labels / degC: [-10, 0, 10, 20, 25, 30, 40, 50]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Download table lists these temperature labels. They are not proof of measured per-row temperature channels.

## Parameter association

Match: `unmatched`. No verified join to the catalog parameter studies. Matching chemistry or manufacturer alone is insufficient.

Missing components: electrode_ocp, diffusion, kinetics.

## Reuse and access

License: **not-stated**. [Source terms](https://calce.umd.edu/data). CALCE provides open access and requests paper citations; no standard redistribution license identified. Link only.

Review level: `source_metadata_only`. Primary description and reuse terms reviewed. Raw payload not downloaded; headers, row counts and per-file availability are not certified.


## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Raw file headers, units and sampling details require review before use.
- Narrative temperature range differs from the download-table labels; listed values describe the table, not a verified complete test matrix.
- Do not join to an A123 model based on brand, dimensions or chemistry alone.

## Evidence

- [Primary source 1](https://calce.umd.edu/data)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
