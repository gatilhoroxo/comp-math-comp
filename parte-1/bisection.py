import pandas as pd

def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Bisection method for root finding.

    Returns:
        root: approximated root
        table: pandas DataFrame with iteration details
    """

    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    rows = []

    for i in range(1, max_iter + 1):

        c = (a + b) / 2
        fc = f(c)

        rows.append({
            "iteration": i,
            "a": a,
            "b": b,
            "midpoint": c,
            "f(midpoint)": fc,
            "interval_width": b - a
        })

        if fc == 0 or (b - a)/2 < tol:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    table = pd.DataFrame(rows)
    return c, table

# =======================
# Define the function
def f(x):
    return x**3 + x - 1

# Initial interval
a = 0
b = 1

# Run the bisection method
root, table = bisection(f, a, b)

print("Approximate root:", root)
print("f(root) =", f(root))

# Display iteration table
table
