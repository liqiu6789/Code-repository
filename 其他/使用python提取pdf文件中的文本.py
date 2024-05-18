from pdfminer.high_level import extract_text
from pathlib import Path


def extract_pdf_to_txt(pdf_path, txt_path):
    # 提取PDF中的文本
    text = extract_text(pdf_path)

    # 将文本写入txt文件
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"PDF text extracted to {txt_path}")


# 使用函数
pdf_file_path = 'pdf_res/output_1.pdf'  # 替换为你的PDF文件路径
txt_file_path = 'extracted_text.txt'  # 提取后的文本文件名

extract_pdf_to_txt(pdf_file_path, txt_file_path)