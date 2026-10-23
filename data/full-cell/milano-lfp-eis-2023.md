# 600 mAh LFP cells: SOC-dependent EIS

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `milano-lfp-eis-2023`. Storage: **external link**. This entry is not an imported measurement file.

Material families: LFP. 600 mAh LFP batteries; manufacturer and commercial part not supplied in the inspected metadata

[Open the original dataset](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1) · Version: `1`

DOI: 10.6084/m9.figshare.23736582.v1. Checked: 2026-10-23.

## Tests and channels

Types: eis. Profiles: No named drive profile verified.

Repeated EIS across SOC and charging cycles; no CC rate sweep verified.

Reported temperature labels / degC: Not verified. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: impedance.

Official metadata describes EIS, but archive columns, impedance sign, units and frequency range were not inspected.

## Parameter association

Match: `unmatched`. No verified join to the catalog parameter studies. Matching chemistry or manufacturer alone is insufficient.

Missing components: electrode_ocp, diffusion, kinetics.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1). Source dataset terms apply to downloaded files; cite the dataset and associated study.

Review level: `source_metadata_only`. Official Figshare JSON metadata and license reviewed; HTML returned HTTP 403. Archive not fetched; MD5 and size are publisher-reported, not independently calculated.

- [Measurements.rar (external; 465799 bytes)](https://ndownloader.figshare.com/files/41673360)
  Publisher/pinned MD5: `94a817377b3f5148806e65d4bb68b29a`.

## Missing items and limits

- No same-study electrode OCP, intrinsic diffusion or reaction-kinetic parameter join established in this catalog.
- No exact specimen join to existing catalog cells.
- Raw file headers, units and sampling details require review before use.
- Exact cell model, temperature, frequency grid, SOC values and complex-impedance convention not verified.
- EIS payload is not a time/current/voltage discharge trace.

## Evidence

- [Primary source 1](https://figshare.com/articles/dataset/Li-ion_Batteries_EIS_measurements/23736582/1)
- [Primary source 2](https://api.figshare.com/v2/articles/23736582)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
