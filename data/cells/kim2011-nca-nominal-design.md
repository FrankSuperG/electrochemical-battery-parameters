# NCA_Kim2011 | NCA/graphite | 0.43 Ah model input

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `kim2011-nca-nominal-design`. Match level: `unmatched`.

A nominal design, not an identified commercial cell. Upstream thermal properties combine Marquis2019 material inputs with effective-heat-capacity scaling; they are not independently measured NCA-cell material properties. No matching raw test is assigned.

A nominal design, not an identified commercial cell. Upstream thermal properties combine Marquis2019 material inputs with effective-heat-capacity scaling; they are not independently measured NCA-cell material properties. No matching raw test is assigned.

## Parameters

[All 100 parameter records (CSV)](../parameters/kim2011-nca-nominal-design.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/kim2011-nca-nominal-design.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

### Diffusion parameters

[6 diffusion records (CSV)](../parameters/kim2011-nca-nominal-design--diffusion.csv)

Two Arrhenius particle-diffusivity functions, with source stoichiometry/temperature inputs retained

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

### Kinetics parameters

[7 kinetics records (CSV)](../parameters/kim2011-nca-nominal-design--kinetics.csv)

Two concentration/temperature exchange-current laws; source area and concentration convention retained

Keep source units, variants and origins. A category can contain activation energies, fitted groups or borrowed functions; records are not automatically interchangeable.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `nca-kim2011-graphite-ocp` | negative / graphite | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/nca-kim2011-graphite-ocp-sampled.csv) | [JSON](../ocp/nca-kim2011-graphite-ocp.json) |
| `nca-kim2011-nca-ocp` | positive / NCA | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/nca-kim2011-nca-ocp-sampled.csv) | [JSON](../ocp/nca-kim2011-nca-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Commercial part number unresolved
- Matching full-cell charge/discharge observations not imported

## Sources and reuse

- [Multi-domain modeling of lithium-ion batteries encompassing multi-physics in varied length scales](<https://doi.org/10.1149/1.3597614>) (`kim-2011`)
- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
