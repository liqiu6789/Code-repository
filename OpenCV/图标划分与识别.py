import cv2
import numpy as np

# 加载图像
image_path = 'test_22.jpg'
image = cv2.imread(image_path)

# 获取图像尺寸
height, width, _ = image.shape

# 定义主体区域
top_border = 240  # 顶部边界，可以调整
bottom_border = height - 200  # 底部边界，可以调整
left_border = 86  # 左侧边界，可以调整
right_border = width - 100  # 右侧边界，可以调整

# 从主体区域裁剪图像
main_area = image[top_border:bottom_border, left_border:right_border]
main_height, main_width, _ = main_area.shape

# 定义网格参数
rows, cols = 9, 6  # 行数和列数
grid_height = 152
grid_width = 150

# 用于存储每个图标的位置和图像
positions = []
cell_images = []

# 遍历每个网格单元
for i in range(rows):
    for j in range(cols):
        # 计算每个单元的顶点坐标（在主体区域内）
        top_left_x = j * grid_width
        top_left_y = i * grid_height
        bottom_right_x = (j + 1) * grid_width
        bottom_right_y = (i + 1) * grid_height

        # 提取该区域的图像
        cell = main_area[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

        # 检查该区域是否包含图标（可以通过图像内容特征来判断）
        if np.mean(cell) < 240:  # 简单判断非空白区域
            absolute_top_left = (top_left_x + left_border, top_left_y + top_border)
            absolute_bottom_right = (bottom_right_x + left_border, bottom_right_y + top_border)
            positions.append((absolute_top_left, absolute_bottom_right))
            cell_images.append(cell)

# 计算第一个单元格的特征
reference_image = cell_images[0]
reference_hist = cv2.calcHist([reference_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
cv2.normalize(reference_hist, reference_hist, 0, 1, cv2.NORM_MINMAX)

# 用于存储相似度和索引
similarities = []

# 遍历其他单元格，计算相似度
for idx, cell_image in enumerate(cell_images):
    if idx == 0:
        continue  # 跳过与自身的比较
    cell_hist = cv2.calcHist([cell_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(cell_hist, cell_hist, 0, 1, cv2.NORM_MINMAX)
    similarity = cv2.compareHist(reference_hist, cell_hist, cv2.HISTCMP_CORREL)
    similarities.append((idx, similarity))

# 找到相似度最高的索引
similarities.sort(key=lambda x: x[1], reverse=True)
most_similar_index = similarities[0][0]

print("与索引0区域相似度最高的区域的索引:", most_similar_index)

# 用imshow方法显示匹配的区域和匹配到的区域
cv2.imshow(f"Matched Area {0}", reference_image)
cv2.imshow(f"Matched Area {most_similar_index}", cell_images[most_similar_index])
cv2.waitKey(0)
cv2.destroyAllWindows()
