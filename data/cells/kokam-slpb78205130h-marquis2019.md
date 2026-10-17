# SLPB78205130H | LCO/graphite | 0.680616 Ah model input

[All cells](../README.md) · [All OCP records](../ocp/README.md) · [How to use the files](../../docs/DATA_ACCESS.md)

Cell ID: `kokam-slpb78205130h-marquis2019`. Match level: `parameter_set_only`.

The upstream set names a Kokam model but borrows Dualfoil electrode functions. Model association does not establish that the OCP, diffusion or kinetics were measured on that commercial specimen.

The upstream set names a Kokam model but borrows Dualfoil electrode functions. Model association does not establish that the OCP, diffusion or kinetics were measured on that commercial specimen.

## Parameters

[All 38 parameter records (CSV)](../parameters/kokam-slpb78205130h-marquis2019.csv) · [Definitions, sources and linked-test metadata (JSON)](../parameters/kokam-slpb78205130h-marquis2019.json)

CSV includes units, definitions, conditions, origins and variant labels. Expressions remain expressions. These are partial collections, not complete validated model inputs.

## OCP curves

| Record | Electrode / material | Type / reference | Coordinate and domain | CSV | Metadata |
|---|---|---|---|---|---|
| `marquis2019-graphite-ocp` | negative / graphite | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/marquis2019-graphite-ocp-sampled.csv) | [JSON](../ocp/marquis2019-graphite-ocp.json) |
| `marquis2019-lco-ocp` | positive / LCO | literature_formula / Li/Li+ | stoichiometry; [0.0, 1.0] | [Generated samples](../ocp/marquis2019-lco-ocp-sampled.csv) | [JSON](../ocp/marquis2019-lco-ocp.json) |

Read each JSON for branch direction, source conditions and coordinate meaning. Generated formula samples are not measured OCP points.

## Full-cell tests

No matching full-cell observation file imported. A named model or chemistry does not establish a test-data match.

## Cell-level gaps

- Identical characterization/validation specimen not established
- Independent full-cell model reproduction not performed
- Matching full-cell charge/discharge observations not imported

## Sources and reuse

- [Dualfoil electrode functions, as attributed by PyBaMM Marquis2019 and Ai2020](<https://raw.githubusercontent.com/pybamm-team/PyBaMM/v25.4.2/src/pybamm/input/parameters/lithium_ion/Marquis2019.py>) (`dualfoil-attribution`)
- [An asymptotic derivation of a single particle model with electrolyte](<https://doi.org/10.1149/2.0341915jes>) (`marquis-2019`)
- [PyBaMM v25.4.2: pinned lithium-ion parameter implementations](<https://github.com/pybamm-team/PyBaMM/tree/v25.4.2/src/pybamm/input/parameters/lithium_ion>) (`pybamm-25-4-2`)

Retain per-record attribution and notices. See [data licenses](../../DATA_LICENSES.md). No independent full-cell model validation is claimed.
