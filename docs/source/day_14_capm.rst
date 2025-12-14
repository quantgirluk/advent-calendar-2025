Day 14 : Capital Asset Pricing Model
====================================



In finance, the capital asset pricing model (CAPM) is a model used to determine a theoretically 
appropriate required rate of return of an asset, to make decisions about adding assets to a well-diversified portfolio.


Definition
----------

The CAPM formula is defined as:

.. math::

   E(R_i) = R_f + \beta_i (E(R_m) - R_f)

Where:

- :math:`E(R_i)` is the expected return of the capital asset
- :math:`R_f` is the risk-free rate of return,
- :math:`E(R_m)` is the expected return of the market
- :math:`\beta_i` (the beta) is the sensitivity of the expected excess asset returns to the expected excess beta of the investment

Moreover,

- :math:`E(R_m) - R_f` is known as the market risk premium
- :math:`E(R_i) - R_f` is known as the individual asset's risk premium


Note 1: the expected market rate of return is usually estimated by measuring the arithmetic average 
of the historical returns on a market portfolio (e.g. S&P 500).

Note 2: the risk free rate of return used for determining the risk premium is usually the arithmetic 
average of historical risk free rates of return and not the current risk free rate of return.


The CAPM makes several asumptions about investors:
- Aim to maximize economic utilities (Asset quantities are given and fixed).
- Are rational and risk-averse.
- Are broadly diversified across a range of investments.
- Are price takers, i.e., they cannot influence prices.
- Can lend and borrow unlimited amounts under the risk free rate of interest.
- Trade without transaction or taxation costs.
- Deal with securities that are all highly divisible into small parcels (All assets are perfectly divisible and liquid).
- Have homogeneous expectations.
- Have all information available all at the same time.



Interpretation
--------------

The CAPM suggests that the expected return of an asset is determined by its sensitivity to market risk (beta),
the risk-free rate, and the expected market return. A higher beta indicates higher risk and thus a higher expected return.


The beta is calculated as follows:

.. math::

   \beta_i = \frac{Cov(R_i, R_m)}{Var(R_m)}    

where:
- :math:`Cov(R_i, R_m)` is the covariance between the asset's returns and the market's returns
- :math:`Var(R_m)` is the variance of the market's returns
