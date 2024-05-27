import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 生成示例数据
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# 创建MinMaxScaler对象，指定范围为0到1
scaler = MinMaxScaler()

# 对数据进行归一化
data_normalized = scaler.fit_transform(data)

print("原始数据:")
print(data)
print("\n归一化后的数据:")
print(data_normalized)
print("\n数据的最小值:", scaler.data_min_)
print("数据的最大值:", scaler.data_max_)
