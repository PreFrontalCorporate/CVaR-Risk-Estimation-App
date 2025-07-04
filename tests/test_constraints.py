import numpy as np
from app.constraints import project_constraints

def test_sector_constraints_respected():
    weights = np.array([0.2, 0.1, 0.2, 0.3, 0.2])
    sector_mask = np.array([True, True, False, False, False])
    adjusted = project_constraints(weights, sector_mask, sector_cap=0.3)
    assert np.sum(adjusted[sector_mask]) <= 0.3 + 1e-5, "Sector cap exceeded"
    assert np.isclose(np.sum(adjusted), 1.0), "Weights do not sum to 1 after constraint"
