import numpy as np

def rotx(a: float) -> np.ndarray:
    """
    Generate rotation matrix about X-axis.
    
    Args:
        a (float): Rotation angle in radians
        
    Returns:
        np.ndarray: 3x3 rotation matrix R_x(a)
        
    Formula:
        R_x(a) = [[1,    0,     0  ],
                  [0, cos(a), -sin(a)],
                  [0, sin(a),  cos(a)]]
    """
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], 
                     [0, c, -s], 
                     [0, s, c]], dtype=float)

# Alias for uppercase compatibility
ROTX = rotx
