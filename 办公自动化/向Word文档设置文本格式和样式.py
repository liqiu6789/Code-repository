from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 打开一个现有的文档
doc = Document('path_to_your_existing_document.docx')

# 修改第一个段落的格式
p = doc.paragraphs[0]
run = p.runs[0]

# 设置字体和字号
run.font.name = 'Arial'
run.font.size = Pt(14)

# 设置加粗和斜体
run.bold = True
run.italic = True

# 设置字体颜色
run.font.color.rgb = RGBColor(255, 0, 0)

# 设置段落对齐方式
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# 保存修改后的文档
doc.save('modified_document.docx')
