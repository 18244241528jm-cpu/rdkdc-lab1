import numpy as np
from skew3 import skew3
def skew6(xi) -> np.ndarray:
    """xi=[v(3), w(3)] -> 4x4 twist hat matrix."""
    vwx = np.asarray(xi,dtype=float).reshape(6)
    v,w = vwx[:3], vwx[3:]
    X = np.zeros((4,4),float)
    X[:3,:3] = skew3(w)
    X[:3, 3] = v
    return X
SKEW6 = skew6
