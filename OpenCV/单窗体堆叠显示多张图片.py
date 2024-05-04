import cv2
import numpy as np

# 读取两张图片
img1 = cv2.imread('liu_3.jpeg')
img2 = cv2.imread('liu_1.jpeg')

# 获取图片的高度和宽度
h1, w1, _ = img1.shape
h2, w2, _ = img2.shape

# 计算画布的大小，这里我们简单地将两张图片垂直堆叠
# 你可以根据需要调整间距和其他布局参数
max_height = max(h1, h2)
total_height = max_height * 2  # 两张图片的高度之和（如果需要间距，可以加上间距）
max_width = max(w1, w2)  # 选择较宽的宽度作为画布的宽度

# 创建一个空白的大画布
canvas = np.zeros((total_height, max_width, 3), dtype=np.uint8)

# 将图片放置到画布上
# 第一张图片放置在顶部
canvas[:h1, :w1] = img1

# 第二张图片放置在下方，注意调整y坐标以放置在第一张图片的下方
canvas[h1:h1 + h2, :w2] = img2[:h2, :w2]  # 如果w2 > max_width，则只复制w2宽度内的部分

# 如果需要，你可以在这里添加间距或其他装饰

# 显示大画布
cv2.imshow('Combined Image', canvas)
cv2.waitKey(0)  # 等待任意按键
cv2.destroyAllWindows()  # 关闭窗口