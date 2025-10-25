import numpy as np
from skew3 import skew3

def skew6(xi) -> np.ndarray:
    """
    Generate 6D twist hat matrix from 6D twist vector.
    
    Args:
        xi: 6D twist vector [v(3), w(3)] where v is linear velocity and w is angular velocity
        
    Returns:
        np.ndarray: 4x4 twist hat matrix [ξ]_×
        
    Formula:
        [ξ]_× = [[[w]_×, v],
                 [  0,   0]]
                 
    Note:
        The twist hat matrix is used in SE(3) exponential mapping.
        It represents the combination of linear and angular velocities.
    """
    vwx = np.asarray(xi, dtype=float).reshape(6)
    v, w = vwx[:3], vwx[3:]  # Split into linear and angular components
    
    # Construct 4x4 twist hat matrix
    X = np.zeros((4, 4), dtype=float)
    X[:3, :3] = skew3(w)  # Angular part (skew-symmetric)
    X[:3, 3] = v          # Linear part
    
    return X

# Alias for uppercase compatibility
SKEW6 = skew6
