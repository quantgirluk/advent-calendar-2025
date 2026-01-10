"""
Sharpe Ratio
============
"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 Day 12 - Sharpe Ratio Visualization


import numpy as np
import matplotlib.pyplot as plt

quant_pastel = "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle"
plt.style.use(quant_pastel)

r_f = 0.04  # Risk-free rate

# Portfolios with same expected return but different risk
returns = np.array([0.10, 0.10, 0.10])
risks = np.array([0.18, 0.12, 0.08])
sharpes = (returns - r_f) / risks


fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=150)
samples = []
for (r, risk, sharpe) in zip(returns, risks, sharpes):
    sample = np.random.normal(loc=r, scale=risk, size=1000)
    samples.append(sample)
    axes[0].hist(sample, bins=30, alpha=0.7, label=f"Sharpe = {sharpe:.2f}")
    axes[2].scatter(risk, r, s=100)
    axes[2].annotate(f"Sharpe = {sharpe:.2f}",
    (risk, r), xytext=(5, -12),
    textcoords="offset points")
axes[0].legend()
bplot=axes[1].boxplot(samples, vert=True, patch_artist=True)     
colors = ['#0079ff', '#ffb84c', '#00dfa2',]
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
axes[0].set_title("Returns Distribution Histogram")
axes[0].set_xlabel("Return")
axes[0].set_ylabel("Frequency") 
axes[1].set_title("Returns Distribution Box Plot")
axes[1].set_ylabel("Return")
axes[2].set_title("Risk vs Return")
axes[2].set_xlabel("Risk")
axes[2].set_ylabel("Return")
plt.suptitle("Sharpe Ratio Visualization\n Portfolios with Same Expected Return but Different Risk Levels", fontsize=16)
plt.tight_layout()
plt.show()  
    