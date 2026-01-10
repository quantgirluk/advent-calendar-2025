"""
Yied Curve
==========

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar Day 3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")


tenors = [
	'30-year',
	'10-year',
	'5-year',
	'3-year',
	'2-year',
	'1-year',
	'6-month',
	'3-month',
	'1-month',
]

tenor_years = [30, 10, 5, 3, 2, 1, 0.5, 0.25, 1/12]

yield_curves = {
    'Date': {
        'date': '2025-11-30',
        'yields': [4.7, 4.09, 3.67, 3.56, 3.55, 3.66, 3.78, 3.94, 4.03]
    }
}

df_all = []
for case_name, case_data in yield_curves.items():
    df_case = pd.DataFrame({
        'case': case_name,
        'date': case_data['date'],
        'tenor': tenors,
        'yield': case_data['yields'],
        'tenor_years': tenor_years
    })
    df_all.append(df_case)

df_yield = pd.concat(df_all, ignore_index=True)


fig, ax = plt.subplots(figsize=(12, 7), dpi=150)
for case_name, group in df_yield.groupby('case'):
    ax.plot(group['tenor_years'], group['yield'], marker='o', linewidth=2, color="red") 
ax.set_xlabel("Tenor (in Years)")
ax.set_ylabel("Yield ($\\%$)")
ax.set_title("U.S. Treasuries Yield Curve - November 30, 2025")
ax.legend()
ax.grid(alpha=0.3)
plt.show()