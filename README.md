<p align="center">
  <img src="assets/logo.png" width="640" alt="E-BatP — Electrochemical Battery Parameters">
</p>
<p align="center"><strong>Traceable electrochemical parameters, connected to the cells and experiments behind them.</strong></p>
<p align="center">
  <a href="https://github.com/FrankSuperG/electrochemical-battery-parameters/actions"><img src="https://github.com/FrankSuperG/electrochemical-battery-parameters/actions/workflows/ci.yml/badge.svg" alt="Catalog and package checks"></a>
  <img src="https://img.shields.io/badge/version-0.2.0-287b78" alt="Version 0.2.0">
  <img src="https://img.shields.io/badge/Python-3.10%2B-203c4c" alt="Python 3.10 or later">
  <a href="DATA_LICENSES.md"><img src="https://img.shields.io/badge/data-per--source%20licenses-758d89" alt="Per-source data licenses"></a>
</p>

E-BatP is an LFP-first library for finding and inspecting inputs to **DFN/P2D, SPM and SPMe** models: electrode OCP curves, diffusion, reaction kinetics, geometry, transport and thermal parameters. Records keep their original definitions, conditions, processing history and cell-match evidence. Parameters with different model conventions are not automatically interchangeable.

**v0.2.0: 12 OCP records · 114 other parameter records · 14 full-cell test files · 4 cell or study-family entries.** The repository is private. The viewer runs locally; no public hosting workflow is configured.

## Coverage and cell matches

| Cell / material | OCP | Diffusion & kinetics | Full-cell observations | Match evidence |
|---|---|---|---|---|
| **A123 AMP20M1HD-A, 20 Ah LFP pouch** | C/25 full-cell pseudo-OCV reported; electrode OCP points not located in the selected deposit | 27 Table 1 values at 30/50/70% SOC + 3 conditional diffusivities; shared diffusion time, volumetric kinetics, transport and thermal fits | 1 Cell I 4C full-discharge trace; current, voltage and thermal-grid mean | **Same commercial model, same study.** Table 1 specimen letter unresolved; no identical-specimen claim |
| **A123 high-power 9 Ah LFP pouch** | External full-cell pseudo-OCV workbooks indexed; redistribution license unresolved | Model assumes fast diffusion; no finite diffusivity or kinetic fit imported | 10 CC charge/discharge files at 2/4/6/8/10C | **Same study family.** Exact part number and per-file serial undisclosed |
| **BPX LFP/graphite 2 Ah 18650 example** | 2 electrode expressions with supplied stoichiometry bounds | 46 scalar values, including two diffusivities, BPX rate constants and activation energies | No matching raw tests supplied | **Unmatched commercial identity.** Chemistry, capacity and format do not identify a cell model |
| **LG M50, 5 Ah NMC811/graphite–SiOx** | 1 effective negative-electrode expression | 36 scalars + 2 exchange-current functions from pinned Chen2020 implementation | 3 original Maccor CSVs and normalized derivatives | **Same model, same study.** Characterization and validation specimens not proven identical |
| **SINTEF LFP and graphite half-cells** | 8 C/50 pseudo-OCP branches from 4 specimens | Not imported | No commercial full-cell match | **Material only** |
| **Afshar2017 LFP expression** | 1 expression via pinned PyBaMM implementation | Not imported | None established | **Material only** |

A record is one stored value, expression or measured branch—not an independent experiment. The 30 AMP20 parameter records include repeated conditions and three derived values. These are partial packages with explicit gaps, not independently validated, drop-in model parameter sets.

The strongest new LFP association is [Lin et al. (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/) and its [Oxford experiment deposit](https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513). Its fitted diffusion time is shared by both electrodes. We expose `D = r²/t_d` using the implementation's **assumed 5 µm radius**, with that condition attached; it is not an independently measured intrinsic LFP diffusivity. The deposited full-discharge trace is linked for future model comparison; this project has not reproduced the paper's validation.

## Install and browse

Use Python 3.10+; Python 3.12 is recommended.

```bash
git clone https://github.com/FrankSuperG/electrochemical-battery-parameters.git
cd electrochemical-battery-parameters
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
ebp validate
ebp serve
```

Open [the local viewer](http://127.0.0.1:8765). Filter and compare OCPs, switch between cell packages, inspect coverage and parameter origins, and download data with metadata. The viewer uses local assets, without CDNs, analytics or remote fonts. `ebp serve` binds to `127.0.0.1`; `ebp build-site --output site` only writes static files.

## Python and CLI

```python
from ebp import Catalog

catalog = Catalog()
curve = catalog.get("bpx-lfp18650-lfp-ocp")
voltage = curve(0.5)                         # V vs Li/Li+
x, voltage = curve.sample(501)              # generated samples, not measurements
curves = catalog.search(material="LFP")
linked_ocp = catalog.search(cell_id="bpx-lfp-18650-2ah-undisclosed")

parameters = catalog.search_parameters(
    cell_id="a123-amp20m1hd-a", category="diffusion"
)
for parameter in parameters:
    print(parameter.value, parameter.record["unit"], parameter.record["conditions"])

tests = catalog.linked_tests("a123-amp20m1hd-a")
rows = catalog.full_cell_data(tests[0]["id"], normalized=True)
```

```bash
ebp search --material LFP
ebp search --cell bpx-lfp-18650-2ah-undisclosed
ebp parameters --cell a123-amp20m1hd-a --category kinetics --json
ebp tests --cell a123-high-power-pouch-9ah
ebp show a123-amp20-effective-diffusivity-soc50
ebp export bpx-lfp18650-lfp-ocp --output formula.csv --count 2001
```

Measured OCP tables support linear interpolation and PCHIP. `.points()` returns native retained points; `.export_csv()` preserves them unless a resampling count is explicit. Formulas use a restricted AST interpreter, without `eval` or arbitrary Python imports. Non-finite inputs and out-of-domain evaluation are rejected; no default extrapolation is allowed.

Original LG M50 CSVs encode current as a magnitude plus `Md=C/D`. Normalized files use **charge-positive current**, temperatures in K and source row/index references. Oxford MAT/ZIP originals stay at checksum-pinned URLs; normalized CSVs retain every time row. Source NaNs become empty fields and are counted in metadata. The 9 Ah temperature column has conflicting source descriptions, so its exact sensor/ROI identity remains unresolved. A model interface that uses discharge-positive current needs an explicit sign conversion.

## Optional PyBaMM OCP adapter

```bash
python -m pip install -e '.[pybamm]'
PYBAMM_DISABLE_TELEMETRY=true python examples/pybamm_ocp.py
```

`curve.to_pybamm()` creates a linear `pybamm.Interpolant` with extrapolation disabled. Expressions are sampled for this conversion. Measured branch-throughput curves require an explicit `StoichiometryMapping(theta_start, theta_end, evidence)`: no absolute electrode balancing is inferred. The adapter supplies an OCP component, not a complete cell model.

## Scientific boundaries

- **Electrode OCP, full-cell pseudo-OCV and loaded terminal voltage remain distinct.** Neither Oxford study's conventional allocation of full-cell OCV establishes measured half-cell OCPs.
- **Electrode lithium fraction, normalized branch throughput and whole-cell SOC remain distinct.** Plots group different coordinate types and directions separately.
- **Kinetic definitions travel with values.** AMP20 volumetric exchange current in A/m³, LG surface exchange-current laws, and BPX rate constants in mol/(m²·s) cannot be substituted directly.
- **Measured, fitted, derived, borrowed and assumed origins remain visible.** Optimizer initial guesses are not imported as fitted results. BPX's estimated thermal properties are labeled.
- **Unknown information stays unknown.** Room temperature does not become 298.15 K; nominal capacity does not create a commercial identity; a study link does not establish the same specimen.
- **No independent full-cell model validation is claimed.** Data checks and adapter tests establish implementation consistency, not DFN/SPM/SPMe predictive accuracy.

PyBaMM's `Prada2013` file borrows its LFP OCP from Afshar2017 and its graphite OCP from Chen2020. Scientific attribution is recorded per function. BPX electrolyte and entropy sources are disclosed in its header; those non-OCP functions/tables are not yet imported.

## Reproduction and layout

```bash
python -m pip install -e '.[dev,pybamm]'
python scripts/seed_v01.py --download   # reconstructs the base and LFP expansion
ebp validate
PYBAMM_DISABLE_TELEMETRY=true python -m pytest -q
ebp build-site
python -m build
```

Upstream commits, URLs and SHA-256 hashes are pinned; Zenodo originals also retain source MD5 checks where supplied. Cached Parquet/MAT/ZIP inputs are ignored by Git. ORA returns HTTP 403 to GitHub-hosted runners, so CI restores the four Oxford inputs from an attributed [private source-cache release](https://github.com/FrankSuperG/electrochemical-battery-parameters/releases/tag/upstream-lfp-v0.2.0) and verifies the same primary-source SHA-256 pins. Primary URLs remain authoritative. Only the selected observations, transcribed evidence, metadata and source notices are packaged. `requirements-lock-py312.txt` documents one Python 3.12 verification environment, not a universal lock.

```text
src/ebp/data/             Authoritative packaged catalog
  catalog.json           Electrode OCP records and representations
  parameters.json        Scalars and kinetic functions
  cells.json             Identities, coverage and match evidence
  full_cell_tests.json    Test metadata, processing and links
  sources.json           Papers, datasets and software roles
  assets.json            Original URLs, versions and checksums
  curves/                Retained OCP points and source coordinates
  full_cell/             Original CSVs / normalized observations
  evidence/              Explicit published-table transcriptions
  schema/                Structural constraints
src/ebp/web/              English static viewer and companion logo
src/ebp/licenses/         Upstream licenses and dataset notices
scripts/seed_lfp.py       LFP extraction and normalization
scripts/lfp_assets.json   Pinned LFP source assets
```

See [data definitions](docs/DATA_MODEL.md), [curation and match decisions](docs/CURATION.md), [roadmap](docs/ROADMAP.md) and [contribution guide](CONTRIBUTING.md).

## Attribution and licenses

Cite the scientific sources for the records you use and retain upstream notices. Project code, documentation and logo use MIT; experimental data and imported implementations keep their source licenses. See [DATA_LICENSES.md](DATA_LICENSES.md) and [CITATION.cff](CITATION.cff).

| Source | Role / license |
|---|---|
| [SINTEF / Zenodo v3](https://zenodo.org/records/20086298) | Half-cell measurements · CC BY 4.0 |
| [Afshar et al., 2017](https://arxiv.org/abs/1709.03970v1) | LFP OCP scientific attribution |
| [Chen et al., 2020](https://doi.org/10.1149/1945-7111/ab9050), [full-cell data](https://zenodo.org/records/4032561) | LG M50 parameter attribution / observations · CC BY 4.0 data |
| [PyBaMM v25.4.2](https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion) | Pinned OCP / Chen2020 implementations · BSD-3-Clause |
| [BPX example](https://github.com/FaradayInstitution/BPX/blob/0f591336937c2c57509f20ab23f9908e58f7a757/examples/lfp_18650_cell_BPX.json) | LFP parameter example · MIT |
| [Lin et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938860/), [data](https://ora.ox.ac.uk/objects/uuid:5f4abb09-c993-4799-9cb1-980218bde513), [code](https://github.com/Battery-Intelligence-Lab/multiscale-coupling/tree/dba3649f2eeb4228d2849e4d4e748c91ed6ad7a4) | AMP20 fitted parameters / observations · CC BY 4.0; code · BSD-2-Clause |
| [Kumtepeli et al., 2026](https://doi.org/10.1016/j.jpowsour.2025.238764), [Oxford data](https://ora.ox.ac.uk/objects/uuid:fe9bad3e-8a72-4e3b-8f01-fec3324b6758) | 9 Ah study family / observations · CC BY 4.0 data |

The README identity is a companion to [Electrochemical Battery Model Atlas](https://github.com/FrankSuperG/electrochemical-battery-model-atlas); its generation brief is recorded in [assets/README.md](assets/README.md).
