"""Find matched LFP study packages without assuming complete model inputs."""

from ebp import Catalog

catalog = Catalog()
for cid in ["isu-uconn-lfp-graphite-lab", "a123-18650m1a-jahn2024"]:
    cell = catalog.cells[cid]
    print(cell["display_name"], cell["match_level"])
    for curve in catalog.search(cell_id=cid):
        r = curve.record
        print("  Electrode curve:", curve.id, r["measurement"], r["x"]["kind"], r["reference"])
    tests = catalog.linked_tests(cid)
    print("  Test exports:", len(tests), "rows:", sum(t["row_count"] for t in tests))
    first = tests[0]
    print("  Coordinate:", first.get("independent_variable", {}).get("column", "time_s"))
    print("  First observation:", catalog.full_cell_data(first["id"], normalized=True)[0])
    print("  Missing:", cell["missing_items"])
