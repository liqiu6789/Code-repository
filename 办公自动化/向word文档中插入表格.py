from docx import Document

# 加载现有的Word文档
doc = Document(r'C:\Users\Administrator\Desktop\Word文档\example.docx')

# 添加一个表格，3行4列
table = doc.add_table(rows=3, cols=4)

# 设置表格样式（可选）
table.style = 'Table Grid'

# 填充表格数据
data = [
    ["Header1", "Header2", "Header3", "Header4"],
    ["Row1 Col1", "Row1 Col2", "Row1 Col3", "Row1 Col4"],
    ["Row2 Col1", "Row2 Col2", "Row2 Col3", "Row2 Col4"]
]

# 将数据填入表格
for row_idx, row_data in enumerate(data):
    row = table.rows[row_idx]
    for col_idx, cell_data in enumerate(row_data):
        cell = row.cells[col_idx]
        cell.text = cell_data

# 保存文档
doc.save(r'C:\Users\Administrator\Desktop\Word文档\example.docx')
