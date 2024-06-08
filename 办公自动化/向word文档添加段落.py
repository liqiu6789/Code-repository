from docx import Document

# 打开一个现有的Word文档
doc = Document(r'C:\Users\Administrator\Desktop\Word文档\example.docx')

# 三国演义的文本
text = (
    "话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。"
    "汉朝自高祖斩白蛇而起义，一统天下。后来光武中兴，传至献帝，遂分为三国。"
)

# 添加一个新的段落
doc.add_paragraph(text)

# 保存文档
doc.save(r'C:\Users\Administrator\Desktop\Word文档\example.docx')
