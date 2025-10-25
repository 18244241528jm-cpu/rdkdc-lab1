import numpy as np
def skew3(w) -> np.ndarray:
    wx,wy,wz = np.asarray(w,dtype=float).reshape(3)
    return np.array([[0,-wz,wy],[wz,0,-wx],[-wy,wx,0]],float)
SKEW3 = skew3
