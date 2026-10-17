# Browse and download the data

Start here when browsing on GitHub. No Python installation or hosted website is required to find files.

1. Choose a cell below, or [browse OCP by material](ocp/README.md).
2. Open the linked **CSV** for data and **JSON** for definitions, source evidence and missing items.
3. Use the file page's **Raw / download raw file** controls to save the complete file. GitHub previews may not display large files. Keep the metadata and source license with your copy.

See [how to download, interpret and use files](../docs/DATA_ACCESS.md) for Excel, Python and model examples. If repository access is restricted, sign in with an account that has access.

Snapshot: 59 OCP records, 397 other parameter records, 61 full-cell test files.

## Choose a cell or study

| Cell / study entry | OCP | Other parameters | Full-cell tests | Match level |
|---|---|---|---|---|
| [LG M50 &#124; 5 Ah NMC811/graphite-SiOx](cells/lg-m50.md) | [2 records](cells/lg-m50.md#ocp-curves) | [38 records](cells/lg-m50.md#parameters) | [3 files](cells/lg-m50.md#full-cell-tests) | `same_model_same_study` |
| [Undisclosed LFP/graphite 18650, 2 Ah (BPX)](cells/bpx-lfp-18650-2ah-undisclosed.md) | [2 records](cells/bpx-lfp-18650-2ah-undisclosed.md#ocp-curves) | [46 records](cells/bpx-lfp-18650-2ah-undisclosed.md#parameters) | Not imported | `unmatched` |
| [A123 AMP20M1HD-A &#124; 20 Ah LFP pouch](cells/a123-amp20m1hd-a.md) | Not linked | [30 records](cells/a123-amp20m1hd-a.md#parameters) | [1 file](cells/a123-amp20m1hd-a.md#full-cell-tests) | `same_model_same_study` |
| [A123 high-power LFP pouch &#124; 9 Ah &#124; part undisclosed](cells/a123-high-power-pouch-9ah.md) | Not linked | Not imported | [10 files](cells/a123-high-power-pouch-9ah.md#full-cell-tests) | `same_study_cell_family` |
| [SLPB78205130H &#124; LCO/graphite &#124; 0.680616 Ah model input](cells/kokam-slpb78205130h-marquis2019.md) | [2 records](cells/kokam-slpb78205130h-marquis2019.md#ocp-curves) | [38 records](cells/kokam-slpb78205130h-marquis2019.md#parameters) | Not imported | `parameter_set_only` |
| [UMBL Mohtat2020 &#124; 5 Ah NMC/graphite research pouch](cells/mohtat2020-nmc532-pouch.md) | [4 records](cells/mohtat2020-nmc532-pouch.md#ocp-curves) | [71 records](cells/mohtat2020-nmc532-pouch.md#parameters) | [5 files](cells/mohtat2020-nmc532-pouch.md#full-cell-tests) | `same_study_cell_family` |
| [NCA_Kim2011 &#124; NCA/graphite &#124; 0.43 Ah model input](cells/kim2011-nca-nominal-design.md) | [2 records](cells/kim2011-nca-nominal-design.md#ocp-curves) | [38 records](cells/kim2011-nca-nominal-design.md#parameters) | Not imported | `unmatched` |
| [Kokam SLPB75106100 &#124; 7.5 Ah NCO/graphite](cells/kokam-slpb75106100-ecker2015.md) | [2 records](cells/kokam-slpb75106100-ecker2015.md#ocp-curves) | [38 records](cells/kokam-slpb75106100-ecker2015.md#parameters) | [2 files](cells/kokam-slpb75106100-ecker2015.md#full-cell-tests) | `same_model_same_study` |
| [Enertech &#124; LCO/graphite &#124; 2.28 Ah model input](cells/enertech-lco-pouch-ai2020.md) | [2 records](cells/enertech-lco-pouch-ai2020.md#ocp-curves) | [38 records](cells/enertech-lco-pouch-ai2020.md#parameters) | [4 files](cells/enertech-lco-pouch-ai2020.md#full-cell-tests) | `same_study_cell_family` |
| [ISU-UConn &#124; laboratory LFP/graphite CR2032 family](cells/isu-uconn-lfp-graphite-lab.md) | [4 records](cells/isu-uconn-lfp-graphite-lab.md#ocp-curves) | Not imported | [21 files](cells/isu-uconn-lfp-graphite-lab.md#full-cell-tests) | `same_study_cell_family` |
| [A123 18650M1A &#124; Jahn2024 LFP/graphite](cells/a123-18650m1a-jahn2024.md) | [2 records](cells/a123-18650m1a-jahn2024.md#ocp-curves) | Not imported | [14 files](cells/a123-18650m1a-jahn2024.md#full-cell-tests) | `same_model_same_study` |
| [LG M50LT &#124; Hallemans2025 grouped SPMe](cells/lg-m50lt-hallemans2025.md) | Not linked | [18 records](cells/lg-m50lt-hallemans2025.md#parameters) | [1 file](cells/lg-m50lt-hallemans2025.md#full-cell-tests) | `same_model_same_study` |
| [LG MJ1 &#124; DLR-SINTEF harvested-electrode characterization](cells/lg-mj1-dlr-sintef.md) | [4 records](cells/lg-mj1-dlr-sintef.md#ocp-curves) | [42 records](cells/lg-mj1-dlr-sintef.md#parameters) | Not imported | `same_model_same_study` |

## Find data by type

| Need | Entry point |
|---|---|
| LFP or another material's OCP | [OCP index](ocp/README.md), with CSV and per-record JSON links |
| Diffusion, kinetics, geometry, transport or thermal values | [Cell parameter CSV/JSON exports](parameters/); filter CSV by `name` / `category` and inspect `definition`, units, conditions and origin |
| Current / voltage / temperature and CC tests | Choose a cell above, then its Full-cell tests table; [stored test files](../src/ebp/data/full_cell/) |
| Original Mohtat MATs and author files | [Packaged evidence](../src/ebp/data/evidence/) and [source audit](../docs/MOHTAT2020.md) |
| Matching evidence and missing items | Cell pages above and the [matching audit](../src/ebp/data/matching_audit.json) |
| Primary papers, datasets, versions and hashes | [Sources](../src/ebp/data/sources.json), [assets](../src/ebp/data/assets.json) and each export's metadata |

## Where the files live

`src/ebp/data/` is authoritative. This `data/` directory is a generated browsing view: parameter CSV/JSON exports, small formula samples, per-record OCP metadata and Markdown links. Large native OCP and full-cell observations are linked to their canonical files rather than duplicated.

Paths inside JSON records are relative to `src/ebp/data/`; use each export's `canonical_data_root` when reading the export from a checkout. GitHub navigation does not change the observations, definitions or validation status.

Maintainers: regenerate with `python scripts/build_data_index.py` after catalog updates. Check freshness with `python scripts/build_data_index.py --check`. Read [CONTRIBUTING.md](../CONTRIBUTING.md) before changing source data.
