from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_image_path, watermark_image_path, output_image_path, position=(0.5, 0.5), opacity=0.5):
    """
    在图片上添加水印

    :param input_image_path: 输入图片路径
    :param watermark_image_path: 水印图片路径
    :param output_image_path: 输出图片路径
    :param position: 水印位置，默认为图片中心 (x, y) 坐标值在0到1之间
    :param opacity: 水印的不透明度，1为完全不透明，0为完全透明
    :return: None
    """
    base_image = Image.open(input_image_path).convert("RGBA")
    watermark = Image.open(watermark_image_path).convert("RGBA")

    # 获取图片尺寸
    base_width, base_height = base_image.size
    watermark_width, watermark_height = watermark.size

    # 计算水印位置
    left = int(base_width * position[0] - watermark_width / 2)
    top = int(base_height * position[1] - watermark_height / 2)

    # 限制水印位置在图片内
    left = max(0, left)
    top = max(0, top)
    right = min(base_width, left + watermark_width)
    bottom = min(base_height, top + watermark_height)

    # 调整水印图片大小以适应新的位置，并使用抗锯齿滤波器
    watermark = watermark.resize((right - left, bottom - top), Image.LANCZOS)

    # 在水印图片上应用透明度
    # 注意：这里我们假设水印图片已经有了一个alpha通道，否则需要另外处理
    # 我们通过创建一个新的RGBA图片，并用水印图片和其alpha值来填充它，然后调整alpha值来改变不透明度
    watermark_rgba = Image.new('RGBA', watermark.size, (255, 255, 255, int(255 * opacity)))
    watermark_rgba.alpha_composite(watermark)

    # 将水印添加到原始图片上
    base_image.paste(watermark_rgba, (left, top), watermark_rgba)

    # 保存图片
    base_image.save(output_image_path)


# 使用示例
add_watermark('1.png', 'te.png', 'output_with_watermark.png')