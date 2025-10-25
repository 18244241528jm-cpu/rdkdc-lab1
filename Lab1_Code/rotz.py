import numpy as np
def rotz(c: float) -> np.ndarray:
    C,S=np.cos(c),np.sin(c)
    return np.array([[C,-S,0],[S,C,0],[0,0,1]],float)
ROTZ = rotz
