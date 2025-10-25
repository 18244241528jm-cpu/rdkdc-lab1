import numpy as np

def eulerxyzinv(R: np.ndarray):
    """
    逆映射：给定 R=Rx(a)@Ry(b)@Rz(c) 求 (a,b,c)。
    数值病态（ill-defined）：|cos(b)|≈0（b≈±90°）时出现gimbal lock，a,c 不唯一。
    处理：当 |cos(b)|<eps 时，设 c=0，以 R 的其它元素稳定求 a。
    """
    assert R.shape==(3,3)
    # 与 intrinsic ZYX 对偶：b = asin(-R[2,0])
    b = np.arctan2(-R[2,0], np.sqrt(R[0,0]**2 + R[1,0]**2))
    cb = np.cos(b)
    eps = 1e-9
    if abs(cb) > eps:
        a = np.arctan2(R[2,1], R[2,2])
        c = np.arctan2(R[1,0], R[0,0])
    else:
        # gimbal lock：合并 c 入 a
        print("警告：检测到gimbal lock情况（|cos(b)|≈0），a,c 不唯一，设 c=0")
        a = np.arctan2(-R[1,2], R[1,1])
        c = 0.0
    return float(a), float(b), float(c)
EULERXYZINV = eulerxyzinv
