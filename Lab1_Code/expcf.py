import numpy as np
from skew3 import skew3
from expcr import expcr

def expcf(xi, theta=None):
    """
    SE(3) exponential map: Convert twist vector to homogeneous transformation matrix.
    
    Args:
        xi: 6D twist vector [v(3), w(3)] where v is linear and w is angular velocity
        theta: Optional scaling factor. If None, uses ||w|| as the angle
        
    Returns:
        np.ndarray: 4x4 homogeneous transformation matrix H = [[R, t], [0, 1]]
        
    Formula:
        H = exp([ξ]_×) = [[R, t], [0, 1]]
        where R = exp([w]_×) and t = V * v
        V = I*θ + (1-cos(θ))*K + (θ-sin(θ))*K²
        
    Note:
        This implements the SE(3) exponential mapping for rigid body motions.
        Handles pure translation case when ||w|| ≈ 0.
    """
    xi = np.asarray(xi, dtype=float).reshape(6)
    v, w = xi[:3], xi[3:]  # Linear and angular components
    wnorm = np.linalg.norm(w)
    
    if theta is None:
        theta = wnorm
        if wnorm > 1e-12:
            w = w / wnorm
            v = v / wnorm
    
    if theta < 1e-12:
        # Pure translation case
        H = np.eye(4)
        H[:3, 3] = v * theta
        return H
    
    # General case: rotation + translation
    K = skew3(w)
    R = expcr(w * theta)  # Rotation part
    
    # Translation part using the V matrix
    V = (np.eye(3) * theta + 
         (1 - np.cos(theta)) * K + 
         (theta - np.sin(theta)) * (K @ K))
    t = V @ v
    
    # Construct homogeneous transformation matrix
    H = np.eye(4)
    H[:3, :3] = R
    H[:3, 3] = t
    
    return H

# Alias for uppercase compatibility
EXPCF = expcf
