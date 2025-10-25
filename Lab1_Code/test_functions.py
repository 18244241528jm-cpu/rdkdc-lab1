import numpy as np
from rotx import rotx; from eulerxyz import eulerxyz
from eulerxyzinv import eulerxyzinv; from finv import finv
from expcr import expcr; from expcf import expcf

R = eulerxyz(0.3,-0.2,0.4)
a,b,c = eulerxyzinv(R)
R2 = eulerxyz(a,b,c)
print("Euler round-trip Frobenius:", np.linalg.norm(R-R2,'fro'))

phi = np.array([0.1,0.2,0.3])
print("expcr orthonormal check:", np.allclose(expcr(phi).T@expcr(phi), np.eye(3), atol=1e-9))

H = expcf([0.1,0.0,0.0, 0.0,0.0,0.2])   # 小旋量
I = H @ finv(H)
print("H * FINV(H) ≈ I:", np.linalg.norm(I - np.eye(4),'fro'))
