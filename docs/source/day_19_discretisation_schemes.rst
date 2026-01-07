Day 19: Discretisation Schemes
==============================


There are two primary discretisation schemes used in numerical simulations of stochastic processes: the Euler-Maruyama method and the Milstein method. These methods are essential for approximating solutions to stochastic differential equations (SDEs) that cannot be solved analytically.
1. Euler-Maruyama Method
2. Milstein Method

Euler-Maruyama
--------------

This method is a straightforward extension of the Euler method for ordinary differential equations to stochastic differential equations. It is widely used due to its simplicity and ease of implementation.

Given an SDE of the form:

.. math::
   dX_t = a(X_t, t) dt + b(X_t, t) dW_t

where :math:`a(X_t, t)` is the drift term, :math:`b(X_t, t)` is the diffusion term, and :math:`W_t` is a Wiener process (Brownian motion), the Euler-Maruyama discretisation is given by:

.. math::
    X_{t+\Delta t} = X_t + a(X_t, t) \Delta t + b(X_t, t) \Delta W_t

where :math:`\Delta W_t` is a normally distributed random variable with mean 0 and variance :math:`\Delta t`.


Milstein 
--------

The Milstein method is a higher-order discretisation scheme that provides better accuracy than the Euler-Maruyama method, especially for SDEs with non-linear diffusion terms. It includes an additional term that accounts for the derivative of the diffusion coefficient.
The Milstein discretisation is given by:

.. math::
    X_{t+\Delta t} = X_t + a(X_t, t) \Delta t + b(X_t, t) \Delta W_t + \frac{1}{2} b(X_t, t) b'(X_t, t) \left( (\Delta W_t)^2 - \Delta t \right)

where :math:`b'(X_t, t)` is the derivative of the diffusion term with respect to :math:`X_t`.
