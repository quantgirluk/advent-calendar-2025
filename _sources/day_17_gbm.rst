Day 17: Geometric Brownian Motion
================================


A Geometric Brownian Motion (GBM) is a continuous-time stochastic process widely used in financial mathematics to model the dynamics of asset prices. It is characterized by the property that the logarithm of the asset price follows a Brownian motion with drift. GBM is particularly popular in option pricing models, such as the Black-Scholes model, due to its ability to capture the random nature of asset price movements while ensuring that prices remain positive.   


Definition
----------

A Geometric Brownian Motion :math:`S(t), t \geq 0` is defined by the stochastic differential equation (SDE):

.. math::
    dS(t) = \mu S(t) dt + \sigma S(t) dB(t)

where:      

- :math:`\mu` is the drift coefficient, representing the expected return of the asset.
- :math:`\sigma` is the volatility coefficient, representing the standard deviation of the asset's returns.
- :math:`B(t)` is a standard Brownian motion (Wiener process).

The solution to this SDE can be expressed as:

.. math::
    S(t) = S(0) \exp\left(\left(\mu - \frac{1}{2} \sigma^2\right)t + \sigma B(t)\right)

where :math:`S(0)` is the initial asset price at time :math:`t = 0`.    

.. figure:: auto_plots/images/sphx_glr_plot_gbm_001.png     
   :alt: Geometric Brownian Motion Simulation
   :align: center

Geometric Brownian Motion Simulation. Image made with `aleatory <https://github.com/quantgirluk/aleatory>`_


