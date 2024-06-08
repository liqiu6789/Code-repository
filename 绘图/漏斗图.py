import plotly.graph_objects as go
import plotly.io as pio

# 设置为在脚本中显示
pio.renderers.default = "browser"

# 漏斗图数据
stages = ["展示", "点击", "访问", "咨询", "订单"]
values = [100, 80, 60, 40, 20]

# 创建漏斗图
fig = go.Figure(go.Funnel(
    y = stages,
    x = values,
    textinfo = "value+percent initial",
    marker = {"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]}
))

# 设置图表标题
fig.update_layout(
    title = "漏斗图示例"
)

# 显示图表
fig.show()
