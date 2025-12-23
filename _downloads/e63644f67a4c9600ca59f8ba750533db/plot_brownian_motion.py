
"""
Brownian Motion
===============

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot Brownian Motion

from aleatory.processes import BrownianMotion
from aleatory.styles import qp_style
qp_style()  # Use quant-pastel-style
p = BrownianMotion()

fig = p.draw(n=100, N=250, figsize=(12, 7), dpi=200)
fig.show()

