import numpy as np
from app.scenario import scenario_analysis

def test_scenario_impact():
    weights = np.ones(5) / 5
    returns = np.random.normal(0.001, 0.02, (500, 5))
    shock = np.zeros_like(returns)
    shock[:, 0] = 0.05

    cvar_before, cvar_after = scenario_analysis(weights, returns, shock)
    assert cvar_after < cvar_before, "CVaR after shock should reflect higher losses"
