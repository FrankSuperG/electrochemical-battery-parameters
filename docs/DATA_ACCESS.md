# Find, download and use data

Start at **[Browse all data](../data/README.md)**. You can use the GitHub file
links without installing Python or running a website. If repository access is
restricted, sign in with an account that has access.

## 1. Find the right file

| What you want | Start here | What you get |
|---|---|---|
| Different LFP electrode OCP curves | [LFP OCP index](../data/ocp/README.md#lfp) | Each curve has a CSV and JSON definitions/source record; material-level measurements are not automatically commercial-cell matches |
| Another material's OCP | [All OCP materials](../data/ocp/README.md) | Separate material, electrode and coordinate labels |
| Parameters and tests for a particular cell | [Cell index](../data/README.md#choose-a-cell-or-study) | A page with parameter CSV/JSON, OCP links, complete test CSVs, original files, matching evidence and gaps |
| A practical same-model/same-study starting case | [LG M50](../data/cells/lg-m50.md) | Two OCP expressions, 38 other inputs and three current/voltage/temperature test files |
| LFP parameters with a full-cell discharge | [A123 AMP20](../data/cells/a123-amp20m1hd-a.md) | Fitted/derived inputs and one 4C trace; electrode OCP remains missing |
| LFP CC charge/discharge tests | [A123 9 Ah study family](../data/cells/a123-high-power-pouch-9ah.md) | Ten files at 2/4/6/8/10C; finite diffusion/kinetic inputs and reusable electrode OCP remain missing |
| LFP laboratory half/full-cell V-Q association | [ISU-UConn](../data/cells/isu-uconn-lfp-graphite-lab.md) | Four C/20 pseudo-OCP branches and 21 full-cell branches from 11 configurations; reference details and I/t/T remain unresolved |
| A123 electrode-model potentials and current/voltage tests | [18650M1A / Jahn2024](../data/cells/a123-18650m1a-jahn2024.md) | Two modeled OCPn tables and 14 full-cell branch/array exports; current only in power/loop files, no temperature trace |
| Mohtat author inputs and charge data | [Mohtat2020](../data/cells/mohtat2020-nmc532-pouch.md) | Separate author/PyBaMM parameter variants and five V–Q/T–Q files; measured current and original time are absent |
| Grouped SPMe and same-study dynamic validation data | [LG M50LT / Hallemans2025](../data/cells/lg-m50lt-hallemans2025.md) | 18 fitted groups, measured t/I/V drive cycle and EIS evidence; OCP reuse permission, temperature and standalone CC observations remain missing |
| MJ1 OCP, diffusion and kinetics with source tables | [LG MJ1 / DLR-SINTEF](../data/cells/lg-mj1-dlr-sintef.md) | Four pseudo-OCP branches, 22 scalars and 20 native tables; model/direction variants and original error bounds retained. No intact-cell full-cell test verified |

Parameters CSVs include a `name`, `category`, `unit`, `definition`, conditions,
source IDs, origin and variant column. Filter by name as well as category to find
diffusivity, kinetics, geometry, thermal or transport inputs. The JSON contains
full metadata and source evidence. Empty or missing data are not replacement
values and are not zeros.

## 2. Download from GitHub

1. Open the cell/material page and click a **CSV** link for values or a **JSON**
   link for definitions and provenance.
2. On the file page, choose **Raw** to view the file or use **download raw file**
   to save it. Download the complete file rather than copying a preview table;
   large files may not have a complete GitHub preview.
3. Keep the associated JSON and the relevant notices from
   [DATA_LICENSES.md](../DATA_LICENSES.md). Preserve attribution when using data.

These controls are described in the
[official GitHub file guide](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-and-understanding-files#viewing-or-copying-the-raw-file-content).
For the full repository, use **Code → Download ZIP**, or
[download the repository ZIP](https://github.com/FrankSuperG/electrochemical-battery-parameters/archive/refs/heads/main.zip)
while signed in. Extract it before using the relative paths in the examples.
The navigation uses authenticated GitHub file links, so a private repository
does not need anonymous raw-file URLs.

### Which representation did I download?

- **Retained table:** links to the stored table under `src/ebp/data/curves/`.
  All retained points and source columns are preserved. The JSON distinguishes
  measurements, published tables and modeled OCPn. `model_ocp` is not a raw
  measurement. `reference=unresolved` must be resolved before PyBaMM adaptation.
- **Generated samples:** `data/ocp/*-sampled.csv` contains 2,001 evaluations of a
  stored expression across its documented domain, rounded to 12 significant
  digits. It is a convenient numeric
  representation of a formula, not new measurements. The formula is in the JSON.
- **Full-cell CSV:** links to `src/ebp/data/full_cell/`. These are complete stored
  series, not the viewer's display-decimated traces. Normalized channels use
  charge-positive current, seconds, volts and kelvin, with source row references.
- **Parameter CSV:** `data/parameters/` contains scalars or expression strings
  with units and definitions. Do not treat an expression as a scalar or combine
  alternative parameterization variants.

CSV files can be opened in a spreadsheet using UTF-8 and comma delimiters.
For parameters, filter rows by `name`/`category` and read the definition and
conditions before copying a value. Blank temperatures stay unknown; a Celsius
conversion is only valid for an actual absolute-temperature value.

## 3. Read files without installing E-BatP

After cloning or extracting the repository, run Python from its root. This uses
only Python's standard library:

```python
import csv
from pathlib import Path

path = Path("src/ebp/data/full_cell/LGM50_cell02-normalized.csv")
with path.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

print(len(rows), rows[0])
# rows contain strings; an empty string means unavailable, not zero.
current_A = [float(row["current_charge_positive_A"]) for row in rows
             if row["current_charge_positive_A"] != ""]
```

For a cell's parameters, replace the path with `data/parameters/lg-m50.csv`.
For an OCP table, use the CSV path linked by the OCP index. When analyzing paired
channels, retain row alignment and explicitly handle missing values instead of
filtering each channel independently and then joining by array index.

## 4. Use interpolation and linked records in Python

Install from a checkout with Python 3.10+ (3.12 recommended):

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

### Find and evaluate an LFP OCP

```python
from ebp import Catalog

catalog = Catalog()
for curve in catalog.search(material="LFP"):
    print(curve.id, curve.record["x"]["kind"])

curve = catalog.get("sintef-lfp-d07eb6-c3-lithiation")
print(curve.record["x"], curve.record["direction"])
x, potential_V = curve.points()            # every retained source point
values_V = curve([0.2, 0.5, 0.8], method="pchip")
```

This measured branch uses **normalized branch capacity**, not absolute electrode
stoichiometry or whole-cell SOC. A material-level LFP curve is not automatically
the OCP of AMP20 or another A123 cell. Evaluation rejects extrapolation.
For a stored formula, call `curve.sample(count)` instead of `curve.points()`.

### Find parameters and read a linked full-cell file

```python
for parameter in catalog.search_parameters("diffusiv", cell_id="lg-m50"):
    record = parameter.record
    print(record["id"], record["representation"], record["unit"])

tests = catalog.linked_tests("lg-m50")
for test in tests:
    print(test["id"], test["protocol"], test["missing_items"])

rows = catalog.full_cell_data("chen-lgm50-cell02", normalized=True)
```

Match evidence belongs to the selected cell/study. Selecting an OCP or parameter
does not automatically assemble a complete model. Rate constants, exchange-current
laws, effective diffusivities and grouped parameters need their own definitions.

### Export or inspect with the CLI

```bash
ebp cells
ebp search --material LFP
ebp parameters diffusiv --cell lg-m50 --json
ebp tests --cell lg-m50
ebp export sintef-lfp-d07eb6-c3-lithiation --output lfp-ocp.csv
ebp export sintef-lfp-d07eb6-c3-lithiation --format json --output lfp-ocp-metadata.json
```

The default table export retains its points. Explicit `--count` resamples a
table; formula exports are generated samples. Keep metadata with either export.

## 5. Download a complete offline cell bundle

```bash
ebp serve
```

Open `http://127.0.0.1:8765`, select a cell under **Cell packages**, then choose
**Offline bundle ZIP**. The archive includes cell-scoped data, metadata,
available original sources and license notices. This runs locally; hosting is
optional. For Mohtat, use the variant selector when inspecting parameters and
select a coherent variant when modeling; the archive retains both for provenance.

Mohtat's charge exports use native `charge_capacity_Ah`. They have no original
time or exported measured current. Do not manufacture these from a C-rate, Q/I
or a row index. Temperature is measured against capacity; the current evidence
supports nominal-protocol V–Q comparison rather than a measured-input V–t test.

## File locations and model integration

| Location | Role |
|---|---|
| [`data/`](../data/README.md) | Generated GitHub navigation, scoped parameter exports, OCP metadata and formula samples |
| [`src/ebp/data/`](../src/ebp/data/) | Authoritative catalog and stored observations used by the Python package |
| [`sources.json`](../src/ebp/data/sources.json) / [`assets.json`](../src/ebp/data/assets.json) | Primary sources, versions, source roles and checksums |
| [`templates/`](../templates/README.md) | Empty contribution templates; these are not experimental data |
| `site/` after `ebp build-site` | Generated local website and offline bundle downloads; not committed to Git |

Paths inside exported JSON records resolve from the authoritative data root,
not from the JSON export's folder. The export provides `canonical_data_root`
(under `export` for OCP metadata) so those paths can be resolved from a checkout.
Primary-source URLs are also retained for originals stored externally.

For model use, read the [PyBaMM OCP example](../examples/pybamm_ocp.py) or the
[CPG-SPMT integration audit](CPG_SPMT_VALIDATION.md). Electrode balancing,
initial state, kinetic definitions and parameter grouping require explicit
choices. The files and data checks do not establish independent model accuracy.
