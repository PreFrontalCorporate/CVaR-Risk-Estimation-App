# app/optimize.py

import numpy as np
from .utils import project_simplex, portfolio_cvar_empirical, portfolio_cvar_parametric
from .constraints import project_constraints
from .config import ALPHA, ETA, SECTOR_CAP

def compute_marginal_cvar(weights, returns_matrix, alpha=ALPHA, epsilon=1e-4, parametric=False):
    base_cvar = (portfolio_cvar_parametric if parametric else portfolio_cvar_empirical)(weights, returns_matrix, alpha)
    marginal_cvar = np.zeros_like(weights)
    for i in range(len(weights)):
        perturbed = weights.copy()
        perturbed[i] += epsilon
        perturbed = project_simplex(perturbed)
        pert_cvar = (portfolio_cvar_parametric if parametric else portfolio_cvar_empirical)(perturbed, returns_matrix, alpha)
        marginal_cvar[i] = (pert_cvar - base_cvar) / epsilon
    return marginal_cvar

def continuous_cvar_update(weights, returns_matrix, alpha=ALPHA, eta=ETA, iterations=20,
                           parametric=False, sector_mask=None, sector_cap=SECTOR_CAP):
    cvar_history = []
    for _ in range(iterations):
        grad = compute_marginal_cvar(weights, returns_matrix, alpha, parametric=parametric)
        weights = weights - eta * grad
        weights = project_simplex(weights)
        if sector_mask is not None:
            weights = project_constraints(weights, sector_mask, sector_cap)
        cvar_val = (portfolio_cvar_parametric if parametric else portfolio_cvar_empirical)(weights, returns_matrix, alpha)
        cvar_history.append(cvar_val)
    return weights, cvar_history
