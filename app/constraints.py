# app/constraints.py

import numpy as np
from .utils import project_simplex

def project_constraints(weights, sector_mask, sector_cap=0.3):
    sector_sum = np.sum(weights[sector_mask])
    if sector_sum > sector_cap:
        excess = sector_sum - sector_cap
        weights[sector_mask] -= excess * weights[sector_mask] / sector_sum
        weights = np.maximum(weights, 1e-5)
        weights = project_simplex(weights)
    return weights
