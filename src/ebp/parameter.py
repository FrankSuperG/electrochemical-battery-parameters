"""Scalar and named multivariable model parameters with explicit provenance."""

import numpy as np
from .expression import evaluate_named


class Parameter:
    def __init__(self, record):
        self.record = record

    @property
    def id(self):
        return self.record["id"]

    @property
    def value(self):
        rep = self.record["representation"]
        if rep["kind"] != "scalar":
            raise ValueError("This parameter is a function; supply its named variables")
        return rep["value"]

    def __call__(self, **variables):
        rep = self.record["representation"]
        if rep["kind"] == "scalar":
            if variables:
                raise ValueError("Scalar parameter takes no variables")
            return self.value
        if set(variables) != set(rep["variables"]):
            raise ValueError("Required variables: " + ", ".join(rep["variables"]))
        values = {k: np.asarray(v, dtype=float) for k, v in variables.items()}
        if any(not np.all(np.isfinite(v)) for v in values.values()):
            raise ValueError("Inputs must be finite")
        if (
            np.any(values["c_e"] < 0)
            or np.any(values["c_s_max"] <= 0)
            or np.any(values["c_s_surf"] < 0)
            or np.any(values["c_s_surf"] > values["c_s_max"])
            or np.any(values["T"] <= 0)
        ):
            raise ValueError("Inputs violate the stated concentration or temperature domain")
        result = evaluate_named(rep["expression"], values)
        if not np.all(np.isfinite(result)):
            raise ValueError("Function returned a non-finite result")
        return float(result) if result.ndim == 0 else result
