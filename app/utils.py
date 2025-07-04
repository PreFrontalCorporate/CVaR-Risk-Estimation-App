# app/utils.py

import numpy as np
from scipy.stats import norm

def project_simplex(w):
    w = np.maximum(w, 1e-5)
    return w / np.sum(w)

def portfolio_cvar_empirical(weights, returns_matrix, alpha=0.05):
    portfolio_returns = returns_matrix @ weights
    losses = -portfolio_returns
    var = np.percentile(losses, 100 * (1 - alpha))
    cvar = losses[losses >= var].mean()
    return cvar

def portfolio_cvar_parametric(weights, returns_matrix, alpha=0.05):
    portfolio_returns = returns_matrix @ weights
    mu = np.mean(portfolio_returns)
    sigma = np.std(portfolio_returns)
    var = - (mu + sigma * norm.ppf(alpha))
    cvar = - (mu + sigma * norm.pdf(norm.ppf(alpha)) / alpha)
    return cvar
