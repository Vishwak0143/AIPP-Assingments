"""Analyze f(x) = 2*x^3 + 4*x + 5 for minima.

The derivative is f'(x) = 6*x^2 + 4 which has no real roots (>=4).
Therefore f is strictly increasing and has no finite minimum (infimum = -inf).
"""
def analyze_minimum():
    # Coefficients for f'(x) = 6x^2 + 0*x + 4
    a, b, c = 6, 0, 4
    disc = b * b - 4 * a * c
    if disc < 0:
        print("Derivative has no real roots (discriminant < 0).")
        print("f'(x) = 6*x^2 + 4 > 0 for all real x, so f is strictly increasing.")
        print("Therefore there is no finite minimum; the function decreases without bound as x -> -infinity.")
    else:
        # (This branch won't be reached for this function, but kept for completeness.)
        import math
        r1 = (-b + math.sqrt(disc)) / (2 * a)
        r2 = (-b - math.sqrt(disc)) / (2 * a)
        print(f"Critical points at x = {r1} and x = {r2}")


if __name__ == '__main__':
    analyze_minimum()
