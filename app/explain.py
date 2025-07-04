# app/explain.py

import pandas as pd
import shap
import matplotlib.pyplot as plt

def explain_asset_contributions(weights, returns_matrix):
    asset_returns = returns_matrix
    X_df = pd.DataFrame(asset_returns)
    y = -(asset_returns @ weights)

    model = lambda X: -(X @ weights).values
    explainer = shap.Explainer(model, X_df)
    shap_values = explainer(X_df)

    shap.summary_plot(shap_values, X_df, show=False)
    plt.savefig("plots/shap_summary.png")
    plt.close()
    return "plots/shap_summary.png"
