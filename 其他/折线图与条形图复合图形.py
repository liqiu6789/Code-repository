import matplotlib.pyplot as plt
import numpy as np

# 示例数据
categories = ['A', 'B', 'C', 'D', 'E']
bar_values = [5, 7, 3, 8, 6]
line_values = [2, 3, 4, 5, 6]

# 创建一个新的图形
fig, ax1 = plt.subplots()

# 绘制条形图
bar_width = 0.4
bar_positions = np.arange(len(categories))
bars = ax1.bar(bar_positions, bar_values, bar_width, label='Bar Values', color='skyblue')

# 设置条形图的Y轴标签
ax1.set_ylabel('Bar Values')
ax1.set_xlabel('Categories')
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(categories)
ax1.legend(loc='upper left')

# 创建第二个Y轴，共享X轴
ax2 = ax1.twinx()

# 绘制折线图
line = ax2.plot(bar_positions, line_values, label='Line Values', color='red', marker='o')

# 设置折线图的Y轴标签
ax2.set_ylabel('Line Values')
ax2.legend(loc='upper right')

# 添加图表标题
plt.title('Combined Bar and Line Chart')

# 显示图表
plt.show()
