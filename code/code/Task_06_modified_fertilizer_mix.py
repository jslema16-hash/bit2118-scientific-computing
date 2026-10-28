import numpy as np

# Modified case: a farmer mixes two fertilizers.
# Fertilizer X is 20% nitrogen and 10% phosphorus.
# Fertilizer Y is 10% nitrogen and 30% phosphorus.
# The field needs exactly 50 kg of nitrogen and 60 kg of phosphorus.
#
# Assumptions: only nitrogen and phosphorus matter, percentages are exact,
# and amounts can be any real number of kilograms.
#
# x = kg of Fertilizer X, y = kg of Fertilizer Y

A = np.array([
    [0.20, 0.10],   # nitrogen fraction in X and Y
    [0.10, 0.30]    # phosphorus fraction in X and Y
])

b = np.array([50.0, 60.0])   # required kg of nitrogen and phosphorus

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Fertilizer X: {solution[0]:.1f} kg")
print(f"Fertilizer Y: {solution[1]:.1f} kg")
print("Nutrients supplied (N, P):", A @ solution)
print("Residual norm:", np.linalg.norm(residual))
print("Determinant:", np.linalg.det(A))
