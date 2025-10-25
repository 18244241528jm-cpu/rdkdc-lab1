import numpy as np
import matplotlib.pyplot as plt

def _fig3d():
    """
    Create a standardized 3D figure for robot visualization.
    
    Returns:
        tuple: (figure, axes) with consistent 3D settings
    """
    f = plt.figure(figsize=(5, 4))
    ax = f.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return f, ax

def PLOTR(R_before, R_after, title="PLOTR"):
    """
    Plot rotation matrices as coordinate frames.
    
    Args:
        R_before: Reference rotation matrix (usually identity)
        R_after: Rotated coordinate frame
        title: Plot title
        
    Returns:
        tuple: (figure, axes) for further customization
    """
    f, ax = _fig3d()
    o = np.zeros(3)
    
    def draw(R, color):
        """Draw coordinate frame axes"""
        ax.quiver(*o, *(R @ np.array([1, 0, 0])), color=color, label='X')
        ax.quiver(*o, *(R @ np.array([0, 1, 0])), color='tab:blue', label='Y')
        ax.quiver(*o, *(R @ np.array([0, 0, 1])), color='tab:orange', label='Z')
    
    draw(np.eye(3), '0.6')  # Reference frame (gray)
    draw(R_after, 'k')      # Rotated frame (black)
    ax.set_title(title)
    return f, ax

def PLOTP3(P, P2=None, title="PLOTP3"):
    """
    Plot 3D points before and after transformation.
    
    Args:
        P: Original 3D points (3xN array)
        P2: Transformed 3D points (3xN array, optional)
        title: Plot title
        
    Returns:
        tuple: (figure, axes) for further customization
    """
    f, ax = _fig3d()
    ax.scatter(*P, s=30, marker='^', color='0.5', label='original')
    if P2 is not None:
        ax.scatter(*P2, s=30, marker='o', color='tab:orange', label='transformed')
    ax.legend(frameon=False)
    ax.set_title(title)
    return f, ax

def PLOTP4(P4, P4_2=None, title="PLOTP4"):
    """
    Plot homogeneous 4D points (extracts 3D coordinates).
    
    Args:
        P4: Original homogeneous points (4xN array)
        P4_2: Transformed homogeneous points (4xN array, optional)
        title: Plot title
        
    Returns:
        tuple: (figure, axes) for further customization
    """
    return PLOTP3(P4[:3], None if P4_2 is None else P4_2[:3], title)

def PLOTV3(v, v2=None, title="PLOTV3"):
    """
    Plot 3D vectors from origin.
    
    Args:
        v: Original 3D vector
        v2: Transformed 3D vector (optional)
        title: Plot title
        
    Returns:
        tuple: (figure, axes) for further customization
    """
    f, ax = _fig3d()
    ax.quiver(0, 0, 0, *np.asarray(v).reshape(3), color='0.5', label='original')
    if v2 is not None:
        ax.quiver(0, 0, 0, *np.asarray(v2).reshape(3), color='tab:orange', label='transformed')
    ax.legend(frameon=False)
    ax.set_title(title)
    return f, ax

def PLOTV4(v4, v4_2=None, title="PLOTV4"):
    """
    Plot homogeneous 4D vectors (extracts 3D coordinates).
    
    Args:
        v4: Original homogeneous vector (4x1 array with w=0)
        v4_2: Transformed homogeneous vector (4x1 array, optional)
        title: Plot title
        
    Returns:
        tuple: (figure, axes) for further customization
    """
    return PLOTV3(v4[:3], None if v4_2 is None else v4_2[:3], title)

def PLOTF(R, t, title="PLOTF"):
    """
    Plot coordinate frame with rotation and translation.
    
    Args:
        R: 3x3 rotation matrix
        t: 3x1 translation vector
        title: Plot title
        
    Returns:
        tuple: (figure, axes) for further customization
    """
    f, ax = _fig3d()
    
    # Reference frame at origin
    o = np.zeros(3)
    ax.quiver(*o, 1, 0, 0, color='0.6', alpha=0.5)
    ax.quiver(*o, 0, 1, 0, color='0.6', alpha=0.5)
    ax.quiver(*o, 0, 0, 1, color='0.6', alpha=0.5)
    
    # Transformed frame
    o2 = np.asarray(t).reshape(3)
    ax.quiver(*o2, *(R @ np.array([1, 0, 0])), color='k', label='X')
    ax.quiver(*o2, *(R @ np.array([0, 1, 0])), color='tab:blue', label='Y')
    ax.quiver(*o2, *(R @ np.array([0, 0, 1])), color='tab:orange', label='Z')
    
    ax.set_title(title)
    return f, ax
