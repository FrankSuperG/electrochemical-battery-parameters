"""A small, non-eval expression interpreter for portable OCP formulas."""

import ast
import operator

import numpy as np

FUNCTIONS = {"exp": np.exp, "tanh": np.tanh, "log": np.log, "sqrt": np.sqrt}
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}


def parse(expression, variables=("x",)):
    if len(expression) > 4096:
        raise ValueError("Expression is too long")
    tree = ast.parse(expression, mode="eval")
    if sum(1 for _ in ast.walk(tree)) > 256:
        raise ValueError("Expression is too complex")

    def check(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if not np.isfinite(node.value) or abs(node.value) > 1e100:
                raise ValueError("Invalid numeric constant")
        elif isinstance(node, ast.Name) and node.id in variables:
            pass
        elif isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            check(node.left)
            check(node.right)
            if isinstance(node.op, ast.Pow):
                exponent = node.right
                if not isinstance(exponent, ast.Constant) or abs(exponent.value) > 16:
                    raise ValueError("Only bounded constant powers are supported")
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            check(node.operand)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in FUNCTIONS
            and len(node.args) == 1
            and not node.keywords
        ):
            check(node.args[0])
        else:
            raise ValueError("Unsupported expression syntax")

    check(tree.body)
    return tree.body


def evaluate_named(expression, bindings):
    arrays = {name: np.asarray(value, dtype=float) for name, value in bindings.items()}
    shape = np.broadcast_shapes(*(value.shape for value in arrays.values()))

    def visit(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            return arrays[node.id]
        if isinstance(node, ast.BinOp):
            return OPERATORS[type(node.op)](visit(node.left), visit(node.right))
        if isinstance(node, ast.UnaryOp):
            return -visit(node.operand) if isinstance(node.op, ast.USub) else visit(node.operand)
        return FUNCTIONS[node.func.id](visit(node.args[0]))

    with np.errstate(over="raise", divide="raise", invalid="raise"):
        value = visit(parse(expression, variables=arrays))
    return np.broadcast_to(value, shape).copy()


def evaluate(expression, x):
    return evaluate_named(expression, {"x": x})
