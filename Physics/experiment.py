import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# 初始条件
initial_conditions = [0.854, 0.1]
t_start_plot = 1300
t_span = (0,1500)
t_steps = 1000
delta_a = 0.04

# 定义微分方程
def system(t, y, gamma, Omega, X, omega, a):
    Y, v = y
    perturbation = np.random.uniform(0, delta_a)
    dYdt = v
    dvdt = (a+perturbation) * np.cos(omega * t) - Omega ** 2 * Y * (1 - 1 / np.sqrt(X ** 2 + Y ** 2)) - gamma * v
    return [dYdt, dvdt]


# 解微分方程并绘制相图
def solve_and_plot(a, ax):
    sol = solve_ivp(system, t_span, initial_conditions, args=(0.5, 1, 0.2, 0.9, a), max_step=0.01, dense_output=True)
    t_vals = np.linspace(t_start_plot, t_span[1], t_steps)
    Y_vals, v_vals = sol.sol(t_vals)

    ax.clear()
    ax.plot(Y_vals, v_vals, color='red')
    ax.set_xlabel('Y')
    ax.set_ylabel('v')
    ax.set_title(f'Phase Space Diagram with Perturbation X = 0.2 (a = {a:.2f})')
    ax.set_aspect('equal')


# 创建动画
fig, ax = plt.subplots(figsize=(8, 8))
a_values = np.arange(0.2, 1.31, 0.01)


def update(frame):
    a = a_values[frame]
    solve_and_plot(a, ax)


ani = FuncAnimation(fig, update, frames=len(a_values), interval=500, repeat=False)

# 指定使用 ffmpeg 作为写入器
writer = FFMpegWriter(fps=2)
ani.save('phase_space_animation_with_perturbation(X=0.2,delta=.04).mp4', writer=writer)