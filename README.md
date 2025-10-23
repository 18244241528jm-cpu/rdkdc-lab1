# Lab 1 (RDKDC) — Submission Scaffold

## 1) 目录结构
- `Lab1_Code/`：所有代码（函数、脚本、测试、绘图脚本）
- `Lab1_Written/`：书面回答与配图（PDF/PNG/JPG 等）

## 2) 运行环境
- 方案A（Python）：Python 3.10+，`numpy`（其余按任务需要补充）
- 方案B（MATLAB）：ROS Toolbox + Robotics System Toolbox
- 仿真：ROS 2 + RViz（在 Windows/WSL2 或 Linux 上运行）

## 3) 最小运行顺序
1. （仿真机）启动：`ros2 launch rdkdc ur5e_simulation.launch.py`
2. （本机）Python：`python Lab1_Code/selfcheck.py`（单元自检）
3. （本机）仿真演示：`python Lab1_Code/lab1_1.py`（或 MATLAB 同名脚本）

## 4) 如何复现实验图（占位）
- 使用 `PLOTR/PLOTP3/...` 绘图脚本输出到 `Lab1_Written/`
- 图名建议：`task2_expcr_axisX_thetaY.png`（见 notes）

## 5) 命名与提交规范（重点）
- 顶层仅保留 `Lab1_Code/` 与 `Lab1_Written/`
- 函数名与文件名大小写一致（例：`ROTZ()` 存于 `ROTZ.m` / `rotz.py`）
- 打包：`Lab1_<YourJHED>.zip`

## 6) 变更记录
- 2025-10-23: 初始化骨架，创建目录/README/.gitignore
