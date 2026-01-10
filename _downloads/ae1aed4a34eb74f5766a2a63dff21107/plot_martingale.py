
"""
Martingales
===========

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Simulate and visualise a Simple Random Walk

from aleatory.processes import SimpleRandomWalk, RandomWalk
from aleatory.styles import qp_style

qp_style()  # Use quant-pastel-style

p = RandomWalk()
fig = p.draw(n=100, N=200, figsize=(12, 7), colormap="cool",
             title="A Standard Random Walk (p = 0.5) is a Martingale")
fig.show()

p = SimpleRandomWalk(p=0.25)
fig = p.draw(n=100, N=200, figsize=(12, 7), colormap="summer",
             title="A Simple Random Walk with p=0.25 is a Supermartingale")
fig.show()

p = SimpleRandomWalk(p=0.75)
fig = p.draw(n=100, N=200, figsize=(12, 7), colormap="autumn",
             title="A Simple Random Walk with p=0.75 is a Submartingale")
fig.show()