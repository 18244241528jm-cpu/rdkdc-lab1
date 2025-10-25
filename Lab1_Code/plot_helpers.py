import numpy as np, matplotlib.pyplot as plt
def _fig3d():
    f=plt.figure(figsize=(5,4)); ax=f.add_subplot(111,projection='3d')
    ax.set_box_aspect([1,1,1]); ax.set_xlim([-1.2,1.2]); ax.set_ylim([-1.2,1.2]); ax.set_zlim([-1.2,1.2])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z'); return f,ax
def PLOTR(R_before, R_after, title="PLOTR"):
    f,ax=_fig3d(); o=np.zeros(3)
    def draw(R,color):
        ax.quiver(*o,*(R@np.array([1,0,0])),color=color)
        ax.quiver(*o,*(R@np.array([0,1,0])),color='tab:blue')
        ax.quiver(*o,*(R@np.array([0,0,1])),color='tab:orange')
    draw(np.eye(3),'0.6'); draw(R_after,'k'); ax.set_title(title); return f,ax
def PLOTP3(P, P2=None, title="PLOTP3"):
    f,ax=_fig3d(); ax.scatter(*P, s=30, marker='^', color='0.5', label='orig')
    if P2 is not None: ax.scatter(*P2, s=30, marker='o', color='tab:orange', label='transformed')
    ax.legend(frameon=False); ax.set_title(title); return f,ax
def PLOTP4(P4, P4_2=None, title="PLOTP4"):  # P4: 4xN
    return PLOTP3(P4[:3], None if P4_2 is None else P4_2[:3], title)
def PLOTV3(v, v2=None, title="PLOTV3"):
    f,ax=_fig3d(); ax.quiver(0,0,0,*np.asarray(v).reshape(3),color='0.5',label='v')
    if v2 is not None: ax.quiver(0,0,0,*np.asarray(v2).reshape(3),color='tab:orange',label='transformed')
    ax.legend(frameon=False); ax.set_title(title); return f,ax
def PLOTV4(v4, v4_2=None, title="PLOTV4"):  # v4: 4x1 (w=0)
    return PLOTV3(v4[:3], None if v4_2 is None else v4_2[:3], title)
def PLOTF(R, t, title="PLOTF"):
    f,ax=_fig3d()
    o=np.zeros(3); ax.quiver(*o,1,0,0,color='0.6'); ax.quiver(*o,0,1,0,color='0.6'); ax.quiver(*o,0,0,1,color='0.6')
    o2=np.asarray(t).reshape(3); ax.quiver(*o2,*(R@np.array([1,0,0])),color='k')
    ax.quiver(*o2,*(R@np.array([0,1,0])),color='tab:blue'); ax.quiver(*o2,*(R@np.array([0,0,1])),color='tab:orange')
    ax.set_title(title); return f,ax
