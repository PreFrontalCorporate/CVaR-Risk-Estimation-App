import numpy as np
from app.optimize import continuous_cvar_update

def test_continuous_update_basic():
    np.random.seed(0)
    n_assets = 5
    returns = np.random.normal(0.001, 0.02, (500, n_assets))
    weights = np.ones(n_assets) / n_assets
    sector_mask = np.array([True, True, False, False, False])

    final_weights, cvar_hist = continuous_cvar_update(
        weights,
        returns,
        alpha=0.05,
        iterations=5,
        parametric=False,
        sector_mask=sector_mask
    )
    assert np.isclose(np.sum(final_weights), 1.0), "Final weights do not sum to 1"
    assert all(final_weights >= 0), "Negative weights found"
    assert np.isfinite(cvar_hist[-1]), "Final CVaR is not finite"
