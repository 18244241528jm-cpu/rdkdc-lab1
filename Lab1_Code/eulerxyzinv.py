import numpy as np

def eulerxyzinv(R: np.ndarray):
    """
    Inverse mapping: Extract Euler angles (a,b,c) from rotation matrix R = R_x(a)@R_y(b)@R_z(c).
    
    Args:
        R (np.ndarray): 3x3 rotation matrix
        
    Returns:
        tuple: (a, b, c) Euler angles in radians
        
    Warning:
        This function is numerically ill-conditioned when |cos(b)| ≈ 0 (b ≈ ±90°).
        This is the gimbal lock condition where a and c are not uniquely determined.
        When gimbal lock is detected, c is set to 0 and a is computed from other elements.
        
    Note:
        The function handles the gimbal lock case by setting c=0 and computing a
        from the remaining matrix elements for numerical stability.
    """
    assert R.shape == (3, 3), "Input must be a 3x3 matrix"
    
    # Extract angle b using the relationship: b = atan2(-R[2,0], sqrt(R[0,0]^2 + R[1,0]^2))
    b = np.arctan2(-R[2, 0], np.sqrt(R[0, 0]**2 + R[1, 0]**2))
    cb = np.cos(b)
    eps = 1e-9  # Numerical threshold for gimbal lock detection
    
    if abs(cb) > eps:
        # Normal case: extract a and c from matrix elements
        a = np.arctan2(R[2, 1], R[2, 2])
        c = np.arctan2(R[1, 0], R[0, 0])
    else:
        # Gimbal lock case: merge c into a for numerical stability
        print("Warning: Gimbal lock detected (|cos(b)| ≈ 0). Setting c=0 for stability.")
        a = np.arctan2(-R[1, 2], R[1, 1])
        c = 0.0
        
    return float(a), float(b), float(c)

# Alias for uppercase compatibility
EULERXYZINV = eulerxyzinv
