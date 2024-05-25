import matplotlib.pyplot as plt

# 示例数据
outer_labels = ['Category A', 'Category B', 'Category C']
outer_sizes = [30, 45, 25]
outer_colors = ['#ff9999','#66b3ff','#99ff99']

inner_labels = ['A1', 'A2', 'A3', 'B1', 'B2', 'C1', 'C2', 'C3']
inner_sizes = [10, 12, 8, 20, 25, 10, 10, 5]
inner_colors = ['#ff6666','#ff9999','#ffcccc', '#66b3ff','#99ccff', '#99ff99','#66ff66','#33cc33']

# 创建一个图形对象
fig, ax = plt.subplots()

# 绘制外层饼图
ax.pie(outer_sizes, labels=outer_labels, colors=outer_colors, radius=1, wedgeprops=dict(width=0.3, edgecolor='w'))

# 绘制内层饼图
ax.pie(inner_sizes, labels=inner_labels, colors=inner_colors, radius=0.7, wedgeprops=dict(width=0.3, edgecolor='w'))

# 设置绘图区域为正方形，确保饼图为圆形
ax.set(aspect="equal")

# 显示图形
plt.show()
