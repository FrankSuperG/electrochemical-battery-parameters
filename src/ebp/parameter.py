"""Scalar and named multivariable model parameters with explicit provenance."""

import numpy as np
from pathlib import Path
import csv
from .expression import evaluate_named


class Parameter:
    def __init__(self, record, root=None):
        self.record = record
        self.root = Path(root) if root is not None else None

    def points(self):
        """Return native table coordinates/values; no extrapolation or fitting."""
        rep = self.record["representation"]
        if rep["kind"] != "table" or self.root is None:
            raise ValueError("Native table and catalog data root required")
        path = (self.root / rep["path"]).resolve()
        if not path.is_relative_to(self.root.resolve()):
            raise ValueError("Parameter path escapes the catalog")
        with path.open(newline="") as f:
            rows = list(csv.DictReader(f))
        return (np.array([float(r[rep["x"]["column"]]) for r in rows]),
                np.array([float(r[rep["y_column"]]) for r in rows]))

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
        if rep["kind"] == "table":
            key = rep["x"]["variable"]
            if set(variables) != {key}:
                raise ValueError("Required variable: " + key)
            x = np.asarray(variables[key], dtype=float)
            xp, yp = self.points()
            if not np.isfinite(x).all() or np.any(x < xp[0]) or np.any(x > xp[-1]):
                raise ValueError("Input outside finite native table domain; extrapolation disabled")
            y = np.interp(x, xp, yp)
            return float(y) if y.ndim == 0 else y
        if set(variables) != set(rep["variables"]):
            raise ValueError("Required variables: " + ", ".join(rep["variables"]))
        values = {k: np.asarray(v, dtype=float) for k, v in variables.items()}
        if any(not np.all(np.isfinite(v)) for v in values.values()):
            raise ValueError("Inputs must be finite")
        concentration_invalid = "c_e" in values and (
            np.any(values["c_e"] < 0)
            or np.any(values["c_s_max"] <= 0)
            or np.any(values["c_s_surf"] < 0)
            or np.any(values["c_s_surf"] > values["c_s_max"])
        )
        stoichiometry_invalid = "sto" in values and (
            np.any(values["sto"] < 0) or np.any(values["sto"] > 1)
        )
        if concentration_invalid or stoichiometry_invalid or np.any(values["T"] <= 0):
            raise ValueError(
                "Inputs violate the stated concentration or temperature domain"
            )
        result = evaluate_named(rep["expression"], values)
        if not np.all(np.isfinite(result)):
            raise ValueError("Function returned a non-finite result")
        return float(result) if result.ndim == 0 else result
