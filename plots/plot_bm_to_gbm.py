"""
GBM via Transformation of BM
============================

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot GBM via Transformation of BM

import matplotlib.pyplot as plt
import numpy as np
from aleatory.processes import BrownianMotion
from aleatory.styles import qp_style
qp_style()  # Use quant-pastel-style

T = 1.0
n = 200
x0 = 2.0 
mu = 1.0
sigma = 0.5
t = 1.0
times = np.linspace(0, T, n)  # Time Partition
BM = BrownianMotion(T=T) # Brownian Motion
bm_path = BM.sample_at(times) # Simulated path from BM
gbm_path = x0*np.exp((mu - 0.5*sigma**2)*times + sigma*bm_path) # Simulated path from GBM


plt.plot(times, bm_path, lw=2, label='Brownian Motion')
plt.plot(times, gbm_path, lw=2, label='Geometric Brownian Motion')
plt.title('Geometric Brownian Motion\n via Transformation of Brownian Motion', fontsize=12)
plt.legend()
plt.show()