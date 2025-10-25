import numpy as np

def rotz(c: float) -> np.ndarray:
    """
    Generate rotation matrix about Z-axis.
    
    Args:
        c (float): Rotation angle in radians
        
    Returns:
        np.ndarray: 3x3 rotation matrix R_z(c)
        
    Formula:
        R_z(c) = [[cos(c), -sin(c), 0],
                  [sin(c),  cos(c), 0],
                  [   0,      0,    1]]
    """
    C, S = np.cos(c), np.sin(c)
    return np.array([[C, -S, 0], 
                     [S, C, 0], 
                     [0, 0, 1]], dtype=float)

# Alias for uppercase compatibility
ROTZ = rotz
