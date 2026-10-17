# Kokam SLPB75106100 | 7.5 Ah NCO/graphite

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `kokam-slpb75106100-ecker2015`. Match level: `same_model_same_study`.

Ecker characterization and validation share the named Kokam SLPB75106100 model. Whole-cell voltage points are digitized from Richardson2020 Figure 8. Exact specimen match is not established.

Commercial capacity is 7.5 Ah; pinned implementation uses 0.15625 Ah. Do not apply full-cell current directly to the reduced implementation without reviewing scaling. NCO label follows upstream; composition ratio unresolved. Thermal values are borrowed from another 5 Ah Kokam.

## Parameters

[All 38 parameter records (CSV)](../parameters/kokam-slpb75106100-ecker2015.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/kokam-slpb75106100-ecker2015.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `ecker2015-graphite-ocp` | negative / graphite | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/ecker2015-graphite-ocp-sampled.csv) | [JSON](../ocp/ecker2015-graphite-ocp.json) |
| `ecker2015-nco-ocp` | positive / NCO | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/ecker2015-nco-ocp-sampled.csv) | [JSON](../ocp/ecker2015-nco-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

CSV links point to the complete stored observations. Blank channels remain unavailable. Channel counts below describe non-empty rows; read the protocol and processing for their origin.

| Test / protocol | Coordinate | Complete CSV | Original | Non-empty time / I / V / cell T rows |
|---|---|---|---|---|
| `ecker-kokam-1c-discharge` — 1C constant-current discharge at 25 degC; published-figure digitization | `time_s` | [CSV](../../src/ebp/data/full_cell/ecker-kokam-1c-discharge-normalized.csv) | [CSV](../../src/ebp/data/evidence/Ecker_1C.csv) | 31 / 0 / 31 / 0 of 31 |
| `ecker-kokam-5c-discharge` — 5C constant-current discharge at 25 degC; published-figure digitization | `time_s` | [CSV](../../src/ebp/data/full_cell/ecker-kokam-5c-discharge-normalized.csv) | [CSV](../../src/ebp/data/evidence/Ecker_5C.csv) | 33 / 0 / 33 / 0 of 33 |

### Test gaps and extra channels

- `ecker-kokam-1c-discharge`: Absolute measured temperature; Ambient temperature trace; Capacity channel; Charge trace; Exact specimen identifier; Measured current trace
- `ecker-kokam-5c-discharge`: Absolute measured temperature; Ambient temperature trace; Capacity channel; Charge trace; Exact specimen identifier; Measured current trace

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed

## Sources and reuse

- [Parameterization of a Physico-Chemical Model of a Lithium-Ion Battery: I. Determination of Parameters](<https://doi.org/10.1149/2.0551509jes>) (`ecker-2015-i`)
- [Parameterization of a Physico-Chemical Model of a Lithium-Ion Battery: II. Model Validation](<https://doi.org/10.1149/2.0541509jes>) (`ecker-2015-ii`)
- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)
- [PyBaMM experimental data release v1.0.2](<https://github.com/pybamm-team/pybamm-data/releases/tag/v1.0.2>) (`pybamm-data-1-0-2`)
- [Generalised single particle models for high-rate operation of graded lithium-ion electrodes: Systematic derivation and validation](<https://doi.org/10.1016/j.electacta.2020.135862>) (`richardson-2020`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
