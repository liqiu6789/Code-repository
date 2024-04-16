import fitz  # PyMuPDF
import os


def pdf_to_images(pdf_path, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

        # 打开PDF文件
    doc = fitz.open(pdf_path)

    # 遍历PDF的每一页
    for page_num in range(len(doc)):
        page = doc[page_num]

        # 设置图片的分辨率（DPI），这会影响图片的质量
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)

        # 生成图片文件名
        image_filename = os.path.join(output_dir, f"page_{page_num + 1}.png")

        # 将图片保存到文件
        pix.save(image_filename)

        # 关闭PDF文件
    doc.close()
    print(f"PDF拆分完成，图片已保存到 {output_dir}")


# 使用函数拆分PDF
pdf_file = '2021年上半年上午试卷答案.pdf'  # 替换为你的PDF文件路径
output_folder = 'output_images'  # 输出图片的文件夹
pdf_to_images(pdf_file, output_folder)