import cv2
import numpy as np

# 读取两张彩色图片
image1_color = cv2.imread('liu_1.jpeg')
image2_color = cv2.imread('liu_2.jpeg')
img_diff = image1_color.copy()
# 确保两张图片的尺寸相同
assert image1_color.shape == image2_color.shape, "两张图片的尺寸必须相同"

# 将彩色图片转换为灰度图片
image1_gray = cv2.cvtColor(image1_color, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2_color, cv2.COLOR_BGR2GRAY)

# 计算灰度图像的差异
diff = cv2.absdiff(image1_gray, image2_gray)

# 应用阈值来识别差异
_, thresholded = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 在原始彩色图像上绘制矩形框标记差异
for contour in contours:
    # 获取边界框
    x, y, w, h = cv2.boundingRect(contour)
    # 在原始彩色图像上绘制矩形框
    cv2.rectangle(img_diff, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 显示结果
cv2.imshow('img1', image1_color)
cv2.imshow('img2', image2_color)
cv2.imshow('Differences', img_diff)
cv2.waitKey(0)
cv2.destroyAllWindows()