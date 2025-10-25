import numpy as np

def roty(b: float) -> np.ndarray:
    """
    Generate rotation matrix about Y-axis.
    
    Args:
        b (float): Rotation angle in radians
        
    Returns:
        np.ndarray: 3x3 rotation matrix R_y(b)
        
    Formula:
        R_y(b) = [[ cos(b), 0, sin(b)],
                  [    0,   1,    0  ],
                  [-sin(b), 0, cos(b)]]
    """
    c, s = np.cos(b), np.sin(b)
    return np.array([[c, 0, s], 
                     [0, 1, 0], 
                     [-s, 0, c]], dtype=float)

# Alias for uppercase compatibility
ROTY = roty
