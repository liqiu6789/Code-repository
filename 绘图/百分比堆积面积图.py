import matplotlib.pyplot as plt
import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
years = [2015, 2016, 2017, 2018, 2019]
category1 = np.array([10, 15, 20, 25, 30])
category2 = np.array([5, 10, 15, 20, 25])
total = category1 + category2

# 计算百分比
category1_percent = category1 / total * 100
category2_percent = category2 / total * 100

# 绘制百分比堆积面积图
plt.fill_between(years, category1_percent, color="skyblue", alpha=0.4)
plt.fill_between(years, 100, category1_percent, color="lightgreen", alpha=0.4)

# 设置标签和标题
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('百分比堆积面积图')

plt.show()
