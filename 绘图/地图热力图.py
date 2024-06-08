import pandas as pd
import random
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType

# 生成全国范围内的50个示例数据
data = pd.DataFrame({
    'latitude': [random.uniform(20.0, 50.0) for _ in range(50)],
    'longitude': [random.uniform(80.0, 130.0) for _ in range(50)],
    'value': [random.randint(10, 100) for _ in range(50)]
})

# 提取经纬度和权重值
locations = [(row['longitude'], row['latitude']) for index, row in data.iterrows()]
values = [row['value'] for index, row in data.iterrows()]

# 初始化地图
geo = Geo()
geo.add_schema(maptype="china")

# 添加地理坐标和权重数据
for (lng, lat), value in zip(locations, values):
    geo.add_coordinate(f"{lng},{lat}", lng, lat)
    geo.add("热力图", [(f"{lng},{lat}", value)], type_=ChartType.HEATMAP)

# 设置地图中心和缩放比例
geo.set_global_opts(
    title_opts=opts.TitleOpts(title="测试热力图"),
    visualmap_opts=opts.VisualMapOpts(max_=100),
)

# 渲染地图到 HTML 文件
geo.render("test_heatmap.html")

print("Heatmap has been saved to 'test_heatmap.html'.")
