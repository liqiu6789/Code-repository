import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
years = [2015, 2016, 2017, 2018, 2019]
category1 = [10, 15, 20, 25, 30]
category2 = [5, 10, 15, 20, 25]

# 绘制堆积面积图
plt.fill_between(years, category1, color="skyblue", alpha=0.4)
plt.fill_between(years, [i+j for i, j in zip(category1, category2)], category1, color="lightgreen", alpha=0.4)

# 设置标签和标题
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('堆积面积图')

plt.show()
