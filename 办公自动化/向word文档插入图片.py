from docx import Document
from docx.shared import Inches

# 打开一个现有的Word文档
doc = Document(r'C:\Users\Administrator\Desktop\Word文档\example.docx')

# 插入图片
doc.add_picture(r'C:\Users\Administrator\Desktop\Word文档\img.png', width=Inches(4))

# 保存文档
doc.save(r'C:\Users\Administrator\Desktop\Word文档\modified_document.docx')
