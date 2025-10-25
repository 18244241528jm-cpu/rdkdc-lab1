from time import sleep
import os
import numpy as np
from ur_interface import UrInterface   # 你的接口类名是 UrInterface

def densify(theta: np.ndarray, max_delta: float = 0.2) -> np.ndarray:
    """把 6xN 的路点矩阵细分，保证任一关节相邻两步 |Δθ| <= max_delta (rad)"""
    assert theta.shape[0] == 6, f"theta should be 6xN, got {theta.shape}"
    cols = [theta[:, 0]]
    for i in range(1, theta.shape[1]):
        prev, nxt = theta[:, i-1], theta[:, i]
        delta = nxt - prev
        steps = int(np.ceil(np.max(np.abs(delta)) / max_delta))
        steps = max(1, steps)
        for s in range(1, steps + 1):
            cols.append(prev + delta * (s / steps))
    return np.column_stack(cols)

def max_step(theta: np.ndarray) -> float:
    """返回细分后轨迹的最大单步关节变化量 |Δθ| 的上界"""
    d = np.abs(np.diff(theta))
    return float(d.max()) if d.size else 0.0

def main():
    ur5e = UrInterface()

    # 读取当前关节角，作为轨迹第0列（避免第一跳过大导致超速）
    q0 = np.array(ur5e.get_current_joints(), dtype=float).reshape(6)

    # 至少4个姿态（按列 6xN）
    waypoints = [
        [0.0,  -1.0,  1.0,  0.5, -0.5,  0.0],
        [0.5,  -0.8,  1.2,  0.4, -0.6,  0.2],
        [-0.3, -1.1,  0.9,  0.3, -0.3, -0.1],
        [0.0,  -0.9,  1.1,  0.6, -0.4,  0.0],
    ]
    theta_user = np.column_stack([np.array(q) for q in waypoints])      # 6xN
    theta_raw  = np.column_stack([q0, theta_user])                      # 先把当前姿态拼到开头

    # 细分整条轨迹（含 q0→第1点）
    max_delta = float(os.getenv("UR_MAX_DELTA", "0.05"))                # 默认更保守
    theta = densify(theta_raw, max_delta=max_delta)

    # 用接口真实限速反推安全 dt：dt >= max_step / (speed_limit*裕量)
    v_limit = float(getattr(ur5e, "speed_limit", 0.25))
    margin  = float(os.getenv("UR_DT_MARGIN", "0.90"))                  # 裕量：用80–90%上限更稳
    dt_req  = max_step(theta) / max(v_limit*margin, 1e-6)
    # 也允许用户通过环境变量强制下限
    dt_floor = float(os.getenv("UR_DT_FLOOR", "0.8"))
    dt = max(dt_req, dt_floor)

    print(f"[info] q0→轨迹已拼接，raw_cols={theta_raw.shape[1]}, densified_cols={theta.shape[1]}, "
          f"max_delta={max_delta:.3f} rad, speed_limit={v_limit:.3f}, margin={margin:.2f}, dt={dt:.3f}s")

    # —— 实验A：一次性下发 ——
    ur5e.move_joints(theta, dt)
    sleep(dt * theta.shape[1] + 0.5)

    # 为实验B准备一条反向轨迹（同样包含现姿态）
    theta_rev_raw = np.column_stack([q0, theta_user[:, ::-1]])
    theta_rev = densify(theta_rev_raw, max_delta=max_delta)

    # —— 实验B-1：不排队（立即覆盖） ——
    ur5e.move_joints(theta, dt)
    ur5e.move_joints(theta_rev, dt)         # 立刻下发反向，会覆盖
    sleep(dt * theta.shape[1] + 0.5)

    # —— 实验B-2：等待完成再下发（不覆盖） ——
    ur5e.move_joints(theta, dt)
    sleep(dt * theta.shape[1] + 0.3)
    ur5e.move_joints(theta_rev, dt)
    sleep(dt * theta.shape[1] + 0.3)

if __name__ == "__main__":
    main()
