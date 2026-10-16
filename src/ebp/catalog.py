"""Versioned catalog and curve evaluation. No network is used when reading data."""

from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path
import csv
import hashlib
import json

import numpy as np
from scipy.interpolate import PchipInterpolator
from jsonschema import Draft202012Validator

from . import expression
from .parameter import Parameter


@dataclass(frozen=True)
class StoichiometryMapping:
    """theta at the start/end of a measured branch, with supporting evidence.

    This is a user-supplied electrode balancing assumption, never an automatic
    conversion from relative passed capacity to absolute stoichiometry.
    """

    theta_start: float
    theta_end: float
    evidence: str

    def __post_init__(self):
        if not (0 <= self.theta_start <= 1 and 0 <= self.theta_end <= 1):
            raise ValueError("Stoichiometry endpoints must be finite and in [0, 1]")
        if self.theta_start == self.theta_end or not self.evidence.strip():
            raise ValueError("Distinct endpoints and mapping evidence are required")


class Curve:
    def __init__(self, record, root):
        self.record = record
        self.root = Path(root)

    @property
    def id(self):
        return self.record["id"]

    def _path(self):
        path = (self.root / self.record["representation"]["path"]).resolve()
        if not path.is_relative_to(self.root.resolve()):
            raise ValueError("Curve path escapes the catalog")
        return path

    def points(self):
        """Return every stored point; analytical expressions have no raw points."""
        if self.record["representation"]["kind"] != "table":
            raise ValueError("Analytical formula: use sample() to generate points")
        values = np.genfromtxt(self._path(), delimiter=",", names=True)
        return np.asarray(values["x"]), np.asarray(values["potential_V"])

    def __call__(self, x, method="linear"):
        if method not in ("linear", "pchip"):
            raise ValueError("Interpolation must be linear or pchip")
        x = np.asarray(x, dtype=float)
        lo, hi = self.record["x"]["domain"]
        if not np.all(np.isfinite(x)) or np.any(x < lo) or np.any(x > hi):
            raise ValueError(
                f"Input must be finite and within [{lo}, {hi}]; extrapolation disabled"
            )
        rep = self.record["representation"]
        if rep["kind"] == "expression":
            result = expression.evaluate(rep["expression"], x)
        else:
            xp, yp = self.points()
            result = (
                np.interp(x, xp, yp)
                if method == "linear"
                else PchipInterpolator(xp, yp, extrapolate=False)(x)
            )
        if not np.all(np.isfinite(result)):
            raise ValueError("Curve evaluation returned non-finite values")
        return float(result) if result.ndim == 0 else result

    def sample(self, count=401, method="linear"):
        if not isinstance(count, int) or not 2 <= count <= 100000:
            raise ValueError("Sample count must be an integer between 2 and 100000")
        x = np.linspace(*self.record["x"]["domain"], count)
        return x, self(x, method=method)

    def export_csv(self, path, count=None, method="linear"):
        """Export native table points, or explicitly sampled analytical values."""
        if count is None and self.record["representation"]["kind"] == "table":
            Path(path).write_bytes(self._path().read_bytes())
            return
        x, y = self.sample(count or 401, method)
        with Path(path).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["x", "potential_V"])
            writer.writerows(zip(x, y))

    def to_pybamm(self, mapping=None, count=2001):
        """Create a linear PyBaMM interpolant; incomplete parameter sets stay incomplete.

        Formulas are sampled, with resolution controlled by count. Callers must
        respect the stated domain. Empirical pseudo-OCP curves require an explicit
        StoichiometryMapping and remain pseudo-OCP after mapping.
        """
        if self.record["x"]["kind"] != "stoichiometry" and mapping is None:
            raise ValueError(
                "Absolute stoichiometry is unknown; provide StoichiometryMapping with evidence"
            )
        if mapping is not None and self.record["x"]["kind"] == "stoichiometry":
            raise ValueError("This curve already uses stoichiometry")
        if mapping is not None and not isinstance(mapping, StoichiometryMapping):
            raise TypeError("mapping must be a StoichiometryMapping")
        if mapping is not None:
            delta = mapping.theta_end - mapping.theta_start
            direction = self.record["direction"]
            if (direction == "lithiation" and delta <= 0) or (
                direction == "delithiation" and delta >= 0
            ):
                raise ValueError(
                    "Stoichiometry mapping disagrees with the electrode direction"
                )
        import pybamm

        if self.record["representation"]["kind"] == "table":
            x, y = self.points()
        else:
            x, y = self.sample(count)
        if mapping is not None:
            x = mapping.theta_start + x * (mapping.theta_end - mapping.theta_start)
            order = np.argsort(x)
            x, y = x[order], y[order]

        def ocp(sto):
            return pybamm.Interpolant(
                x, y, sto, interpolator="linear", extrapolate=False
            )

        ocp.ebp_metadata = {
            "record_id": self.id,
            "record_version": self.record["version"],
            "mapping": None if mapping is None else mapping.__dict__,
            "interpolation": "linear",
            "sample_count": len(x),
            "independently_validated": False,
        }
        return ocp


class Catalog:
    def __init__(self, root=None):
        self.root = (
            Path(root) if root is not None else Path(str(files("ebp").joinpath("data")))
        )
        self.document = self._load("catalog.json")
        self.sources = self._load("sources.json")
        self.materials = self._load("materials.json")
        self.experiments = self._load("experiments.json")
        self.assets = self._load("assets.json")
        self.cells = self._load("cells.json")
        self.parameters = self._load("parameters.json")["records"]
        self.full_cell_tests = self._load("full_cell_tests.json")["records"]
        self._records = self.document.get("records", [])

    def _load(self, name):
        return json.loads((self.root / name).read_text(encoding="utf-8"))

    def get(self, record_id):
        for record in self._records:
            if record["id"] == record_id:
                return Curve(record, self.root)
        raise KeyError(f"Unknown curve: {record_id}")

    def search(
        self,
        query="",
        material=None,
        representation=None,
        direction=None,
        source=None,
        cell_id=None,
    ):
        matches = []
        for record in self._records:
            if cell_id and record["cell_link"]["cell_id"] != cell_id:
                continue
            if material and record["material"].casefold() != material.casefold():
                continue
            if representation and record["representation"]["kind"] != representation:
                continue
            if direction and record["direction"] != direction:
                continue
            if source and source not in record["source_ids"]:
                continue
            haystack = json.dumps(record, ensure_ascii=False).casefold()
            if query.casefold() in haystack:
                matches.append(Curve(record, self.root))
        return matches

    def search_parameters(self, query="", cell_id=None, category=None):
        return [
            Parameter(p)
            for p in self.parameters
            if (not cell_id or p["cell_id"] == cell_id)
            and (not category or p["category"] == category)
            and query.casefold() in json.dumps(p).casefold()
        ]

    def get_parameter(self, parameter_id):
        for p in self.parameters:
            if p["id"] == parameter_id:
                return Parameter(p)
        raise KeyError(f"Unknown parameter: {parameter_id}")

    def linked_tests(self, cell_id):
        return [test for test in self.full_cell_tests if test["cell_id"] == cell_id]

    def full_cell_data(self, test_id, normalized=False):
        """Read CSV rows, retaining source or explicitly normalized column names.

        Maccor originals have an instrument banner. MAT/ZIP experiments expose
        normalized CSV rows; their originals remain external checksum-pinned assets.
        Pass normalized=True for the documented charge-positive current convention.
        """
        for test in self.full_cell_tests:
            if test["id"] == test_id:
                use_normalized = normalized or test["path"] is None
                path = (
                    self.root / test["normalized_path" if use_normalized else "path"]
                ).resolve()
                if not path.is_relative_to(self.root.resolve()):
                    raise ValueError("Test path escapes the catalog")
                with path.open(encoding="utf-8", newline="") as handle:
                    for _ in range(
                        0 if use_normalized else test.get("csv_header_rows", 13)
                    ):
                        next(handle)
                    return list(csv.DictReader(handle))
        raise KeyError(f"Unknown full-cell test: {test_id}")

    def validate(self):
        """Return actionable structural, reference, numerical, and hash errors."""
        errors = []
        schema = self._load("schema/catalog.schema.json")
        errors.extend(
            f"schema: {error.json_path}: {error.message}"
            for error in Draft202012Validator(schema).iter_errors(self.document)
        )
        if errors:
            return errors
        linked_schema = self._load("schema/linked-data.schema.json")
        errors.extend(
            f"linked data schema: {error.json_path}: {error.message}"
            for error in Draft202012Validator(linked_schema).iter_errors(
                {"parameters": self.parameters, "full_cell_tests": self.full_cell_tests}
            )
        )
        if errors:
            return errors
        ids = [r["id"] for r in self._records]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate record IDs")
        for aid, asset in self.assets.items():
            if asset.get("source_id") not in self.sources:
                errors.append(f"asset {aid}: unknown source")
            if not asset.get("sha256") or not asset.get("url", "").startswith(
                "https://"
            ):
                errors.append(f"asset {aid}: missing checksum or HTTPS URL")
            if asset.get("path"):
                local = (self.root / asset["path"]).resolve()
                if not local.is_relative_to(self.root.resolve()) or not local.is_file():
                    errors.append(f"asset {aid}: invalid local evidence path")
                elif hashlib.sha256(local.read_bytes()).hexdigest() != asset["sha256"]:
                    errors.append(f"asset {aid}: local evidence SHA-256 mismatch")
        for eid, experiment in self.experiments.items():
            if (
                experiment.get("source_id") not in self.sources
                or experiment.get("asset_id") not in self.assets
            ):
                errors.append(f"experiment {eid}: unknown source or asset")
        parameter_ids = [p["id"] for p in self.parameters]
        if len(parameter_ids) != len(set(parameter_ids)):
            errors.append("Duplicate parameter IDs")
        for p in self.parameters:
            if p["cell_id"] not in self.cells or any(
                sid not in self.sources for sid in p["source_ids"]
            ):
                errors.append(f"{p['id']}: unknown cell or source")
            if p["provenance"]["asset_id"] not in self.assets:
                errors.append(f"{p['id']}: unknown asset")
            rep = p["representation"]
            try:
                if rep["kind"] == "scalar":
                    if not np.isfinite(rep["value"]):
                        raise ValueError("Non-finite scalar")
                elif rep["kind"] == "expression":
                    Parameter(p)(c_e=1000, c_s_surf=10000, c_s_max=30000, T=298.15)
                else:
                    raise ValueError("Unknown parameter representation")
            except (ValueError, KeyError, SyntaxError, FloatingPointError) as exc:
                errors.append(f"{p['id']}: {exc}")
        test_ids = [t["id"] for t in self.full_cell_tests]
        if len(test_ids) != len(set(test_ids)):
            errors.append("Duplicate full-cell test IDs")
        for test in self.full_cell_tests:
            try:
                if (
                    test["cell_id"] not in self.cells
                    or test["source_id"] not in self.sources
                    or test["asset_id"] not in self.assets
                ):
                    raise ValueError("Unknown cell, source or asset")
                if test["path"] is not None:
                    path = (self.root / test["path"]).resolve()
                    if not path.is_relative_to(self.root.resolve()):
                        raise ValueError("Test path escapes the catalog")
                    if (
                        hashlib.sha256(path.read_bytes()).hexdigest()
                        != self.assets[test["asset_id"]]["sha256"]
                    ):
                        raise ValueError("Original full-cell file SHA-256 mismatch")
                if len(self.full_cell_data(test["id"])) != test["row_count"]:
                    raise ValueError("Full-cell row count mismatch")
                rows = self.full_cell_data(test["id"], normalized=True)
                if len(rows) != test["row_count"]:
                    raise ValueError("Normalized row count mismatch")
                time = np.array([float(r["time_s"]) for r in rows])
                if not np.isfinite(time).all() or np.any(np.diff(time) < 0):
                    raise ValueError("Invalid normalized timebase")
                for column in (
                    "voltage_V",
                    "current_charge_positive_A",
                    "cell_temperature_K",
                ):
                    if any(
                        r[column] and not np.isfinite(float(r[column])) for r in rows
                    ):
                        raise ValueError(
                            f"Invalid normalized {column}; missing values must be empty"
                        )
                    if (
                        column in test.get("missing_values", {})
                        and sum(not r[column] for r in rows)
                        != test["missing_values"][column]
                    ):
                        raise ValueError(f"Missing count mismatch for {column}")
                normalized = (self.root / test["normalized_path"]).resolve()
                if not normalized.is_relative_to(self.root.resolve()):
                    raise ValueError("Normalized test path escapes the catalog")
                if (
                    hashlib.sha256(normalized.read_bytes()).hexdigest()
                    != test["normalized_sha256"]
                ):
                    raise ValueError("Normalized full-cell SHA-256 mismatch")
            except (ValueError, KeyError, OSError) as exc:
                errors.append(f"{test['id']}: {exc}")
        for cid, cell in self.cells.items():
            if any(pid not in parameter_ids for pid in cell.get("parameter_ids", [])):
                errors.append(f"cell {cid}: unknown linked parameter")
            if any(
                tid not in {t["id"] for t in self.full_cell_tests}
                for tid in cell.get("full_cell_test_ids", [])
            ):
                errors.append(f"cell {cid}: unknown linked full-cell test")
            for key, expected in (
                (
                    "parameter_ids",
                    {p["id"] for p in self.parameters if p["cell_id"] == cid},
                ),
                (
                    "full_cell_test_ids",
                    {t["id"] for t in self.full_cell_tests if t["cell_id"] == cid},
                ),
                (
                    "ocp_record_ids",
                    {
                        r["id"]
                        for r in self._records
                        if r["cell_link"]["cell_id"] == cid
                    },
                ),
            ):
                if key in cell and set(cell[key]) != expected:
                    errors.append(f"cell {cid}: {key} disagrees with record ownership")
        for record in self._records:
            rid = record["id"]
            for sid in record["source_ids"]:
                if sid not in self.sources:
                    errors.append(f"{rid}: unknown source {sid}")
            if record["material_id"] not in self.materials:
                errors.append(f"{rid}: unknown material")
            experiment = record["experiment_id"]
            if experiment is not None and experiment not in self.experiments:
                errors.append(f"{rid}: unknown experiment")
            if (
                record["cell_link"]["cell_id"] is not None
                and record["cell_link"]["cell_id"] not in self.cells
            ):
                errors.append(f"{rid}: unknown cell")
            for asset in record["provenance"]["asset_ids"]:
                if asset not in self.assets:
                    errors.append(f"{rid}: unknown upstream asset {asset}")
            try:
                curve = Curve(record, self.root)
                lo, hi = record["x"]["domain"]
                if not (np.isfinite(lo) and np.isfinite(hi) and lo < hi):
                    raise ValueError("Invalid domain")
                if record["representation"]["kind"] == "table":
                    x, y = curve.points()
                    if (
                        len(x) < 2
                        or not np.all(np.isfinite(x))
                        or not np.all(np.isfinite(y))
                    ):
                        raise ValueError("Non-finite or insufficient table points")
                    if not np.all(np.diff(x) > 0):
                        raise ValueError("Table coordinates must strictly increase")
                    if x[0] != lo or x[-1] != hi:
                        raise ValueError("Table endpoints disagree with domain")
                    digest = hashlib.sha256(curve._path().read_bytes()).hexdigest()
                    if digest != record["representation"]["sha256"]:
                        raise ValueError("Curve SHA-256 mismatch")
                    if len(x) != record["representation"]["point_count"]:
                        raise ValueError("Point count mismatch")
                curve.sample(101)
            except (
                ValueError,
                OSError,
                KeyError,
                SyntaxError,
                FloatingPointError,
            ) as exc:
                errors.append(f"{rid}: {exc}")
        return errors
