import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 创建图形和三维坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维曲面图
ax.plot_surface(x, y, z, cmap='viridis')

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 设置标题
plt.title('3D Surface Plot')

# 显示图形
plt.show()
