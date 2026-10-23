# CALCE Samsung INR18650-20R: OCV and dynamic profiles

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `calce-samsung-20r-dynamic`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. Samsung INR18650-20R, 2 Ah; LiNiMnCo/graphite as stated by CALCE

[Open the original dataset](https://calce.umd.edu/data) · Version: `unversioned page; reviewed 2026-10-23`

DOI: Not assigned in the inspected source. Checked: 2026-10-23.

## Tests and channels

Types: dynamic, ocv, pulse. Profiles: US06, DST, FUDS, BJDST.

Source describes low-current and incremental-current OCV protocols; no multi-rate CC sweep asserted.

Reported temperature labels / degC: [0, 25, 45]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Protocols are described on the source page. Per-file measured channel headers were not inspected.

## Parameter association

Match: `unmatched`. No verified join to the catalog parameter studies. Matching chemistry or manufacturer alone is insufficient.

Missing components: electrode_ocp, diffusion, kinetics.

## Reuse and access

License: **not-stated**. [Source terms](https://calce.umd.edu/data). CALCE provides open access and requests citation of the experiment papers; no standard redistribution license was identified on the page. Link only.

Review level: `source_metadata_only`. Primary description and reuse terms reviewed. Raw payload not downloaded; headers, row counts and per-file availability are not certified.


## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Raw file headers, units and sampling details require review before use.
- Dynamic tests start at 80% and 50% battery level; exact specimen chain to OCV tests not verified.
- No standard reuse license verified; obtain terms from the provider before redistributing payloads.

## Evidence

- [Primary source 1](https://calce.umd.edu/data)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
