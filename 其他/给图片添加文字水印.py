from PIL import Image, ImageDraw, ImageFont


def add_text_watermark(input_image_path, output_image_path, text, position, font_path, font_size, color):
    # 打开图片
    img = Image.open(input_image_path)

    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)

    # 加载字体，并设置字体大小
    font = ImageFont.truetype(font_path, font_size)

    # 获取文本大小（宽度，高度）
    #text_width, text_height = draw.textsize(text, font)

    # 根据给定的位置调整文本位置
    # 这里假设position是一个元组，包含(x, y)坐标
    # 例如，如果你想让文本在右下角，你可以使用(img.width - text_width, img.height - text_height)
    x, y = position

    # 在图片上添加文本
    draw.text((x, y), text, fill=color, font=font)

    # 保存图片
    img.save(output_image_path)


# 使用示例
input_image_path = '心形.jpg'  # 输入图片路径
output_image_path = 'output_with_watermark.jpg'  # 输出图片路径
text = 'Watermark'  # 要添加的水印文本
position = (10, 10)  # 水印文本的起始位置（左上角）
font_path = 'arial.ttf'  # 字体文件路径，确保你有这个文件
font_size = 36  # 字体大小
color = (0, 0, 255)  # 字体颜色

add_text_watermark(input_image_path, output_image_path, text, position, font_path, font_size, color)