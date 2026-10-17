# LG M50LT / Hallemans2025 curation

Reviewed 2026-10-17. **18 jointly fitted grouped-SPMe values, one measured
drive cycle (164,953 rows) and an EIS evidence table (585 rows) are imported.**
Electrode OCP reuse remains unresolved and no OCP data are redistributed.
Repository visibility remains private; no site or public release is deployed.

**[Open the cell package](../data/cells/lg-m50lt-hallemans2025.md)** ·
[Parameter CSV](../data/parameters/lg-m50lt-hallemans2025.csv) ·
[Measured t/I/V CSV](../src/ebp/data/full_cell/hallemans2025-m50lt-drive-80to20-normalized.csv) ·
[Measured/fitted EIS CSV](../src/ebp/data/evidence/hallemans2025-m50lt-eis.csv)

## Source and version decisions

- Scientific source: Hallemans et al., *Physics-based battery model
  parametrisation from impedance data*, JES 172 060507 (2025),
  [DOI](https://doi.org/10.1149/1945-7111/add41b).
- Definitions and experiment matching were checked against
  [arXiv v4](https://arxiv.org/html/2412.10896v4), dated 2025-04-23,
  Tables 2/4/5 and Section 7.3. Its Table 5 agrees with the stored fit at
  printed precision. Earlier v3 has different EIS settings and fitted values;
  these are not alternative rows of this import.
- [Author repository](https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068),
  pinned to `3308a34396b8b56cd614291dd151c3405577c068` (2025-10-20),
  updates scripts to PyBOP 25.6. Source arrays predate that script update.
  Original MAT files and Fig10/Fig11 scripts are packaged unchanged; scripts
  are inspected as text, never executed by the importer.
- [Asset manifest](../scripts/hallemans_assets.json) records exact URLs,
  SHA-256 and redistribution status. The importer is
  [seed_hallemans.py](../scripts/seed_hallemans.py).

## Reuse: what is and is not cleared

The author repository's root BSD-3-Clause notice is retained verbatim in
[Hallemans2025-BSD-3-Clause.txt](../src/ebp/licenses/Hallemans2025-BSD-3-Clause.txt).
It is the redistribution basis for the authors' whole-cell measurements,
fitted results and scripts. Derived CSVs retain that license, author attribution,
source URLs and explicit changes. The paper's CC BY 4.0 label is not substituted
for the dataset's license.

OCP needs a separate decision. Section 7 attributes the half-cell curves to
**About:Energy, personal communication**. The accompanying notes, dated
2024-09-10, do not state separate reuse terms. The root BSD notice does not
independently establish that the authors may sublicense those third-party
inputs. This is **unresolved permission**, not a finding that reuse is forbidden.

The company's official [open-source BPX repository](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation)
does carry CC-BY-SA-4.0, but its [NMC README](https://github.com/About-Energy-OpenSource/About-Energy-BPX-Parameterisation/blob/main/NMC/README.md)
describes a 12.5 Ah NMC111 pouch cell. That grant is not applied to M50LT.
`OCP_LGM50LT.mat`, `LG_M50LT_Uneg.csv`, `LG_M50LT_Upos.csv` and the notes PDF
remain external checksum-pinned leads, without packaged bytes, sampled curves
or substitute Chen2020 OCPs. An explicit M50LT grant or documented rights-holder
clarification would allow this decision to be revisited. No author was contacted.

## Group definitions and model conventions

Values are extracted directly from `thetahat`, with the order independently
checked in Fig10 and Fig11. **All eighteen belong to one fit.** Their definitions,
units, bounds and computational near-bound flags are in each parameter record.
Here `p/n` means positive/negative, `L` is the combined electrode/separator
thickness, `epsilon` is porosity, `alpha` is active volume fraction, `R` is
particle radius, and `m` is the paper's exchange-current prefactor.

| Quantity | Definition retained | Interpretation boundary |
|---|---|---|
| Particle time scales, s | `tau_d = R^2 / D` | Not intrinsic `D`; no independent M50LT particle radii imported |
| Electrode electrolyte times, s | `epsilon_sep * L^2 / (epsilon_electrode^b * D_e)` | Not measured electrolyte diffusivity |
| Separator electrolyte time, s | `L^2 / (epsilon_sep^(b_sep-1) * D_e)` | Paper Table 2 convention; see helper discrepancy below |
| Charge-transfer groups, s | `tau_ct = F*R/(m*sqrt(c_e0))` | Not a Butler-Volmer rate constant or directly the RC relaxation time |
| Electrode capacitance, F | `3*alpha*Cdl*L_electrode*A/R` | Whole-electrode capacitance, not area-specific `Cdl` |
| Relative porosity | `zeta = epsilon_electrode/epsilon_sep` | A ratio may exceed one; it is not an absolute void fraction |
| Reference electrolyte capacity, A.s | `Q_e = F*epsilon_sep*c_e0*L*A` | Not measured cell capacity in Ah |
| Stoichiometry bounds | `c_at_0_or_100_percent_SOC/c_max` | Positive minimum is at full-cell 100% SOC; negative minimum is at 0% |
| Series resistance, Ohm; transference number | Lumped `R_0`; fitted `t_plus` | Estimated jointly with the remaining groups |

The paper relates `tau_ct` to a typical charge-transfer resistance through
`Rct_typ = (2*Rg*T/F)*tau_ct/(3*Qth)`. The RC time also depends on capacitance
and operating state. Neither resistance nor an intrinsic kinetic coefficient
is derived here. Units/concentration conventions of another model's `k` cannot
be substituted for the paper's `m` without an explicit mapping.

**Implementation discrepancy:** the [PyBOP v25.6 conversion helper](https://github.com/pybop-team/PyBOP/blob/v25.6/pybop/models/lithium_ion/basic_SPMe.py)
uses `L^2/(epsilon_sep^b_sep*D_e)` for the separator group, whereas Table 2
uses exponent `b_sep-1`. This importer preserves the actual fitted scalar and
documents the paper definition; it does not call the helper, invert this value,
or silently correct the author's result.

The scripts initialize from **Chen2020 LG M50**, then override OCP, thickness
ratios, measured capacity and the fitted vector. Separator thickness is borrowed
from that base. Those initial inputs are not added as M50LT measurements.
The fit therefore is a partial model package, with external OCP dependencies.
Several groups reach fitting bounds; flags do not represent uncertainties or
identifiability guarantees. The paper's fit used 1,000 PSO iterations; the later
script allows 2,000, so importing its saved vector is not a claim to rerun PSO.

## Whole-cell evidence and matching

| Component | Confirmed link | Missing or limited |
|---|---|---|
| EIS | `impedanceLGM50LT_Hybrid_4h_3mVrms.mat`: 65 frequencies, nine SOCs (10-90%); paper's 3 mV rms protocol, EIS ambient 25 degC | No raw sinusoidal instrument waveforms or measured temperature trace |
| Fitted vector | Fit MAT `Z` equals raw `Z[:,1:8]` exactly; frequency arrays and normalized SOCs also agree exactly (20-80%, 455 complex observations) | No fitting uncertainty; some bounded groups and poor low-frequency fits |
| Drive cycle | Fig11 loads the same fit and `DrivecycleMeasurement_80to20.mat`; v4 Section 7.3/Fig11 identifies measured terminal voltage | Same model/study, without a complete serialized-specimen chain to OCP half-cells |
| Electrode OCP | Same-study external About:Energy input is identified | Redistribution permission and same-specimen chain unresolved |
| Basic CC tests | CC preparation is described in the EIS protocol | No standalone measured CC charge/discharge series in the reviewed file set |

The EIS CSV preserves signed real/imaginary components, frequency order and
full-cell OCV. Its `fitted_Z_*` fields are **model output**, blank at 10/90% SOC.
The full-cell OCV column is not an electrode OCP. EIS evidence is counted
separately from the one time-domain test file.

Drive-cycle CSV transformations:

1. Extract original `t` in seconds, `i` in amperes and `v` in volts, preserving
   all rows, order and float precision, without interpolation or smoothing.
2. Retain charge-positive source `i`. Fig11 negates it for PyBaMM's
   discharge-positive convention. The net trapezoidal charge is approximately
   -2.92384 Ah, a consistency check rather than an inferred SOC/capacity trace.
3. Keep original one-based array indices. Infer mode solely from current sign;
   do not invent cycle or step IDs. Temperature fields remain blank.
4. Leave `u` only in the original MAT: it is current-like, and its exact command/
   measurement/processing meaning is unresolved. It is never used as voltage.

The recorded duration is 24,742.8 s with 0.15 s sampling, consistent with the
paper's validation description. EIS ambient setpoint is **not** imputed into
the drive cycle. The current Fig11 script plots a simulated voltage after
loading the measured current; it does not itself compare stored `v`. We use the
paper and original measured MAT for linkage, never that simulation as a measured
trace. Published model-error claims have not been independently reproduced.

## Use the curated subset

```python
from ebp import Catalog

c = Catalog()
cell_id = "lg-m50lt-hallemans2025"
tau = c.get_parameter("hallemans2025-tau-d-p")
print(tau.value, tau.record["unit"], tau.record["definition"])
test = c.linked_tests(cell_id)[0]
rows = c.full_cell_data(test["id"], normalized=True)
# For a PyBaMM current input, negate current_charge_positive_A.
# Temperature remains unavailable; no complete model run is implied.
```

The local viewer's cell ZIP includes original MATs, script evidence, EIS CSV,
normalized drive cycle, parameter metadata and license notice. GitHub direct
links above work for signed-in users with repository access. Reproduction:
`python scripts/seed_hallemans.py` uses packaged evidence; a full catalog rebuild
uses `python scripts/seed_v01.py --download` with checksum-pinned sources.
