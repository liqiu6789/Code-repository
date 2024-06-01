import matplotlib.pyplot as plt
import numpy as np

# 示例数据
categories = ['Start', 'Product A', 'Product B', 'Product C', 'End']
values = [1000, 200, -300, 150, 0]  # 最后一个值为0，表示结束点

# 计算每一步的累计值
cumulative = np.cumsum(values)
cumulative = np.insert(cumulative, 0, 0)  # 插入起始点
cumulative = cumulative[:-1]  # 去掉最后一个点的累计值

# 定义颜色
colors = ['green' if val >= 0 else 'red' for val in values]

# 创建瀑布图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制矩形
for i in range(len(values)):
    ax.bar(categories[i], values[i], bottom=cumulative[i], color=colors[i])

# 添加标签
for i in range(len(values)):
    if values[i] >= 0:
        ax.text(i, cumulative[i] + values[i]/2, f"+{values[i]}", ha='center', va='center', color='black')
    else:
        ax.text(i, cumulative[i] + values[i]/2, f"{values[i]}", ha='center', va='center', color='black')

# 设置标题和标签
ax.set_title('Waterfall Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# 显示图表
plt.show()
