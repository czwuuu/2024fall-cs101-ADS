import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 定义参数
gamma = 0.5
Omega = 1.0
X = 0.2

# 定义微分方程组
def equations(t, state):
    v, Y = state
    dvdt = -gamma * v - Omega**2 * Y * (1 - 1 / np.sqrt(X**2 + Y**2))
    dYdt = v
    return [dvdt, dYdt]

# 定义求解函数
def solve_equations(v0, y0):
    sol = solve_ivp(equations, [0, 200], [v0, y0], method='RK45')
    return sol.y[1, -1]  # 返回最后一个时间点的Y值

# 生成数据点
y0_values = np.arange(-200, 200.1, 0.5)
v0_values = np.arange(-200, 200.1, 0.5)
data = [(y0, v0, solve_equations(v0, y0)) for y0 in y0_values for v0 in v0_values]

# 根据最终的Y值给点上色
color_data = [(y0, v0, 'red' if yFinal > 0 else 'blue') for y0, v0, yFinal in data]

# 提取颜色和坐标信息
colors = [point[2] for point in color_data]
points = [point[:2] for point in color_data]

# 绘制相图
plt.figure(figsize=(8, 8))
plt.scatter(*zip(*points), c=colors, s=10)
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.xlabel('Y', fontsize=12, fontweight='bold')
plt.ylabel('v', fontsize=12, fontweight='bold')
plt.title('Phase Diagram', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()