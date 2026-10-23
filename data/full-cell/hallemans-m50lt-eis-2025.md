# LG M50LT: measured EIS and grouped parameters

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `hallemans-m50lt-eis-2025`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. LG M50LT; same study as the catalog grouped SPMe parameters; exact serialized specimen chain unresolved

[Open the original dataset](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068) · Version: `3308a34396b8b56cd614291dd151c3405577c068`

DOI: 10.1149/1945-7111/add41b. Checked: 2026-10-23.

## Tests and channels

Types: eis, dynamic. Profiles: No named drive profile verified.

3 mV rms EIS; 9 SOC levels and 65 frequencies (585 measured rows).

Reported temperature labels / degC: [25]. These are source conditions, not measured temperature channels.

Reported time-series channels: t (s), i (A; charge-positive), v (V).

Reported frequency-domain channels: frequency_Hz, measured_Z_real_Ohm, measured_Z_imag_Ohm.

Existing audited author MAT t/i/v drive-cycle channels and measured whole-cell EIS evidence. Source u is not used as measured voltage/current. The 25 degC EIS setpoint is not a measured temperature trace or a drive-cycle condition. Seven-SOC fitting subset is distinct from all nine measured EIS SOCs.

## Parameter association

Match: `same_model_same_study`. Pinned author Figure 10 script connects the measured EIS file to the same grouped SPMe fit. Exact specimen identity across EIS, drive-cycle and harvested-electrode characterization is not established.

[LG M50LT &#124; Hallemans2025 grouped SPMe](../cells/lg-m50lt-hallemans2025.md)

Missing components: electrode_ocp, intrinsic_diffusion, intrinsic_kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | Third-party OCP permission unresolved; no electrode OCP imported. Missing: About:Energy OCP redistribution permission and a reusable same-study electrode OCP record. |
| diffusion | `same_model_same_study` / `grouped_time_scale` | `hallemans2025-tau-d-p`, `hallemans2025-tau-d-n` | Same source fitted vector supplies electrode particle diffusion time scales R^2/D. Radius and intrinsic D are not separately identified. Missing: Independent particle radius and intrinsic diffusivity per electrode.; Exact serialized specimen chain. |
| kinetics | `same_model_same_study` / `grouped_kinetics` | `hallemans2025-tau-ct-p`, `hallemans2025-tau-ct-n`, `hallemans2025-c-p`, `hallemans2025-c-n` | Same fitted vector supplies grouped charge-transfer times and electrode capacitances, not an independently identified reaction-rate prefactor or exchange-current law. Missing: Intrinsic reaction-rate or exchange-current law and its independent concentration/area inputs.; Exact serialized specimen chain. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| multi_rate_discharge | `not_located` | No specifically verified file of this class in this selected review; not proof of absence. |
| US06 | `not_established` | Same-study drive cycle is available but no source evidence names it US06. |
| EIS | `previously_audited` | Pinned author MAT and existing 585-row measured EIS evidence CSV, same model/study as six linked diffusion/kinetic group records. |

## File locations

Selected verified file/container locators, not an exhaustive test matrix. Repeated basenames are distinct when source_path differs.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `Data/LGM50LT/impedanceLGM50LT_Hybrid_4h_3mVrms.mat` | LG M50LT / No sample ID | eis;  | 25 degC | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/impedanceLGM50LT_Hybrid_4h_3mVrms.mat) |
| `Data/LGM50LT/Zhat3mV_SOC_SPMe_LGM50LT.mat` | LG M50LT / No sample ID | ;  | Temperature unknown | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/Zhat3mV_SOC_SPMe_LGM50LT.mat) |
| `Data/LGM50LT/DrivecycleMeasurement_80to20.mat` | LG M50LT / No sample ID | dynamic;  | Temperature unknown | `existing_source_audit`; content `existing_source_audit` | [Open source file](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/DrivecycleMeasurement_80to20.mat) |

File notes:

- `Data/LGM50LT/impedanceLGM50LT_Hybrid_4h_3mVrms.mat`: Previously audited measured whole-cell EIS. Ambient 25 degC is a source setpoint; no per-row measured temperature trace.
- `Data/LGM50LT/Zhat3mV_SOC_SPMe_LGM50LT.mat`: Source fitted-group vector, not measured EIS or independent model results; existing audit ties it to the catalog grouped values.
- `Data/LGM50LT/DrivecycleMeasurement_80to20.mat`: Previously curated same-study measured t/i/v drive cycle. No named US06 designation and no measured temperature trace.

## Reuse and access

License: **BSD-3-Clause**. [Source terms](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/blob/3308a34396b8b56cd614291dd151c3405577c068/LICENSE). Pinned author BSD-3-Clause notice applies to author-owned observations; it does not clear third-party About:Energy OCP rights.

Review level: `existing_source_audit`. Uses the catalog pinned Hallemans source audit; no additional raw file downloaded. Existing 585-row EIS evidence CSV remains available.

- [impedanceLGM50LT_Hybrid_4h_3mVrms.mat](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/impedanceLGM50LT_Hybrid_4h_3mVrms.mat)
  Publisher/pinned SHA256: `5f06cf0b495eeb2d5704b41a6e3c93b8e480e977b71809d5b8f5e39c643ad8c5`.
- [Zhat3mV_SOC_SPMe_LGM50LT.mat](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/Zhat3mV_SOC_SPMe_LGM50LT.mat)
  Publisher/pinned SHA256: `b451a9c009479efe6b5f3a13989d424d35ae4d20f033371a4ecb87b95d6840df`.
- [DrivecycleMeasurement_80to20.mat](https://raw.githubusercontent.com/Battery-Intelligence-Lab/Hallemans-2025-JES/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/DrivecycleMeasurement_80to20.mat)
  Publisher/pinned SHA256: `981e5b045556a226ad7c08ed1401004f980d7983cafa45592f291833bfd9e0d0`.

[Supporting evidence (CSV)](../../src/ebp/data/evidence/hallemans2025-m50lt-eis.csv)


## Missing items and limits

- OCP redistribution permission unresolved.
- Grouped diffusion/charge-transfer times are not intrinsic D or reaction-rate prefactors.
- Exact specimen mapping and measured temperature traces unresolved.
- No standalone CC observations found in the reviewed author files.

## Evidence

- [Primary source 1](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068)
- [Primary source 2](https://arxiv.org/html/2412.10896v4)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
