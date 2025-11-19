"""Linear optimization for chocolate production case study.

Maximize profit: 6*A + 5*B
Subject to:
  A + B <= 5    (milk)
  3*A + 2*B <= 12 (choco)
  A, B >= 0

The script tries `scipy.optimize.linprog` first and falls back to
checking LP corner points if SciPy isn't available.
"""
from math import isclose


def solve_with_scipy():
    try:
        from scipy.optimize import linprog # pyright: ignore[reportMissingImports]
    except Exception:
        return None
    # linprog minimizes c^T x, so minimize negative profit
    c = [-6, -5]
    A_ub = [[1, 1], [3, 2]]
    b_ub = [5, 12]
    bounds = [(0, None), (0, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    if res.success:
        A, B = res.x
        profit = 6 * A + 5 * B
        return (A, B, profit)
    return None


def solve_by_corners():
    # Manually evaluate corner points for this 2-variable LP.
    corners = []
    # origin
    corners.append((0.0, 0.0))
    # A = 0, limited by milk and choco -> milk gives B<=5, choco gives B<=6 => B=5
    corners.append((0.0, 5.0))
    # B = 0, limited by milk and choco -> milk gives A<=5, choco gives A<=4 => A=4
    corners.append((4.0, 0.0))
    # intersection of A+B=5 and 3A+2B=12
    # solve: A = 5 - B -> 3(5-B) + 2B = 12 -> 15 -3B +2B =12 -> B=3 -> A=2
    corners.append((2.0, 3.0))
    best = (0, 0, -float('inf'))
    for A, B in corners:
        profit = 6 * A + 5 * B
        # check feasibility (numerical safety)
        if A + B <= 5 + 1e-9 and 3 * A + 2 * B <= 12 + 1e-9 and A >= -1e-9 and B >= -1e-9:
            if profit > best[2]:
                best = (A, B, profit)
    return best


def main():
    res = solve_with_scipy()
    if res is None:
        A, B, profit = solve_by_corners()
        method = 'corner-point fallback'
    else:
        A, B, profit = res
        method = 'scipy.optimize.linprog'
    # If values are very close to integers, show as ints
    if isclose(A, round(A), abs_tol=1e-8):
        A = int(round(A))
    if isclose(B, round(B), abs_tol=1e-8):
        B = int(round(B))
    if isclose(profit, round(profit), abs_tol=1e-8):
        profit = int(round(profit))
    print(f"Method: {method}")
    print(f"Produce A = {A} units and B = {B} units for maximum profit of Rs {profit}.")


if __name__ == '__main__':
    main()
