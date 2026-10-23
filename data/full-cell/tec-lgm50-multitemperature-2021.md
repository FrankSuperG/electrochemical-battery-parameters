# LG M50 multi-temperature discharge with explicitly reused Chen2020 electrode OCP

[Full-cell index](README.md) · [Usage and review notes](../../docs/FULL_CELL_DATASETS.md)

Dataset link ID: `tec-lgm50-multitemperature-2021`. Storage: **external link**. This entry is not an imported measurement file.

Material families: NMC. LG M50 21700 NMC811/graphite-SiOx. Author TEC2021 paper explicitly reuses Chen2020 electrode OCP; cells labelled 781–796 are not joined to Chen2020 specimen serials.

[Open the original dataset](https://zenodo.org/records/4864437) · Version: `v1.0; 978f8c38005892d98f1204b71422f6ff64c32acd`

DOI: 10.5281/zenodo.4864437. Checked: 2026-10-23.

## Electrode OCP anchor

**Explicitly reused catalog expression**. Primary TEC2021 paper Table 1 attributes the LG M50 electrode OCP to Chen2020. Two existing catalog expressions therefore provide an explicit reused OCP anchor; full-cell experiments are a different study, without shared serials. This does not associate ORegan2022 diffusion/kinetic tables as same-study TEC measurements.

Reported half-cell temperature labels / degC: Not independently verified. Full-cell temperatures below do not establish half-cell OCP temperature coverage.

Source paths: `PyBaMM/v25.4.2/Chen2020.py`

OCP evidence: [Source 1](https://wrap.warwick.ac.uk/id/eprint/152012/7/WRAP-Systematic-derivation-validation-reduced-thermal-electrochemical-2021.pdf) · [Source 2](https://raw.githubusercontent.com/pybamm-team/PyBaMM/v25.4.2/src/pybamm/input/parameters/lithium_ion/Chen2020.py)

## Tests and channels

Types: constant_current. Profiles: No named drive profile verified.

Four source-listed discharge rates 0.1C, 0.5C, 1C and 2C, four cell labels per rate and three temperatures; 48 CSV filenames. No named WLTP file exists in the inspected v1.0 ZIP.

Reported temperature labels / degC: [0, 10, 25]. These are source conditions, not measured temperature channels.

Reported time-series channels: Raw headers not inspected.

Reported frequency-domain channels: Not verified / not applicable.

Observation headers and units were not independently read; source conditions remain distinct from measured channels.

## Ageing data

**Not reported**. The reviewed source reports characterization or validation tests without an established longitudinal ageing series.

[Ageing coverage evidence](https://zenodo.org/records/4864437). This status applies to the dataset, not every file. Formation and repeated initial characterization are not a longitudinal ageing series.

## Parameter association

Match: `same_model_different_study`. Primary TEC2021 paper Table 1 attributes the LG M50 electrode OCP to Chen2020. Two existing catalog expressions therefore provide an explicit reused OCP anchor; full-cell experiments are a different study, without shared serials. This does not associate ORegan2022 diffusion/kinetic tables as same-study TEC measurements.

[LG M50 &#124; 5 Ah NMC811/graphite-SiOx](../cells/lg-m50.md)

Components without a native catalog join: diffusion, kinetics.

| Component | Match / quantity | Catalog record IDs | Evidence and missing items |
|---|---|---|---|
| ocp | `same_model_different_study` / `electrode_ocp` | `graphite-chen2020-formula`, `nmc811-lgm50-chen2020-formula` | Primary TEC2021 paper Table 1 attributes the LG M50 electrode OCP to Chen2020. Two existing catalog expressions therefore provide an explicit reused OCP anchor; full-cell experiments are a different study, without shared serials. This does not associate ORegan2022 diffusion/kinetic tables as same-study TEC measurements. Missing: No same-study or serialized-specimen match; cross-study reuse does not establish transferable aged-cell parameters. |
| diffusion | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |
| kinetics | `missing` / `missing` | None | No current catalog OCP/D/kinetics record is verified for this model/study. External half-cell files or published parameter packages are source leads, not silently imported parameters. Missing: No verified current-catalog record for this component and study. |

## Requested-test coverage

| Test class | Review result | Evidence / limits |
|---|---|---|
| multi_rate_charge | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| multi_rate_discharge | `file_located` | 48 measured-data filenames: 0.1/0.5/1/2C at 0/10/25 degC with source cell labels. Directory-only review, not raw channel verification. |
| US06 | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |
| EIS | `not_located` | No file for this requested class was identified in the inspected source; this does not establish absence elsewhere. |

## File locations

Selected confirmed source paths and parameter evidence. Counts describe locators, not independent experiments or a complete cell-by-temperature matrix.

An archive-member link downloads its parent container; extract the named member yourself. Listed files do not certify raw columns or model accuracy.

| Source path / member | Cell / source label | Test / profile | Temperature / rate | Review | Link |
|---|---|---|---|---|---|
| `data/0degC/Cell781_0p1C_0degC.csv` | LG M50 / Cell781 | constant_current;  | 0 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell781_0p1C_0degC.csv) |
| `data/0degC/Cell782_0p1C_0degC.csv` | LG M50 / Cell782 | constant_current;  | 0 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell782_0p1C_0degC.csv) |
| `data/0degC/Cell783_0p1C_0degC.csv` | LG M50 / Cell783 | constant_current;  | 0 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell783_0p1C_0degC.csv) |
| `data/0degC/Cell784_0p1C_0degC.csv` | LG M50 / Cell784 | constant_current;  | 0 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell784_0p1C_0degC.csv) |
| `data/0degC/Cell785_0p5C_0degC.csv` | LG M50 / Cell785 | constant_current;  | 0 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell785_0p5C_0degC.csv) |
| `data/0degC/Cell786_0p5C_0degC.csv` | LG M50 / Cell786 | constant_current;  | 0 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell786_0p5C_0degC.csv) |
| `data/0degC/Cell787_0p5C_0degC.csv` | LG M50 / Cell787 | constant_current;  | 0 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell787_0p5C_0degC.csv) |
| `data/0degC/Cell788_0p5C_0degC.csv` | LG M50 / Cell788 | constant_current;  | 0 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell788_0p5C_0degC.csv) |
| `data/0degC/Cell789_1C_0degC.csv` | LG M50 / Cell789 | constant_current;  | 0 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell789_1C_0degC.csv) |
| `data/0degC/Cell790_1C_0degC.csv` | LG M50 / Cell790 | constant_current;  | 0 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell790_1C_0degC.csv) |
| `data/0degC/Cell791_1C_0degC.csv` | LG M50 / Cell791 | constant_current;  | 0 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell791_1C_0degC.csv) |
| `data/0degC/Cell792_1C_0degC.csv` | LG M50 / Cell792 | constant_current;  | 0 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell792_1C_0degC.csv) |
| `data/0degC/Cell793_2C_0degC.csv` | LG M50 / Cell793 | constant_current;  | 0 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell793_2C_0degC.csv) |
| `data/0degC/Cell794_2C_0degC.csv` | LG M50 / Cell794 | constant_current;  | 0 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell794_2C_0degC.csv) |
| `data/0degC/Cell795_2C_0degC.csv` | LG M50 / Cell795 | constant_current;  | 0 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell795_2C_0degC.csv) |
| `data/0degC/Cell796_2C_0degC.csv` | LG M50 / Cell796 | constant_current;  | 0 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell796_2C_0degC.csv) |
| `data/10degC/Cell781_0p1C_10degC.csv` | LG M50 / Cell781 | constant_current;  | 10 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell781_0p1C_10degC.csv) |
| `data/10degC/Cell782_0p1C_10degC.csv` | LG M50 / Cell782 | constant_current;  | 10 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell782_0p1C_10degC.csv) |
| `data/10degC/Cell783_0p1C_10degC.csv` | LG M50 / Cell783 | constant_current;  | 10 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell783_0p1C_10degC.csv) |
| `data/10degC/Cell784_0p1C_10degC.csv` | LG M50 / Cell784 | constant_current;  | 10 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell784_0p1C_10degC.csv) |
| `data/10degC/Cell785_0p5C_10degC.csv` | LG M50 / Cell785 | constant_current;  | 10 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell785_0p5C_10degC.csv) |
| `data/10degC/Cell786_0p5C_10degC.csv` | LG M50 / Cell786 | constant_current;  | 10 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell786_0p5C_10degC.csv) |
| `data/10degC/Cell787_0p5C_10degC.csv` | LG M50 / Cell787 | constant_current;  | 10 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell787_0p5C_10degC.csv) |
| `data/10degC/Cell788_0p5C_10degC.csv` | LG M50 / Cell788 | constant_current;  | 10 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell788_0p5C_10degC.csv) |
| `data/10degC/Cell789_1C_10degC.csv` | LG M50 / Cell789 | constant_current;  | 10 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell789_1C_10degC.csv) |
| `data/10degC/Cell790_1C_10degC.csv` | LG M50 / Cell790 | constant_current;  | 10 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell790_1C_10degC.csv) |
| `data/10degC/Cell791_1C_10degC.csv` | LG M50 / Cell791 | constant_current;  | 10 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell791_1C_10degC.csv) |
| `data/10degC/Cell792_1C_10degC.csv` | LG M50 / Cell792 | constant_current;  | 10 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell792_1C_10degC.csv) |
| `data/10degC/Cell793_2C_10degC.csv` | LG M50 / Cell793 | constant_current;  | 10 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell793_2C_10degC.csv) |
| `data/10degC/Cell794_2C_10degC.csv` | LG M50 / Cell794 | constant_current;  | 10 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell794_2C_10degC.csv) |
| `data/10degC/Cell795_2C_10degC.csv` | LG M50 / Cell795 | constant_current;  | 10 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell795_2C_10degC.csv) |
| `data/10degC/Cell796_2C_10degC.csv` | LG M50 / Cell796 | constant_current;  | 10 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell796_2C_10degC.csv) |
| `data/25degC/Cell781_0p1C_25degC.csv` | LG M50 / Cell781 | constant_current;  | 25 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell781_0p1C_25degC.csv) |
| `data/25degC/Cell782_0p1C_25degC.csv` | LG M50 / Cell782 | constant_current;  | 25 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell782_0p1C_25degC.csv) |
| `data/25degC/Cell783_0p1C_25degC.csv` | LG M50 / Cell783 | constant_current;  | 25 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell783_0p1C_25degC.csv) |
| `data/25degC/Cell784_0p1C_25degC.csv` | LG M50 / Cell784 | constant_current;  | 25 degC; 0.1C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell784_0p1C_25degC.csv) |
| `data/25degC/Cell785_0p5C_25degC.csv` | LG M50 / Cell785 | constant_current;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell785_0p5C_25degC.csv) |
| `data/25degC/Cell786_0p5C_25degC.csv` | LG M50 / Cell786 | constant_current;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell786_0p5C_25degC.csv) |
| `data/25degC/Cell787_0p5C_25degC.csv` | LG M50 / Cell787 | constant_current;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell787_0p5C_25degC.csv) |
| `data/25degC/Cell788_0p5C_25degC.csv` | LG M50 / Cell788 | constant_current;  | 25 degC; 0.5C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell788_0p5C_25degC.csv) |
| `data/25degC/Cell789_1C_25degC.csv` | LG M50 / Cell789 | constant_current;  | 25 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell789_1C_25degC.csv) |
| `data/25degC/Cell790_1C_25degC.csv` | LG M50 / Cell790 | constant_current;  | 25 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell790_1C_25degC.csv) |
| `data/25degC/Cell791_1C_25degC.csv` | LG M50 / Cell791 | constant_current;  | 25 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell791_1C_25degC.csv) |
| `data/25degC/Cell792_1C_25degC.csv` | LG M50 / Cell792 | constant_current;  | 25 degC; 1.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell792_1C_25degC.csv) |
| `data/25degC/Cell793_2C_25degC.csv` | LG M50 / Cell793 | constant_current;  | 25 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell793_2C_25degC.csv) |
| `data/25degC/Cell794_2C_25degC.csv` | LG M50 / Cell794 | constant_current;  | 25 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell794_2C_25degC.csv) |
| `data/25degC/Cell795_2C_25degC.csv` | LG M50 / Cell795 | constant_current;  | 25 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell795_2C_25degC.csv) |
| `data/25degC/Cell796_2C_25degC.csv` | LG M50 / Cell796 | constant_current;  | 25 degC; 2.0C | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell796_2C_25degC.csv) |
| `PyBaMM/v25.4.2/Chen2020.py` | LG M50 / No sample ID | ;  | Temperature unknown | `source_listing`; content `not_read` | [Open source file](https://raw.githubusercontent.com/pybamm-team/PyBaMM/v25.4.2/src/pybamm/input/parameters/lithium_ion/Chen2020.py) |

File notes:

- `data/0degC/Cell781_0p1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell782_0p1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell783_0p1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell784_0p1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell785_0p5C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell786_0p5C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell787_0p5C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell788_0p5C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell789_1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell790_1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell791_1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell792_1C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell793_2C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell794_2C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell795_2C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/0degC/Cell796_2C_0degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell781_0p1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell782_0p1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell783_0p1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell784_0p1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell785_0p5C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell786_0p5C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell787_0p5C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell788_0p5C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell789_1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell790_1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell791_1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell792_1C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell793_2C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell794_2C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell795_2C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/10degC/Cell796_2C_10degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell781_0p1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell782_0p1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell783_0p1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell784_0p1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell785_0p5C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell786_0p5C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell787_0p5C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell788_0p5C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell789_1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell790_1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell791_1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell792_1C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell793_2C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell794_2C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell795_2C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `data/25degC/Cell796_2C_25degC.csv`: Pinned author file path agrees with released ZIP directory. Filename rate/temperature and measured-data role are source-supported; raw headers/current sign/temperature channels remain unread.
- `PyBaMM/v25.4.2/Chen2020.py`: Existing Chen2020 OCP implementation, explicitly reused by the TEC2021 paper. This is an expression/source-code link, not new raw half-cell data; do not execute upstream code as part of discovery.

## Reuse and access

License: **BSD-3-Clause**. [Source terms](https://github.com/brosaplanella/TEC-reduced-model/blob/978f8c38005892d98f1204b71422f6ff64c32acd/LICENSE). Pinned author repository has BSD-3-Clause and explicitly describes code and experimental data. Zenodo API uses other-open; the exact repository license is cited rather than relabelled CC BY. No observations redistributed.

Review level: `archive_directory_reviewed`. Complete v1.0 ZIP directory, pinned author tree/README/LICENSE and primary paper inspected. No CSV observation read or author code executed.

- [data/0degC/Cell781_0p1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell781_0p1C_0degC.csv)
- [data/0degC/Cell782_0p1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell782_0p1C_0degC.csv)
- [data/0degC/Cell783_0p1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell783_0p1C_0degC.csv)
- [data/0degC/Cell784_0p1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell784_0p1C_0degC.csv)
- [data/0degC/Cell785_0p5C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell785_0p5C_0degC.csv)
- [data/0degC/Cell786_0p5C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell786_0p5C_0degC.csv)
- [data/0degC/Cell787_0p5C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell787_0p5C_0degC.csv)
- [data/0degC/Cell788_0p5C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell788_0p5C_0degC.csv)
- [data/0degC/Cell789_1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell789_1C_0degC.csv)
- [data/0degC/Cell790_1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell790_1C_0degC.csv)
- [data/0degC/Cell791_1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell791_1C_0degC.csv)
- [data/0degC/Cell792_1C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell792_1C_0degC.csv)
- [data/0degC/Cell793_2C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell793_2C_0degC.csv)
- [data/0degC/Cell794_2C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell794_2C_0degC.csv)
- [data/0degC/Cell795_2C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell795_2C_0degC.csv)
- [data/0degC/Cell796_2C_0degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/0degC/Cell796_2C_0degC.csv)
- [data/10degC/Cell781_0p1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell781_0p1C_10degC.csv)
- [data/10degC/Cell782_0p1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell782_0p1C_10degC.csv)
- [data/10degC/Cell783_0p1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell783_0p1C_10degC.csv)
- [data/10degC/Cell784_0p1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell784_0p1C_10degC.csv)
- [data/10degC/Cell785_0p5C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell785_0p5C_10degC.csv)
- [data/10degC/Cell786_0p5C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell786_0p5C_10degC.csv)
- [data/10degC/Cell787_0p5C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell787_0p5C_10degC.csv)
- [data/10degC/Cell788_0p5C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell788_0p5C_10degC.csv)
- [data/10degC/Cell789_1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell789_1C_10degC.csv)
- [data/10degC/Cell790_1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell790_1C_10degC.csv)
- [data/10degC/Cell791_1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell791_1C_10degC.csv)
- [data/10degC/Cell792_1C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell792_1C_10degC.csv)
- [data/10degC/Cell793_2C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell793_2C_10degC.csv)
- [data/10degC/Cell794_2C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell794_2C_10degC.csv)
- [data/10degC/Cell795_2C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell795_2C_10degC.csv)
- [data/10degC/Cell796_2C_10degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/10degC/Cell796_2C_10degC.csv)
- [data/25degC/Cell781_0p1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell781_0p1C_25degC.csv)
- [data/25degC/Cell782_0p1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell782_0p1C_25degC.csv)
- [data/25degC/Cell783_0p1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell783_0p1C_25degC.csv)
- [data/25degC/Cell784_0p1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell784_0p1C_25degC.csv)
- [data/25degC/Cell785_0p5C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell785_0p5C_25degC.csv)
- [data/25degC/Cell786_0p5C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell786_0p5C_25degC.csv)
- [data/25degC/Cell787_0p5C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell787_0p5C_25degC.csv)
- [data/25degC/Cell788_0p5C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell788_0p5C_25degC.csv)
- [data/25degC/Cell789_1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell789_1C_25degC.csv)
- [data/25degC/Cell790_1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell790_1C_25degC.csv)
- [data/25degC/Cell791_1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell791_1C_25degC.csv)
- [data/25degC/Cell792_1C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell792_1C_25degC.csv)
- [data/25degC/Cell793_2C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell793_2C_25degC.csv)
- [data/25degC/Cell794_2C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell794_2C_25degC.csv)
- [data/25degC/Cell795_2C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell795_2C_25degC.csv)
- [data/25degC/Cell796_2C_25degC.csv](https://raw.githubusercontent.com/brosaplanella/TEC-reduced-model/978f8c38005892d98f1204b71422f6ff64c32acd/data/25degC/Cell796_2C_25degC.csv)
- [PyBaMM/v25.4.2/Chen2020.py](https://raw.githubusercontent.com/pybamm-team/PyBaMM/v25.4.2/src/pybamm/input/parameters/lithium_ion/Chen2020.py)

[Supporting evidence (JSON)](../../src/ebp/data/evidence/ocp-first-expansion-review.json)


## Missing items and limits

- No new measured half-cell points; explicit published OCP-expression reuse only. No same-specimen join to Chen2020.
- Raw CSV columns, current convention and measured temperature channel not independently read. No full temperature/rate matrix outside listed paths is asserted.
- No WLTP, US06, EIS or longitudinal ageing file located in the inspected v1.0 release.
- ORegan2022 parameter tables (Zenodo 5171874) are a separate parameter study; they are not silently merged with TEC2021 or current Chen D/k.

## Evidence

- [Primary source 1](https://zenodo.org/records/4864437)
- [Primary source 2](https://github.com/brosaplanella/TEC-reduced-model/tree/978f8c38005892d98f1204b71422f6ff64c32acd)
- [Primary source 3](https://doi.org/10.1016/j.electacta.2021.138524)
- [Primary source 4](https://wrap.warwick.ac.uk/id/eprint/152012/7/WRAP-Systematic-derivation-validation-reduced-thermal-electrochemical-2021.pdf)

No external payload is fetched by the library, viewer or CI. Dataset coverage does not assert a complete cell × temperature × profile matrix. Whole-cell OCV is not electrode OCP; EIS is frequency-domain evidence, not a current/voltage drive-cycle trace.
