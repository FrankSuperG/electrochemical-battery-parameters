# Data and third-party code licenses

The root MIT license applies to original project code and documentation, not to
third-party experimental observations or formula implementations.

| Content | Attribution | License |
|---|---|---|
| `src/ebp/data/curves/sintef-*.csv` | Eibar Flores, Sridevi Krishnamurthi, Killian Stokes-Rodriguez, Julie Cathrine Guldahl, Charifa Hakim, Simon Clark, Nils Peter Wagner, Sergi Obrador, Andrés Bernabeu Santisteban; SINTEF and collaborators; Zenodo record 20086298 v3 | CC BY 4.0 |
| SINTEF experimental and electrode metadata | Same dataset and authors | CC BY 4.0 |
| `src/ebp/data/full_cell/lg-m50-*.csv`, originals and normalized derivatives | Chang-Hui Chen, Ferran Brosa Planella, Kieran O'Regan, Dominika Gastol, W. Dhammika Widanage, Emma Kendrick; Zenodo record 4032561 | CC BY 4.0 |
| PyBaMM OCP expressions and their generated samples | Copyright (c) 2018–2025, the PyBaMM team; v25.4.2 pinned parameter modules | BSD-3-Clause |
| LG M50 non-OCP numeric parameters and kinetics expressions | Copyright (c) 2018–2025, the PyBaMM team; v25.4.2 `Chen2020.py`; Chen et al. 2020 and references therein | BSD-3-Clause |
| Original software, schemas and explanatory documentation | FrankSuperG | MIT |

SINTEF dataset: https://doi.org/10.5281/zenodo.20086298

Changes to SINTEF data: selected the third recorded cycle, selected the two
constant-current steps, excluded rest, removed repeated capacity values (first
point retained), added a branch-relative capacity coordinate, and retained source
row positions. No voltage smoothing or resampling is applied to distributed CSV
files. The browser graph samples values for display; CSV downloads preserve the
full extracted points. Detailed counts and transformation parameters are in each
record's provenance. The source authors have not endorsed this project.

Formula implementation: https://github.com/pybamm-team/PyBaMM/blob/v25.4.2/src/pybamm/input/parameters/lithium_ion/Prada2013.py

Formula changes: renamed `sto` to `x`, removed the NumPy namespace, and retained
the original coefficients. Scientific attribution is Afshar et al. (2017) for LFP
and Chen et al. (2020) for graphite, as stated in that upstream file. The original
papers' formula equations have not been independently audited in this release.

LG M50 full-cell data: https://doi.org/10.5281/zenodo.4032561

Original CSV files are copied byte-for-byte. Normalized derivatives skip the
instrument banner, use Md=C/D to interpret current magnitude as charge-positive
signed current, convert temperatures from degrees Celsius to kelvin, and retain
record numbers and zero-based original file-row positions. No smoothing or
resampling is applied to distributed test files. Source authors have not endorsed
this project. Browser plots select the four validation discharge steps and sample
them for display; original and normalized downloads preserve every observation.

The kinetics implementation fixes the gas constant to 8.314462618 J/mol/K and
retains the upstream Arrhenius law and concentration convention. Numeric parameters
are extracted without executing the source dictionary. No claim is made that each
entry is a directly measured property of the same physical specimen.

License texts are distributed in `src/ebp/licenses/` and copied into the local
viewer. Keep attribution, source links and change notices when redistributing
data or generated exports. Each record carries its own license identifier.

## LFP expansion in v0.2

| Content | Attribution / source | License |
|---|---|---|
| `a123-amp20-*.csv` and Table 1 evidence / parameters | Jie Lin, Howie N. Chu, David A. Howey, Charles W. Monroe; 2022 paper and Oxford ORA deposit, DOI 10.5287/bodleian:NGQkq49wG | CC BY 4.0 |
| Model radius provenance | University of Oxford and multiscale-coupling developers; pinned `Battery_model.m` | BSD-2-Clause |
| `a123-9ah-*.csv` | Oxford high-power pouch-cell researchers; ORA deposit, DOI 10.5287/ora-eonzaxjpm | CC BY 4.0 |
| BPX LFP example OCP expressions, scalar inputs and generated samples | Copyright (c) 2022 University of Oxford; About:Energy parameterization; pinned FaradayInstitution/BPX example | MIT |
| E-BatP companion logo | Original project identity generated with ImageGen; generation brief in `assets/README.md` | MIT |

The earlier full-cell CSV attribution to Chen applies specifically to `lg-m50-*`
files, not to the Oxford additions above. Likewise, the PyBaMM parameter license
applies to LG M50 inputs, not every scalar in the expanded catalog.

Oxford changes: selected one AMP20 full-discharge MAT and ten 9 Ah CC MAT members;
retained signed current, voltage and all source time rows; converted temperatures
from Celsius to kelvin; expressed documented 1 Hz sample indices as relative
seconds; left absent ambient temperatures empty. Source NaNs become empty CSV
fields with missing counts. For AMP20, temperature is the arithmetic mean of the
provided thermal grid without an additional ROI. For the 9 Ah data, ambiguity in
the fourth column's sensor/ROI description is retained. Large MAT/ZIP originals
remain external, checksum-pinned downloads. No smoothing or imputation is applied.
The dataset copyright notices are preserved verbatim in
`Oxford-Lin2022-data-notice.txt` and `Oxford-9Ah-data-notice.txt`.

Table 1 changes: transcribed the nine This work rows at three SOCs, converted
units explicitly, and derived three conditional diffusivities from a fitted time
and the source model's assumed radius. The local transcription hash identifies
our evidence JSON, not the publisher HTML. These are effective model parameters,
not new independent measurements.

BPX changes: copied two expressions verbatim, limited them to supplied operating
stoichiometry bounds, and transcribed numeric scalar fields. Estimated thermal
properties and borrowed sources are disclosed. Other functional fields are not
imported. `BPX-MIT.txt` preserves its license; `Oxford-BSD-2-Clause.txt` preserves
the multiscale model license. Related 9 Ah OCP workbooks with unresolved reuse
licensing are linked as external references only. Source authors have not
endorsed this project.

The private `upstream-lfp-v0.2.0` release mirrors four original Oxford files for CI
reproduction because ORA rejects hosted-runner downloads with HTTP 403. The files
are byte-identical, retain CC BY 4.0, and include both original dataset notices.
Release notes preserve authors, primary URLs, DOIs, license and SHA-256 values.
The source-cache release does not change the scientific attribution or license.

## Multi-material expansion in v0.3

The additional NMC111/NMC532/LNMO/silicon/silicon–graphite CSVs are selected
observations from the same SINTEF Zenodo v3 dataset and retain CC BY 4.0 and its
existing attribution. Processing follows the fixed cycle-3 C/50 branch rule,
with source coordinates, duplicate-capacity removal counts and no smoothing.
The two SiGr formulations are retained separately. No new independent study or
commercial-cell association is inferred from adding specimens or materials.

Additional OCP, diffusion and kinetic implementations are from PyBaMM v25.4.2
`Chen2020.py`, `Marquis2019.py`, `Mohtat2020.py` and `NCA_Kim2011.py`, under the
existing PyBaMM BSD-3-Clause notice. Scientific attributions are recorded per
module/function; Dualfoil borrowing is explicit for Marquis electrode functions.
AST-local substitution and constant folding preserve the source math; the gas
constant is fixed for portable evaluation. Source reference parameters used by
Kim kinetics are resolved from that same pinned parameter set. Native measured
points are not claimed for any implementation expression or its generated CSV.

## Matched full-cell expansion in v0.4

`Ecker2015.py` and `Ai2020.py` inputs retain the existing PyBaMM v25.4.2
BSD-3-Clause notice. Ecker scientific attribution is Ecker2015 I/II and
Richardson2020 / Simon O'Kane; Enertech attribution is Ai2020 and Rieger2016.
Borrowed Dualfoil diffusion/kinetics remain labeled for Ai2020. AST substitutions
fix R=8.314462618 J/mol/K and F=96485.33212331001 C/mol.

The six new voltage files, three temperature-rise channels and two published
Enertech OCP tables are redistributed by the PyBaMM team in
https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2 under BSD-3-Clause.
Its separate Copyright (c) 2024, PyBaMM Team notice is preserved verbatim in
`src/ebp/licenses/PyBaMM-data-BSD-3-Clause.txt`. Scientific authors and the
figure-history chain are recorded in `docs/FULL_CELL_MATCHING.md`.

Changes: original time/voltage and temperature-rise files are copied byte-for-byte
to `data/evidence/`. Normalized CSVs retain all numeric source pairs and row order
with one-based source positions; unavailable current and absolute temperatures
stay empty. Temperature rise stays in separate native-clock sidecars, without
interpolation, synchronization or assumed ambient temperature. Ecker points are
upstream figure digitizations, not instrument raw. Enertech tables omit comments
and the explicitly synthetic negative-OCP `(0,3.5)` guard; all other numeric points
and source line references are retained. No smoothing or extrapolation is added.

The Mohtat DOI is indexed as a lead only. DataCite declares CC BY 4.0; no dataset
files are redistributed because access was unavailable. Source authors have not
endorsed this project.
