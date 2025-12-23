"""
Euler, Milstein Schemes Convergence
===================================

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot Euler, Milstein Convergence

import matplotlib.pyplot as plt
import numpy as np
from aleatory.processes import BrownianMotion
from aleatory.styles import qp_style
qp_style()  # Use quant-pastel-style

# GBM parameters
S0 = 100.0
mu = 0.05
sigma = 0.3
T = 1.0

M = 5000          # number of paths
N_ref = 2**12     # fine grid for reference solution
dt_ref = T / N_ref

# Coarse step sizes
N_values = [2**k for k in range(4, 10)]  # 16 ... 512
dt_values = [T / N for N in N_values]

# --- Storage ---
errors_euler = []
errors_milstein = []

np.random.seed(42)

for N in N_values:
    dt = T / N
    ratio = N_ref // N

    err_euler = 0.0
    err_mil = 0.0

    for _ in range(M):
        # Fine Brownian increments
        dW_fine = np.sqrt(dt_ref) * np.random.randn(N_ref)

        # Aggregate increments for coarse grid
        dW_coarse = dW_fine.reshape(N, ratio).sum(axis=1)

        # --- Exact solution ---
        W_T = dW_fine.sum()
        S_exact = S0 * np.exp(
            (mu - 0.5 * sigma**2) * T + sigma * W_T
        )

        # --- Euler scheme ---
        S_e = S0
        for dW in dW_coarse:
            S_e += mu * S_e * dt + sigma * S_e * dW

        # --- Milstein scheme ---
        S_m = S0
        for dW in dW_coarse:
            S_m += (
                mu * S_m * dt
                + sigma * S_m * dW
                + 0.5 * sigma**2 * S_m * (dW**2 - dt)
            )

        err_euler += abs(S_e - S_exact)
        err_mil += abs(S_m - S_exact)

    errors_euler.append(err_euler / M)
    errors_milstein.append(err_mil / M)

# --- Plot ---
plt.figure(figsize=(8, 6))
plt.loglog(dt_values, errors_euler, "o-", label="Euler–Maruyama")
plt.loglog(dt_values, errors_milstein, "s-", label="Milstein")

# Reference slopes
plt.loglog(
    dt_values,
    errors_euler[0] * (np.array(dt_values) / dt_values[0])**0.5,
    "k--",
    label="Slope 1/2",
)
plt.loglog(
    dt_values,
    errors_milstein[0] * (np.array(dt_values) / dt_values[0]),
    "k-.",
    label="Slope 1",
)

plt.xlabel(r"$\Delta t$")
plt.ylabel("Strong error at T")
plt.title("Strong Convergence for GBM")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.show()

