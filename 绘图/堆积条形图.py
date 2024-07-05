import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Category A', 'Category B', 'Category C', 'Category D']
subcategories1 = [5, 10, 15, 20]
subcategories2 = [3, 7, 8, 12]
subcategories3 = [2, 3, 4, 5]

# 生成位置
bar_width = 0.5
r = np.arange(len(categories))

# 绘制堆积条形图（横向）
plt.barh(r, subcategories1, color='b', edgecolor='white', height=bar_width, label='Subcategory 1')
plt.barh(r, subcategories2, left=subcategories1, color='r', edgecolor='white', height=bar_width, label='Subcategory 2')
plt.barh(r, subcategories3, left=np.array(subcategories1)+np.array(subcategories2), color='g', edgecolor='white', height=bar_width, label='Subcategory 3')

# 添加标签和标题
plt.ylabel('Category', fontweight='bold')
plt.xlabel('Values', fontweight='bold')
plt.yticks(r, categories)
plt.title('Horizontal Stacked Bar Chart Example')

# 添加图例
plt.legend()

# 显示图表
plt.show()
