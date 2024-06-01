import numpy as np
import matplotlib.pyplot as plt

# 示例数据
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
values = [4, 7, 1, 8, 5, 9, 6, 3]

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]  # 使得图形首尾相连
angles += angles[:1]  # 使得图形首尾相连

# 绘制南丁格尔图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)

# 添加标签
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# 添加标题
plt.title('Nightingale Rose Chart', size=20, color='blue')

# 显示图表
plt.show()
