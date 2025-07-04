# CVaR Risk Estimation App — System & API Architecture

## 🏗️ Overview

This document summarizes the architecture of the CVaR Risk Estimation App, designed for robust financial risk estimation and portfolio optimization.

---

## 🧩 Components

### API Layer

- Built with Flask for all financial APIs
- Endpoints:
  - `/optimize`: CVaR-based portfolio optimization
  - `/explain`: SHAP-based explainability reports
  - `/scenario`: Scenario-based shock analysis
  - `/history`: Historical trajectories (placeholder)

---

### Core Modules

- `optimize.py`: Continuous-time inspired dynamic CVaR optimizer
- `constraints.py`: Sector caps, projection logic
- `scenario.py`: Stress testing with shocks
- `explain.py`: SHAP interpretability integration
- `utils.py`: Shared CVaR functions and projection utilities

---

### Data

- Example returns (simulated or historical): `data/example_returns.csv`
- Scenario shock definitions: `data/sample_scenarios.csv`

---

## 💡 Design Philosophy

- Modular and clear separation of concerns
- Mathematically rigorous (Lyapunov stability, duality proofs)
- Flexible (parametric & non-parametric modes)
- Transparent (SHAP explainability)

---

## ⚙️ Future Extensions

- Integrate robust optimization extensions
- Real-time data ingestion and streaming analysis
- Add authentication and logging (planned via `cbb.homes`)
