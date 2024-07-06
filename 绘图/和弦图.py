import pandas as pd
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

# 示例数据
data = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('A', 'D', 6),
    ('B', 'A', 2),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('C', 'A', 4),
    ('C', 'B', 3),
    ('C', 'D', 5),
    ('D', 'A', 6),
    ('D', 'B', 8),
    ('D', 'C', 5)
]

# 转换为DataFrame
df = pd.DataFrame(data, columns=['source', 'target', 'value'])

# 创建和弦图
chord = hv.Chord(df)

# 设置图表选项
chord.opts(
    opts.Chord(
        cmap='Category20',
        edge_cmap='Category20',
        edge_color=hv.dim('source').str(),
        labels='source',
        node_color=hv.dim('index').str(),
        edge_line_width=hv.dim('value')*0.1
    )
)

# 将图表保存为HTML文件
hv.save(chord, 'chord.html', fmt='html')

# 打印提示信息
print("和弦图已保存为 chord.html")
