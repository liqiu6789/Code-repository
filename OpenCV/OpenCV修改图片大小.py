import cv2

# 读取图像
img = cv2.imread('liu_1.jpeg')

# 确保图像已经成功读取
if img is None:
    print("Error: Could not read image.")
    exit()

# 定义新的大小
width = 320
height = 450
dim = (width, height)

# 改变图像大小
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# 显示原图
cv2.imshow('Original Image', img)

# 显示改变大小后的图像
cv2.imshow('Resized Image', resized)

# 等待按键事件，0表示无限等待
cv2.waitKey(0)

# 关闭所有OpenCV窗口
cv2.destroyAllWindows()