# LG M50 — O'Regan experimental tables and model inputs

[Battery package](../data/batteries/lg-m50-oregan2022.md) · [All extraction decisions](PARAMETER_AUDIT.md)

The [fixed Zenodo deposit](https://zenodo.org/records/5171874) is CC BY 4.0,
version 1.0. Its original 479,705-byte ZIP and license metadata are packaged in
`src/ebp/data/evidence/`. Archive SHA-256:
`1c5052e8af198429c29b6784681e7b1b7d8a4e48dfca03c6fc23df639ce084de`.
The [published study](https://doi.org/10.1016/j.electacta.2022.140700) concerns
LG M50, a 5 Ah 21700 NMC811/graphite-SiOx cell. It is not M50T or M50LT.

## Experimental variant: 55 native tables

| Source folder | Native records | Coordinate and conversion | Retained conditions |
|---|---:|---|---|
| Solid-state Diffusivity | 40 | Source stoichiometry; m2/s unchanged | Negative/positive, specimens 001/002, lithiation/delithiation, 5/15/25/35/45 C; source capacity per area and R-squared retained |
| Exchange Current | 8 | Source stoichiometry; mA/cm2 multiplied by **10** to A/m2 | Two electrodes at 15/25/35/45 C; no specimen identity supplied per table |
| Entropic Term | 4 | Source stoichiometry; mV/K multiplied by **0.001** to V/K | Two electrodes, specimens 001/002; numerical test temperature not supplied per file |
| Electronic Conductivity | 1 | Source temperature in K; S/m unchanged | Positive electrode; native first temperature is **288 K**, not corrected to 288.15 K |
| Thermal Conductivity | 2 | Source temperature in K; W/m/K unchanged | Negative/positive electrode |

Files use the uniform parameter-table representation: ascending coordinate,
`value`, original value, and one-based `source_csv_row`. Diffusivity additionally
preserves capacity, R-squared and source temperature. Source headers, character
encoding, member path, electrode, specimen, direction, temperature and conversion
factor remain in each record. There is no smoothing, averaging across specimens,
resampling or extrapolation. R-squared is fit quality, not an uncertainty interval.

## Three quarantined source files

The `Specific Heat Capacity/Specific_Heat_Capacity_*` CSVs contain 4,500 rows
each and headers claiming J/kg/K, but include negative values and a
physically inconsistent magnitude. Their definition/processing remains unresolved.
They stay unmodified inside the licensed source archive and are listed in the cell
metadata's `quarantined_source_files`. They are **not admitted as physical Cp
tables**. No guessed scale, offset or unit correction is applied.

## Published implementation variant

The separate `oregan-pybamm-v25-4-2` variant contains **73 non-OCP inputs** and
**two borrowed Chen2020 OCP expressions**, transcribed from the pinned
[BSD-3-Clause PyBaMM implementation](https://github.com/pybamm-team/PyBaMM/blob/v25.4.2/src/pybamm/input/parameters/lithium_ion/ORegan2022.py).
The original module is packaged with its source/hash reference. Heat-capacity
model laws come from that implementation; they are not presented as corrections
to the suspect experimental CSVs.

The implementation also borrows CRC collector properties and Landesfeind2019
EC:EMC 3:7 electrolyte laws. Their origins remain explicit. All formulas preserve
source conventions: absolute Kelvin, concentration in mol/m3 and electrode
stoichiometry. Source scalar porosity/reference concentrations are inlined from
this same variant. The importer performs bounded AST substitutions without
executing author code; `10**f(sto)` is normalized to `exp(log(10)*f(sto))`.
The mathematical input domain does not establish an experimental fit interval.

## Full-cell association

The paper points to the [TEC2021 comparison dataset](https://zenodo.org/records/4864437).
Its 0/10/25 C rate tests are discoverable from the model page with a **cross-study,
same-commercial-model** label. They are not asserted to share serialized
specimens with the parameter experiments. The existing Chen2020 tests likewise
remain a distinct study. The parameter ZIP itself contains no full-cell I/V/T
trace. All newly linked full-cell observations remain external.

```python
from ebp import Catalog

c = Catalog()
p = c.get_parameter(
    "oregan-data-diffusivity-negative-electrode-cell001-25-degc-lit"
)
x, diffusivity = p.points()       # all source nodes, not a generated fit
value = p(sto=0.5)               # linear interpolation inside this table's domain
model = c.search_parameters(
    cell_id="lg-m50-oregan2022", variant="oregan-pybamm-v25-4-2"
)                               # keep separate from experimental tables
```
