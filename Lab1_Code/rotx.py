import numpy as np
def rotx(a: float) -> np.ndarray:
    c,s=np.cos(a),np.sin(a)
    return np.array([[1,0,0],[0,c,-s],[0,s,c]],float)
ROTX = rotx
