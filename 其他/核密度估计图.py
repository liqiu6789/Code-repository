import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# 生成示例数据
data = np.random.normal(0, 1, 1000)  # 生成1000个符合正态分布的数据点

# 使用高斯核密度估计
kde = gaussian_kde(data)

# 生成核密度估计的x值
x_vals = np.linspace(min(data), max(data), 1000)
# 计算核密度估计的y值
y_vals = kde(x_vals)

# 绘制核密度估计图
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='KDE', color='blue')
plt.fill_between(x_vals, y_vals, alpha=0.5)
plt.title('Kernel Density Estimation')
plt.xlabel('Data')
plt.ylabel('Density')
plt.legend()
plt.show()
