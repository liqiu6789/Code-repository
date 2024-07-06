import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
# 示例数据
kpi_name = 'Sales Growth'
kpi_value = '15%'

# 绘制指标卡
fig, ax = plt.subplots(figsize=(3, 1.5))
ax.text(0.5, 0.7, kpi_name, horizontalalignment='center', verticalalignment='center', fontsize=12)
ax.text(0.5, 0.3, kpi_value, horizontalalignment='center', verticalalignment='center', fontsize=24, color='green')
ax.axis('off')
plt.title('指标卡')
plt.show()
