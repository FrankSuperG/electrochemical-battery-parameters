# Panasonic NCR18650B beginning-of-life pseudo-OCV, pulses and EIS (92 cells)

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `bayreuth-ncr18650b-2023`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NCA. 92 Panasonic NCR18650B cells at beginning of life. Source rows identify individual cells within this dataset; no cross-study row/serial correspondence is established.

[Open the original dataset](https://zenodo.org/records/8369275) · Version: `1.0 (fixed record 8369275)`

DOI: 10.5281/zenodo.8369275. Checked: 2026-10-23.

## Electrode OCP anchor

**Whole-cell OCV only**. The reviewed OCV/pseudo-OCV locators describe the whole cell. No electrode half-cell OCP association is established.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: Use the cited catalog curves/source evidence; no verified external half-cell member path.

OCP evidence: [Source 1](https://zenodo.org/records/8369275)

## Tests and channels

Types: constant_current, ocv, pulse, eis. Profiles: No named drive profile verified.

Whole-cell pseudo-OCV at 0.05C in both directions; 0.5C, 10 s charge/discharge pulses at 50% SOC. A single pulse rate is not a multi-rate continuous CC sweep.

Reported temperature labels / degC: [25]. These are source conditions, not measured temperature channels.

Reported time-series channels: pulse_time, pulse_voltage, whole_cell_pseudo_OCV, SOC.

Reported frequency-domain channels: frequency_Hz, Z_real_Ohm, Z_imag_Ohm.

Field names/units are documented on the source page, not verified from CSV/MAT contents. Pseudo-OCV curves are interpolated to 5000 SOC points. EIS: 50% SOC, four-hour rest, 250 mA excitation, 0.01 Hz–10 kHz. Pulses follow two-hour rest. 25 degC is a chamber condition, not a measured temperature trace; no pulse current trace is claimed.

## Ageing data

**Not reported**. The source describes initial characterization, not a longitudinal ageing series.

[Ageing coverage evidence](https://zenodo.org/records/8369275). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set.

Components without a native catalog join: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |
| diffusion | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |
| kinetics | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |
| multi_rate_discharge | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |
| US06 | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |
| EIS | `file_located` | impedance.mat, f.csv, Z_real.csv and Z_imag.csv are explicitly listed with source-documented frequency and complex-impedance definitions. File contents remain unread. |

## File locations

All 13 source-listed files: three MAT containers and ten CSV companions. CSV and MAT are alternative representations, not additional specimens or independent tests.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `Z_imag.csv` | Panasonic NCR18650B / No sample ID | eis;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/Z_imag.csv/content) |
| `Z_real.csv` | Panasonic NCR18650B / No sample ID | eis;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/Z_real.csv/content) |
| `f.csv` | Panasonic NCR18650B / No sample ID | eis;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/f.csv/content) |
| `impedance.mat` | Panasonic NCR18650B / No sample ID | eis;  | 25 degC | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/impedance.mat/content) |
| `pocv.mat` | Panasonic NCR18650B / No sample ID | ocv, constant_current;  | 25 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pocv.mat/content) |
| `pocv_ch.csv` | Panasonic NCR18650B / No sample ID | ocv, constant_current;  | 25 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pocv_ch.csv/content) |
| `pocv_dc.csv` | Panasonic NCR18650B / No sample ID | ocv, constant_current;  | 25 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pocv_dc.csv/content) |
| `pocv_soc.csv` | Panasonic NCR18650B / No sample ID | ocv, constant_current;  | 25 degC; 0.05C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pocv_soc.csv/content) |
| `pulse.mat` | Panasonic NCR18650B / No sample ID | pulse;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pulse.mat/content) |
| `pulse_neg_time.csv` | Panasonic NCR18650B / No sample ID | pulse;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pulse_neg_time.csv/content) |
| `pulse_neg_voltage.csv` | Panasonic NCR18650B / No sample ID | pulse;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pulse_neg_voltage.csv/content) |
| `pulse_pos_time.csv` | Panasonic NCR18650B / No sample ID | pulse;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pulse_pos_time.csv/content) |
| `pulse_pos_voltage.csv` | Panasonic NCR18650B / No sample ID | pulse;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://zenodo.org/api/records/8369275/files/pulse_pos_voltage.csv/content) |

File notes:

- `Z_imag.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `Z_real.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `f.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `impedance.mat`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pocv.mat`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pocv_ch.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pocv_dc.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pocv_soc.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pulse.mat`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pulse_neg_time.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pulse_neg_voltage.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pulse_pos_time.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.
- `pulse_pos_voltage.csv`: Source-listed file; documented field definitions and shared row grain only. Contents and publisher MD5 were not independently checked.

## Reuse and access

License: **not-stated**. [Source terms](https://zenodo.org/records/8369275/export/json). No license was found in the inspected API metadata, record export or landing page. Open access is not a redistribution grant; keep observations external and resolve permission before reuse/redistribution.

Review level: `source_file_listing`. Primary metadata and listed file paths inspected; no experimental file contents read or imported.

- [Z_imag.csv](https://zenodo.org/api/records/8369275/files/Z_imag.csv/content)
  Publisher/pinned MD5: `625f64adb72f4cebd0977b40186bbbc2`.
- [Z_real.csv](https://zenodo.org/api/records/8369275/files/Z_real.csv/content)
  Publisher/pinned MD5: `66c912594aebfd612c5cdf84e4aca86b`.
- [f.csv](https://zenodo.org/api/records/8369275/files/f.csv/content)
  Publisher/pinned MD5: `92c140ad832996c876b84fd2d87b9fd5`.
- [impedance.mat](https://zenodo.org/api/records/8369275/files/impedance.mat/content)
  Publisher/pinned MD5: `73d6c64790063f076f24b47d4781a1c7`.
- [pocv.mat](https://zenodo.org/api/records/8369275/files/pocv.mat/content)
  Publisher/pinned MD5: `6193e6355e9d845f77b4decf691afa38`.
- [pocv_ch.csv](https://zenodo.org/api/records/8369275/files/pocv_ch.csv/content)
  Publisher/pinned MD5: `0f02774494b93c18edd335c9a188408f`.
- [pocv_dc.csv](https://zenodo.org/api/records/8369275/files/pocv_dc.csv/content)
  Publisher/pinned MD5: `485ea0795d373c2ec19bca93643130bb`.
- [pocv_soc.csv](https://zenodo.org/api/records/8369275/files/pocv_soc.csv/content)
  Publisher/pinned MD5: `02e4d69ca3600f3f72a3c1ff86203ba4`.
- [pulse.mat](https://zenodo.org/api/records/8369275/files/pulse.mat/content)
  Publisher/pinned MD5: `035611fc459b22e26daf64423145fe01`.
- [pulse_neg_time.csv](https://zenodo.org/api/records/8369275/files/pulse_neg_time.csv/content)
  Publisher/pinned MD5: `ae99b9c526e6dec00e63c916dae18b25`.
- [pulse_neg_voltage.csv](https://zenodo.org/api/records/8369275/files/pulse_neg_voltage.csv/content)
  Publisher/pinned MD5: `4bd137cc3aaa4401f683b856e1083504`.
- [pulse_pos_time.csv](https://zenodo.org/api/records/8369275/files/pulse_pos_time.csv/content)
  Publisher/pinned MD5: `fa0ab49979a1c02b4de50748153bf516`.
- [pulse_pos_voltage.csv](https://zenodo.org/api/records/8369275/files/pulse_pos_voltage.csv/content)
  Publisher/pinned MD5: `dd6c6da30a3d738e0b884dfd4493c2ba`.

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ncr18650b-source-review.json)


## Missing items and limits

- No stated dataset reuse license identified.
- Whole-cell pseudo-OCV is not electrode OCP; no matched intrinsic D or kinetic-law records.
- No longitudinal ageing series, US06 or multi-rate continuous charge/discharge sweep reported in the reviewed source.
- Raw matrix dimensions, row identity across companion files and measured temperature/current traces remain unchecked.

## Evidence

- [Primary source 1](https://zenodo.org/records/8369275)
- [Primary source 2](https://zenodo.org/api/records/8369275)
- [Primary source 3](https://zenodo.org/records/8369275/export/json)
- [Primary source 4](https://doi.org/10.1016/j.jpowsour.2023.233677)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
