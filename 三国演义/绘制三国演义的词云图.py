import re
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
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

# 生成词云
wordcloud = WordCloud(
    font_path='simhei.ttf',  # 设置字体路径
    width=800,
    height=400,
    background_color='white',
    max_words=200
).generate_from_frequencies(word_counts)

# 显示词云图
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('《三国演义》词云图')
plt.show()
