
"""
Capital Asset Pricing Model
===========================

"""

###############################################################################

# Author: Dialid Santiago <d.santiago@outlook.com>
# License: MIT
# Description: Advent Calendar 2025 - Plot Capital Asset Pricing Model (CAPM) 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

plt.style.use(
    "https://raw.githubusercontent.com/quantgirluk/matplotlib-stylesheets/main/quant-pastel-light.mplstyle")    


# Asset inputs
mu = np.array([0.18, 0.020, 0.1, 0.07]) # expected returns
variances = np.array([0.20, 0.18, 0.15, 0.19]) # variances
sdtdevs = np.sqrt(variances)
n = len(mu)
Sigma = np.array([
[variances[0], 0.02, 0.04, 0.01],
[0.02, variances[1], 0.02, 0.01],
[0.04, 0.02, variances[2], 0.03],
[0.01, 0.01, 0.03, variances[3]]
])

# Porftfolio simulation
n_portfolios = 5000
returns = np.zeros(n_portfolios)
risks = np.zeros(n_portfolios)

for i in range(n_portfolios):
    w = np.random.rand(n)
    w /= w.sum()
    returns[i] = w @ mu
    risks[i] = np.sqrt(w @ Sigma @ w)


# Sharpe ratios
r_f = 0.04  # risk-free rate
sharpes = (returns - r_f) / risks

# Tangency portfolio (maximum Sharpe ratio)
idx = np.argmax(sharpes)
tan_return = returns[idx]
tan_risk = risks[idx]

# Capital Market Line
sml_x = np.linspace(0, risks.max(), 100)
sml_y = r_f + (tan_return - r_f) / tan_risk * sml_x

# Constraints
cons_sum = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = [(0, 1)] * n

# Portfolio functions
def port_return(w):
    return w @ mu

def port_risk(w):
    return np.sqrt(w @ Sigma @ w)

# Minimum variance portfolio
res_mvp = minimize(port_risk, x0=np.ones(n)/n,
bounds=bounds, constraints=cons_sum)
w_mvp = res_mvp.x

# Efficient frontier
target_returns = np.linspace(mu.min(), mu.max(), 50)
frontier_risk = []

for r in target_returns:
    cons = (
    cons_sum,
    {'type': 'eq', 'fun': lambda w, r=r: w @ mu - r}
    )
    res = minimize(port_risk, x0=np.ones(n)/n,
    bounds=bounds, constraints=cons)
    frontier_risk.append(res.fun)
    
# Plot
fig, ax = plt.subplots(figsize=(12, 7), dpi=200)
plt.scatter(risks, returns, c=sharpes, cmap="coolwarm_r", alpha=0.25)
plt.colorbar(label="Sharpe Ratio")
plt.scatter(sdtdevs, mu, marker='o', s=50, color='black', edgecolor='black', zorder=5, label="Individual Assets")
plt.plot(sml_x, sml_y, linestyle='-', linewidth=2, label="Capital Market Line (CML)", color="lightgreen")
plt.plot(frontier_risk, target_returns, linewidth=2, linestyle='--', color="steelblue", label="Efficient Frontier")
plt.scatter(port_risk(w_mvp), port_return(w_mvp), s=200, marker='*', color='red', zorder=5, label="Minimum Variance Portfolio")
plt.scatter(tan_risk, tan_return, s=200, marker='*', color='magenta', zorder=5, label="Maximum Sharpe Ratio Portfolio")
plt.scatter(0, r_f, s=200, marker='*', color='black', zorder=5, label="Risk-Free Portfolio")
plt.xlabel("Risk (Std Dev)")
plt.ylabel("Expected Return")
plt.title("Capital Asset Pricing Model (CAPM)")
plt.legend()
plt.show()