# University of Malaya: LFP, NCA and NMC dynamic tests

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `malaya-three-chemistries-2022`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP, NMC, NCA. Source names an LFP 18650 3.3 V 1100 mAh cell, Panasonic NCR18650B 3400 mAh and Murata VTC6 18650 3000 mAh; per-model chemistry/profile matrix not independently inspected

[Open the original dataset](https://data.mendeley.com/datasets/29kw38kzwj/1) · Version: `1`

DOI: 10.17632/29kw38kzwj.1. Checked: 2026-10-23.

## Tests and channels

Types: dynamic, pulse. Profiles: US06, DST, FUDS, UDDS, WLTP.

HPPC and pulse charge/discharge are described; numeric rates not verified.

Reported temperature labels / degC: Not verified. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Source reports Neware BTS 4000 testing at four temperatures. Numeric setpoints and raw channel definitions were not verified.

## Parameter association

Match: `unmatched`. No verified join to the catalog parameter studies. Matching chemistry or manufacturer alone is insufficient.

Missing components: electrode_ocp, diffusion, kinetics.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://data.mendeley.com/datasets/29kw38kzwj/1). Source dataset terms apply to downloaded files; cite the dataset and associated study.

Review level: `source_metadata_only`. Primary description and reuse terms reviewed. Raw payload not downloaded; headers, row counts and per-file availability are not certified.


## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Raw file headers, units and sampling details require review before use.
- Material/profile coverage is dataset-level; no assertion that every named profile is available for every cell or temperature.
- Numeric temperatures, per-cell filenames and rates await source-file inspection.
- Not linked to Kim2011 nominal NCA parameters; chemistry alone does not establish a parameter match.

## Evidence

- [Primary source 1](https://data.mendeley.com/datasets/29kw38kzwj/1)
- [Primary source 2](https://doi.org/10.1016/j.est.2022.106049)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
