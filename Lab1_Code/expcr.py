import numpy as np
from skew3 import skew3

def expcr(phi) -> np.ndarray:
    """
    SO(3) exponential map: Convert axis-angle representation to rotation matrix.
    
    Args:
        phi: 3D axis-angle vector [ωx, ωy, ωz] where ||phi|| = θ (angle)
        
    Returns:
        np.ndarray: 3x3 rotation matrix R = exp([ω]_×)
        
    Formula:
        R = I + sin(θ)/θ * [ω]_× + (1-cos(θ))/θ² * [ω]_×²
        
    Note:
        This implements the Rodrigues' rotation formula.
        For small angles (θ ≈ 0), uses first-order approximation: R ≈ I + [ω]_×
    """
    phi = np.asarray(phi, dtype=float).reshape(3)
    theta = np.linalg.norm(phi)
    
    if theta < 1e-12:
        # Small angle approximation to avoid division by zero
        return np.eye(3) + skew3(phi)
    
    # Normalize to get unit axis
    w = phi / theta
    K = skew3(w)
    
    # Rodrigues' rotation formula
    return np.eye(3) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)

# Alias for uppercase compatibility
EXPCR = expcr
