import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Category A', 'Category B', 'Category C', 'Category D']
subcategories1 = np.array([5, 10, 15, 20])
subcategories2 = np.array([3, 7, 8, 12])
subcategories3 = np.array([2, 3, 4, 5])

# 计算每个类别的总和
totals = subcategories1 + subcategories2 + subcategories3

# 计算每个子类别的百分比
subcategories1_perc = subcategories1 / totals * 100
subcategories2_perc = subcategories2 / totals * 100
subcategories3_perc = subcategories3 / totals * 100

# 生成位置
bar_width = 0.5
r = np.arange(len(categories))

# 绘制百分比堆积条形图
plt.barh(r, subcategories1_perc, color='b', edgecolor='white', height=bar_width, label='Subcategory 1')
plt.barh(r, subcategories2_perc, left=subcategories1_perc, color='r', edgecolor='white', height=bar_width, label='Subcategory 2')
plt.barh(r, subcategories3_perc, left=subcategories1_perc+subcategories2_perc, color='g', edgecolor='white', height=bar_width, label='Subcategory 3')

# 添加标签和标题
plt.ylabel('Category', fontweight='bold')
plt.xlabel('Percentage (%)', fontweight='bold')
plt.yticks(r, categories)
plt.title('Percentage Stacked Bar Chart Example')

# 添加图例
plt.legend()

# 显示图表
plt.show()
