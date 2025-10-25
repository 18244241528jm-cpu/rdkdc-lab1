import numpy as np
def finv(H: np.ndarray) -> np.ndarray:
    """Inverse of H=[[R,t],[0,1]]"""
    R = H[:3,:3]; t = H[:3,3]
    Hi = np.eye(4)
    Hi[:3,:3] = R.T
    Hi[:3, 3] = -R.T @ t
    return Hi
FINV = finv
