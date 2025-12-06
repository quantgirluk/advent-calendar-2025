Day 2: Time Value of Money
==========================

    "A dollar today is worth more than a dollar tomorrow."

    — Common Saying

**Definition.** The Time Value of Money is the idea that a sum of money today is worth more than the same amount in the future, because it can be invested and earn returns. In other words — money has a cost of time.

The future value (FV) of money today is:

.. math::

   FV = PV \ (1 + r)^{n}

where

- ``PV`` : Present Value (or value at time zero)
- ``r`` : interest rate at which the amount compounds each period
- ``n`` : number of periods

.. figure:: auto_plots/images/sphx_glr_plot_tvm_001.png
   :name: fv-fig

   Future Value illustration with different interest rates.

Thus, we have the following formula for Present Value

.. math::

   PV = \frac{FV}{(1 + r)^{n}}

.. figure:: auto_plots/images/sphx_glr_plot_tvm_002.png
   :name: pv-fig

   Present Value illustration with different interest rates.

Random Facts
------------

- The concept of the time value of money has been recognized for centuries, with its oldest mention found in the Talmud, a central text in Judaism.

- TVM and **inflation** are closely linked concepts that reveal why money today is more valuable than the same amount in the future. TVM reflects the idea that money can earn returns over time, while inflation gradually reduces its purchasing power by making goods and services more expensive. Even if money is left untouched, inflation ensures that it buys less in the future.

For example, in England prices have increased by 91.9% between 2000 and October 2025. In other words, you would need £191.86 in October 2025 to have the same purchasing power as £100.00 in 2000.

.. figure:: images/inflation25years.png
   :height: 500px
   :name: inflation-fig

   Inflation impact on purcharsing power. Source: `BoE Inflation Calculator <https://www.bankofengland.co.uk/monetary-policy/inflation/inflation-calculator>`_.

- Present value calculations, and similarly future value calculations, are used to value loans, mortgages, annuities, sinking funds, perpetuities, bonds, and more.
