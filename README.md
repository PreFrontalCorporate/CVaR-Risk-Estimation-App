# CVaR Risk Estimation App

## 🚨 Overview

The CVaR Risk Estimation App provides an advanced, production-grade toolkit for risk-aware portfolio optimization using Conditional Value-at-Risk (CVaR). It combines rigorous mathematical proofs, robust dynamic update algorithms, explainability (via SHAP), sector constraint modules, and scenario-based stress testing.

This application is designed to help institutional investors, quant teams, and researchers build resilient portfolios against extreme market shocks.

---

## 💡 Features

- ✅ CVaR-based optimization (parametric and non-parametric options)
- ✅ Dynamic continuous updates with convergence guarantees
- ✅ Constraint modules (e.g., sector caps, no short selling)
- ✅ Scenario stress testing (pandemic, interest rate shocks, etc.)
- ✅ Explainability via SHAP (per-asset risk contributions)
- ✅ Modular, production-ready code structure

---

## 📁 Project Structure

app/ Core backend modules (API logic, optimization, explainability)
notebooks/ Jupyter notebooks for demos and experiments
tests/ Unit tests
data/ Example returns and scenarios
docs/ LaTeX theoretical summary, architecture, explainability write-up
plots/ Example CVaR and SHAP plots

yaml
Copy
Edit

---

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/PreFrontalCorporate/CVaR-Risk-Estimation-App.git
cd CVaR-Risk-Estimation-App

# Install dependencies
pip install -r requirements.txt

# Run local example or start API server (to be implemented)
python app/main.py
💬 Example Usage
Optimize portfolio with CVaR constraints and view dynamic CVaR trajectory.

Visualize SHAP summary plot to understand asset risk contributions.

Simulate scenario shocks to analyze portfolio robustness.

📄 Documentation
Theoretical summary in docs/CVaR_Summary.tex (PDF version also included).

Architecture and module design details in docs/architecture.md.

Explainability methodology in docs/README_explainability.md.

🤝 License
MIT License. See LICENSE file.

🌐 Contributors
PreFrontal Corporate research team

Community and external collaborators

yaml
Copy
Edit

---

# ✅ 📄 **docs/architecture.md**

```markdown
# Architecture Overview

## 💡 High-Level Design

This application is designed in a modular fashion to separate risk optimization logic, explainability, scenario stress testing, and constraints handling. It is built to support an API layer (Flask or FastAPI) for easy integration into larger platforms.

---

## 🔥 Core Modules

### app/optimize.py

- Contains CVaR dynamic update algorithms
- Supports parametric and non-parametric modes
- Implements continuous-time inspired convergence with constraints

### app/constraints.py

- Handles sector caps and custom allocation constraints
- Projection onto feasible sets to respect regulatory or internal policies

### app/explain.py

- SHAP integration to explain per-asset contributions
- Generates summary and force plots for transparency

### app/scenario.py

- Defines functions to simulate shocks (e.g., pandemic, jumps)
- Evaluates portfolio CVaR before and after shock

---

## 📄 API Endpoints (planned)

- `/optimize` — Run CVaR optimization with given returns and constraints
- `/explain` — Return per-asset contribution summaries and plots
- `/scenario` — Run shock scenario analysis
- `/history` — Return historical CVaR and weight paths

---

## 🏗️ Data Flow

User Input (returns, weights, constraints)
↓
Optimization & Constraints Module
↓
Explainability (optional)
↓
Scenario Analysis (optional)
↓
API Response (weights, plots, CVaR metrics)

yaml
Copy
Edit

---

## ⚖️ Future Extensions

- Integration of robust optimization extensions
- Parametric tail models beyond normal (e.g., EVT)
- Real-time streaming data updates

---

## 📄 Additional References

See `docs/CVaR_Summary.tex` for mathematical proofs and theoretical background.