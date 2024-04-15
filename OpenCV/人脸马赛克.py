import cv2
import dlib

# 加载人脸检测器
detector = dlib.get_frontal_face_detector()


def blur_face(image_path, output_path, kernel_size):
    # 读取图像
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    rects = detector(gray, 0)

    for rect in rects:
        # 计算人脸区域的坐标
        x, y, w, h = (rect.left(), rect.top(), rect.width(), rect.height())

        # 在人脸区域上应用马赛克效果
        face_region = image[y:y + h, x:x + w]
        face_region = cv2.medianBlur(face_region, kernel_size)

        # 将处理后的区域放回原图像中
        image[y:y + h, x:x + w] = face_region

        # 保存结果
    cv2.imwrite(output_path, image)


# 使用示例
blur_face('liu_1.jpeg', 'output.jpg', 21)