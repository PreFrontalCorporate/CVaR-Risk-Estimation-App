# Explainability and SHAP Integration

## 🎯 Motivation

Transparency is critical for financial models, especially in portfolio risk management. To comply with regulatory demands and improve investor trust, we integrate per-asset interpretability.

---

## 💡 SHAP Values

SHAP (SHapley Additive exPlanations) values quantify each asset’s contribution to portfolio tail risk. Based on cooperative game theory, SHAP assigns each feature (asset) a risk contribution score.

---

## 🏗️ Implementation

- Uses the SHAP Explainer on per-asset return matrix
- Computes global summary plots to visualize contributions
- Supports local force plots for individual "what-if" scenarios

---

## 📈 Outputs

- Beeswarm summary plot: highlights dominant risk contributors
- Local force plots: explain asset-specific impacts on a single scenario
- Textual summary: "Asset 2 contributes 40% of tail risk; consider reducing allocation"

---

## 🤖 Code Reference

See `app/explain.py` for SHAP integration details and `notebooks/Explainability_Demo.ipynb` for sample plots.

---

## 📄 References

- Lundberg, S., and Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. NeurIPS.
