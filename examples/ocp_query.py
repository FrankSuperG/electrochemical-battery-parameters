"""Run after pip install -e .; reads bundled data without network access."""

from ebp import Catalog

catalog = Catalog()
assert not catalog.validate()
for curve in catalog.search(material="LFP"):
    print(curve.id, curve.record["x"]["kind"], curve(0.5))

measured = catalog.get("sintef-lfp-d07eb6-c3-lithiation")
print("PCHIP:", measured([0.1, 0.5, 0.9], method="pchip"))
print("Interpret x as branch-relative capacity, not stoichiometry or cell SOC.")
