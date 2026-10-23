"""Command-line search, inspection, export, data checks, and private local preview."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path

from .catalog import Catalog


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ebp")
    sub = parser.add_subparsers(dest="command", required=True)
    search = sub.add_parser("search", help="Search curves without network access")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--material")
    search.add_argument("--representation", choices=["table", "expression"])
    search.add_argument(
        "--direction", choices=["lithiation", "delithiation", "unspecified"]
    )
    search.add_argument("--source")
    search.add_argument(
        "--cell", help="Filter by explicitly linked cell or parameter-example ID"
    )
    search.add_argument("--json", action="store_true")
    show = sub.add_parser("show")
    show.add_argument("id")
    parameters = sub.add_parser("parameters", help="Search non-OCP model parameters")
    parameters.add_argument("query", nargs="?", default="")
    parameters.add_argument("--cell", default=None)
    parameters.add_argument("--category", default=None)
    parameters.add_argument("--variant", default=None)
    parameters.add_argument("--json", action="store_true")
    sub.add_parser("cells", help="List cell IDs, chemistry and match levels")
    tests = sub.add_parser("tests", help="List full-cell tests linked to a cell model")
    tests.add_argument("--cell", default="lg-m50")
    datasets = sub.add_parser("datasets", help="Find external full-cell dataset links; no data download")
    datasets.add_argument("query", nargs="?", default="")
    datasets.add_argument("--material", choices=["LFP", "NMC", "NCA", "LCO", "NCO", "Other", "Unknown"])
    datasets.add_argument("--test-type", choices=["constant_current", "cccv", "pulse", "dynamic", "eis", "ocv"])
    datasets.add_argument("--profile", help="Exact profile name, for example US06 or UDDS")
    datasets.add_argument("--cell", help="Only datasets explicitly linked to this catalog cell")
    datasets.add_argument("--json", action="store_true")
    export = sub.add_parser("export")
    export.add_argument("id")
    export.add_argument("--output", required=True, type=Path)
    export.add_argument("--format", choices=["csv", "json"], default="csv")
    export.add_argument(
        "--count", type=int, help="Resample explicitly; default preserves table points"
    )
    export.add_argument("--method", choices=["linear", "pchip"], default="linear")
    sub.add_parser("validate", help="Check data schemas, references, values and SHA-256 hashes")
    build = sub.add_parser("build-site")
    build.add_argument("--output", type=Path, default=Path("site"))
    serve = sub.add_parser("serve", help="Build and serve only on 127.0.0.1")
    serve.add_argument("--output", type=Path, default=Path("site"))
    serve.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    catalog = Catalog()
    try:
        if args.command == "search":
            results = catalog.search(
                args.query,
                material=args.material,
                representation=args.representation,
                direction=args.direction,
                source=args.source,
                cell_id=args.cell,
            )
            if args.json:
                print(
                    json.dumps(
                        [curve.record for curve in results],
                        ensure_ascii=False,
                        indent=2,
                    )
                )
            else:
                for curve in results:
                    record = curve.record
                    print(
                        f"{curve.id:48} {record['material']:9} {record['direction']:13} {record['representation']['kind']}"
                    )
        elif args.command == "show":
            try:
                record = catalog.get(args.id).record
            except KeyError:
                record = catalog.get_parameter(args.id).record
            print(json.dumps(record, ensure_ascii=False, indent=2))
        elif args.command == "parameters":
            parameters = catalog.search_parameters(
                args.query,
                cell_id=args.cell,
                category=args.category,
                variant=args.variant,
            )
            if args.json:
                print(
                    json.dumps(
                        [p.record for p in parameters], ensure_ascii=False, indent=2
                    )
                )
            else:
                for p in parameters:
                    rep = p.record["representation"]
                    if rep["kind"] == "scalar":
                        value = rep["value"]
                    elif rep["kind"] == "table":
                        value = f"table: {rep['point_count']} nodes"
                    else:
                        value = "function"
                    print(
                        f"{p.record['name']:65} {str(value):15} {p.record['category']}"
                    )
        elif args.command == "cells":
            for cid, cell in catalog.cells.items():
                print(f"{cid:44} {cell['match_level']:24} {cell['display_name']}")
        elif args.command == "tests":
            print(
                json.dumps(
                    catalog.linked_tests(args.cell), ensure_ascii=False, indent=2
                )
            )
        elif args.command == "datasets":
            records = catalog.search_datasets(args.query, material=args.material,
                test_type=args.test_type, profile=args.profile, cell_id=args.cell)
            if args.json:
                print(json.dumps(records, indent=2, ensure_ascii=False))
            else:
                for record in records:
                    print("{} | {} | {}\n  {}".format(record["id"],
                        ", ".join(record["material_families"]),
                        ", ".join(record["test_types"]), record["source"]["url"]))
        elif args.command == "export":
            curve = catalog.get(args.id)
            if args.format == "json":
                package = {
                    "record": curve.record,
                    "sources": {
                        sid: catalog.sources[sid] for sid in curve.record["source_ids"]
                    },
                    "experiment": catalog.experiments.get(
                        curve.record["experiment_id"]
                    ),
                    "upstream_assets": {
                        aid: catalog.assets[aid]
                        for aid in curve.record["provenance"]["asset_ids"]
                    },
                }
                args.output.write_text(
                    json.dumps(package, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
            else:
                curve.export_csv(args.output, count=args.count, method=args.method)
            print(args.output)
        elif args.command == "validate":
            errors = catalog.validate()
            if errors:
                for error in errors:
                    print(error)
                return 1
            print(
                f"OK: {len(catalog.search())} OCP curves, {len(catalog.parameters)} other parameters, {len(catalog.full_cell_tests)} full-cell tests, {len(catalog.external_datasets)} external dataset links; data schemas, references, axes, values, and packaged SHA-256 verified; remote payloads not downloaded"
            )
        else:
            from .site import build_site

            build_site(catalog, args.output)
            if args.command == "build-site":
                print(args.output.resolve() / "index.html")
            else:
                handler = partial(
                    SimpleHTTPRequestHandler, directory=str(args.output.resolve())
                )
                print(
                    f"Private local preview: http://127.0.0.1:{args.port}", flush=True
                )
                with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
                    try:
                        server.serve_forever()
                    except KeyboardInterrupt:
                        pass
    except (ValueError, KeyError, OSError, ImportError) as exc:
        parser.exit(2, f"ebp: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
