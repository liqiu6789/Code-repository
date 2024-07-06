import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
years = [2015, 2016, 2017, 2018, 2019]
values = [10, 15, 20, 25, 30]

# 绘制面积图
plt.fill_between(years, values, color="skyblue", alpha=0.4)
plt.plot(years, values, color="Slateblue", alpha=0.6)

# 设置标签和标题
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('面积图')

plt.show()
