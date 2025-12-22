Day 18: Martingale
====================

    "A martingale is like a fair game, where your expected winnings at any point in time are equal to your current stake."
    ― Anonymous


A martingale is a type of stochastic process that models a fair game in probability theory. It is characterized by the property that the conditional expectation of the next value in the process, given all prior values, is equal to the current value. In simpler terms, a martingale represents a sequence of random variables where, on average, future values are expected to be equal to the present value, indicating no predictable trend or bias over time.

Definition
----------
A stochastic process :math:`X = {X_t, t \geq 0}` defined on a probability space :math:`(Ω, F, P)` with a filtration :math:`{F_t, t \geq 0}` is called a martingale if it satisfies
the following conditions:
1. :math:`X_t` is :math:`F_t`-measurable for all :math:`t \geq 0`.
2. :math:`E[|X_t|] < \infty` for all :math:`t \geq 0`.
3. For all :math:`s < t`, :math:`E[X_t | F_s] = X_s` almost surely.
