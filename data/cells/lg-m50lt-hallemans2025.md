# LG M50LT | Hallemans2025 grouped SPMe

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `lg-m50lt-hallemans2025`. Match level: `same_model_same_study`.

Same explicit LG M50LT model and Hallemans2025 study: Fig11 loads this drive-cycle MAT and the same fitted vector; v4 Section 7.3 identifies measured terminal voltage and Fig11 validation. Exact serialized-specimen chain to harvested OCP half-cells is not supplied.

M50LT is separate from Chen2020 LG M50. No intrinsic D or exchange-current law is reconstructed. About:Energy OCP inputs remain external with unresolved reuse scope. Paper v4 values match this vector after rounding; v3 describes a different fit.

## Parameters

[Curation review: definitions, licensing and matching limits](../../docs/HALLEMANS2025.md)

[All 18 parameter records (CSV)](../parameters/lg-m50lt-hallemans2025.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/lg-m50lt-hallemans2025.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

### Diffusion parameters

[2 diffusion records (CSV)](../parameters/lg-m50lt-hallemans2025--diffusion.csv)

Two fitted R^2/D particle time scales; not independent solid diffusivities. EIS Z/f/SOC exactly matches fit MAT selection.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Kinetics parameters

[4 kinetics records (CSV)](../parameters/lg-m50lt-hallemans2025--kinetics.csv)

Two fitted F*R/(m*sqrt(c_e0)) groups and two electrode capacitances; no intrinsic k or exchange-current density law.

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

## OCP curves

No electrode-resolved OCP record linked to this cell. Full-cell pseudo-OCV and unrelated same-chemistry curves do not fill this gap.

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `hallemans2025-m50lt-drive-80to20` — Measured drive cycle, nominal 80 to 20% SOC; repeated excitation, 0.15 s sampling, 24742.8 s elapsed; paper v4 Section 7.3 / Figure 11. | `time_s` | [CSV](../../src/ebp/data/full_cell/hallemans2025-m50lt-drive-80to20-normalized.csv) | [MAT](../../src/ebp/data/evidence/hallemans-DrivecycleMeasurement_80to20.mat) | 164953 / 164953 / 164953 / 0 of 164953 |

### Test gaps and extra channels

- `hallemans2025-m50lt-drive-80to20`: About:Energy M50LT OCP redistribution permission unresolved; no OCP imported; Absolute measured temperature; Ambient temperature trace; Independent full-cell model reproduction not performed; Intrinsic solid diffusivity and reaction-rate prefactors not identified separately; Measured cell and ambient temperature traces absent; Serialized specimen mapping between OCP half-cells, EIS cell and drive-cycle cell unresolved; Standalone CC charge/discharge observations not deposited in the reviewed file set

### External full-cell datasets

These links retain their source licenses and matching evidence; external payloads are not automatically downloaded.

- [LG M50LT: measured EIS and grouped parameters](../full-cell/hallemans-m50lt-eis-2025.md)

### Additional study evidence

- [Download CSV](../../src/ebp/data/evidence/hallemans2025-m50lt-eis.csv): EIS: 65 frequencies x 9 SOCs; measured complex impedance, full-cell OCV and seven-SOC model fit; 585 rows. Imaginary part retains source sign, not -Im(Z). License: BSD-3-Clause.

## Cell-level gaps

- About:Energy M50LT OCP redistribution permission unresolved; no OCP imported
- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Intrinsic solid diffusivity and reaction-rate prefactors not identified separately
- Measured cell and ambient temperature traces absent
- Serialized specimen mapping between OCP half-cells, EIS cell and drive-cycle cell unresolved
- Standalone CC charge/discharge observations not deposited in the reviewed file set

## Sources and reuse

- [About:Energy LG M50LT OCP inputs (reuse scope unresolved)](<https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/blob/3308a34396b8b56cd614291dd151c3405577c068/Data/LGM50LT/Notes%20on%20LG%20M50LT%20OCP.pdf>) (`aboutenergy-m50lt-ocp-lead`)
- [Physics-based battery model parametrisation from impedance data](<https://arxiv.org/html/2412.10896v4>) (`hallemans-2025-paper-v4`)
- [Hallemans2025 LG M50LT author data and scripts](<https://github.com/Battery-Intelligence-Lab/Hallemans-2025-JES/tree/3308a34396b8b56cd614291dd151c3405577c068>) (`hallemans-2025-repository`)
- [PyBOP v25.6 grouped SPMe](<https://github.com/pybop-team/PyBOP/blob/v25.6/pybop/models/lithium_ion/basic_SPMe.py>) (`pybop-25-6-grouped`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
