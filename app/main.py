# cvar_app/app/main.py

from flask import request, jsonify
import numpy as np

from . import cvar_bp  # Import blueprint instead of creating app directly

from .optimize import continuous_cvar_update
from .explain import explain_asset_contributions
from .scenario import scenario_analysis
from .config import ALPHA

@cvar_bp.route("/optimize", methods=["POST"])
def optimize():
    data = request.json
    weights = np.array(data["weights"])
    returns = np.array(data["returns"])
    sector_mask = np.array(data.get("sector_mask", [False]*len(weights)))
    parametric = data.get("parametric", False)

    final_weights, cvar_hist = continuous_cvar_update(
        weights,
        returns,
        alpha=ALPHA,
        parametric=parametric,
        sector_mask=sector_mask
    )
    return jsonify({
        "final_weights": final_weights.tolist(),
        "cvar_history": [float(val) for val in cvar_hist]
    })

@cvar_bp.route("/explain", methods=["POST"])
def explain():
    data = request.json
    weights = np.array(data["weights"])
    returns = np.array(data["returns"])
    plot_path = explain_asset_contributions(weights, returns)
    return jsonify({"shap_summary_plot": plot_path})

@cvar_bp.route("/scenario", methods=["POST"])
def scenario():
    data = request.json
    weights = np.array(data["weights"])
    base_returns = np.array(data["returns"])
    shock_vector = np.array(data["shock_vector"])
    parametric = data.get("parametric", False)

    cvar_before, cvar_after = scenario_analysis(weights, base_returns, shock_vector, parametric=parametric)
    return jsonify({
        "cvar_before": float(cvar_before),
        "cvar_after": float(cvar_after)
    })

@cvar_bp.route("/history", methods=["GET"])
def history():
    return jsonify({"message": "History module will be implemented in future iterations."})
