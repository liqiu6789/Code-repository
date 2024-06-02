import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体
font_path = 'C:/Windows/Fonts/simhei.ttf'  # Windows 系统的字体路径
# font_path = '/System/Library/Fonts/STHeiti Medium.ttc'  # macOS 系统的字体路径
my_font = fm.FontProperties(fname=font_path)

# 生成示例数据
np.random.seed(0)
dates = pd.date_range('2020-01-01', periods=365 * 3)  # 3年数据
values = np.random.rand(len(dates)) * 100

# 创建 DataFrame
df = pd.DataFrame({'date': dates, 'value': values})

# 添加年份和月份列
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.strftime('%b')  # 月份名称

# 为了避免重复数据，按每个月计算平均值
df_monthly_avg = df.groupby(['year', 'month']).mean().reset_index()

# 透视表格，按年份和月份分组
pivot_table = df_monthly_avg.pivot(index='month', columns='year', values='value')
pivot_table = pivot_table.reindex(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# 绘制季节图
plt.figure(figsize=(12, 6))
for year in pivot_table.columns:
    plt.plot(pivot_table.index, pivot_table[year], marker='o', label=year)

# 设置图表标题和标签
plt.title('季节图示例', fontsize=16, fontproperties=my_font)
plt.xlabel('月份', fontsize=14, fontproperties=my_font)
plt.ylabel('值', fontsize=14, fontproperties=my_font)
plt.legend(title='年份', prop=my_font)

# 显示图表
plt.show()
