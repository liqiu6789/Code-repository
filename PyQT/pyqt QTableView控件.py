import sys
from PyQt5.QtWidgets import QApplication, QTableView,QFrame
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


class TableViewExample(QTableView):
    def __init__(self):
        super().__init__()

        # 创建一个模型
        self.model = QStandardItemModel(4, 3)  # 4行3列

        # 设置表头标签
        self.model.setHorizontalHeaderLabels(['Header 1', 'Header 2', 'Header 3'])

        # 填充数据
        for row in range(4):
            for column in range(3):
                item = QStandardItem(f"Row {row + 1}, Column {column + 1}")
                self.model.setItem(row, column, item)

                # 将模型设置为表格视图的模型
        self.setModel(self.model)

        # 显示网格线和边框
        self.setGridStyle(Qt.SolidLine)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table_view = TableViewExample()
    table_view.show()
    sys.exit(app.exec_())