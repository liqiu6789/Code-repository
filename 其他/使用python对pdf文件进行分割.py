import os
import PyPDF2


def split_pdf(input_path, output_folder, page_range=None):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 打开PDF文件
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # 获取PDF文件的总页数
        num_pages = len(reader.pages)

        # 如果没有指定页面范围，则分割所有页面
        if page_range is None:
            page_range = list(range(num_pages))

            # 遍历页面范围并保存每个页面为一个单独的PDF文件
        for page_num in page_range:
            page = reader.pages[page_num]  # 使用reader.pages[page_num] 替代getPage(page_num)

            # 创建PDF文件名
            output_filename = f"{output_folder}/output_{page_num + 1}.pdf"
            with open(output_filename, 'wb') as output_pdf:
                writer = PyPDF2.PdfWriter()
                writer.add_page(page)
                writer.write(output_pdf)

            # 使用示例


input_pdf_path = '2021年上半年下午试卷答案.pdf'  # 输入PDF文件路径
output_folder = "./pdf_res"  # 输出到当前目录
split_pdf(input_pdf_path, output_folder)