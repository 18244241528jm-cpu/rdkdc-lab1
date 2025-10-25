import numpy as np
from skew3 import skew3

def expcr(phi) -> np.ndarray:
    """Rotation exponential: phi = ω*θ (3,)"""
    phi = np.asarray(phi,float).reshape(3)
    th = np.linalg.norm(phi)
    if th < 1e-12:
        return np.eye(3) + skew3(phi)
    w = phi / th
    K = skew3(w)
    return np.eye(3) + np.sin(th)*K + (1-np.cos(th))*(K@K)
EXPCR = expcr
