"""Read-only prepublication checks; reports secret pattern names, never values.

This supplements the catalog/source tests. A clean scan is not a guarantee that
all sensitive content or licensing issues have been identified.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

import numpy as np

from ebp import Catalog


ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = {
    "github_token": rb"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})",
    "aws_access_key": rb"AKIA[0-9A-Z]{16}",
    "private_key": rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    "api_secret_assignment": rb"(?i)(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*[:=]\s*[\x22\x27][A-Za-z0-9/+_-]{20,}[\x22\x27]",
    "openai_key": rb"(?<![A-Za-z0-9])sk-(?:proj-)?[A-Za-z0-9_-]{24,}",
}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def scan_history():
    objects = {}
    for line in git("rev-list", "--objects", "--all").decode().splitlines():
        oid, _, name = line.partition(" ")
        objects[oid] = name
    patterns = {name: re.compile(pattern) for name, pattern in SECRET_PATTERNS.items()}
    findings = []
    scanned = 0
    process = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        for oid, name in objects.items():
            process.stdin.write((oid + "\n").encode())
            process.stdin.flush()
            header = process.stdout.readline().split()
            if len(header) != 3:
                raise RuntimeError("Unexpected git object response")
            body = process.stdout.read(int(header[2]))
            if process.stdout.read(1) != b"\n":
                raise RuntimeError("Truncated git object response")
            if header[1] not in (b"blob", b"commit") or b"\0" in body:
                continue
            scanned += 1
            for label, pattern in patterns.items():
                if pattern.search(body):
                    findings.append({"object": oid, "path": name or "commit-message",
                                     "pattern": label})
    finally:
        process.stdin.close()
        process.stdout.close()
        process.wait()
    return {"commits": int(git("rev-list", "--all", "--count")),
            "text_objects_scanned": scanned, "findings": findings}


def audit():
    catalog = Catalog(ROOT / "src/ebp/data")
    tracked = [p for p in git("ls-files", "-z").decode().split("\0") if p]
    inappropriate = [p for p in tracked if any(
        part in {".cache", ".venv", "__pycache__", ".DS_Store"}
        for part in Path(p).parts
    ) or Path(p).name in {".env", "id_rsa", "id_ed25519"}]
    patterns = {name: re.compile(pattern) for name, pattern in SECRET_PATTERNS.items()}
    working_findings = []
    # Git text filters can change originals while working-tree hashes still pass.
    index_objects = {}
    for entry in git("ls-files", "--stage", "-z").decode().split("\0"):
        if not entry:
            continue
        header, name = entry.split("\t", 1)
        _, oid, stage = header.split()
        if stage == "0":
            index_objects[name] = oid
    object_format = git("rev-parse", "--show-object-format").decode().strip()
    index_mismatches = []
    for name in tracked:
        path = ROOT / name
        if not path.is_file():
            continue
        body = path.read_bytes()
        if name.startswith("src/ebp/data/"):
            h = hashlib.new(object_format)
            h.update(b"blob " + str(len(body)).encode() + b"\0" + body)
            if index_objects.get(name) != h.hexdigest():
                index_mismatches.append(name)
        if b"\0" in body:
            continue
        for label, pattern in patterns.items():
            if pattern.search(body):
                working_findings.append({"path": name, "pattern": label})
    profiles = []
    for test in catalog.full_cell_tests:
        rows = catalog.full_cell_data(test["id"], normalized=True)
        axis = test.get("independent_variable", {}).get("column", "time_s")
        coordinates = np.array([float(r[axis]) for r in rows])
        channels = {}
        for key in ["time_s", "current_charge_positive_A", "voltage_V",
                    "cell_temperature_K", "ambient_temperature_K"]:
            values = np.array([float(r[key]) for r in rows if r.get(key)])
            finite = values[np.isfinite(values)]
            channels[key] = {"present": len(values), "missing": len(rows) - len(values),
                             "nonfinite": int(np.sum(~np.isfinite(values))),
                             "minimum": float(np.min(finite)) if len(finite) else None,
                             "maximum": float(np.max(finite)) if len(finite) else None}
        source_rows = [r.get("source_record", "") for r in rows]
        profiles.append({
            "id": test["id"], "rows": len(rows), "axis": axis,
            "backwards_axis_steps": int(np.sum(np.diff(coordinates) < 0)),
            "repeated_axis_steps": int(np.sum(np.diff(coordinates) == 0)),
            "duplicate_source_record_ids": len(source_rows) - len(set(source_rows)),
            "channels": channels,
        })
    table_issues = []
    table_points = 0
    for curve in catalog.search(representation="table"):
        x, y = curve.points()
        table_points += len(x)
        if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)) or np.any(np.diff(x) <= 0):
            table_issues.append(curve.id)
    errors = catalog.validate()
    history = scan_history()
    invalid_profiles = [p["id"] for p in profiles if p["backwards_axis_steps"]
                        or p["duplicate_source_record_ids"]
                        or any(c["nonfinite"] for c in p["channels"].values())]
    blocking = bool(errors or inappropriate or working_findings or history["findings"]
                    or table_issues or invalid_profiles or index_mismatches)
    return {
        "reviewed_head": git("rev-parse", "HEAD").decode().strip(),
        "scope": "Current tracked working files, staged canonical-data bytes, reachable local Git history, catalog integrity and stored-series profiles; no network or model validation.",
        "status": "review_required" if blocking else "automated_checks_passed",
        "tracked_files": len(tracked), "catalog_errors": errors,
        "inappropriate_tracked_paths": inappropriate,
        "working_tree_secret_patterns": working_findings,
        "index_data_byte_mismatches": index_mismatches,
        "history_scan": history,
        "catalog": {"ocp_records": len(catalog.search()),
                    "retained_table_points": table_points,
                    "parameter_records": len(catalog.parameters),
                    "full_cell_files": len(profiles),
                    "full_cell_rows": sum(p["rows"] for p in profiles),
                    "record_licenses": dict(Counter(
                        [c.record["license"] for c in catalog.search()]
                        + [p["license"] for p in catalog.parameters]
                        + [t["license"] for t in catalog.full_cell_tests]))},
        "nonfinite_or_nonmonotone_ocp_tables": table_issues,
        "series_requiring_review": invalid_profiles,
        "full_cell_profiles": profiles,
        "limits": ["Pattern scan is not an exhaustive secret detector.",
                   "Source licenses and exact cell identity require human review.",
                   "Repeated timestamps and documented missing channels can be legitimate source properties.",
                   "This does not establish independent electrochemical model accuracy."],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "tracked_files", "catalog"]}))
    if result["status"] != "automated_checks_passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
