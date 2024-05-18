import os
from PyPDF2 import PdfFileReader, PdfWriter,PdfReader


def merge_pdfs(directory, output_filename):
    pdf_writer = PdfWriter()

    # 遍历指定文件夹中的所有PDF文件
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(directory, filename)
            pdf_reader = PdfReader(open(pdf_file_path, 'rb'))

            # 逐页添加到PDF写入器中
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

                # 将合并后的PDF写入到输出文件中
    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    # 使用函数


directory_path = './pdf_res'  # 替换为你的PDF文件夹路径
output_filename = 'merged_output.pdf'  # 合并后的PDF文件名
merge_pdfs(directory_path, output_filename)

print(f"PDFs merged successfully to {output_filename}")