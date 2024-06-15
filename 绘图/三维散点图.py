import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

# 创建三维散点图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('3D Scatter Plot')
plt.show()
