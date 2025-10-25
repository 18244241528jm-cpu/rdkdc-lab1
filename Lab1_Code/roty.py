import numpy as np
def roty(b: float) -> np.ndarray:
    c,s=np.cos(b),np.sin(b)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]],float)
ROTY = roty
