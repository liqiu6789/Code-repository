import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 15, 20, 25, 30]
growth_rate = [1, 2, 1.5, 3, 2.5]

fig, ax1 = plt.subplots()

# 绘制柱状图
ax1.bar(months, sales, color='b', alpha=0.6)
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales', color='b')

# 绘制折线图
ax2 = ax1.twinx()
ax2.plot(months, growth_rate, color='r', marker='o')
ax2.set_ylabel('Growth Rate', color='r')

plt.title('柱线图')
plt.show()
