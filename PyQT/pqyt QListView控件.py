from PyQt5.QtWidgets import QApplication, QListView, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


class ListViewExample(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化UI
        self.initUI()

    def initUI(self):
        # 设置布局
        layout = QVBoxLayout(self)

        # 创建一个模型
        self.model = QStandardItemModel(0, 1)  # 0行1列

        # 添加一些数据
        for i in range(50):  # 假设有50条数据
            item = QStandardItem(f"Item {i + 1}")
            self.model.appendRow(item)

            # 设置模型可以排序
        self.model.setSortRole(Qt.DisplayRole)
        self.model.sort(0, Qt.AscendingOrder)

        # 创建一个视图并设置模型
        self.view = QListView()
        self.view.setModel(self.model)

        # 添加视图到布局
        layout.addWidget(self.view)

        # 可选：添加一个按钮以触发排序
        sort_button = QPushButton("Sort Descending")
        sort_button.clicked.connect(self.sortDescending)
        layout.addWidget(sort_button)

        # 设置窗口标题和大小
        self.setWindowTitle('QListView Example with Sorting')
        self.setGeometry(100, 100, 300, 300)

    def sortDescending(self):
        # 根据第一列降序排序
        self.model.sort(0, Qt.DescendingOrder)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = ListViewExample()
    ex.show()
    sys.exit(app.exec_())