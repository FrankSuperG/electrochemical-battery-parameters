# Full-cell dataset links and material groups

[Browse by material](../data/full-cell/README.md) · [Metadata CSV](../data/full-cell/datasets.csv) · [Metadata JSON](../data/full-cell/datasets.json)

E-BatP keeps large new full-cell datasets with their original providers. The
catalog stores a small reviewed link registry: cell identity, material families,
test types, named profiles, rate and temperature conditions, source versions,
reuse terms, parameter joins and missing items. Reading, exporting, building the
viewer and running CI do not download these external observations.

The existing 61 packaged branch/test files remain available. They are not
duplicated by the material index. The seven external records describe datasets,
not seven tests or seven independent cells; one multi-material dataset appears
under LFP, NMC and NCA. Previously curated M50LT EIS evidence is indexed here
without counting it again as a new time-domain full-cell file.

## Find a test

- [LFP](../data/full-cell/LFP.md): A123 multi-rate charging, UDDS, CALCE DST/FUDS,
  SOC-dependent EIS and existing catalog CC records.
- [NMC](../data/full-cell/NMC.md): CALB US06/UDDS/WLTP, HPPC and EIS; CALCE 20R
  US06/DST/FUDS/BJDST; existing LG M50 and M50LT study data.
- [NCA](../data/full-cell/NCA.md): an external multi-chemistry dynamic-test
  deposit. Its per-cell/profile matrix is not independently inspected; it has
  no verified join to the Kim2011 nominal-design parameters.
- [LCO](../data/full-cell/LCO.md) and [NCO](../data/full-cell/NCO.md): existing
  source-preserving observations, with their current missing-channel limits.

The local viewer has material filters for cell packages and a separate external
dataset section with material, test-type, profile and text filters. An **Open
original dataset** button takes you to the provider. It does not imply the data
have been imported or normalized by E-BatP.

```bash
ebp datasets --material LFP --test-type cccv
ebp datasets --material NMC --test-type dynamic --profile US06
ebp datasets --material NCA --profile US06 --json
ebp datasets --test-type eis
ebp datasets --cell lg-m50lt-hallemans2025 --json
```

```python
from ebp import Catalog

catalog = Catalog()
datasets = catalog.search_datasets(material="NMC", test_type="dynamic", profile="US06")
for dataset in datasets:
    print(dataset["title"], dataset["source"]["url"])
    print(dataset["parameter_link"], dataset["missing_items"])
```

`Catalog.full_cell_data()` reads existing packaged test IDs only. It does not
silently fetch or parse external dataset IDs. To use an external record, open
its source, choose a specific cell/test file, retain its license and review its
units, signs, timestamps and actual measured channels. Source temperature
setpoints are not measured temperature traces. Unknown values stay unknown.

## Primary-source review, 2026-10-23

| Source | Confirmed coverage | Parameter match and access limits |
|---|---|---|
| [A123 26650 M1B / UCCS, v1](https://data.mendeley.com/datasets/p8kf893yv3/1) | LFP; 1/2/3/4C CCCV charging at 25 degC, UDDS at 25/35 degC, OCV and dynamic characterization; CC BY 4.0 | Unmatched to catalog parameter studies. Whole-cell OCV does not supply electrode OCP. Other A123 formats and studies remain separate. Raw files not fetched. |
| [CALCE Samsung 20R and A123](https://calce.umd.edu/data) | NMC 20R: US06/DST/FUDS/BJDST and OCV; A123 LFP: DST/FUDS and OCV | Two link records for distinct cell sections on one source page. No parameter join. Standard redistribution license not identified; source requests citations. A123 part identity and temperature wording remain unresolved. |
| [CALB L148N58A, v2](https://data.mendeley.com/datasets/ycx459r5c3/2), [paper](https://doi.org/10.1016/j.dib.2025.111301) | NMC/graphite; eleven B-grade 58 Ah cells; C/20, HPPC, US06/UDDS/WLTP, EIS at 10/25/40 degC; CC BY 4.0 | No electrode OCP/D/kinetics join. Paper links deposit v1; v2 is pinned here without claiming identical bytes. HPPC folder labels and rate assignments require checking. Raw files not fetched. |
| [University of Malaya, v1](https://data.mendeley.com/datasets/29kw38kzwj/1) | Source names LFP, NCA and NMC, three 18650 cell types, DST/FUDS/UDDS/WLTP/US06 and HPPC/pulse tests; CC BY 4.0 | Dataset-level tags only. No guarantee of a complete cell-by-profile or temperature matrix. Numeric setpoints, rates and columns remain unverified. No catalog parameter join. |
| [600 mAh LFP EIS, v1](https://doi.org/10.6084/m9.figshare.23736582.v1), [official metadata](https://api.figshare.com/v2/articles/23736582) | SOC-dependent EIS; CC BY 4.0. Provider lists a 465,799-byte RAR and MD5. | Manufacturer/model, frequency grid, signs, units and temperatures unresolved. HTML returned 403; official metadata was accessible. Archive not fetched; listed checksum is not an independently calculated hash. |
| [LG M50LT / Hallemans pinned author files](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068), [curation audit](HALLEMANS2025.md) | Measured 9-SOC/65-frequency EIS; same study as the grouped SPMe fit; BSD-3-Clause author data | Same model and same study, with unresolved specimen mapping. Existing measured EIS CSV is linked. Third-party OCP permission and intrinsic D/k remain missing; grouped coefficients are not intrinsic material properties. |

The associated CALB paper identifies NMC/graphite. The Malaya source declares
three chemistry families collectively; its labels are retained at dataset
grain. NCO in the Ecker/Kokam catalog stays NCO. Chemistry is a navigation
category and never sufficient evidence for joining a test to OCP or parameters.

## Meanings and boundaries

- `constant_current` and `cccv` describe continuous segments or charging
  protocols. A 1C pulse is not a complete 1C discharge curve. Multi-rate claims
  require explicit numeric source evidence.
- `dynamic` records named schedules such as US06, UDDS and WLTP. An EPA current
  command or a simulated voltage is not a measured battery response. The
  existing M50LT drive cycle remains unnamed; it is not relabeled US06.
- `eis` is frequency-domain evidence. It does not create a time-domain I/V/T
  trace, electrode-resolved OCP or unique intrinsic D/k values.
- `ocv` means whole-cell OCV characterization, possibly finite-current
  pseudo-OCV; it is distinct from electrode OCP versus a reference electrode.
- `source_metadata_only` means source descriptions and terms were inspected;
  raw columns, units, row counts and every download URL were not independently
  checked. `existing_source_audit` points to observations already reviewed.
- `unmatched` means no verified catalog parameter join. A matched record must
  name catalog cell IDs and retain its evidence. Dataset links do not upgrade
  specimen identity or scientific completeness.
- `not-stated` is not a permissive license. Link to the provider and resolve
  reuse terms before redistributing raw data. Dataset links do not grant rights.

Model simulation, fitting and model validation remain outside this repository's
scope. This expansion improves access and provenance; it reports no new model
performance or independently measured material parameters.

## Add another external dataset

Use [the external-dataset contribution template](../templates/external-dataset.json).
Replace placeholders and append a reviewed record to
`src/ebp/data/external_datasets.json`. Never fill a missing temperature, chemistry,
rate or cell match by inference. Keep observed file checksums distinct from
publisher-reported ones. Add no raw payload or automatic-download step.

```bash
ebp validate
python scripts/build_data_index.py
```

The external registry is manually reviewed metadata and is not rewritten by
raw-data reconstruction. Generated pages, CSV and JSON are deterministic views
of that registry and the existing catalog. A dead provider link remains a
source-access problem; it should be recorded rather than silently replaced with
an unrelated same-chemistry dataset.
