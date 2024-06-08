import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 生成示例数据
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# 创建图形
plt.figure(figsize=(10, 6))

# 使用seaborn绘制小提琴图
sns.violinplot(data=data)

# 添加标题和标签
plt.title('Violin Plot')
plt.xlabel('Category')
plt.ylabel('Values')

# 显示图表
plt.show()
