import cv2
import numpy as np

# 读取图像
img = cv2.imread('liu_1.jpeg')

# 获取图像的高度和宽度
rows, cols, ch = img.shape

# 定义平移矩阵，tx和ty是x和y方向的平移量
# 这里我们假设tx=100, ty=50
tx = 100
ty = 50

# 创建平移矩阵 M，这里我们使用了numpy的float32类型
# 注意OpenCV的warpAffine函数需要这个数据类型
M = np.float32([[1, 0, tx], [0, 1, ty]])

# 进行仿射变换，使用线性插值（INTER_LINEAR）
# 注意这里dsize参数指定了输出图像的大小，这里我们简单地使用原图像的大小
# 如果你想让图像在平移后填充一些空白区域，你需要调整这个参数
translated = cv2.warpAffine(img, M, (cols, rows))

# 显示平移后的图像
cv2.imshow('Translated Image', translated)

# 等待按键并关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 如果你还想保存平移后的图像
cv2.imwrite('translated.jpg', translated)