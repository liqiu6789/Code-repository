import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.arange(5)
y = np.random.randint(1, 10, size=5)
z = np.zeros(5)

dx = np.ones(5)
dy = np.ones(5)
dz = [1, 2, 3, 4, 5]

# 创建图形和三维坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维条形图
ax.bar3d(x, y, z, dx, dy, dz, color='b')

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置标题
plt.title('3D Bar Plot')

# 显示图形
plt.show()
