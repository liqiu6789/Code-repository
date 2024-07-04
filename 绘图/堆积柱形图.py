import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
subcategories = ['Subcategory A', 'Subcategory B', 'Subcategory C']
data = np.array([
    [5, 3, 4, 7],
    [2, 4, 6, 8],
    [3, 7, 8, 2]
])

# 定义柱状条的位置
x = np.arange(len(categories))

# 绘制堆积柱形图
fig, ax = plt.subplots()

# 底部初始值
bottom = np.zeros(len(categories))

# 为每个子类别绘制条形
for i in range(len(subcategories)):
    ax.bar(x, data[i], bottom=bottom, label=subcategories[i])
    bottom += data[i]

# 设置图表标题和标签
plt.title('Stacked Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 设置x轴刻度
plt.xticks(x, categories)

# 添加图例
plt.legend(subcategories)

# 显示图表
plt.tight_layout()
plt.show()
