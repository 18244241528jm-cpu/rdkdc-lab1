import numpy as np

def finv(H: np.ndarray) -> np.ndarray:
    """
    Compute inverse of homogeneous transformation matrix.
    
    Args:
        H: 4x4 homogeneous transformation matrix [[R, t], [0, 1]]
        
    Returns:
        np.ndarray: 4x4 inverse transformation matrix H⁻¹
        
    Formula:
        H⁻¹ = [[Rᵀ, -Rᵀt], [0, 1]]
        
    Note:
        This exploits the special structure of homogeneous transformation matrices.
        The rotation part R is orthogonal, so R⁻¹ = Rᵀ.
        The translation part is computed as -Rᵀt.
    """
    R = H[:3, :3]  # Rotation part
    t = H[:3, 3]   # Translation part
    
    # Construct inverse matrix
    Hi = np.eye(4)
    Hi[:3, :3] = R.T        # R⁻¹ = Rᵀ for rotation matrices
    Hi[:3, 3] = -R.T @ t    # Translation part: -Rᵀt
    
    return Hi

# Alias for uppercase compatibility
FINV = finv
