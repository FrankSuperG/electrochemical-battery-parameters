# Panasonic NCR18650B ageing and repeated reference tests (116 cells)

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `virtual-vehicle-ncr18650b-aging-2023`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NCA. 116 Panasonic NCR18650B 3.25 Ah cells in the Virtual Vehicle study. Source file stems are cell IDs; they do not identify cells in other NCR18650B studies.

[Open the original dataset](https://zenodo.org/records/7896429) · Version: `1.0.0 (fixed record 7896429)`

DOI: 10.5281/zenodo.7896429. Checked: 2026-10-23.

## Tests and channels

Types: constant_current, cccv, pulse, dynamic. Profiles: No named drive profile verified.

37 source-reported ageing load profiles plus repeated reference tests. RTP includes C/3 and 1C discharges, C/3 and C/2 CCCV charges and pulse sequences. Ageing-profile rates vary by cell; no complete same-state multi-rate characterization matrix is asserted.

Reported temperature labels / degC: [0, 5, 15, 20, 25, 30, 35, 40, 45]. These are source conditions, not measured temperature channels.

Reported time-series channels: voltage, current, temperature, charge_capacity, discharge_capacity, step_index.

Reported frequency-domain channels: Not verified / not applicable.

Fields are described in the author PDF; HDF5 groups, units, time axes and actual raw headers were not read. Initial RTPs use 5/15/25/35/45 degC; subsequent RTPs use 25 degC. Ageing-load temperatures differ (Table 2); source labels are not measured temperature extrema.

## Ageing data

**Yes (cycle, calendar)**. Source lists 116 per-cell H5 files, 37 ageing profiles and periodic RTP. PDF describes a 70%-capacity or project-end stopping rule. Zero-current storage arms in Table 2 support the calendar category; nonzero-current load profiles support cycle ageing. This is documented availability, not a full content audit.

[Ageing coverage evidence](https://zenodo.org/api/records/7896429/files/Galijatovic_2023_Ageing%20Data%20of%20Lithium-ion%20Panasonic%20NCR18650B%20Battery%20Cells.pdf/content). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `unmatched`. The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set.

Missing components: electrode_ocp, diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |
| diffusion | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |
| kinetics | `missing` / `missing` | None | The source identifies Panasonic NCR18650B, but no existing catalog OCP/D/kinetics record is verified for this model and study. The Kim2011 nominal NCA design has no verified NCR18650B identity. Same commercial model in other deposits does not establish a shared batch, specimen or transferable parameter set. Missing: No verified current-catalog parameter record for this model and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_established` | Author RTP and ageing arms use several currents, but no independently checked same-state continuous CC rate-sweep matrix exists. H5 paths are located; phase boundaries remain unread. |
| multi_rate_discharge | `not_established` | Author RTP and ageing arms use several currents, but no independently checked same-state continuous CC rate-sweep matrix exists. H5 paths are located; phase boundaries remain unread. |
| US06 | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |
| EIS | `not_located` | No file for this test class was identified in the inspected source listing/documentation; absence elsewhere is not established. |

## File locations

All 116 external HDF5 cell-file links and the source documentation PDF. One H5 contains multiple tests of one source cell; file count is not a test/cycle count. The 27.1 GB payload remains external.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `2_009.h5` | Panasonic NCR18650B / 2_009 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_009.h5/content) |
| `2_010.h5` | Panasonic NCR18650B / 2_010 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_010.h5/content) |
| `2_011.h5` | Panasonic NCR18650B / 2_011 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_011.h5/content) |
| `2_012.h5` | Panasonic NCR18650B / 2_012 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_012.h5/content) |
| `2_013.h5` | Panasonic NCR18650B / 2_013 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_013.h5/content) |
| `2_014.h5` | Panasonic NCR18650B / 2_014 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_014.h5/content) |
| `2_015.h5` | Panasonic NCR18650B / 2_015 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_015.h5/content) |
| `2_016.h5` | Panasonic NCR18650B / 2_016 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_016.h5/content) |
| `2_017.h5` | Panasonic NCR18650B / 2_017 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_017.h5/content) |
| `2_018.h5` | Panasonic NCR18650B / 2_018 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_018.h5/content) |
| `2_019.h5` | Panasonic NCR18650B / 2_019 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_019.h5/content) |
| `2_020.h5` | Panasonic NCR18650B / 2_020 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_020.h5/content) |
| `2_021.h5` | Panasonic NCR18650B / 2_021 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_021.h5/content) |
| `2_022.h5` | Panasonic NCR18650B / 2_022 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_022.h5/content) |
| `2_023.h5` | Panasonic NCR18650B / 2_023 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_023.h5/content) |
| `2_024.h5` | Panasonic NCR18650B / 2_024 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_024.h5/content) |
| `2_025.h5` | Panasonic NCR18650B / 2_025 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_025.h5/content) |
| `2_026.h5` | Panasonic NCR18650B / 2_026 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_026.h5/content) |
| `2_027.h5` | Panasonic NCR18650B / 2_027 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_027.h5/content) |
| `2_028.h5` | Panasonic NCR18650B / 2_028 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_028.h5/content) |
| `2_029.h5` | Panasonic NCR18650B / 2_029 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_029.h5/content) |
| `2_030.h5` | Panasonic NCR18650B / 2_030 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_030.h5/content) |
| `2_031.h5` | Panasonic NCR18650B / 2_031 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_031.h5/content) |
| `2_032.h5` | Panasonic NCR18650B / 2_032 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_032.h5/content) |
| `2_033.h5` | Panasonic NCR18650B / 2_033 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_033.h5/content) |
| `2_034.h5` | Panasonic NCR18650B / 2_034 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_034.h5/content) |
| `2_035.h5` | Panasonic NCR18650B / 2_035 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_035.h5/content) |
| `2_036.h5` | Panasonic NCR18650B / 2_036 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_036.h5/content) |
| `2_037.h5` | Panasonic NCR18650B / 2_037 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_037.h5/content) |
| `2_038.h5` | Panasonic NCR18650B / 2_038 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_038.h5/content) |
| `2_039.h5` | Panasonic NCR18650B / 2_039 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_039.h5/content) |
| `2_040.h5` | Panasonic NCR18650B / 2_040 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_040.h5/content) |
| `2_041.h5` | Panasonic NCR18650B / 2_041 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_041.h5/content) |
| `2_042.h5` | Panasonic NCR18650B / 2_042 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_042.h5/content) |
| `2_043.h5` | Panasonic NCR18650B / 2_043 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_043.h5/content) |
| `2_044.h5` | Panasonic NCR18650B / 2_044 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_044.h5/content) |
| `2_045.h5` | Panasonic NCR18650B / 2_045 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_045.h5/content) |
| `2_046.h5` | Panasonic NCR18650B / 2_046 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_046.h5/content) |
| `2_047.h5` | Panasonic NCR18650B / 2_047 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_047.h5/content) |
| `2_048.h5` | Panasonic NCR18650B / 2_048 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_048.h5/content) |
| `2_049.h5` | Panasonic NCR18650B / 2_049 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_049.h5/content) |
| `2_050.h5` | Panasonic NCR18650B / 2_050 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_050.h5/content) |
| `2_051.h5` | Panasonic NCR18650B / 2_051 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_051.h5/content) |
| `2_052.h5` | Panasonic NCR18650B / 2_052 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_052.h5/content) |
| `2_053.h5` | Panasonic NCR18650B / 2_053 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_053.h5/content) |
| `2_054.h5` | Panasonic NCR18650B / 2_054 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_054.h5/content) |
| `2_055.h5` | Panasonic NCR18650B / 2_055 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_055.h5/content) |
| `2_056.h5` | Panasonic NCR18650B / 2_056 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_056.h5/content) |
| `2_057.h5` | Panasonic NCR18650B / 2_057 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_057.h5/content) |
| `2_058.h5` | Panasonic NCR18650B / 2_058 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_058.h5/content) |
| `2_059.h5` | Panasonic NCR18650B / 2_059 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_059.h5/content) |
| `2_060.h5` | Panasonic NCR18650B / 2_060 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_060.h5/content) |
| `2_061.h5` | Panasonic NCR18650B / 2_061 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_061.h5/content) |
| `2_062.h5` | Panasonic NCR18650B / 2_062 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_062.h5/content) |
| `2_063.h5` | Panasonic NCR18650B / 2_063 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_063.h5/content) |
| `2_067.h5` | Panasonic NCR18650B / 2_067 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_067.h5/content) |
| `2_068.h5` | Panasonic NCR18650B / 2_068 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_068.h5/content) |
| `2_069.h5` | Panasonic NCR18650B / 2_069 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_069.h5/content) |
| `2_070.h5` | Panasonic NCR18650B / 2_070 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_070.h5/content) |
| `2_071.h5` | Panasonic NCR18650B / 2_071 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_071.h5/content) |
| `2_072.h5` | Panasonic NCR18650B / 2_072 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_072.h5/content) |
| `2_073.h5` | Panasonic NCR18650B / 2_073 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_073.h5/content) |
| `2_075.h5` | Panasonic NCR18650B / 2_075 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_075.h5/content) |
| `2_076.h5` | Panasonic NCR18650B / 2_076 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_076.h5/content) |
| `2_077.h5` | Panasonic NCR18650B / 2_077 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_077.h5/content) |
| `2_078.h5` | Panasonic NCR18650B / 2_078 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_078.h5/content) |
| `2_079.h5` | Panasonic NCR18650B / 2_079 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_079.h5/content) |
| `2_080.h5` | Panasonic NCR18650B / 2_080 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_080.h5/content) |
| `2_081.h5` | Panasonic NCR18650B / 2_081 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_081.h5/content) |
| `2_082.h5` | Panasonic NCR18650B / 2_082 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_082.h5/content) |
| `2_083.h5` | Panasonic NCR18650B / 2_083 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_083.h5/content) |
| `2_084.h5` | Panasonic NCR18650B / 2_084 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_084.h5/content) |
| `2_085.h5` | Panasonic NCR18650B / 2_085 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_085.h5/content) |
| `2_086.h5` | Panasonic NCR18650B / 2_086 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_086.h5/content) |
| `2_087.h5` | Panasonic NCR18650B / 2_087 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_087.h5/content) |
| `2_088.h5` | Panasonic NCR18650B / 2_088 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_088.h5/content) |
| `2_089.h5` | Panasonic NCR18650B / 2_089 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_089.h5/content) |
| `2_090.h5` | Panasonic NCR18650B / 2_090 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_090.h5/content) |
| `2_091.h5` | Panasonic NCR18650B / 2_091 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_091.h5/content) |
| `2_092.h5` | Panasonic NCR18650B / 2_092 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_092.h5/content) |
| `2_093.h5` | Panasonic NCR18650B / 2_093 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_093.h5/content) |
| `2_094.h5` | Panasonic NCR18650B / 2_094 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_094.h5/content) |
| `2_095.h5` | Panasonic NCR18650B / 2_095 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_095.h5/content) |
| `2_096.h5` | Panasonic NCR18650B / 2_096 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_096.h5/content) |
| `2_097.h5` | Panasonic NCR18650B / 2_097 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_097.h5/content) |
| `2_098.h5` | Panasonic NCR18650B / 2_098 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_098.h5/content) |
| `2_099.h5` | Panasonic NCR18650B / 2_099 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_099.h5/content) |
| `2_100.h5` | Panasonic NCR18650B / 2_100 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_100.h5/content) |
| `2_101.h5` | Panasonic NCR18650B / 2_101 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_101.h5/content) |
| `2_102.h5` | Panasonic NCR18650B / 2_102 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_102.h5/content) |
| `2_103.h5` | Panasonic NCR18650B / 2_103 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_103.h5/content) |
| `2_104.h5` | Panasonic NCR18650B / 2_104 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_104.h5/content) |
| `2_105.h5` | Panasonic NCR18650B / 2_105 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_105.h5/content) |
| `2_106.h5` | Panasonic NCR18650B / 2_106 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_106.h5/content) |
| `2_107.h5` | Panasonic NCR18650B / 2_107 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_107.h5/content) |
| `2_108.h5` | Panasonic NCR18650B / 2_108 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_108.h5/content) |
| `2_109.h5` | Panasonic NCR18650B / 2_109 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_109.h5/content) |
| `2_110.h5` | Panasonic NCR18650B / 2_110 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_110.h5/content) |
| `2_111.h5` | Panasonic NCR18650B / 2_111 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_111.h5/content) |
| `2_112.h5` | Panasonic NCR18650B / 2_112 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_112.h5/content) |
| `2_113.h5` | Panasonic NCR18650B / 2_113 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_113.h5/content) |
| `2_114.h5` | Panasonic NCR18650B / 2_114 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_114.h5/content) |
| `2_115.h5` | Panasonic NCR18650B / 2_115 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_115.h5/content) |
| `2_116.h5` | Panasonic NCR18650B / 2_116 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_116.h5/content) |
| `2_117.h5` | Panasonic NCR18650B / 2_117 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_117.h5/content) |
| `2_118.h5` | Panasonic NCR18650B / 2_118 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_118.h5/content) |
| `2_119.h5` | Panasonic NCR18650B / 2_119 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_119.h5/content) |
| `2_120.h5` | Panasonic NCR18650B / 2_120 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_120.h5/content) |
| `2_121.h5` | Panasonic NCR18650B / 2_121 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_121.h5/content) |
| `2_123.h5` | Panasonic NCR18650B / 2_123 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_123.h5/content) |
| `2_127.h5` | Panasonic NCR18650B / 2_127 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_127.h5/content) |
| `2_128.h5` | Panasonic NCR18650B / 2_128 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_128.h5/content) |
| `2_129.h5` | Panasonic NCR18650B / 2_129 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_129.h5/content) |
| `2_130.h5` | Panasonic NCR18650B / 2_130 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_130.h5/content) |
| `2_131.h5` | Panasonic NCR18650B / 2_131 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_131.h5/content) |
| `2_132.h5` | Panasonic NCR18650B / 2_132 | constant_current, cccv, pulse;  | Temperature unknown | `source_documentation`; content `not_read` | [Open source file](https://zenodo.org/api/records/7896429/files/2_132.h5/content) |
| `Galijatovic_2023_Ageing Data of Lithium-ion Panasonic NCR18650B Battery Cells.pdf` | Panasonic NCR18650B / No sample ID | ;  | Temperature unknown | `source_listing`; content `documentation_reviewed` | [Open source file](https://zenodo.org/api/records/7896429/files/Galijatovic_2023_Ageing%20Data%20of%20Lithium-ion%20Panasonic%20NCR18650B%20Battery%20Cells.pdf/content) |

File notes:

- `2_009.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_010.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_011.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_012.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_013.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_014.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_015.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_016.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_017.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_018.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_019.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_020.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_021.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_022.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_023.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_024.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_025.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_026.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_027.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_028.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_029.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_030.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_031.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_032.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_033.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_034.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_035.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_036.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_037.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_038.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_039.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_040.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_041.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_042.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_043.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_044.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_045.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_046.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_047.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_048.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_049.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_050.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_051.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_052.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_053.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_054.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_055.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_056.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_057.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_058.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_059.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_060.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_061.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_062.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_063.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_067.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_068.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_069.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_070.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_071.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_072.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_073.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_075.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_076.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_077.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_078.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_079.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_080.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_081.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_082.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_083.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_084.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_085.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_086.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_087.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_088.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_089.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_090.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_091.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_092.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_093.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_094.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_095.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_096.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_097.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_098.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_099.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_100.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_101.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_102.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_103.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_104.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_105.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_106.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_107.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_108.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_109.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_110.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_111.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_112.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_113.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_114.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_115.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_116.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_117.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_118.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_119.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_120.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_121.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_123.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_127.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_128.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_129.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_130.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_131.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `2_132.h5`: Per-cell ageing/reference container, according to source documentation. Actual H5 groups, units, phases and profile-to-cell assignment were not read; no per-file rate/temperature is assigned. Only the common source-documented RTP types are tagged; a dynamic ageing profile is not assigned to every cell, including storage arms.
- `Galijatovic_2023_Ageing Data of Lithium-ion Panasonic NCR18650B Battery Cells.pdf`: Author protocol/field documentation, not an experimental trace.

## Reuse and access

License: **CC-BY-4.0**. [Source terms](https://zenodo.org/api/records/7896429). CC BY 4.0 is stated in Zenodo metadata/export. Retain author attribution and this DOI. Publisher file MD5 values identify external objects; no HDF5 checksum independently verified or data redistributed.

Review level: `source_file_listing`. Complete Zenodo file metadata (116 H5 plus one PDF) and author PDF text reviewed; Table 2 and RTP page visually checked. No H5 observations read. Experiment ends at 70% remaining capacity or project end, so not every cell is certified to reach EOL.

- [2_009.h5](https://zenodo.org/api/records/7896429/files/2_009.h5/content)
  Publisher/pinned MD5: `8408795eba16a5fcc9e4c1fad936b073`.
- [2_010.h5](https://zenodo.org/api/records/7896429/files/2_010.h5/content)
  Publisher/pinned MD5: `451ece35f174aa3e5cc777da2ad3e96b`.
- [2_011.h5](https://zenodo.org/api/records/7896429/files/2_011.h5/content)
  Publisher/pinned MD5: `45aabf56c35af916ff35593dd9a60ddb`.
- [2_012.h5](https://zenodo.org/api/records/7896429/files/2_012.h5/content)
  Publisher/pinned MD5: `f77cbe28dea3c408efc24717178eed38`.
- [2_013.h5](https://zenodo.org/api/records/7896429/files/2_013.h5/content)
  Publisher/pinned MD5: `7d0763820d0079887a6067e3c8164eac`.
- [2_014.h5](https://zenodo.org/api/records/7896429/files/2_014.h5/content)
  Publisher/pinned MD5: `3078d4f47f113386f91ba976635bdf65`.
- [2_015.h5](https://zenodo.org/api/records/7896429/files/2_015.h5/content)
  Publisher/pinned MD5: `841058f75156e9f55a280d4a65ebfb13`.
- [2_016.h5](https://zenodo.org/api/records/7896429/files/2_016.h5/content)
  Publisher/pinned MD5: `a873824fffa9a4c9e1c355f18a986a0f`.
- [2_017.h5](https://zenodo.org/api/records/7896429/files/2_017.h5/content)
  Publisher/pinned MD5: `e3a2c9310015868119e4c7063a9c28e0`.
- [2_018.h5](https://zenodo.org/api/records/7896429/files/2_018.h5/content)
  Publisher/pinned MD5: `cdcead5aa854647a7fa30e5f52d6b0ac`.
- [2_019.h5](https://zenodo.org/api/records/7896429/files/2_019.h5/content)
  Publisher/pinned MD5: `3351b6537bbf13435df9696d050524fa`.
- [2_020.h5](https://zenodo.org/api/records/7896429/files/2_020.h5/content)
  Publisher/pinned MD5: `002d4e56787f66e714402c6ae38fb85f`.
- [2_021.h5](https://zenodo.org/api/records/7896429/files/2_021.h5/content)
  Publisher/pinned MD5: `f82671ae13ed1895ad610ce0f11139a0`.
- [2_022.h5](https://zenodo.org/api/records/7896429/files/2_022.h5/content)
  Publisher/pinned MD5: `d060424713034a2bd8889ffc56f3f1cf`.
- [2_023.h5](https://zenodo.org/api/records/7896429/files/2_023.h5/content)
  Publisher/pinned MD5: `9c0a821bf33e8f159e2a8d96424b0183`.
- [2_024.h5](https://zenodo.org/api/records/7896429/files/2_024.h5/content)
  Publisher/pinned MD5: `d2bf8754bd2b66cf3edf6662cc7f41fa`.
- [2_025.h5](https://zenodo.org/api/records/7896429/files/2_025.h5/content)
  Publisher/pinned MD5: `6ba246455f1d5daaa5b5d7c68a424dd2`.
- [2_026.h5](https://zenodo.org/api/records/7896429/files/2_026.h5/content)
  Publisher/pinned MD5: `426480b6e2f187f9713033734c1a037b`.
- [2_027.h5](https://zenodo.org/api/records/7896429/files/2_027.h5/content)
  Publisher/pinned MD5: `b48c5badf1e0733fbb115745a3d76713`.
- [2_028.h5](https://zenodo.org/api/records/7896429/files/2_028.h5/content)
  Publisher/pinned MD5: `d7348791336783dcaee88190541932cf`.
- [2_029.h5](https://zenodo.org/api/records/7896429/files/2_029.h5/content)
  Publisher/pinned MD5: `d6f0d6eb94ca33e671738ece713d5ee3`.
- [2_030.h5](https://zenodo.org/api/records/7896429/files/2_030.h5/content)
  Publisher/pinned MD5: `614f4d2d8684e70c54fd776636fd194b`.
- [2_031.h5](https://zenodo.org/api/records/7896429/files/2_031.h5/content)
  Publisher/pinned MD5: `881536cea22e31c7705cacf59c2dae78`.
- [2_032.h5](https://zenodo.org/api/records/7896429/files/2_032.h5/content)
  Publisher/pinned MD5: `b5d66bdeb85e708f9239d98e6621ed3e`.
- [2_033.h5](https://zenodo.org/api/records/7896429/files/2_033.h5/content)
  Publisher/pinned MD5: `0f1d2c913aa94c771aada28232549268`.
- [2_034.h5](https://zenodo.org/api/records/7896429/files/2_034.h5/content)
  Publisher/pinned MD5: `fbf381e843ab98ec60d9a8c65d52eb61`.
- [2_035.h5](https://zenodo.org/api/records/7896429/files/2_035.h5/content)
  Publisher/pinned MD5: `270805d5114142aa94f570687b941476`.
- [2_036.h5](https://zenodo.org/api/records/7896429/files/2_036.h5/content)
  Publisher/pinned MD5: `07428386cf463ee8f49aad5000f9abe6`.
- [2_037.h5](https://zenodo.org/api/records/7896429/files/2_037.h5/content)
  Publisher/pinned MD5: `942cb7b4d7b35b23c9e0bd585e6e498a`.
- [2_038.h5](https://zenodo.org/api/records/7896429/files/2_038.h5/content)
  Publisher/pinned MD5: `36c13fc8b1df8e11cf1a403eb36642eb`.
- [2_039.h5](https://zenodo.org/api/records/7896429/files/2_039.h5/content)
  Publisher/pinned MD5: `77e0efde013d56f81c5d2499641b3007`.
- [2_040.h5](https://zenodo.org/api/records/7896429/files/2_040.h5/content)
  Publisher/pinned MD5: `22ea19578f05ad665484340907d74f28`.
- [2_041.h5](https://zenodo.org/api/records/7896429/files/2_041.h5/content)
  Publisher/pinned MD5: `e4ca461fe5f6f358d6428bed0caea2e3`.
- [2_042.h5](https://zenodo.org/api/records/7896429/files/2_042.h5/content)
  Publisher/pinned MD5: `a7c956c402f6622f62c6942ccdca7a70`.
- [2_043.h5](https://zenodo.org/api/records/7896429/files/2_043.h5/content)
  Publisher/pinned MD5: `ae524aae22c9bfa3fa910c73a36d2388`.
- [2_044.h5](https://zenodo.org/api/records/7896429/files/2_044.h5/content)
  Publisher/pinned MD5: `1c01466adf264171c28d60f949382c02`.
- [2_045.h5](https://zenodo.org/api/records/7896429/files/2_045.h5/content)
  Publisher/pinned MD5: `c7e435c0cab34f88c825f0e82a424a18`.
- [2_046.h5](https://zenodo.org/api/records/7896429/files/2_046.h5/content)
  Publisher/pinned MD5: `0a6a30a5ac593f39b3adc0653a5df079`.
- [2_047.h5](https://zenodo.org/api/records/7896429/files/2_047.h5/content)
  Publisher/pinned MD5: `c82012a802ac5a625121f9782dd43240`.
- [2_048.h5](https://zenodo.org/api/records/7896429/files/2_048.h5/content)
  Publisher/pinned MD5: `5ac00e59e5bd1953ff4fcc76dc4f3234`.
- [2_049.h5](https://zenodo.org/api/records/7896429/files/2_049.h5/content)
  Publisher/pinned MD5: `deda0e693146bec459b272ab9410b53e`.
- [2_050.h5](https://zenodo.org/api/records/7896429/files/2_050.h5/content)
  Publisher/pinned MD5: `133cfc34520b8cead2c876a596ffb078`.
- [2_051.h5](https://zenodo.org/api/records/7896429/files/2_051.h5/content)
  Publisher/pinned MD5: `67177faa8f8b1bbfcf5883aa956e0b4b`.
- [2_052.h5](https://zenodo.org/api/records/7896429/files/2_052.h5/content)
  Publisher/pinned MD5: `b3bcba69b7285400de52c0d1a3c6a1f9`.
- [2_053.h5](https://zenodo.org/api/records/7896429/files/2_053.h5/content)
  Publisher/pinned MD5: `3afebf624e84ba3652d47c56ef9049be`.
- [2_054.h5](https://zenodo.org/api/records/7896429/files/2_054.h5/content)
  Publisher/pinned MD5: `3ce707be336ca85433bda1b571f410b8`.
- [2_055.h5](https://zenodo.org/api/records/7896429/files/2_055.h5/content)
  Publisher/pinned MD5: `cc25f0167085996c34944884781b8f36`.
- [2_056.h5](https://zenodo.org/api/records/7896429/files/2_056.h5/content)
  Publisher/pinned MD5: `0493bc7639bdc35bb1c1caa94d4cde6a`.
- [2_057.h5](https://zenodo.org/api/records/7896429/files/2_057.h5/content)
  Publisher/pinned MD5: `9374790e6444369ba1f439800ee7856a`.
- [2_058.h5](https://zenodo.org/api/records/7896429/files/2_058.h5/content)
  Publisher/pinned MD5: `5e548e0188f7c71d193ae572fd58c201`.
- [2_059.h5](https://zenodo.org/api/records/7896429/files/2_059.h5/content)
  Publisher/pinned MD5: `663d3fc69832c3af2d59c49bc6dfe6c1`.
- [2_060.h5](https://zenodo.org/api/records/7896429/files/2_060.h5/content)
  Publisher/pinned MD5: `09549ba5d04c4b8f6a96b7fc8468d381`.
- [2_061.h5](https://zenodo.org/api/records/7896429/files/2_061.h5/content)
  Publisher/pinned MD5: `8c6e136df25689456d7df4d6401f67d8`.
- [2_062.h5](https://zenodo.org/api/records/7896429/files/2_062.h5/content)
  Publisher/pinned MD5: `dafa81fdc8b3cf289b5729e0fd1f62b9`.
- [2_063.h5](https://zenodo.org/api/records/7896429/files/2_063.h5/content)
  Publisher/pinned MD5: `fef440f475afa7005528a68de3f456c7`.
- [2_067.h5](https://zenodo.org/api/records/7896429/files/2_067.h5/content)
  Publisher/pinned MD5: `4091f1124bf5854c15a0e82ec1ae2be3`.
- [2_068.h5](https://zenodo.org/api/records/7896429/files/2_068.h5/content)
  Publisher/pinned MD5: `1d1ff658ba902b368e700adf6c84d0b7`.
- [2_069.h5](https://zenodo.org/api/records/7896429/files/2_069.h5/content)
  Publisher/pinned MD5: `7381665b985379d31920f911ee0eddd8`.
- [2_070.h5](https://zenodo.org/api/records/7896429/files/2_070.h5/content)
  Publisher/pinned MD5: `5c7c1b673fd009af705b2d61971b563c`.
- [2_071.h5](https://zenodo.org/api/records/7896429/files/2_071.h5/content)
  Publisher/pinned MD5: `22530a97918a258057f65742c5e06d3a`.
- [2_072.h5](https://zenodo.org/api/records/7896429/files/2_072.h5/content)
  Publisher/pinned MD5: `0d2d6a3697a09fdf7fef7e938daaca40`.
- [2_073.h5](https://zenodo.org/api/records/7896429/files/2_073.h5/content)
  Publisher/pinned MD5: `94b72e987c3c619920799cb81362ccb0`.
- [2_075.h5](https://zenodo.org/api/records/7896429/files/2_075.h5/content)
  Publisher/pinned MD5: `e81c370ff2e7263a021d7ed62c9f7262`.
- [2_076.h5](https://zenodo.org/api/records/7896429/files/2_076.h5/content)
  Publisher/pinned MD5: `d2fbd7d23a864b6721ac8828ad5a0473`.
- [2_077.h5](https://zenodo.org/api/records/7896429/files/2_077.h5/content)
  Publisher/pinned MD5: `83b52ea0b08ccd1a5811370dcd8ea0ff`.
- [2_078.h5](https://zenodo.org/api/records/7896429/files/2_078.h5/content)
  Publisher/pinned MD5: `ae2e5f751b149178787e52383481fdfa`.
- [2_079.h5](https://zenodo.org/api/records/7896429/files/2_079.h5/content)
  Publisher/pinned MD5: `5cbd1881f7442b9d140b0e2c933bbd83`.
- [2_080.h5](https://zenodo.org/api/records/7896429/files/2_080.h5/content)
  Publisher/pinned MD5: `5d1584451febe8fb33f4d310bc4ae34f`.
- [2_081.h5](https://zenodo.org/api/records/7896429/files/2_081.h5/content)
  Publisher/pinned MD5: `9f6b7f14ff8f7f85317e905381b331d0`.
- [2_082.h5](https://zenodo.org/api/records/7896429/files/2_082.h5/content)
  Publisher/pinned MD5: `2452735e6019a8ab5a44d6e6aaafaf5a`.
- [2_083.h5](https://zenodo.org/api/records/7896429/files/2_083.h5/content)
  Publisher/pinned MD5: `a81cc96be67e947b3ba7b751cdc686b3`.
- [2_084.h5](https://zenodo.org/api/records/7896429/files/2_084.h5/content)
  Publisher/pinned MD5: `568b2df7bd852c8dc9088d22b10c75c6`.
- [2_085.h5](https://zenodo.org/api/records/7896429/files/2_085.h5/content)
  Publisher/pinned MD5: `1e562324f2d77a4921b596350b59dd39`.
- [2_086.h5](https://zenodo.org/api/records/7896429/files/2_086.h5/content)
  Publisher/pinned MD5: `fbf36c329f5f59d4b7f285f87bc12816`.
- [2_087.h5](https://zenodo.org/api/records/7896429/files/2_087.h5/content)
  Publisher/pinned MD5: `c8acd38980e9bb38dcf91929a19924e8`.
- [2_088.h5](https://zenodo.org/api/records/7896429/files/2_088.h5/content)
  Publisher/pinned MD5: `d6c6c050ecbb457e6eadcc80e63dfc52`.
- [2_089.h5](https://zenodo.org/api/records/7896429/files/2_089.h5/content)
  Publisher/pinned MD5: `6512d89385a6bbb127d1c61e546a5acf`.
- [2_090.h5](https://zenodo.org/api/records/7896429/files/2_090.h5/content)
  Publisher/pinned MD5: `8d79b4c3173d1160996cb56b3bcc662a`.
- [2_091.h5](https://zenodo.org/api/records/7896429/files/2_091.h5/content)
  Publisher/pinned MD5: `3e09c9355b5957daf069932f111c07d1`.
- [2_092.h5](https://zenodo.org/api/records/7896429/files/2_092.h5/content)
  Publisher/pinned MD5: `edaf982b049de1484fce61471412b7be`.
- [2_093.h5](https://zenodo.org/api/records/7896429/files/2_093.h5/content)
  Publisher/pinned MD5: `e3c39e4b1ee789691f80d9e15c9b6610`.
- [2_094.h5](https://zenodo.org/api/records/7896429/files/2_094.h5/content)
  Publisher/pinned MD5: `7ad4231a42ed404716d37681f870554f`.
- [2_095.h5](https://zenodo.org/api/records/7896429/files/2_095.h5/content)
  Publisher/pinned MD5: `83b6aa6466e5cb917f5e9bbdfd720020`.
- [2_096.h5](https://zenodo.org/api/records/7896429/files/2_096.h5/content)
  Publisher/pinned MD5: `6b7e5719a5e60ed2837c161208f2c9a3`.
- [2_097.h5](https://zenodo.org/api/records/7896429/files/2_097.h5/content)
  Publisher/pinned MD5: `8e682d827ac9c75e0d5018a8dbbc0ba0`.
- [2_098.h5](https://zenodo.org/api/records/7896429/files/2_098.h5/content)
  Publisher/pinned MD5: `4daeb89257d6f5af52aecb8305031440`.
- [2_099.h5](https://zenodo.org/api/records/7896429/files/2_099.h5/content)
  Publisher/pinned MD5: `f07c58bee428a94a496b66f05e029cbe`.
- [2_100.h5](https://zenodo.org/api/records/7896429/files/2_100.h5/content)
  Publisher/pinned MD5: `56b427593b99170cfe5a87194278ba59`.
- [2_101.h5](https://zenodo.org/api/records/7896429/files/2_101.h5/content)
  Publisher/pinned MD5: `33119b6381e62f75428bc2d5016ee4ed`.
- [2_102.h5](https://zenodo.org/api/records/7896429/files/2_102.h5/content)
  Publisher/pinned MD5: `c826f8f1a186d7a866a44ab202f9205b`.
- [2_103.h5](https://zenodo.org/api/records/7896429/files/2_103.h5/content)
  Publisher/pinned MD5: `f6f9fd3c02232eb18afac37dfe349b5d`.
- [2_104.h5](https://zenodo.org/api/records/7896429/files/2_104.h5/content)
  Publisher/pinned MD5: `177e018263668c2f09f408d97a3a3961`.
- [2_105.h5](https://zenodo.org/api/records/7896429/files/2_105.h5/content)
  Publisher/pinned MD5: `0f40daf9a02a5c253075bc08ba3ddb5f`.
- [2_106.h5](https://zenodo.org/api/records/7896429/files/2_106.h5/content)
  Publisher/pinned MD5: `d2c2ea7bd13f4a4aaf962bd551836d64`.
- [2_107.h5](https://zenodo.org/api/records/7896429/files/2_107.h5/content)
  Publisher/pinned MD5: `dd35e4d8201ae61eddb99c5f22362fc5`.
- [2_108.h5](https://zenodo.org/api/records/7896429/files/2_108.h5/content)
  Publisher/pinned MD5: `7eddc63b28e6b572ecefe9550149cec8`.
- [2_109.h5](https://zenodo.org/api/records/7896429/files/2_109.h5/content)
  Publisher/pinned MD5: `49a72cb7fce3ad8ffc15b320f57e7a59`.
- [2_110.h5](https://zenodo.org/api/records/7896429/files/2_110.h5/content)
  Publisher/pinned MD5: `81d7488cc6fa982a99f3b30e0f6d4f12`.
- [2_111.h5](https://zenodo.org/api/records/7896429/files/2_111.h5/content)
  Publisher/pinned MD5: `5f64533df76116e5ed6f30a624771ef4`.
- [2_112.h5](https://zenodo.org/api/records/7896429/files/2_112.h5/content)
  Publisher/pinned MD5: `e74f5ffdb17bc20a0a7f2f75f7296bac`.
- [2_113.h5](https://zenodo.org/api/records/7896429/files/2_113.h5/content)
  Publisher/pinned MD5: `caebd810a65d350028a68cc7ec2c4cb9`.
- [2_114.h5](https://zenodo.org/api/records/7896429/files/2_114.h5/content)
  Publisher/pinned MD5: `22005d66788e7999e3875b7e781cdcca`.
- [2_115.h5](https://zenodo.org/api/records/7896429/files/2_115.h5/content)
  Publisher/pinned MD5: `84a179af05d984be1b315b1df851e659`.
- [2_116.h5](https://zenodo.org/api/records/7896429/files/2_116.h5/content)
  Publisher/pinned MD5: `ea4743d64510f1a4c244c2af310fa354`.
- [2_117.h5](https://zenodo.org/api/records/7896429/files/2_117.h5/content)
  Publisher/pinned MD5: `9f958cf7486356f52f23b49235f9c832`.
- [2_118.h5](https://zenodo.org/api/records/7896429/files/2_118.h5/content)
  Publisher/pinned MD5: `a0be4409f4ba57ec383f914178bdc70f`.
- [2_119.h5](https://zenodo.org/api/records/7896429/files/2_119.h5/content)
  Publisher/pinned MD5: `2cec6cbfee3629992d85954e664a1387`.
- [2_120.h5](https://zenodo.org/api/records/7896429/files/2_120.h5/content)
  Publisher/pinned MD5: `ea935f85f2802cd5d7fbb08613296e06`.
- [2_121.h5](https://zenodo.org/api/records/7896429/files/2_121.h5/content)
  Publisher/pinned MD5: `d0a9a0842764bbb25274a0d008714a41`.
- [2_123.h5](https://zenodo.org/api/records/7896429/files/2_123.h5/content)
  Publisher/pinned MD5: `ff86111736657c725fd8dd06919ccea3`.
- [2_127.h5](https://zenodo.org/api/records/7896429/files/2_127.h5/content)
  Publisher/pinned MD5: `0aea8f54115ad54e8eed0d92b3598939`.
- [2_128.h5](https://zenodo.org/api/records/7896429/files/2_128.h5/content)
  Publisher/pinned MD5: `cc7354a8b4496e2226fe50ab98768523`.
- [2_129.h5](https://zenodo.org/api/records/7896429/files/2_129.h5/content)
  Publisher/pinned MD5: `2f16edc08cff75e5c468c1b8686405c3`.
- [2_130.h5](https://zenodo.org/api/records/7896429/files/2_130.h5/content)
  Publisher/pinned MD5: `ae7ca9db201423aed6bb92feb6be5c7a`.
- [2_131.h5](https://zenodo.org/api/records/7896429/files/2_131.h5/content)
  Publisher/pinned MD5: `1d24444f235e522b8a409679a3739589`.
- [2_132.h5](https://zenodo.org/api/records/7896429/files/2_132.h5/content)
  Publisher/pinned MD5: `7d567a0ee194347e7236104db560fa2d`.
- [Galijatovic_2023_Ageing Data of Lithium-ion Panasonic NCR18650B Battery Cells.pdf](https://zenodo.org/api/records/7896429/files/Galijatovic_2023_Ageing%20Data%20of%20Lithium-ion%20Panasonic%20NCR18650B%20Battery%20Cells.pdf/content)
  Publisher/pinned MD5: `9ff2e0a534cd5f9b1b3ca54b1701c4dd`.

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ncr18650b-source-review.json)


## Missing items and limits

- No electrode OCP, intrinsic diffusion or kinetic-law parameter association to the current catalog.
- No H5 content inspection: group names, time axes, units, column coverage, cycle counts and payload checksums are not verified.
- Table 2 reuses cell IDs 2_013/2_014/2_015 across distinct profile rows (L35/L26 and L205); L221 prints 2_57 rather than the listed 2_057.h5. No authoritative per-cell profile map is imported or silently corrected.
- The stopping rule permits project-end censoring; do not label every cell as measured through EOL.
- No named US06 or EIS measurement file identified. Pulse resistance is not EIS.
- The other NCR18650B deposits share a commercial model only, not a verified study, batch, state of health or specimen.

## Evidence

- [Primary source 1](https://zenodo.org/records/7896429)
- [Primary source 2](https://zenodo.org/api/records/7896429)
- [Primary source 3](https://zenodo.org/records/7896429/export/json)
- [Primary source 4](https://zenodo.org/api/records/7896429/files/Galijatovic_2023_Ageing%20Data%20of%20Lithium-ion%20Panasonic%20NCR18650B%20Battery%20Cells.pdf/content)
- [Primary source 5](https://doi.org/10.1109/IECON48115.2021.9589655)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
