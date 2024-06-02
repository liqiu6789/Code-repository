import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calmap
import matplotlib.font_manager as fm

# 设置中文字体
# 可以使用系统内的中文字体，例如 SimHei 或者你电脑中的其他字体
# 请确保系统中有该字体，路径可以根据需要修改
# Windows 系统可以使用 C:\Windows\Fonts\SimHei.ttf
# macOS 系统可以使用 /System/Library/Fonts/STHeiti Medium.ttc
font_path = 'C:/Windows/Fonts/simhei.ttf'
my_font = fm.FontProperties(fname=font_path)

# 生成示例数据
dates = pd.date_range('2023-01-01', periods=365)
data = np.random.randint(0, 100, len(dates))
df = pd.DataFrame({'date': dates, 'value': data})
df.set_index('date', inplace=True)

# 使用 calmap 绘制日历热力图
plt.figure(figsize=(16, 10))
calmap.yearplot(df['value'], year=2023, cmap='YlGn', fillcolor='grey', linewidth=0.5)

# 添加标题
plt.title('日历热力图示例 (2023)', fontproperties=my_font)
plt.show()
