# CPG-SPMT validation integration

CPG-SPMT is a suitable first model for testing whether selected E-BatP inputs
produce useful full-cell voltage predictions. A successful comparison supports
that parameter combination, model and protocol; it does not independently verify
each physical parameter or all models in the catalog.

Status: interface and equation audit only. No new experimental validation,
parameter fitting or predictive-accuracy result is reported here. The upstream
model has not been modified.

## Reviewed implementation

- [CPG-SPMT repository](https://github.com/FrankSuperG/CPG-SPMT)
- Reviewed local commit: `21a6816c2a70f43cf26744db464b437ae1723a8e`.
- `cpg_spmt.py` SHA-256:
  `35d93234f730624b24173f0cff723302fd95d157aa173af55548cf9eb386ea46`.
- Code signature: `cpg_spmt(I, T, param=None)`; `param` is a 14-element sequence.
  The README's dictionary example does not match the implementation.
- Inputs: current in A, positive for charge; supplied temperature in Celsius.
  E-BatP already uses charge-positive current, but temperatures are in K and need
  an explicit `T_C = T_K - 273.15` conversion.
- Output: terminal voltage. Temperature is an input; this implementation cannot
  independently validate a predicted temperature trajectory.

These findings describe the reviewed code. The parameter mappings below are
conditional deductions from its equations, not a verified transcription of the
associated papers.

## Interface and equation checks before a new benchmark

1. Accept separate positive/negative OCP callables, with their record IDs,
   stoichiometry domains and interpolation settings. The current code embeds
   both OCPs; the README associates its existing benchmark with a CALCE A123
   1.1 Ah LFP reference. Those defaults cannot establish a match to AMP20, a
   9 Ah pouch or an NMC cell.
2. Accept measured timestamps or an explicit timestep. The current implementation
   advances every row by exactly 1 s. For a compatibility run, resampling must
   document current hold/interpolation, gaps, temperature interpolation and
   voltage comparison times. Capacity-only data cannot supply measured time.
3. Expose raw terminal voltage and stoichiometry-domain violations. The current
   code clips output to 2.0–3.9 V and clips surface stoichiometry before voltage
   evaluation. A cross-chemistry benchmark must report violations; clipping can
   hide an invalid trajectory and truncate an NMC test reaching 4.2 V.
4. Reconcile electrode-overpotential signs with the governing equations. In the
   current function, equal positive/negative kinetic denominators give opposite
   `y_neg` and `y_pos`, whose `asinh` sum in terminal voltage is zero. An offline
   diagnostic at 1 A, `b_n=b_p=10000`, `d_n=d_p=0.001` and both stoichiometries
   0.5 returned `y_neg=-1/30`, `y_pos=1/30`, sum zero. This is a consistency probe,
   not evidence that a new physical formulation has been validated.
5. Verify activation-energy assignments from equations. The executable code
   applies `E_1/E_2` inversely to `a`, and `E_3/E_4` directly to `d`; some README
   descriptions label their physical roles differently. Do not map by those
   descriptions alone.
6. Set initial electrode stoichiometries from independent balancing evidence
   and test history. Whole-cell SOC is not either electrode's lithium fraction.
   A single starting terminal voltage does not uniquely determine both states.

## Conditional physical-to-grouped mapping

For electrode `k`, under a uniform spherical-particle SPM and the symmetric
concentration-based Butler–Volmer convention below, the reviewed matrix and
kinetic denominators suggest:

| CPG-SPMT input | Candidate mapping | Units / required evidence |
|---|---|---|
| `a_k_1` | `R_k**2 / D_s,k(T_ref)` | s; particle radius and solid diffusivity |
| `b_k` | `F * A * L_k * epsilon_s,k * c_s,max,k` | C; total active area, thickness, solid active fraction and maximum concentration |
| `d_k_1` | `k_k(T_ref) * sqrt(c_e,ref) / R_k` | 1/s under the rate-constant convention below |
| `soc_k` | Initial electrode lithium fraction `theta_k,0` | dimensionless; balancing and initial-state evidence |
| `R_ini_1` | Model-consistent effective series resistance | ohm; definition and calibration needed |

Here `A` is the total electrochemically active geometric area under the source's
layer/pair convention, and `epsilon_s` is active-solid volume fraction, not
porosity. `b_k / 3600` is the electrode capacity for a full unit stoichiometry
swing; usable cell capacity also depends on balancing windows. Neither nominal
cell Ah nor a measured cycling capacity directly equals `b_k` in coulombs.

The candidate `d` relation assumes
`i0 = F * k * sqrt(c_e) * c_s,max * sqrt(theta*(1-theta))` and
`a_s = 3*epsilon_s/R`. An exchange-current prefactor containing `F`, a BPX rate
constant, volumetric exchange current and a surface exchange-current density
need different conversions. The raw solid diffusivity `D_s` must never be copied
into `d_n_1` or `d_p_1`. Retain all conversion formulas, units and parent IDs.

Under these assumptions and constant geometry/concentration, `E_1/E_2` would
describe diffusion through the inverse temperature dependence of `a`, while
`E_3/E_4` would describe kinetics through `d`. Confirm against the intended model
version before use. A particle-size distribution, fitted shared diffusion time
or SOC-dependent function needs an explicit reduction rule; do not invent an
effective radius or a universal constant. Lumped resistance can include effects
absent from a source contact-resistance parameter.

## Candidate datasets

| Candidate | Useful evidence | Remaining limitations / role |
|---|---|---|
| Existing CPG-SPMT CALCE benchmark | Existing code, data and reported results | First reproduce the pinned baseline. Its default parameters do not transfer to other cells; existing reported fits do not establish a new independent holdout. |
| `lg-m50` | Same-model/same-study electrode OCP, diffusion/kinetics and three full-cell files with measured time/current/temperature; multiple CC rates | Strong first candidate after OCP/time/voltage-range changes. Effective graphite–SiOx treatment, parameter grouping, initialization and series resistance need review. Specimen equality is unproven. |
| `a123-amp20m1hd-a` | Same-model/same-study 4C discharge with measured current, voltage and thermal-grid mean; fitted diffusion/kinetics inputs | Good LFP follow-up. Electrode OCP points are missing; the study's full-cell OCV allocation, shared diffusion time and SOC-dependent fits are not directly interchangeable with physical electrode quantities. One imported discharge is insufficient for both fitting and independent validation. |
| `a123-high-power-pouch-9ah` | Ten measured CC charge/discharge files at 2/4/6/8/10C | Useful after characterization: finite diffusivity, kinetics and reusable electrode OCP/balancing are missing. Never borrow AMP20 or CALCE parameters merely because all are A123 LFP. |
| `mohtat2020-nmc532-pouch` | Original author inputs and five charge-capacity/voltage/temperature exports | No exported measured current or original time. Use only a clearly labeled nominal-protocol V–Q comparison after explicit model reduction; multi-particle author inputs and author/PyBaMM variants must remain separate. No measured-input V–t benchmark is currently possible. |

## Reproducible validation workflow

1. Freeze the model commit, OCP IDs, parameter variant, source hashes and mapping
   formulas. Record every assumption and unresolved input. Stop a benchmark when
   mandatory inputs are missing rather than silently using model defaults.
2. Declare experiment/condition splits before fitting. Use complete experiments,
   rates or specimens as holdouts instead of randomly splitting correlated rows.
   Audit which traces informed the published parameters: a reused source
   validation trace is a reproduction, not automatically an independent holdout.
3. First evaluate published parameters without refitting. If calibration is
   needed, save a separate derived variant with fitted bounds, calibration IDs,
   initialization policy and optimizer settings. Freeze it before holdout runs.
4. Drive the voltage model with measured `I(t)` and supplied cell `T(t)`. Preserve
   missing values and source timing. Record excluded intervals and every
   resampling rule; do not replace measured inputs with nominal C-rates.
5. Compare voltage on observed timestamps. Report RMSE, MAE, maximum absolute
   error, signed bias, covered duration and domain violations by experiment and
   regime. Separate CC, CV and rest results. A high-rate failure can reflect SPM
   reduction error as well as parameter uncertainty.
6. Save observed/predicted voltage CSVs, exact run configuration, metrics,
   model/data provenance and an English plot. Label results as baseline
   reproduction, calibration, independent validation or nominal-protocol
   comparison. No successful catalog check alone grants a validated-model label.

The intended pipeline is **cell package → explicit parameter mapping → pinned
CPG-SPMT adapter → declared experiment split → traceable voltage comparison**.
The first milestone is the audited adapter and one no-refit LG M50 comparison;
LFP cases follow when their missing OCP/balancing or characterization inputs have
been resolved.
