# app/scenario.py

from .utils import portfolio_cvar_empirical, portfolio_cvar_parametric
from .config import ALPHA

def scenario_analysis(weights, base_returns, shock_vector, alpha=ALPHA, parametric=False):
    shocked_returns = base_returns + shock_vector
    cvar_before = (portfolio_cvar_parametric if parametric else portfolio_cvar_empirical)(weights, base_returns, alpha)
    cvar_after = (portfolio_cvar_parametric if parametric else portfolio_cvar_empirical)(weights, shocked_returns, alpha)
    return cvar_before, cvar_after
