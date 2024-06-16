import re
import jieba
from collections import Counter, defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl

# 设置中文字体，确保图表中能显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 读取本地《三国演义》文本文件
with open('三国演义.txt', 'r', encoding='utf-8') as file:
    sanguo_text = file.read()

# 去除标点符号和换行符
sanguo_text = re.sub(r'[^\w\s]', '', sanguo_text)
sanguo_text = re.sub(r'\n', '', sanguo_text)

# 使用jieba进行分词
words = jieba.lcut(sanguo_text)

# 读取停用词列表
with open('常用停用词.txt', 'r', encoding='utf-8') as file:
    stopwords = set(file.read().split())

# 去除停用词
filtered_words = [word for word in words if word not in stopwords]

# 三国演义主要人物及其别名列表（扩展版）
characters = {
    "刘备": ["刘备", "玄德", "皇叔"],
    "关羽": ["关羽", "云长"],
    "张飞": ["张飞", "翼德"],
    "曹操": ["曹操", "孟德", "丞相", "曹孟德"],
    "孙权": ["孙权", "仲谋"],
    "诸葛亮": ["诸葛亮", "孔明", "卧龙"],
    "周瑜": ["周瑜", "公瑾"],
    "吕布": ["吕布", "奉先"],
    "貂蝉": ["貂蝉"],
    "赵云": ["赵云", "子龙"],
    "黄忠": ["黄忠", "汉升"],
    "马超": ["马超", "孟起"],
    "许褚": ["许褚", "仲康"],
    "典韦": ["典韦"],
    "司马懿": ["司马懿", "仲达"],
    "郭嘉": ["郭嘉", "奉孝"],
    "袁绍": ["袁绍", "本初"],
    "袁术": ["袁术", "公路"],
    "孙策": ["孙策", "伯符"],
    "甘宁": ["甘宁", "兴霸"],
    "鲁肃": ["鲁肃", "子敬"],
    "庞统": ["庞统", "凤雏"],
    "姜维": ["姜维", "伯约"]
}

# 创建一个人物关系计数字典
relation_counts = defaultdict(int)

# 遍历文本，统计人物间的关系
for i in range(len(filtered_words) - 1):
    for name1, aliases1 in characters.items():
        if filtered_words[i] in aliases1:
            for name2, aliases2 in characters.items():
                if filtered_words[i + 1] in aliases2 and name1 != name2:
                    relation_counts[(name1, name2)] += 1

# 创建网络图
G = nx.Graph()

# 添加节点
for character in characters.keys():
    G.add_node(character)

# 添加边及权重
for (name1, name2), count in relation_counts.items():
    G.add_edge(name1, name2, weight=count)

# 绘制关系图
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=1)
edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]

# 绘制节点和边
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', width=weights)

# 在图中显示边的权重
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('《三国演义》人物关系网（扩展版）')
plt.show()
