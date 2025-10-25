#!/usr/bin/env python3
"""
生成Lab1 Task 2缺失的图片
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# 添加当前目录到路径，以便导入我们的函数
sys.path.append('.')

try:
    from rotx import rotx
    from eulerxyz import eulerxyz
    from eulerxyzinv import eulerxyzinv
    from expcr import expcr
    from expcf import expcf
    from finv import finv
    from plot_helpers import PLOTR, PLOTP3, PLOTP4, PLOTV3, PLOTV4, PLOTF
    print("✅ 所有函数导入成功")
except ImportError as e:
    print(f"❌ 导入错误: {e}")
    sys.exit(1)

# 确保输出目录存在
output_dir = '../Lab1_Written'
os.makedirs(output_dir, exist_ok=True)
print(f"输出目录: {output_dir}")

def create_rotx_plots():
    """生成ROTX相关图片"""
    print("生成ROTX图片...")
    theta = np.pi/4
    R = rotx(theta)
    
    # 1. ROTX PLOTR
    try:
        f, ax = PLOTR(np.eye(3), R, "ROTX(π/4)")
        plt.savefig(f'{output_dir}/t2_rotx_plotr.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_rotx_plotr.png")
    except Exception as e:
        print(f"❌ ROTX PLOTR 失败: {e}")
    
    # 2. ROTX PLOTP3
    try:
        P = np.array([[1,0,0], [0,1,0], [0,0,1]]).T
        P2 = R @ P
        f, ax = PLOTP3(P, P2, "ROTX Points")
        plt.savefig(f'{output_dir}/t2_rotx_plotp3.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_rotx_plotp3.png")
    except Exception as e:
        print(f"❌ ROTX PLOTP3 失败: {e}")
    
    # 3. ROTX PLOTP4
    try:
        P = np.array([[1,0,0], [0,1,0], [0,0,1]]).T
        P4 = np.vstack([P, np.ones(P.shape[1])])
        P4_2 = R @ P4[:3]
        P4_2 = np.vstack([P4_2, np.ones(P4_2.shape[1])])
        f, ax = PLOTP4(P4, P4_2, "ROTX Homogeneous")
        plt.savefig(f'{output_dir}/t2_rotx_plotp4.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_rotx_plotp4.png")
    except Exception as e:
        print(f"❌ ROTX PLOTP4 失败: {e}")
    
    # 4. ROTX PLOTV3
    try:
        v = np.array([1, 1, 1])
        v2 = R @ v
        f, ax = PLOTV3(v, v2, "ROTX Vector")
        plt.savefig(f'{output_dir}/t2_rotx_plotv3.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_rotx_plotv3.png")
    except Exception as e:
        print(f"❌ ROTX PLOTV3 失败: {e}")
    
    # 5. ROTX PLOTV4
    try:
        v4 = np.array([1, 1, 1, 0])
        v4_2 = R @ v4[:3]
        v4_2 = np.append(v4_2, 0)
        f, ax = PLOTV4(v4, v4_2, "ROTX Homogeneous Vector")
        plt.savefig(f'{output_dir}/t2_rotx_plotv4.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_rotx_plotv4.png")
    except Exception as e:
        print(f"❌ ROTX PLOTV4 失败: {e}")
    
    # 6. ROTX PLOTF
    try:
        t = np.array([0.5, 0.3, 0.2])
        f, ax = PLOTF(R, t, "ROTX Frame")
        plt.savefig(f'{output_dir}/t2_rotx_plotf.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_rotx_plotf.png")
    except Exception as e:
        print(f"❌ ROTX PLOTF 失败: {e}")

def create_euler_plots():
    """生成Euler相关图片"""
    print("生成Euler图片...")
    
    # 1. Euler 周期性
    try:
        angles = np.linspace(0, 4*np.pi, 100)
        R_periodic = [eulerxyz(a, 0.1, 0.2) for a in angles]
        trace_values = [np.trace(R) for R in R_periodic]
        
        plt.figure(figsize=(10, 6))
        plt.plot(angles, trace_values, 'b-', linewidth=2)
        plt.xlabel('Angle (rad)')
        plt.ylabel('Trace(R)')
        plt.title('Euler XYZ Periodicity')
        plt.grid(True)
        plt.savefig(f'{output_dir}/t2_euler_periodicity.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_euler_periodicity.png")
    except Exception as e:
        print(f"❌ Euler 周期性 失败: {e}")
    
    # 2. Euler 逆变换反例
    try:
        R_test = eulerxyz(0.1, np.pi/2, 0.3)  # 接近gimbal lock
        a, b, c = eulerxyzinv(R_test)
        R_reconstructed = eulerxyz(a, b, c)
        error = np.linalg.norm(R_test - R_reconstructed, 'fro')
        
        plt.figure(figsize=(8, 6))
        plt.imshow(np.abs(R_test - R_reconstructed), cmap='hot')
        plt.colorbar()
        plt.title(f'Euler Inverse Error (Frobenius: {error:.2e})')
        plt.savefig(f'{output_dir}/t2_euler_inv_counterexample.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_euler_inv_counterexample.png")
    except Exception as e:
        print(f"❌ Euler 逆变换反例 失败: {e}")
    
    # 3. Euler 往返测试
    try:
        test_angles = [(0.1, 0.2, 0.3), (0.5, -0.3, 0.8), (1.2, 0.1, -0.5)]
        errors = []
        for a, b, c in test_angles:
            R = eulerxyz(a, b, c)
            a2, b2, c2 = eulerxyzinv(R)
            R2 = eulerxyz(a2, b2, c2)
            error = np.linalg.norm(R - R2, 'fro')
            errors.append(error)
        
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(errors)), errors)
        plt.xlabel('Test Case')
        plt.ylabel('Round-trip Error')
        plt.title('Euler XYZ Round-trip Accuracy')
        plt.yscale('log')
        plt.savefig(f'{output_dir}/t2_euler_roundtrip.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_euler_roundtrip.png")
    except Exception as e:
        print(f"❌ Euler 往返测试 失败: {e}")

def create_exp_plots():
    """生成指数映射图片"""
    print("生成指数映射图片...")
    
    # 1. EXPCR
    try:
        phi = np.array([0.1, 0.2, 0.3])
        R_expcr = expcr(phi)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # PLOTR for EXPCR
        f, ax = PLOTR(np.eye(3), R_expcr, "EXPCR")
        ax1 = ax
        ax1.set_title("EXPCR Rotation")
        
        # PLOTV3 for EXPCR
        v = np.array([1, 0, 0])
        v_rotated = R_expcr @ v
        f, ax = PLOTV3(v, v_rotated, "EXPCR Vector")
        ax2 = ax
        ax2.set_title("EXPCR Vector")
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/t2_expcr_plotr_plotv3.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_expcr_plotr_plotv3.png")
    except Exception as e:
        print(f"❌ EXPCR 失败: {e}")
    
    # 2. EXPCF
    try:
        xi = np.array([0.1, 0.2, 0.3, 0.0, 0.0, 0.1])
        H_expcf = expcf(xi)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # PLOTF for EXPCF
        R = H_expcf[:3, :3]
        t = H_expcf[:3, 3]
        f, ax = PLOTF(R, t, "EXPCF Frame")
        ax1 = ax
        ax1.set_title("EXPCF Frame")
        
        # PLOTV3 for EXPCF
        v = np.array([1, 0, 0])
        v_transformed = H_expcf @ np.append(v, 1)
        v_transformed = v_transformed[:3]
        f, ax = PLOTV3(v, v_transformed, "EXPCF Vector")
        ax2 = ax
        ax2.set_title("EXPCF Vector")
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/t2_expcf_plotf_plotv3.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_expcf_plotf_plotv3.png")
    except Exception as e:
        print(f"❌ EXPCF 失败: {e}")

def create_finv_plot():
    """生成FINV数值证据图片"""
    print("生成FINV数值证据...")
    
    try:
        # 测试多个随机变换矩阵
        np.random.seed(42)
        errors = []
        for i in range(10):
            # 生成随机旋转矩阵
            phi = np.random.randn(3) * 0.5
            R = expcr(phi)
            t = np.random.randn(3)
            
            # 构造齐次变换矩阵
            H = np.eye(4)
            H[:3, :3] = R
            H[:3, 3] = t
            
            # 计算逆矩阵
            H_inv = finv(H)
            
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
        plt.savefig(f'{output_dir}/t2_finv_numeric.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("✅ t2_finv_numeric.png")
    except Exception as e:
        print(f"❌ FINV 失败: {e}")

if __name__ == "__main__":
    print("开始生成Task 2图片...")
    
    # 生成各类图片
    create_rotx_plots()
    create_euler_plots()
    create_exp_plots()
    create_finv_plot()
    
    print("\n图片生成完成！")
    print("检查生成的文件：")
    
    expected_files = [
        't2_rotx_plotr.png', 't2_rotx_plotp3.png', 't2_rotx_plotp4.png',
        't2_rotx_plotv3.png', 't2_rotx_plotv4.png', 't2_rotx_plotf.png',
        't2_euler_periodicity.png', 't2_euler_inv_counterexample.png', 't2_euler_roundtrip.png',
        't2_expcr_plotr_plotv3.png', 't2_expcf_plotf_plotv3.png', 't2_finv_numeric.png'
    ]
    
    for f in expected_files:
        if os.path.exists(f'{output_dir}/{f}'):
            print(f"✅ {f}")
        else:
            print(f"❌ {f} - 未生成")
