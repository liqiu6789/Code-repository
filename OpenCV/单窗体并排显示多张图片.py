import cv2
import numpy as np


def opencv_multi_img():
    # 读取图片
    img1 = cv2.imread('saw_1.jpeg')
    img2 = cv2.imread('saw_2.jpeg')
    img3 = cv2.imread('saw_3.jpeg')

    # 检查图片是否成功加载
    if img1 is None or img2 is None or img3 is None:
        print("Error: Unable to load one or more images.")
        return

        # 获取图片的高度和宽度
    h1, w1, _ = img1.shape
    h2, w2, _ = img2.shape
    h3, w3, _ = img3.shape

    # 确保所有图片的高度相同
    if h1 != h2 or h1 != h3:
        print("Error: Images must have the same height.")
        return

        # 创建一个空白的大画布
    max_width = w1 + w2 + w3  # 三张图片的总宽度
    canvas = np.zeros((h1, max_width, 3), dtype=np.uint8)

    # 将图片放置到画布上
    canvas[:, :w1] = img1
    canvas[:, w1:w1 + w2] = img2
    canvas[:, w1 + w2:w1 + w2 + w3] = img3

    # 展示多个图片
    cv2.imshow("multi_img", canvas)

    # 等待用户按键关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 调用函数
opencv_multi_img()