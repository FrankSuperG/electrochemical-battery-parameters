# LG MJ1 / DLR-SINTEF curation

Reviewed 2026-10-17 for v0.8.0. **Four pseudo-OCP tables and 42 parameter
records** are imported. No same-study intact commercial MJ1 full-cell test was
verified. This is a partial characterization package.

**[Cell and download index](../data/cells/lg-mj1-dlr-sintef.md)** ·
[Parameters CSV](../data/parameters/lg-mj1-dlr-sintef.csv) ·
[Full metadata JSON](../data/parameters/lg-mj1-dlr-sintef.json)

## Sources, rights and association

| Source | Imported scope | Reuse basis |
|---|---|---|
| [Characterization collection 15407849](https://zenodo.org/records/15407849) | Parent/study identity | CC BY 4.0 |
| [Direct characterization 15497193](https://zenodo.org/records/15497193) | Selected original workbook cells, four native pseudo-OCP Parquets, processed D/i0 Parquets and JSON-LD | CC BY 4.0 |
| [Anode GITT parameters 15528177](https://zenodo.org/records/15528177) | Six fitted D tables, with original error bounds | CC BY 4.0 |
| [Cathode GITT parameters 15538164](https://zenodo.org/records/15538164) | Six fitted D tables, with original error bounds | CC BY 4.0 |
| [Continuum input set 15496570](https://zenodo.org/records/15496570) | Original Python file as source evidence; not executed or indiscriminately converted into catalog values | CC BY 4.0 |
| [Structured anode GITT 15520717](https://zenodo.org/records/15520717) | External hash-pinned test links; file contents inspected, not counted as full-cell observations | CC BY 4.0 |

Attribution: Yannick Kuhn, Bhawna Rana, Micha Philipp, Christina Schmitt,
Roberto Scipioni, Eibar Flores, Dennis Kopljar, Simon Clark, Arnulf Latz and
Birger Horstmann. Fixed-record API metadata preserve authors, explicit license,
versions and relationships. Original source files are checked against published MD5 and pinned SHA-256.
The original workbook remains external: its OCV sheet includes separately
attributed silicon literature curves. Only selected laboratory cells are
packaged in `mj1-workbook-cell-selection.json`, with original hashes, addresses,
NA/blanks and a separate derivative hash. Entire OCV/electrolyte sheets are
excluded from this JSON. No rights are reassigned to the literature columns. See [asset manifest](../scripts/mj1_assets.json).
Retain [CC BY 4.0](../src/ebp/licenses/CC-BY-4.0.txt), attribution and changes
when redistributing. Source authors have not endorsed this catalog.

The associated [paper](https://doi.org/10.1039/D5DD00247H), *Workflows and
principles for collaboration and communication in battery research*, appeared
in Digital Discovery 2026, 5, 177-192, first published 2025-11-05. The inspected
publisher PDF labels the **article CC BY 3.0**, separately from the **datasets'
CC BY 4.0**. Article text/images are not repackaged as data.

Matching is **same commercial model and study**, with component-level limits.
Direct characterization identifies harvested cell #001. Shared collection and
processing relations establish the GITT lineage; they do not establish one
serialized original cell across every measurement or an intact validation cell.

## Imported data and definitions

- Four pseudo-OCP branches: NMC and graphite-SiOx, each with the source
  `charging` and `discharging` labels. The source JSON-LD reports 0.05 C and a
  lithium reference. They remain finite-current pseudo-OCP, not equilibrium OCP.
- Twenty-two scalar/specification records: selected coating/collector/original
  separator thicknesses, electrode areas, porosities, particle diameters, BET
  areas, conductivities, four SOC-specific activation energies and nominal
  commercial capacity. Diameter is not radius; BET area is not automatically
  electrochemically active area. Microstructure estimates retain the paper's
  external Heenan et al. MJ1 tomography lineage limit.
- Four laboratory GITT-derived diffusion tables and four EIS-derived
  exchange-current tables, with native workbook SOC-percent coordinates.
- Twelve model-based GITT diffusion fits: positive/negative electrode,
  lithiation/delithiation and **SPM, SPMe, DFN** alternatives. Original lower and
  upper error bounds remain in each CSV; no coverage probability is invented.

Lab and model-derived diffusion are alternatives with different estimation
assumptions. Variant labels do not make complete parameter sets. Select the
appropriate record and coordinate/model convention explicitly. Neither broad
error bounds nor clipped/prior-dominated fits are hidden by averaging models.

### Transformations and source defects

| Issue | Curation decision |
|---|---|
| Workbook `Di` has `NA` endpoints; `i0` has blank endpoints. Several Parquet exports replace these with zero, and round other values. | Use numeric workbook cells at full stored precision. Each lab table retains 36 nodes, omitted row addresses and source Excel rows. Preserve processed Parquets as evidence, without adopting their zero substitutions. |
| D is reported in cm2/s; i0 in mA/cm2. | Multiply D by `1e-4` for m2/s and i0 by `10` for A/m2. Keep source units and multipliers. The i0 active/geometric area basis remains unresolved. |
| Native OCP has duplicate graphite coordinates and 1,402 NMC-charging rows without a coordinate. | Retain first finite observation per native coordinate and sort ascending. Record omitted counts and original one-based Parquet row for every retained node. No smoothing, resampling, voltage correction or coordinate imputation. |
| OCP column is named `stoichiometry_unit_one`, but absolute calibration is not independently established. | Use `source_reported_stoichiometry`, separately from full-cell SOC or branch throughput; require explicit mapping for PyBaMM. Source charging/discharging remains a label, without asserting physical lithiation direction. |
| Workbook NMC composition is 83:5:12; later paper reports 84:5:11. | Use generic NMC; keep the discrepancy visible instead of silently relabeling NMC811. |
| Workbook nominal voltage is `3635 V`, concentration units say `mol/l`, and positive max/min stoichiometry labels appear reversed. | Exclude these ambiguous fields. Do not silently repair units, reverse labels or generate initial concentrations. |
| Workbook coating thicknesses are 88/74 um; later paper says 87/73 um. | Keep the workbook variant and source method; do not merge editions. |
| Simulation file contains substitutions, placeholder initial states, borrowed settings and a 260 um separator. | Retain it only as original source evidence. Original separator geometry stays separate; no complete simulation dictionary is claimed. |

Native parameter CSVs include coordinates, values and source rows or error bounds.
`Parameter.points()` returns stored nodes. Evaluation uses **arithmetic linear
interpolation inside the native domain**, with no extrapolation or unreported
log-space fit. Missing endpoints stay outside that domain.

## Full-cell search and remaining gaps

The original workbook has six sheets: specifications, physical quantities,
electrolyte, i0, Di and OCV. It has no time/current/full-cell cycling sheet.
The collection separates harvested-anode/cathode processing records. The paper's
Section 3.4 uses 18 mm harvested electrodes assembled into three-electrode
EL-CELL fixtures, with a **260 um Whatman GF/A replacement separator** and
lithium reference. Commercial MJ1's original separator is about 12 um.

The inspected structured anode GITT files contain 1,569,414 and 1,589,467 rows
with time, signed current, working-versus-reference voltage, command and segment
index. Their voltage is an electrode potential, not intact-cell terminal voltage.
No temperature array is present. The paper's 25 degC chamber setting is not a
measured temperature trace. The files begin with GITT preparation/rest and
pulse segments; they do not provide the paper's preceding intact-cell CC cycles.
Native command names and current signs also require an electrode-specific
interpretation before reuse.

Consequently **no new full-cell test is added**. A three-electrode reference
potential is not substituted for terminal voltage, and unrelated public MJ1
cycling data are not joined as same-study evidence. Intact-cell CC charge,
discharge, dynamic t/I/V/T, serialized specimen correspondence, absolute
electrode balancing, full kinetic concentration laws and independent model
validation remain missing. Direct GITT links remain available through the source
and asset metadata.

The OCP adapter maps native domain endpoints to the supplied lithium-fraction
endpoints. For an NMC source domain starting at 0.21, the low endpoint maps
explicitly rather than being implicitly treated as a 0..1 branch. The mapping
and original source domain remain in runtime metadata.

## Use a native parameter table

```python
from ebp import Catalog

c = Catalog()
p = c.get_parameter("mj1-lab-negative-di-charging")
x, D = p.points()  # source SOC percent, D in m2/s
print(p(source_soc_percent=50))
print(p.record["conditions"], p.record["limitations"])

fit = c.get_parameter("mj1-gitt-positive-dfn-lithiation")
source_coordinate, D_fit = fit.points()
```

The cell index links every native table directly. The offline cell ZIP retains
the selected-cell JSON, licensed original Parquet/fit files, parameter tables,
OCP nodes, metadata and CC BY 4.0 text. The full XLSX remains an external source
link; its literature silicon OCV content is not redistributed. No author code runs during import or table evaluation. Reconstruction:
`python scripts/seed_mj1.py`, or the full `scripts/seed_v01.py --download` chain.
