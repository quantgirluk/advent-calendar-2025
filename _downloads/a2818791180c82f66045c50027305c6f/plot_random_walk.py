
"""
Random Walk
============

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot Random Walk

from aleatory.processes import SimpleRandomWalk, RandomWalk
from aleatory.styles import qp_style

qp_style()  # Use quant-pastel-style

p = RandomWalk()
fig = p.draw(n=100, N=300, figsize=(12, 7), dpi=200)
fig.show()


p = SimpleRandomWalk(p=0.75)
fig = p.draw(n=100, N=300, figsize=(12, 7), dpi=200)
fig.show()