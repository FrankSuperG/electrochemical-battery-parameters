# Data contribution: [study, cell or material]

Copy this file and replace the placeholders. Fill applicable sections in English;
write `unknown`, `not reported` or `not applicable` rather than guessing. A partial
contribution is welcome when its limits are explicit. This is a submission form,
not an executable catalog record.

## 1. Summary and contributor credit

- Contribution: [new data / source lead / correction / parameter-to-test link]
- Contributor name or GitHub handle: [preferred credit]
- Contact (optional): [public contact, or contact the maintainer privately]
- What can a modeler use this for? [one or two sentences]
- Included components: [OCP / diffusion / kinetics / geometry / transport / thermal / full-cell tests / other]

## 2. Sources and reuse

| Source ID | Role (paper/data/code) | DOI or original URL | Version/commit/access date | Exact table, figure, file or function | Reuse license and evidence |
|---|---|---|---|---|---|
| [source-1] | [role] | [URL] | [version] | [location] | [license + license URL/file] |

- Required citation and notices: [text or file links]
- Data redistribution permission: [established / unresolved; explain separately from code/paper license]
- Files kept external because reuse is unresolved: [links, or none]
- Unmodified originals and normalized outputs: [filenames and SHA-256 for each; identify digest scope]

## 3. Material, electrode and cell identity

- Study and laboratory: [identity]
- Positive material and formulation: [composition, supplier, batch if disclosed]
- Negative material and formulation: [composition, supplier, batch if disclosed]
- Cell manufacturer and exact commercial model: [identity or unknown]
- Format and nominal capacity: [format; Ah; source]
- Cell/lot/specimen identifiers: [identifiers or unknown]
- Electrode specimen and its link to the full cell: [direct evidence or unknown]
- Existing catalog cell/material IDs, if applicable: [IDs or proposed new entry]

## 4. Parameter-to-test matching

Use the [defined match levels](../docs/DATA_MODEL.md#matching-levels):
`material_only`, `unmatched`, `same_study_cell_family`, `parameter_set_only` or
`same_model_same_study`. Apply the appropriate level to each proposed association.
Do not assert identical specimens without direct evidence. If an exact-specimen
link is documented, supply it separately for curator review.

| Component | Submitted record/file IDs | Related full-cell test IDs | Proposed match level | Exact supporting evidence | Missing identity/measurement information |
|---|---|---|---|---|---|
| OCP | [IDs or missing] | [IDs] | [level] | [page/table/file/quote location] | [gaps] |
| Solid diffusion | [IDs or missing] | [IDs] | [level] | [evidence] | [gaps] |
| Reaction kinetics | [IDs or missing] | [IDs] | [level] | [evidence] | [gaps] |
| Geometry / transport / thermal | [IDs or missing] | [IDs] | [level] | [evidence] | [gaps] |
| Basic CC / CCCV tests | [IDs or missing] | [IDs] | [level] | [evidence] | [gaps] |

## 5. OCP curves or expressions

Complete once per electrode, branch or distinct parameterization; copy this
section if needed. Use `ocp-points.csv` for tabulated points.

- Record/file ID, electrode and material: [identity]
- Representation: [measured points / published table / digitized figure / analytical expression / generated formula samples]
- Reference electrode and potential reference: [e.g. V vs Li/Li+; source]
- Lithiation/delithiation direction: [direction or unknown]
- Independent variable: [name, definition, unit and domain]
- Coordinate evidence: [absolute stoichiometry / normalized branch capacity; balancing or normalization method]
- Temperature and protocol: [K, measured/reference/unknown; current/rate, rests, cycle and selected branch]
- Expression, if applicable: [full formula, coefficients and coefficient units]
- Interpolation, sampling and extrapolation policy: [method; distinguish generated samples from observations]
- Source file/member/sheet and row indexing: [mapping]
- Limitations: [finite-current polarization, hysteresis, endpoint validity or other]

## 6. Diffusion, kinetics and other model inputs

Use `parameters.csv`; add one row per value, condition, expression or native table.
Keep author and software variants separate.

- Parameter IDs and variant: [IDs; original-author / implementation version / fitted variant]
- Definitions and origin: [intrinsic/effective/grouped; measured/fitted/derived/borrowed/assumed]
- Equations, variable meanings and units: [complete definition, not only a symbol or value]
- Conditions and domain: [temperature, cell SOC or electrode stoichiometry, concentration range]
- Diffusion method and assumptions: [GITT/PITT/EIS/fit; geometry, particle radius, concentration definition; or not applicable]
- Kinetic convention: [rate constant / surface or volumetric exchange current; reaction equation, F factors, active area and concentration powers]
- Arrhenius law: [full sign convention, reference temperature, activation energy and units]
- Derivations or reductions: [formula and parent record IDs; no inferred effective radius without evidence]
- Fitting information: [experiments used, objective, bounds, uncertainty if reported; or unknown]
- Native table, if applicable: [CSV path; x/y column meanings and units; exact source coordinate; missing cells/rows; interpolation domain; meaning of error-bound columns]
- Model/direction alternatives: [keep SPM, SPMe, DFN and branches separate; state which is intended for each use]
- Borrowed/assumed inputs and source conflicts: [explicit list]

## 7. Full-cell and basic tests

Complete once per file or protocol. Use the time-series template when measured
time is available, or the capacity-series template for a native charge-capacity
axis. Adapt column names for other native coordinates and document them.

- Test ID and original file/member/sheet: [identity]
- Cell/specimen and relationship to characterized electrodes: [evidence]
- Test type: [CC charge / CC discharge / CCCV / pulse / drive cycle / rest / other]
- Protocol: [currents/rates, cutoffs, CV termination, rests, cycles, chamber settings]
- Observation type: [instrument series / published experimental series / figure digitization]
- Available channels: [measured time, measured current, voltage, cell temperature, ambient temperature, capacity, other]
- Unavailable channels: [explicit list]
- Time/capacity coordinate and acquisition: [original definition, sampling, start/reset rules]
- Original current convention and conversion: [charge/discharge sign; magnitude+mode rule if used]
- Temperature definition: [absolute or rise; cell surface/core/ROI/chamber; sensor and timebase]
- Source row mapping and missing-value counts: [details]
- Pairing, alignment or resampling: [evidence and method, or none]
- Published use of this test: [calibration / validation / neither / unknown; source location]
- Proposed role here: [reproduction / calibration / held-out comparison / nominal-protocol comparison / not yet run]

## 8. Processing and reproducibility

- Extraction script and pinned dependencies: [paths and versions, or no processing]
- Reproduction command: [command from originals to submitted outputs]
- Unit/sign/coordinate conversions: [every transformation and formula]
- Filtering, smoothing, digitization or interpolation: [parameters and retained original data; or none]
- Source rows dropped or altered: [none, or exact reason and row references]
- Original/processed hashes and row counts: [inventory]
- Validation actually performed: [commands, checks and results; no assumed model-accuracy claim]

## 9. Remaining gaps and review checklist

- Missing items, conflicting source statements and follow-up leads: [list]
- [ ] Each value or file has an accessible source and exact source location.
- [ ] Reuse terms are identified, or unresolved files remain external links.
- [ ] Material identity and cell/specimen matches are supported without joining by chemistry alone.
- [ ] Measured, fitted, derived, borrowed and assumed inputs are distinguished.
- [ ] Coordinate meanings, units, protocols and kinetic conventions are explicit.
- [ ] Unavailable measurements remain blank; nominal inputs are labeled as protocol metadata.
- [ ] Originals, processing and source-row mapping are traceable.
- [ ] Missing components and calibration/validation overlap are disclosed.

Unchecked items are welcome as explicitly documented open questions; they do not
become verified facts when the submission is accepted for review.
