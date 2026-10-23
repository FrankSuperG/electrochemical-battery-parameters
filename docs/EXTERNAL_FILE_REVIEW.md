# External file and parameter-link review — 2026-10-23

[File locator CSV](../data/full-cell/files.csv) · [Seven source records](../data/full-cell/datasets.json) · [Archive directory evidence](../src/ebp/data/evidence/external-archive-directory-review.json)

This review checks the seven existing external records. The unit is an external
source path or archive member, qualified by dataset ID; repeated basenames such
as `59294.mat` are different records in different protocol folders. Selected
locators are not an exhaustive test matrix, independent-cell count or proof of
measurement content. No new experimental observation files are packaged.

## Evidence ledger

| Source and version | Observed result | Limits / confidence |
|---|---|---|
| [UCCS A123, v1](https://data.mendeley.com/datasets/p8kf893yv3/1) | Normal source UI lists five CCCV MAT files spanning 1/2/3/4C, UDDS P25/P35, a pulse MAT and an OCV representative; all have stable per-file UUID links. | High confidence in paths and labels; no MAT/XLSX content read. Two 1C variants and the repeated A002 label do not establish independent cells or exact repeat processing. |
| [CALCE Samsung 20R](https://calce.umd.edu/data) | OCV and three-temperature dynamic ZIP links extracted from the primary page. The 25 degC US06 ZIP directory contains two XLS members with 50SOC/80SOC labels. | High confidence in links and representative member names. Other archives/headers remain unchecked; OCV SP1/SP3 and dynamic SP2 are distinct source labels. No standard reuse license identified. |
| [CALCE A123](https://calce.umd.edu/data) | Primary source table links eight dynamic and eight OCV ZIPs. The 25 degC dynamic ZIP contains A1-007 and A1-008 XLSX filenames naming DST-US06-FUDS. | US06 is supported by archive-member filenames although page prose mentions only DST/FUDS. Workbook phase boundaries, exact commercial part and OCV specimen mapping remain unresolved. |
| [CALB, v2](https://data.mendeley.com/datasets/ycx459r5c3/2), [paper](https://doi.org/10.1016/j.dib.2025.111301) | Raw/Processed branches and 10/25/40 degC directories observed. At 25 degC, processed CC/US06/EIS and representative 59294 raw workbooks have exact source-listed download UUIDs. US06/EIS folders list eleven cell labels. | Only selected 59294 locators are retained, not a certified eleven-cell × three-temperature matrix. Generic raw dynamic workbooks do not establish where each drive-cycle phase begins. EIS-labelled raw XLSX columns were not checked. |
| [Malaya, v1](https://data.mendeley.com/datasets/29kw38kzwj/1) | Primary UI exposes a single `Battery Test Data.rar` and its stable UUID link. | Container found, inner per-model paths unverified. Direct automated header access returned HTTP 403. Dataset collective LFP/NCA/NMC and US06 declarations remain dataset-level; no exact NCA/US06 file is claimed. |
| [LFP EIS, v1](https://doi.org/10.6084/m9.figshare.23736582.v1), [official metadata](https://api.figshare.com/v2/articles/23736582) | Complete RAR5 directory: 539 entries, including 461 files: 440 EIS CSV, 11 capacity CSV and 10 BMP. EIS paths cover B01–B11, Test_1/Test_2 and twenty SOC labels (5–100%). Filenames include IFR14500. | Header CRCs checked; packed data skipped in the successful scan. No CSV content, frequency grid, units, temperature, measured capacity or full archive MD5 independently checked. IFR14500 is not a unique manufacturer part. |
| [M50LT pinned author source](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068), [prior source audit](HALLEMANS2025.md) | Existing author MAT/hash evidence connects measured whole-cell EIS and fitted-group vector; drive-cycle MAT is also located. | Same model/study. OCP rights, intrinsic D/k and serialized-specimen mapping remain unresolved. No source evidence names the drive cycle US06. |

## Parameter associations

Only M50LT has a verified current-catalog parameter association:

- Diffusion: `hallemans2025-tau-d-p` and `hallemans2025-tau-d-n`, in seconds,
  retain the particle diffusion groups R²/D. They are not intrinsic diffusivities.
- Kinetics: `hallemans2025-tau-ct-p`, `hallemans2025-tau-ct-n`,
  `hallemans2025-c-p` and `hallemans2025-c-n` retain grouped charge-transfer
  times and capacitances. They are not independent exchange-current laws or k.
- OCP: no imported electrode OCP; third-party reuse rights remain unresolved.

The six other sources remain unmatched to catalog OCP/D/kinetics. UCCS 26650 m1b
is distinct from catalog 18650M1A, AMP20 and 9 Ah cells. CALCE A123 has unresolved
part identity; Samsung 20R is not an LG cell. CALB 58 Ah is not a Mohtat/LG pouch
or cylinder. Malaya Panasonic NCR18650B does not identify the Kim2011 nominal
design, and its archive matrix is uninspected. The EIS source lacks a verified
manufacturer/model. No join was strengthened using chemistry/capacity alone.

## Inspectable methods

The [optional inspector](../scripts/inspect_external_archives.py) reads only ZIP
central-directory or RAR5 header ranges, refuses a full HTTP 200 download in
place of the requested range, checks RAR header CRCs and skips compressed data
without extracting observations. Its output contains names, sizes and method
statistics only. Encryption/split archives and oversized headers fail explicitly.
It is never run automatically by normal catalog, viewer, reconstruction or CI.

Successful directory-scan evidence records 270 bytes for the Samsung 25 degC
ZIP, 413 bytes for the A123 25 degC ZIP, and 61,632 bytes for the EIS RAR headers.
These are statistics for those recorded scans, not totals for all access probes.
They do not verify full payload checksums. The RAR format reference is the
[official RAR5 specification](https://www.rarlab.com/technote.htm).

```bash
python scripts/inspect_external_archives.py \
  https://web.calce.umd.edu/batteries/data/SP2_25C_US06.zip \
  --kind zip --output .cache/samsung-us06-directory.json
python scripts/inspect_external_archives.py \
  https://ndownloader.figshare.com/files/41673360 \
  --kind rar5 --output .cache/lfp-eis-directory.json
```

Mendeley directories were inspected through the normal public UI. Automated
API/header 403 responses were retained as access limits, not treated as evidence
that listed files are absent. No sign-in, CAPTCHA solving or raw archive download
was used. Per-file download health is not certified by a directory listing.

The persisted directory metadata are checked against each curated archive-member
path and size. Component IDs are checked against current catalog records, cell
joins and parameter categories; diffusion time scales cannot be labeled intrinsic
D. File-path uniqueness uses dataset plus full source path, not basename.

`ebp datasets --files --profile US06` uses file-level tags. It deliberately omits
uninspected NCA-specific files in the Malaya container while dataset-level search
still returns that source. This distinction preserves the outstanding review
rather than promoting a general description into a per-model observation.
