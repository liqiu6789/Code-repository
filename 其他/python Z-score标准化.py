import numpy as np
from sklearn.preprocessing import StandardScaler

# 生成示例数据
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# 创建StandardScaler对象
scaler = StandardScaler()

# 对数据进行标准化
data_standardized = scaler.fit_transform(data)

print("原始数据:")
print(data)
print("\n标准化后的数据:")
print(data_standardized)
print("\n均值:", scaler.mean_)
print("标准差:", scaler.scale_)
