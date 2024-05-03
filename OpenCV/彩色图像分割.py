import cv2 as cv
import numpy as np


def color_seperate(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # 对目标图像进行色彩空间转换
    lower_hsv = np.array([100, 43, 46])  # 设定蓝色下限
    upper_hsv = np.array([124, 255, 255])  # 设定蓝色上限

    # 依据设定的上下限对目标图像进行二值化转换
    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)

    # 将二值化图像与原图进行“与”操作；实际是提取蓝色部分
    dst = cv.bitwise_and(image, image, mask=mask)  # 注意：这里将src替换为image

    return dst


# 导入目标图像，获取图像信息
src = cv.imread('blue_1.jpeg')
if src is not None:  # 确保图像被正确读取
    # 调用函数并显示结果
    dst = color_seperate(src)
    cv.imshow('image', src)  # 显示原始图像
    cv.imshow('result', dst)  # 显示处理后的图像
    cv.waitKey(0)  # 等待按键
    cv.destroyAllWindows()  # 销毁所有窗口
else:
    print("Error: Unable to load image.")