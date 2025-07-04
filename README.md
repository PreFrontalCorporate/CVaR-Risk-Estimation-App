# 📄 CVaR Risk Estimation App

## 🚨 Overview

The CVaR Risk Estimation App is a production-grade, research-driven toolkit for advanced portfolio risk optimization using Conditional Value-at-Risk (CVaR). It combines rigorous mathematical foundations, dynamic CVaR adjustment algorithms, sector constraints, explainability (SHAP integration), and scenario stress testing into a single modular system.

---

## 💡 Features

* ✅ CVaR-based optimization (parametric and empirical options)
* ✅ Continuous-time inspired dynamic updates with convergence guarantees
* ✅ Sector and allocation constraint handling
* ✅ Scenario stress testing (e.g., market shocks)
* ✅ Per-asset explainability via SHAP (risk attribution)
* ✅ Clean, modular Flask API design

---

## 📁 Directory Structure

```
app/                 Core backend modules (API logic, optimization, explainability)
notebooks/          Jupyter notebooks for experiments and demo workflows
tests/              Unit tests with fixtures
data/               Example return matrices and scenario files
docs/               Theoretical LaTeX companion, architecture docs, explainability docs
plots/              Example CVaR trajectory, SHAP plots, scenario comparison
```

---

## ⚙️ Quick Start

```bash
git clone https://github.com/PreFrontalCorporate/CVaR-Risk-Estimation-App.git
cd CVaR-Risk-Estimation-App

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run tests
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest tests/

# Start Flask server
python app/main.py
```

---

## 🛰️ API Endpoints

### `/optimize`

Run CVaR-based portfolio optimization.

**POST JSON payload:**

```json
{
  "weights": [0.2, 0.2, 0.2, 0.2, 0.2],
  "returns": [[0.01, -0.02, ...]],
  "parametric": false,
  "sector_mask": [true, true, false, false, false]
}
```

**Response:** Optimized weights and CVaR trajectory.

---

### `/explain`

Generate SHAP explainability summary plot.

**POST JSON payload:**

```json
{
  "weights": [0.2, 0.2, 0.2, 0.2, 0.2],
  "returns": [[0.01, -0.02, ...]]
}
```

**Response:** Path to saved SHAP summary plot.

---

### `/scenario`

Run scenario shock analysis.

**POST JSON payload:**

```json
{
  "weights": [0.2, 0.2, 0.2, 0.2, 0.2],
  "returns": [[0.01, -0.02, ...]],
  "shock_vector": [[0.05, 0, 0, 0, 0]],
  "parametric": false
}
```

**Response:** CVaR before and after shock.

---

### `/history`

Placeholder endpoint for future historical trajectory analysis.

---

## 🧪 Tests

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest tests/
```

**Expected output:**

```
4 passed in X.XXs
```

All core modules (optimization, constraints, explain, scenario) are fully tested and validated.

---

## 📄 Documentation

* Theoretical proofs and math: `docs/CVaR_Summary.tex` and `docs/CVaR_Summary.pdf`
* Architecture: `docs/architecture.md`
* Explainability: `docs/README_explainability.md`

---

## 💬 Example Use Cases

* Rebalance portfolios under extreme market scenarios.
* Create explainability reports for compliance and stakeholders.
* Enforce sector allocation caps dynamically.

---

## 🤝 License

MIT License — see `LICENSE` file.

---

## 🌐 Maintained by

PreFrontal Corporate research and engineering team.
