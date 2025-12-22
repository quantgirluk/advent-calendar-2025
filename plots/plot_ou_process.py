
"""
Ornstein-Uhlenbeck Process
==========================

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot Geometric Ornstein-Uhlenbeck Process


from aleatory.processes import OUProcess
from aleatory.styles import qp_style

qp_style()  # Use quant-pastel-style

p = OUProcess()
fig = p.draw(n=200, N=200, figsize=(12, 7), colormap="twilight")
fig.show()



p = OUProcess(theta=1.0, sigma=1.0, initial=0.0, T=2.0)
fig = p.draw(n=200, N=200, figsize=(12, 7), colormap="Blues")
fig.show()