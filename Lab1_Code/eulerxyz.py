import numpy as np
from rotx import rotx
from roty import roty
from rotz import rotz

def eulerxyz(a: float, b: float, c: float) -> np.ndarray:
    """R = Rx(a) @ Ry(b) @ Rz(c)  (extrinsic X->Y->Z)."""
    return rotx(a) @ roty(b) @ rotz(c)
EULERXYZ = eulerxyz
