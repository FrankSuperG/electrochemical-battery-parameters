"""Export an OCP component to PyBaMM and inspect interpolation differences."""

import numpy as np
import pybamm
from ebp import Catalog

curve = Catalog().get("lfp-afshar2017-formula")
function = curve.to_pybamm(count=10001)
sto = pybamm.InputParameter("sto")
symbol = function(sto)
test_points = np.array([0.05, 0.2, 0.5, 0.8, 0.95])
converted = np.array(
    [float(np.asarray(symbol.evaluate(inputs={"sto": float(x)})).item()) for x in test_points]
)
print("PyBaMM OCP component:", converted)
print("Maximum interpolation error / V:", np.max(np.abs(converted - curve(test_points))))
print("OCP component export only; no cell simulation is run.")
