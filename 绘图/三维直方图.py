import matplotlib.pyplot as plt
import numpy as np

# 示例数据
data = np.random.normal(size=(3, 100))

# 创建图形和三维坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维直方图
hist, edges = np.histogramdd(data.T, bins=(4, 4, 4))

xpos, ypos, zpos = np.meshgrid(edges[0][:-1] + 0.25, edges[1][:-1] + 0.25, edges[2][:-1] + 0.25, indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = zpos.flatten()
dx = dy = dz = 0.5 * np.ones_like(zpos)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置标题
plt.title('3D Histogram')

# 显示图形
plt.show()
