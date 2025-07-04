import numpy as np
import os
from app.explain import explain_asset_contributions

def test_shap_explanation_plot():
    returns = np.random.normal(0.001, 0.02, (200, 5))
    weights = np.ones(5) / 5
    plot_path = explain_asset_contributions(weights, returns)
    assert os.path.exists(plot_path), "SHAP summary plot file not created"
