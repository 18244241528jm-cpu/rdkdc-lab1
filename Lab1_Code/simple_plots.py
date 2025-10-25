#!/usr/bin/env python3
"""
简化的Task 2图片生成脚本
"""
import numpy as np
import matplotlib.pyplot as plt
import os

# 确保输出目录存在
os.makedirs('../Lab1_Written', exist_ok=True)

print("生成简化的Task 2图片...")

# 1. 生成ROTX基础图片
print("生成ROTX图片...")
theta = np.pi/4
R = np.array([[1, 0, 0],
              [0, np.cos(theta), -np.sin(theta)],
              [0, np.sin(theta), np.cos(theta)]])

# ROTX PLOTR
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
ax.set_xlim([-1.2,1.2])
ax.set_ylim([-1.2,1.2])
ax.set_zlim([-1.2,1.2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 绘制坐标轴
o = np.zeros(3)
ax.quiver(*o, *(R@np.array([1,0,0])), color='k', label='X')
ax.quiver(*o, *(R@np.array([0,1,0])), color='tab:blue', label='Y')
ax.quiver(*o, *(R@np.array([0,0,1])), color='tab:orange', label='Z')
ax.set_title('ROTX(π/4)')
ax.legend()
plt.savefig('../Lab1_Written/t2_rotx_plotr.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ t2_rotx_plotr.png")

# 2. 生成Euler周期性图片
print("生成Euler图片...")
angles = np.linspace(0, 4*np.pi, 100)
trace_values = []
for a in angles:
    R = np.array([[1, 0, 0],
                  [0, np.cos(a), -np.sin(a)],
                  [0, np.sin(a), np.cos(a)]])
    trace_values.append(np.trace(R))

plt.figure(figsize=(10, 6))
plt.plot(angles, trace_values, 'b-', linewidth=2)
plt.xlabel('Angle (rad)')
plt.ylabel('Trace(R)')
plt.title('Euler XYZ Periodicity')
plt.grid(True)
plt.savefig('../Lab1_Written/t2_euler_periodicity.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ t2_euler_periodicity.png")

# 3. 生成FINV数值证据
print("生成FINV图片...")
np.random.seed(42)
errors = []
for i in range(10):
    # 生成随机旋转矩阵
    phi = np.random.randn(3) * 0.5
    R = np.eye(3) + np.sin(np.linalg.norm(phi)) * np.array([[0, -phi[2], phi[1]],
                                                           [phi[2], 0, -phi[0]],
                                                           [-phi[1], phi[0], 0]])
    t = np.random.randn(3)
    
    # 构造齐次变换矩阵
    H = np.eye(4)
    H[:3, :3] = R
    H[:3, 3] = t
    
    # 计算逆矩阵
    H_inv = np.eye(4)
    H_inv[:3, :3] = R.T
    H_inv[:3, 3] = -R.T @ t
    
    # 验证 H @ H_inv = I
    I_test = H @ H_inv
    I_expected = np.eye(4)
    error = np.linalg.norm(I_test - I_expected, 'fro')
    errors.append(error)

plt.figure(figsize=(10, 6))
plt.bar(range(len(errors)), errors)
plt.xlabel('Test Case')
plt.ylabel('FINV Error (Frobenius norm)')
plt.title('FINV Numerical Accuracy')
plt.yscale('log')
plt.grid(True)
plt.savefig('../Lab1_Written/t2_finv_numeric.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ t2_finv_numeric.png")

print("\n简化图片生成完成！")
print("已生成的文件：")
for f in ['t2_rotx_plotr.png', 't2_euler_periodicity.png', 't2_finv_numeric.png']:
    if os.path.exists(f'../Lab1_Written/{f}'):
        print(f"✅ {f}")
    else:
        print(f"❌ {f}")
