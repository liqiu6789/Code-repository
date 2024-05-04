import cv2
import numpy as np

# 读取图像
img = cv2.imread('liu_1.jpeg', 1)

# 初始化亮度值
brightness = 50


# 定义回调函数，用于处理滑动条值的变化
def brightness_change(value):
    # 创建一个 HSV 颜色空间的副本
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 计算 V 通道的新值
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0

    # 将新的 V 通道与 H 和 S 通道合并
    final_hsv = cv2.merge((h, s, v))

    # 将图像从 HSV 转换回 BGR
    img_brightness = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    # 显示调整亮度后的图像
    cv2.imshow('Brightness Adjustment', img_brightness)


# 创建窗口和滑动条
cv2.namedWindow('Brightness Adjustment')
cv2.createTrackbar('Brightness', 'Brightness Adjustment', brightness, 255, brightness_change)

# 显示原始图像
cv2.imshow('Brightness Adjustment', img)

# 等待键盘输入，按 'q' 键退出
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 关闭所有窗口
cv2.destroyAllWindows()