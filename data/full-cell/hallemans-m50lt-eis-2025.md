# LG M50LT: measured EIS and grouped parameters

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `hallemans-m50lt-eis-2025`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. LG M50LT; same study as the catalog grouped SPMe parameters; exact serialized specimen chain unresolved

[Open the original dataset](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068) · Version: `3308a34396b8b56cd614291dd151c3405577c068`

DOI: 10.1149/1945-7111/add41b. Checked: 2026-10-23.

## Tests and channels

Types: eis. Profiles: No named drive profile verified.

3 mV rms EIS; 9 SOC levels and 65 frequencies (585 measured rows).

Reported temperature labels / degC: [25]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: frequency_Hz, measured_Z_real_Ohm, measured_Z_imag_Ohm.

Measured whole-cell spectrum from the existing source audit. Setpoint is not a measured temperature trace. Seven-SOC fitting slice is separate from all nine measured SOCs.

## Parameter association

Match: `same_model_same_study`. Pinned author Figure 10 script connects the measured EIS file to the same grouped SPMe fit. Exact specimen identity across EIS, drive-cycle and harvested-electrode characterization is not established.

[LG M50LT &#124; Hallemans2025 grouped SPMe](../cells/lg-m50lt-hallemans2025.md)

Missing components: electrode_ocp, intrinsic_diffusion, intrinsic_kinetics.

## Reuse and access

License: **BSD-3-Clause**. [Source terms](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/blob/3308a34396b8b56cd614291dd151c3405577c068/LICENSE). Pinned author BSD-3-Clause notice applies to author-owned observations; it does not clear third-party About:Energy OCP rights.

Review level: `existing_source_audit`. Uses the catalog pinned Hallemans source audit; no additional raw file downloaded. Existing 585-row EIS evidence CSV remains available.

- [Measured EIS MAT (external pinned original)](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/impedanceLGM50LT_Hybrid_4h_3mVrms.mat)
  Publisher/pinned SHA256: `5f06cf0b495eeb2d5704b41a6e3c93b8e480e977b71809d5b8f5e39c643ad8c5`.

[Previously curated supporting evidence (CSV)](../../src/ebp/data/evidence/hallemans2025-m50lt-eis.csv)


## Missing items and limits

- OCP redistribution permission unresolved.
- Grouped diffusion/charge-transfer times are not intrinsic D or reaction-rate prefactors.
- Exact specimen mapping and measured temperature traces unresolved.
- No standalone CC observations found in the reviewed author files.

## Evidence

- [Primary source 1](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068)
- [Primary source 2](https://arxiv.org/html/2412.10896v4)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
