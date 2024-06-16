import re
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from pylab import mpl

# 设置中文字体，确保图表中能显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 读取本地《三国演义》文本文件
with open('三国演义.txt', 'r', encoding='utf-8') as file:
    sanguo_text = file.read()

# 去除标点符号和特殊字符，以及换行符
sanguo_text = re.sub(r'[^\w\s]', '', sanguo_text)
sanguo_text = re.sub(r'\n', '', sanguo_text)

# 使用jieba进行分词
words = jieba.lcut(sanguo_text)

# 读取停用词列表
with open('常用停用词.txt', 'r', encoding='utf-8') as file:
    stopwords = set(file.read().split())

# 去除停用词
filtered_words = [word for word in words if word not in stopwords]

# 统计词频
word_counts = Counter(filtered_words)

# 输出出现频率最高的10个词
print("词频最高的10个词：", word_counts.most_common(10))

# 三国演义主要人物及其别名列表
characters = {
    "刘备": ["刘备", "玄德", "皇叔"],
    "关羽": ["关羽", "云长"],
    "张飞": ["张飞", "翼德"],
    "曹操": ["曹操", "孟德", "丞相"],
    "孙权": ["孙权"],
    "诸葛亮": ["诸葛亮", "孔明", "卧龙"],
    "周瑜": ["周瑜", "公瑾"],
    "吕布": ["吕布", "奉先"],
    "貂蝉": ["貂蝉"],
    "赵云": ["赵云", "子龙"]
}

# 初始化人物出场次数统计字典
character_counts = {key: 0 for key in characters}

# 统计人物出场次数
for character, aliases in characters.items():
    count = 0
    for alias in aliases:
        count += sanguo_text.count(alias)
    character_counts[character] = count

# 输出人物出场次数
print("主要人物出场次数：", character_counts)

# 提取人物和出场次数
names = list(character_counts.keys())
counts = list(character_counts.values())

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(names, counts, color='skyblue')
plt.xlabel('人物')
plt.ylabel('出场次数')
plt.title('《三国演义》主要人物出场次数统计')
plt.show()
