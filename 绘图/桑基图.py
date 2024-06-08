import plotly.graph_objects as go

# 定义节点标签
labels = ["煤炭", "天然气", "核能", "太阳能", "风能", "居民用电", "商业用电", "工业用电", "交通运输"]

# 定义链接：源节点，目标节点，流量
sources = [0, 1, 2, 3, 4, 0, 1, 1, 2, 3, 4, 0, 1, 2, 3, 4]
targets = [5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8]
values = [10, 15, 5, 10, 7, 8, 10, 5, 12, 5, 3, 10, 8, 7, 3, 2]

# 定义链接颜色
link_colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FF33A6",
               "#FFBD33", "#33FFBD", "#FF5733", "#57FF33", "#5733FF",
               "#F333FF", "#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FF33A6"]

# 创建桑基图
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,  # 节点之间的填充距离
        thickness=20,  # 节点的厚度
        line=dict(color="black", width=0.5),  # 节点的边界颜色和宽度
        label=labels,  # 节点标签
    ),
    link=dict(
        source=sources,  # 源节点
        target=targets,  # 目标节点
        value=values,  # 流量值
        color=link_colors  # 链接颜色
    )
))

# 更新布局
fig.update_layout(title_text="能源流动桑基图", font_size=10)

# 显示图表
fig.show()
