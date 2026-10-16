# Data and third-party code licenses

The root MIT license applies to original project code and documentation, not to
third-party experimental observations or formula implementations.

| Content | Attribution | License |
|---|---|---|
| `src/ebp/data/curves/sintef-*.csv` | Eibar Flores, Sridevi Krishnamurthi, Killian Stokes-Rodriguez, Julie Cathrine Guldahl, Charifa Hakim, Simon Clark, Nils Peter Wagner, Sergi Obrador, Andrés Bernabeu Santisteban; SINTEF and collaborators; Zenodo record 20086298 v3 | CC BY 4.0 |
| SINTEF experimental and electrode metadata | Same dataset and authors | CC BY 4.0 |
| `src/ebp/data/full_cell/*.csv`, originals and normalized derivatives | Chang-Hui Chen, Ferran Brosa Planella, Kieran O'Regan, Dominika Gastol, W. Dhammika Widanage, Emma Kendrick; Zenodo record 4032561 | CC BY 4.0 |
| Two formula expressions and their generated samples | Copyright (c) 2018–2025, the PyBaMM team; v25.4.2 `Prada2013.py` | BSD-3-Clause |
| Non-OCP numeric parameters and kinetics expressions | Copyright (c) 2018–2025, the PyBaMM team; v25.4.2 `Chen2020.py`; Chen et al. 2020 and references therein | BSD-3-Clause |
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
papers' formula equations have not been independently audited in v0.1.

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
