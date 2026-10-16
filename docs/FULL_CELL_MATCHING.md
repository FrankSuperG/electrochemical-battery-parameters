# Full-cell matching ledger

Audit date: 2026-10-16. This covers sources imported or investigated for v0.4,
not all available literature. Machine-readable results are in
`src/ebp/data/matching_audit.json` and each cell's `evidence_matrix`.

## Imported associations

| Cell / study | OCP / diffusion / kinetics | Basic full-cell data | Match and remaining gaps |
|---|---|---|---|
| LG M50 / Chen2020 | Both electrode OCP fits; two scalar D inputs; two exchange-current laws | Three Maccor files with CCCV charging and CC discharges at 0.1/0.5/1/1.5C; measured current, voltage and temperatures | Same commercial model and study. Validation sample IDs available; dissection/characterization specimen join unresolved. Individual parameter origins remain implementation-level unless established. |
| A123 AMP20M1HD-A / Lin2022 | No electrode OCP points imported; shared fitted diffusion time, three conditional D values from assumed 5 µm radius; volumetric kinetic fits | One Cell I 4C full-discharge trace with measured current/voltage and thermal-grid mean | Same commercial model and study. Table 1 specimen letter unresolved; D is not an intrinsic measured electrode diffusivity. C/25 full-cell pseudo-OCV is reported but absent from selected deposit. |
| A123 9 Ah high-power pouch / Oxford | External pseudo-OCV workbooks only; no imported finite D or kinetic fit | Ten CC files, charge/discharge at 2/4/6/8/10C, with measured current | Same study family. Exact commercial part and serials unresolved. Fast-diffusion assumption and unresolved workbook reuse license remain visible. |
| UMBL research pouch / Mohtat2020 | Two author OCPs and 33 original inputs alongside 38 explicitly separate PyBaMM inputs | Five capacity-coordinate charging exports with measured V/T at nominal 0.1/0.2/0.5/1/2C | Same study family. Current/time/discharge/C20 exports absent; graphite OCP and Cover2 protocol differences documented. See [Mohtat audit](MOHTAT2020.md). |
| Kokam SLPB75106100 / Ecker2015 | Two figure-fitted OCP expressions, two D(sto,T) fits and two exchange-current laws via Richardson/PyBaMM | Two CC discharge curves, 1C and 5C at 25°C, time/voltage only | Same named model and Ecker study lineage. **Figure digitization**, not instrument raw. Current, charge, capacity and absolute measured temperature channels absent; identical specimen unresolved. |
| Enertech LCO/graphite / Ai2020–Rieger2016 | Two published OCP tables; two diffusivity functions and two exchange-current laws borrowed from Dualfoil | Four BOL voltage series at 0.1/0.5/1/2C; three temperature-rise sidecars at 0.5/1/2C | Same study family; exact part/specimen unresolved. Published experimental series, instrument-raw status unestablished. Measured current/charge/capacity absent. Borrowed D/kinetics are not same-cell measurements. |

The six new discharge series come from
[PyBaMM data v1.0.2](https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2),
with SHA-256 pins in `scripts/fullcell_assets.json`. Its
[v1.0.0 notes](https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.0)
document WebPlotDigitizer extraction from Figure 8 of
[Richardson2020](https://doi.org/10.1016/j.electacta.2020.135862), attributing the
experiments to [Ecker II](https://doi.org/10.1149/2.0541509jes).
[Ecker I](https://doi.org/10.1149/2.0551509jes) describes the 7.5 Ah cell
characterization. Digitization uncertainty and instrument timestamps are absent.

**Capacity scaling:** Ecker2015.py specifies 0.15625 Ah; the commercial cell is
7.5 Ah. Both are retained. No automatic current/geometry/heat scaling is applied.
Thermal properties are borrowed from another 5 Ah Kokam cell; tab positions have
another source. NCO follows the upstream label; a precise NMC/NCA ratio is not
inferred.

The official [Enertech example](https://docs.pybamm.org/en/v26.6.0.0/source/examples/notebooks/models/Validating_mechanical_models_Enertech_DFN.html)
uses these files with Ai2020. The lineage is
[Ai2020](https://doi.org/10.1149/2.0122001JES) and
[Rieger2016](https://doi.org/10.1149/2.0441608jes). Originals are retained
byte-for-byte. The negative OCP source labels `(0, 3.5 V)` as an extra
extrapolation guard; that synthetic point is excluded. Other points remain
unchanged, without resampling. The positive table retains its supplied
0.4–0.998903136 domain. Published tables are distinct from SINTEF instrument-derived
C/50 branches.

The project defaults to linear interpolation with optional PCHIP. Upstream
Ai2020 uses cubic interpolation. Retained nodes match; identical between-node
values or an unchanged full-model response are not claimed.

Enertech `*_T.txt` files contain **temperature rise in kelvin**, with native time
arrays and row counts different from the voltage files. No assumed ambient
temperature is added; no interpolation or identical-run synchronization is
asserted. A sidecar is an additional channel, not another independent experiment.

## Additional association status

| Candidate | Evidence | Status / required work |
|---|---|---|
| Mohtat2020 NMC532/graphite | [Official deposit retrieved](https://deepblue.lib.umich.edu/data/concern/data_sets/kp78gg60j), five charging files and original author code | **Imported in v0.5.** Capacity/voltage/temperature available; measured current/time, discharge and C/20 exports absent. Author/PyBaMM variants and Cover2 protocol conflict are documented in [MOHTAT2020.md](MOHTAT2020.md). |
| Marquis2019 / Kokam SLPB78205130H | Named implementation; borrowed Dualfoil functions | Matching instrument files not located in audited sources. Ecker's SLPB75106100 is a different model. |
| BPX LFP/graphite 2 Ah 18650 | Reusable OCP/D/rate-constant example | Manufacturer/part undisclosed; associated raw full-cell tests absent. Capacity/chemistry/format alone cannot identify a model. |
| Kim2011 NCA | Nominal-design inputs | Commercial model, specimen and matching full-cell tests unresolved. |
| SINTEF LFP, graphite, NMC111, NMC532, LNMO, silicon, silicon–graphite | Laboratory half-cell specimens and C/50 branches | No same-electrode commercial full-cell identity supplied. Same-cell D/kinetics and CC full-cell data remain absent. A different matched cell in the same family does not resolve these specimens. |

COMSOL outputs and drive-cycle input profiles are excluded from experimental
counts. Source equality and formula comparisons verify data/implementation
fidelity; no independent DFN/SPM/SPMe predictive validation is claimed.

## Reuse

Read `Catalog.linked_tests(cell_id)` and `Catalog.full_cell_data(test_id,
normalized=True)`. Check `basic_test`, `observation_kind`, `channel_availability`,
`missing_items` and the cell component matrix first. Blank current means an
unavailable measurement, never zero. C-rate and Ecker's 25°C remain protocol
metadata. Original files, normalized voltage CSVs, separate temperature-rise CSVs
and metadata are downloadable in the local viewer. Attribution and separate
PyBaMM/PyBaMM-data BSD notices are listed in `DATA_LICENSES.md`.
