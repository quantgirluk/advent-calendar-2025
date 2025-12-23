
"""
Geometric Brownian Motion
===============

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot Geometric Brownian Motion

from aleatory.processes import GBM
from aleatory.styles import qp_style
qp_style()  # Use quant-pastel-style
p = GBM()   
fig = p.draw(n=100, N=250, figsize=(12, 7), dpi=200, colormap='viridis')
fig.show()
