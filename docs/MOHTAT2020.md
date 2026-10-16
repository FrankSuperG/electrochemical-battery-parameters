# Mohtat2020: official data and parameter association

The [official dataset](https://deepblue.lib.umich.edu/data/concern/data_sets/kp78gg60j)
and DOI [10.7302/wwma-hx25](https://doi.org/10.7302/wwma-hx25) are open access under
CC BY 4.0. A normal browser downloaded the author's zipped dataset on 2026-10-16.
The earlier HTTP 403 was a failure of automated access, not proof that the data
were unavailable. No alternate paper-download service is used or linked.

Ten original files are packaged byte-for-byte with URL/SHA-256 pins in
`scripts/mohtat_assets.json`: five MATs, four MATLAB files and `READ_ME.pdf`.
The download ZIP's generated metadata report is not treated as experimental data;
the individual original files are the reproducible inputs. Curation parses MATLAB
numeric assignments and expressions without executing the author's code.

## Measurements and missing channels

| File | Nominal charge rate | Protocol current magnitude | Paired Q/V/T rows |
|---|---:|---:|---:|
| Cover10.mat | 0.1C | 0.5 A | 3,561 |
| Cover5.mat | 0.2C | 1 A | 1,745 |
| Cover2.mat | 0.5C, source conflict noted below | 2.5 A in main.m | 682 |
| Cover1.mat | 1C | 5 A | 330 |
| 2C.mat | 2C | 10 A | 156 |

The README defines `Q_data` as the capacity coordinate synchronized with voltage.
`Vt_data` is terminal voltage and `Temp_data` is cell temperature; plotting code
labels Ah, V and degrees Celsius. All 6,474 paired rows are retained. Temperature
is converted to kelvin; the project's CSVs do not apply the moving average used
by the author's model-comparison plot. Expansion and derivative arrays retain
separate capacity coordinates in the original MATs and are not aligned by index.

**No measured current or original time array is present.** The README reports
10-second acquisition, but that interval is not imposed on the processed exports.
The author's comparison script constructs a time grid from the simulated end
time; the project does not use that synthetic time as an observation. Nominal
currents stay in protocol metadata and never populate the measured-current
column. Capacity, not reconstructed time or SOC, is the plotted independent axis.

The README describes CC charge to 4.2 V, CV to C/40, three-hour rest and same-rate
discharge, after conditioning; the last of three repeats is reported. The deposit
contains only the five charging exports. Full discharge, C/20 pseudo-OCV, complete
CV/rest channels, original cycler records and raw half-cell OCP points are absent.
No exact specimen identifier is supplied. The UMBL research pouch is laboratory
fabricated; it is not an undisclosed commercial model.

**Cover2 conflict:** Methods says C/2.5, the inventory says C/2, and `main.m`
associates this file with -2.5 A (author convention: negative means charge).
The catalog uses nominal 0.5C/2.5 A from inventory and code, preserves the conflict,
and does not claim a verified instrument current.

## Same study, distinct implementations

The deposited model and experiments explicitly accompany the same paper,
[10.1149/1945-7111/aba5d1](https://doi.org/10.1149/1945-7111/aba5d1).
This establishes a study/model lineage, not a same-specimen dissection join or
independent predictive validation. The NMC532 label comes from the pinned PyBaMM
module; the deposit uses NMC without a composition assay.

- Original graphite OCP uses `exp(-75*(x+0.007))`; PyBaMM v25.4.2 uses
  `exp(-75*(x+0.001))`. Both expressions are retained as separately named variants.
- Positive OCP coefficients agree. The author expressions retain the balancing
  endpoints explicitly supplied by `main.m`.
- Author diffusivities are constant 5e-15 and 8e-15 m²/s. PyBaMM agrees at its
  reference temperature but adds Arrhenius dependence.
- Author k0 values are 1.1e-11 and 5e-11. The DAE defines
  `i0=F*k0*sqrt(c_e)*c_s,max*sqrt(theta*(1-theta))`. PyBaMM uses rounded,
  unit-converted exchange-current prefactors and added temperature laws. The
  source's inline k0 unit comment is incomplete; the catalog definition follows
  the DAE concentration powers and keeps this issue visible.
- Thermal geometry and multiparticle radii/population fractions require review;
  no automatic effective-radius or cooling-area substitution is performed.

The 33 imported original-author scalar inputs have
`conditions.parameterization_variant=original_author_mpm`; the 38 earlier
implementation inputs have `pybamm_v25_4_2`. Inspect
`data/evidence/mohtat2020-parameter-crosswalk.json` and the viewer Variant filter.
These are partial input collections, not two complete drop-in model sets.

The 2021 cyclic-aging dataset is a different study and has not been silently
substituted for the 2020 charging deposit. Source files, CSVs, metadata and license
notices travel together in the cell's offline ZIP bundle.
