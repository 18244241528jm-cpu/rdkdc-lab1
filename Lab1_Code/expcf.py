import numpy as np
from skew3 import skew3
from expcr import expcr

def expcf(xi, theta=None):
    """
    SE(3) exponential (左乘/固定坐标系作用)：
      xi=[v, w] (6,). 若 theta=None，则用 ||w|| 作为角度并归一化。
      返回 4x4 变换矩阵 H = [[R, t],[0,0,0,1]]
    """
    xi = np.asarray(xi,float).reshape(6)
    v, w = xi[:3], xi[3:]
    wnorm = np.linalg.norm(w)
    if theta is None:
        theta = wnorm
        if wnorm > 1e-12:
            w = w/wnorm; v = v/wnorm
    if theta < 1e-12:   # 纯平移
        H = np.eye(4); H[:3,3] = v*theta; return H
    K = skew3(w)
    R = expcr(w*theta)
    V = (np.eye(3)*theta + (1-np.cos(theta))*K + (theta-np.sin(theta))*(K@K))
    t = V @ v
    H = np.eye(4); H[:3,:3]=R; H[:3,3]=t
    return H
EXPCF = expcf
