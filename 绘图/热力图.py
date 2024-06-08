import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成示例数据
np.random.seed(0)
data = np.random.rand(10, 12)  # 10行12列的随机数据
columns = [f'Col_{i}' for i in range(12)]
index = [f'Row_{i}' for i in range(10)]
df = pd.DataFrame(data, columns=columns, index=index)

# 使用 Seaborn 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap='coolwarm')
plt.title('Heatmap using Seaborn and Matplotlib')
plt.show()
