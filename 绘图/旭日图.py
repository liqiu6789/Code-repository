import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
sub_sizes = [7, 8, 15, 15, 20, 25, 5, 5]
sub_labels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

# 绘制旭日图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, radius=1.3, wedgeprops=dict(width=0.3, edgecolor='w'))
ax.pie(sub_sizes, labels=sub_labels, radius=1, wedgeprops=dict(width=0.3, edgecolor='w'))
ax.set(aspect="equal")
plt.title('旭日图')
plt.show()
