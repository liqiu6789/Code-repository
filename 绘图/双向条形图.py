import matplotlib.pyplot as plt
import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [5, 7, 3, 4, 6]
values2 = [6, 4, 8, 3, 5]

# 绘制双向条形图
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(categories, values1, color='blue', label='Category 1')
ax.barh(categories, -np.array(values2), color='red', label='Category 2')

# 设置标签和标题
ax.set_xlabel('Values')
ax.set_title('双向条形图')
ax.legend()

plt.show()
