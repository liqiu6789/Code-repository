from docx import Document

# 加载现有的Word文档
doc = Document(r'C:\Users\Administrator\Desktop\Word文档\example.docx')

# 假设我们知道表格的位置（例如文档中的第一个表格）
table = doc.tables[0]

# 定义新的数据
new_data = [
    ["New Header1", "New Header2", "New Header3", "New Header4"],
    ["New Row1 Col1", "New Row1 Col2", "New Row1 Col3", "New Row1 Col4"],
    ["New Row2 Col1", "New Row2 Col2", "New Row2 Col3", "New Row2 Col4"]
]

# 将新数据填入表格
for row_idx, row_data in enumerate(new_data):
    row = table.rows[row_idx]
    for col_idx, cell_data in enumerate(row_data):
        cell = row.cells[col_idx]
        cell.text = cell_data

# 保存文档
doc.save(r'C:\Users\Administrator\Desktop\Word文档\example.docx')
