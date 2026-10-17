"""Check authored modules against the declared Python 3.10 syntax floor.

This supplements actual version-matrix CI; original evidence is data, not code
that this project executes or rewrites to meet its own runtime requirements.
"""

import ast
from pathlib import Path


def test_authored_python_syntax_supports_declared_minimum():
    root = Path(__file__).resolve().parents[1]
    paths = list((root / "src/ebp").glob("*.py")) + list((root / "scripts").glob("*.py")) + list((root / "tests").glob("*.py"))
    for path in paths:
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 10))
