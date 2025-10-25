import numpy as np
from rotx import rotx
from roty import roty
from rotz import rotz

def eulerxyz(a: float, b: float, c: float) -> np.ndarray:
    """
    Generate rotation matrix from Euler angles (XYZ extrinsic).
    
    Args:
        a (float): Rotation angle about X-axis in radians
        b (float): Rotation angle about Y-axis in radians  
        c (float): Rotation angle about Z-axis in radians
        
    Returns:
        np.ndarray: 3x3 rotation matrix R = R_x(a) @ R_y(b) @ R_z(c)
        
    Note:
        This uses extrinsic XYZ rotation order (fixed frame).
        The rotations are applied in sequence: first X, then Y, then Z.
    """
    return rotx(a) @ roty(b) @ rotz(c)

# Alias for uppercase compatibility
EULERXYZ = eulerxyz
