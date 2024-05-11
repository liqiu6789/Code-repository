# 导入必要的库
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image
# 假设你的文本文件名为 'text.txt'，并且位于当前工作目录下
file_name = '三国演义.txt'

# 读取文件内容
with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()

# 使用jieba进行中文分词
seg_list = jieba.cut(text, cut_all=False)
words = " ".join(seg_list)

# 设置字体文件路径（确保支持中文）
font_path = 'simhei.ttf'  # 你需要指定一个支持中文的字体文件路径
mask_shape = np.array(Image.open("心形.jpg"))
# 创建词云对象，设置词云的一些属性
wordcloud = WordCloud(font_path=font_path,  # 设置字体文件路径，确保支持中文
                      background_color="white",  # 设置背景颜色
                      mask=mask_shape,
                      max_words=200,  # 最多显示的词数
                      max_font_size=100,  # 字体最大值
                      random_state=42,  # 设置随机种子以获得可重复的结果
                      width=800, height=800,  # 设置图片的尺寸
                      margin=2  # 设置词与词之间的距离
                      ).generate(words)

# 使用matplotlib显示词云图
plt.figure(figsize=(8, 8), facecolor=None)  # 创建一个8x8的绘图对象
plt.imshow(wordcloud)
plt.axis("off")  # 不显示坐标轴
plt.tight_layout(pad=0)  # 调整子图参数，使之填充整个图像区域
plt.show()  # 显示图像