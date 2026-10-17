# LFP study packages: ISU-UConn and A123 18650M1A

Curated on 2026-10-17. These are partial source packages with explicit matching
boundaries. They add **six electrode curves and 35 full-cell branch/array files**,
not 35 independent cells. No diffusion or intrinsic reaction-kinetic values were
added. Repository access remains restricted; this import does not publish a site.

| Package | Electrode curves | Full-cell observations | Association |
|---|---|---|---|
| [ISU-UConn CR2032 family](../data/cells/isu-uconn-lfp-graphite-lab.md) | Four C/20 pseudo-OCP branches, 3,057 retained nodes | 21 branches from 11 selected configurations, 24,891 rows | Same study and MTI electrode family; no commercial model or identical harvested-specimen mapping |
| [A123 18650M1A / Jahn2024](../data/cells/a123-18650m1a-jahn2024.md) | Two **modeled PD-ECM OCPn** tables, 1,001 native nodes | 14 files from five deposited observation files, 54,018 rows | Same named model, paper and author code/data chain; serialized specimen mapping unresolved |

## ISU-UConn selection and source

The [primary deposit](https://digitalcommons.lib.uconn.edu/reil_datasets/6/)
describes 50 laboratory cells (15 half-cells and 35 full-cells), mostly C/20,
with three graphite half-cells at C/30. This curation uses a **subset**, not all
50 cells. The [author repository](https://github.com/REIL-UConn/Multi-Objective-Optimization-for-Lithium-Ion-Battery-Degradation-Diagnostics/tree/1188c371e5836df4a7e5f5acf336a34ffd4027e6)
explicitly identifies its workbook as the deposited CC BY 4.0 dataset. Its code
is separately MIT. The primary university README/license download endpoints
returned HTTP 403. The byte-identical author-hosted workbook is packaged and
SHA-256 pinned; byte identity to the inaccessible university copy is **not**
established. Scientific attribution: [Li et al., 2026](https://doi.org/10.1016/j.etran.2026.100593).

The author's notebook cell 6 selects index 1 (second capacity/voltage pair after
the latest date marker), block 6, for both electrodes. The fixed extraction uses:

- LFP: `12-LFP C_20 Updated`, columns E:F. Its S2 association follows the
  corresponding earlier sheet's labels. The updated sheet itself has no S2
  header, so the exact address is the stable identifier.
- Graphite: `12-Graphite Half-cell @ C_20`, columns J:K, local label S2.
- Both zero-based block 6 and the following reverse block 7 are retained as
  separate pseudo-OCP curves. Blank rows delimit blocks; these indices are not
  instrument-recorded cycle or step identifiers.

For each half-cell branch, extraction ends at the **first maximum capacity**,
then retains the first occurrence of each capacity and normalizes the retained
range to 0..1. There is no smoothing or resampling. Every output node retains
`source_capacity_mAh` and its one-based `source_excel_row`. The graphite source
pair has many repeated, coarsely quantized capacities; first-occurrence removal
therefore leaves 213/215 nodes from 1,197/1,205 branch rows. Exact removal counts
are in each record. The complete XLSX preserves omitted tails and repeated values.
This follows the author's duplicate-capacity policy but is not a byte-for-byte
reproduction of the notebook's endpoint slicing, mass scaling or fitted results.

Finite-current branch voltage is marked `measurement=pseudo_ocp`. The accessible
workbook/notebook do not establish the counter/reference construction or numeric
temperature. `reference=unresolved` avoids asserting Li/Li+ from convention alone;
PyBaMM adaptation refuses these records until supporting reference evidence is
curated. Lithiation/delithiation labels are inferred from potential trend, not
instrument current. Full-cell fitting in the author code supports the study-family
association without resolving these measurement details.

Notebook cell 8 names eleven full-cell configurations. Their sheet, pair and
branch addresses are fixed in [the selection manifest](../scripts/isu_uconn_selection.json).
The selected charge branch and its following discharge branch are exported where
present. `Full cell after FM SOC 0` has only the selected charge branch. All
numeric rows in each full-cell block are retained, including repeated capacities
and constant-capacity tails. `Capacity/mAh` becomes `passed_capacity_Ah` by
division by 1000, for both directions. Time/current/temperature stay blank.
Local column/sample labels are not promoted to globally unique specimen IDs.

## A123: modeled OCPn and experimental observations

Use the fixed [data v2](https://zenodo.org/records/11958572) and
[code deposit](https://zenodo.org/records/10852695). Both API metadata declare
CC BY 4.0; snapshots, selected source bytes, published MD5 and SHA-256 pins are
retained. The seven observation/curve file checksums also match data v1. The
[paper's Methods and Parameterization](https://www.nature.com/articles/s44172-024-00221-4)
identify A123 18650M1A, 25 degC chamber testing, electrode harvesting afterwards,
and the approximation/parameterization of single-string OCPn.

`param_ocpn_lfp.mat` and `param_ocpn_graphite.mat` contain `pot_dol`/`pot` arrays
of 399 and 602 nodes. They are **model inputs**, not raw GITT/electrode OCP points.
Both are labeled `measurement=model_ocp`, `x.kind=model_soc`. The LFP potential
rises with this source coordinate; it must not silently become lithium fraction.
The positive graphite `pot` values are retained versus Li/Li+; the author code's
negation belongs to full-cell assembly. The bounded catalog interpolator offers
linear/PCHIP interpolation without reproducing the author's graphite spline,
electrode balancing or extrapolation. An explicit, justified stoichiometry
mapping is necessary before adapter use and does not validate the PD-ECM-to-DFN
transfer. Non-monotonic LFP values are retained unchanged.

| Observation | Export count / rows | Available channels | Preserved boundary |
|---|---:|---|---|
| C/20 pseudo-OCV full cycle | 1 / 13,413 | time, stored charge, terminal voltage | Current absent. The author's differentiated-capacity simulation current is not imported as measured current. |
| Incremental whole-cell OCV | 2 / 202 total | stored charge and voltage | Split after first maximum Q, with no duplicated/deleted observations. Passed-capacity coordinate is derived per branch; original Q remains alongside it. No time/current. |
| SOC50 / SOC100 power tests | 2 / 1,059 total | time, stored charge, signed current, voltage | Every deposited row retained, including SOC100 conditioning. SOC50 retains 336 rows despite the author's 275-row simulation trim. |
| C/10 partial hysteresis loops | 9 / 39,344 total | source time, source SOC, voltage, signed current, stored charge | Nine native `minor_loops` arrays; original absolute clocks and stored-charge offsets retained. |

Signed current is charge positive, checked against stored-charge increments.
The deposit describes C/2 conditioning and 4C discharge for power tests. Measured
conditioning current reaches approximately 1.1 A; the slow-cycle maximum stored
charge is approximately 1.019 Ah. These do not establish a universal nominal
capacity/C-rate denominator. Reported rates remain protocol context, and no
nominal capacity is invented. None of the selected files has a cell or ambient
temperature trace; the chamber setting is not used to fill either channel.

PD-ECM/R-RC resistances and optimized vectors are not reclassified as intrinsic
solid diffusivity, exchange-current density or Butler-Volmer rate constants.
The raw electrode/GITT observations underlying the modeled OCPn arrays remain
missing. This commercial model stays separate from AMP20, the 9 Ah pouch family
and the distinct APR18650M1B aging dataset.

## Reproduce and use

From an installed checkout:

```bash
python scripts/seed_lfp_studies.py
ebp validate
python scripts/build_data_index.py
python -m pytest tests/test_lfp_studies.py -q
python examples/lfp_studies.py
```

Packaged original files support offline reconstruction of this subset. The full
catalog rebuild `scripts/seed_v01.py --download` also invokes this importer.
No author notebook, pickle or MATLAB is executed. Tests compare extracted nodes
and source addresses with the original XLSX numeric XML, CSV and MAT arrays,
verify row coverage and check the current convention. Metadata and channel checks
do not establish independent electrochemical-model prediction accuracy.

Keep the notices in [DATA_LICENSES.md](../DATA_LICENSES.md), source links, hashes
and transformation labels with downstream copies. The source authors have not
endorsed E-BatP.
