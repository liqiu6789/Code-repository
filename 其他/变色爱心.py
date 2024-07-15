import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 定义爱心形状的函数
def heart_shape(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# 定义颜色渐变函数
def color_gradient(frame):
    colors = plt.cm.rainbow(np.linspace(0, 1, 100))
    return colors[frame % 100]

# 初始化绘图
fig, ax = plt.subplots()
t = np.linspace(0, 2*np.pi, 1000)
x, y = heart_shape(t)
patch = ax.fill(x, y, color='red')[0]
ax.set_aspect('equal')
ax.axis('off')

# 更新函数
def update(frame):
    patch.set_facecolor(color_gradient(frame))
    return patch,

# 创建动画
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# 显示动画
plt.show()
