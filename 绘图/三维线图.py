import matplotlib.pyplot as plt
import numpy as np

# 示例数据
t = np.linspace(0, 10, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# 创建图形和三维坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维线图
ax.plot(x, y, z, label='3D Line')

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置标题
plt.title('3D Line Plot')

# 显示图形
plt.show()
