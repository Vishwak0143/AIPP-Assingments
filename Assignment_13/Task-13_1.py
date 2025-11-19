"""Clean, modular area calculator with dictionary dispatch.

Provides helper functions for each shape and a single `calculate_area`
entry point that dispatches based on the `shape` argument.
"""
from typing import Callable, Dict
import math


def area_rectangle(width: float, height: float) -> float:
    return width * height


def area_square(side: float, *_: float) -> float:
    return side * side


def area_circle(radius: float, *_: float) -> float:
    return math.pi * radius * radius


_DISPATCH: Dict[str, Callable[[float, float], float]] = {
    "rectangle": area_rectangle,
    "square": area_square,
    "circle": area_circle,
}


def calculate_area(shape: str, x: float, y: float = 0.0) -> float:
    """Calculate area for supported shapes.

    - `shape`: one of 'rectangle', 'square', 'circle'
    - For 'rectangle' provide `x=width`, `y=height`.
    - For 'square' provide `x=side` (y ignored).
    - For 'circle' provide `x=radius` (y ignored).

    Raises `ValueError` for unknown shapes or invalid parameters.
    """
    if shape not in _DISPATCH:
        raise ValueError(f"Unsupported shape: {shape!r}")
    try:
        x_val = float(x)
        y_val = float(y)
    except (TypeError, ValueError):
        raise ValueError("x and y must be numeric")
    if shape == "rectangle":
        if y_val == 0.0:
            raise ValueError("Rectangle requires both width (x) and height (y)")
    return _DISPATCH[shape](x_val, y_val)


if __name__ == "__main__":
    examples = [
        ("rectangle", 4, 3),
        ("square", 5, 0),
        ("circle", 2, 0),
    ]
    for shape, x, y in examples:
        area = calculate_area(shape, x, y)
        print(f"{shape.title()} area (x={x}, y={y}): {area}")
