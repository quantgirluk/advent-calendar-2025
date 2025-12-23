"""
Time Value of Money 
===================

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar Day 

import numpy as np
import matplotlib.pyplot as plt

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")


PV = 100
t = np.linspace(0, 10, 200) # time in years
rates = [0.01, 0.02, 0.05, 0.10] # 1%, 2%, 5%, 10%



fig, ax = plt.subplots(dpi=150, figsize=(10, 7))
# Future Value (given PV now what is value in the future)

for r in rates:
    FV = PV * (1 + r) ** t
    label = rf"r = {r*100:.0f}\%"
    ax.plot(t, FV, label=label, linewidth=2)
ax.axhline(PV, linestyle='--')
ax.set_xlabel("Years")
ax.set_ylabel("Value")
ax.set_title("Future Value of Money (PV = 100)")
ax.legend()
ax.grid(alpha=0.3)

plt.show()

# Present Value (value today of receiving FV in the future)
fig, ax = plt.subplots(figsize=(10, 7), dpi=150)
FV_future = 100
for r in rates:
    PV_t = FV_future / (1 + r) ** t
    label = rf"r = {r*100:.0f}\%"
    ax.plot(t, PV_t, label=label, linewidth=2)
ax.axhline(FV_future, linestyle='--')
ax.set_xlabel("Years")
ax.set_ylabel("Value")
ax.set_title("Present Value of Future Amount (FV = 100)")
ax.legend()
ax.grid(alpha=0.3)
plt.show()