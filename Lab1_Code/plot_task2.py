# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from transforms3d.axangles import axangle2mat
from transforms3d.euler import euler2mat, mat2euler

OUT = "../Lab1_Written/"

def draw_axes(R, ax, L=1.0, color_set=('0.6', 'tab:blue', 'tab:orange'), label=None):
    o = np.zeros(3)
    X = R @ np.array([L, 0, 0])
    Y = R @ np.array([0, L, 0])
    Z = R @ np.array([0, 0, L])
    ax.quiver(*o, *X, length=1, color=color_set[1], normalize=False)
    ax.quiver(*o, *Y, length=1, color=color_set[2], normalize=False)
    ax.quiver(*o, *Z, length=1, color='tab:green', normalize=False)
    if label:
        ax.plot([], [], color=color_set[1], label=label)

def fig3d():
    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1,1,1])
    ax.set_xlim([-1.2,1.2]); ax.set_ylim([-1.2,1.2]); ax.set_zlim([-1.2,1.2])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    return fig, ax

# 1) Rodrigues：绕任意轴旋转
def plot_rodrigues():
    axis = np.array([1,1,0.3]); axis = axis/np.linalg.norm(axis)
    theta = np.deg2rad(60)
    R = axangle2mat(axis, theta)
    fig, ax = fig3d()
    draw_axes(np.eye(3), ax, label='World')
    draw_axes(R, ax, label='Rotated')
    ax.legend(loc='upper left', frameon=False)
    ax.set_title("Rodrigues (axis-angle, 60°)")
    fig.tight_layout(); fig.savefig(OUT+"task2_rodrigues.png", dpi=220); plt.close(fig)

# 2) EXPCF/EXPCR 概念示意（位姿作用在点上 vs 坐标系上）
def plot_expcf_exper():
    R = euler2mat(0.3, -0.2, 0.5, axes='sxyz')
    t = np.array([0.5, -0.3, 0.2])
    P = np.array([[0.7,0.0,0.0],[0.0,0.7,0.0],[0.0,0.0,0.7]])
    P_cf = (R @ P) + t.reshape(3,1)  # EXPCF: 点变换

    fig, ax = fig3d()
    draw_axes(np.eye(3), ax, label='World')
    draw_axes(R, ax, label="Frame' (EXPCR)")
    ax.scatter(*P, s=35, marker='^', color='0.5', label='Points (orig)')
    ax.scatter(*P_cf, s=35, marker='o', color='tab:orange', label='EXPCF(P)')
    ax.legend(loc='upper left', frameon=False)
    ax.set_title("EXPCF (points) vs EXPCR (frame change)")
    fig.tight_layout(); fig.savefig(OUT+"task2_expcf_expcr.png", dpi=220); plt.close(fig)

# 3) Euler XYZ 与逆映射：周期与奇异性
def plot_euler_xyz():
    angles = (np.deg2rad(30), np.deg2rad(20), np.deg2rad(10))
    R  = euler2mat(*angles, axes='sxyz')
    est = mat2euler(R, axes='sxyz')
    angles2 = (angles[0]+2*np.pi, angles[1], angles[2]-2*np.pi)
    R2 = euler2mat(*angles2, axes='sxyz')
    err = np.linalg.norm(R - R2, ord='fro')

    fig, ax = plt.subplots(figsize=(6,3.2))
    ax.axis('off')
    ax.text(0.02, 0.95,
            "Euler XYZ (rad): {}\nRecovered:        {}\nEqv (±2π) ‖R-R'‖₍F₎ = {:.2e}\n"
            "Note: near pitch≈±90° (gimbal lock) inverse non-unique.".format(
                np.round(angles,3), np.round(est,3), err),
            va='top', fontsize=12)
    fig.tight_layout(); fig.savefig(OUT+"task2_eulerxyz.png", dpi=220); plt.close(fig)

def main():
    import os
    os.makedirs(OUT, exist_ok=True)
    plot_rodrigues()
    plot_expcf_exper()
    plot_euler_xyz()
    print("Saved figures to", OUT)

if __name__ == "__main__":
    main()
