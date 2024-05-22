import numpy as np

# 创建一个n维数组（例如，3维数组）
n_dim_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# 使用flatten方法将其转换为一维数组
flat_array = n_dim_array.flatten()

flat_list = flat_array.tolist()

print(flat_list)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]