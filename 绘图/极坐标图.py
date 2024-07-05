import plotly.express as px
import pandas as pd

# 示例数据
data = {
    '方向': ['北', '东北', '东', '东南', '南', '西南', '西', '西北'],
    '值': [1, 2, 3, 4, 5, 4, 3, 2]
}

df = pd.DataFrame(data)

# 创建极坐标图
fig = px.line_polar(df, r='值', theta='方向', line_close=True, title='极坐标图示例')

# 显示图表
fig.show()
