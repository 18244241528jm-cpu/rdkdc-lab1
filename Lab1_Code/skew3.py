import numpy as np

def skew3(w) -> np.ndarray:
    """
    Generate 3D skew-symmetric matrix from 3D vector.
    
    Args:
        w: 3D vector [wx, wy, wz] or array-like
        
    Returns:
        np.ndarray: 3x3 skew-symmetric matrix [w]_×
        
    Formula:
        [w]_× = [[  0, -wz,  wy],
                 [ wz,   0, -wx],
                 [-wy,  wx,   0]]
                 
    Note:
        The skew-symmetric matrix is used to represent cross products:
        w × v = [w]_× v
    """
    wx, wy, wz = np.asarray(w, dtype=float).reshape(3)
    return np.array([[0, -wz, wy], 
                     [wz, 0, -wx], 
                     [-wy, wx, 0]], dtype=float)

# Alias for uppercase compatibility
SKEW3 = skew3
