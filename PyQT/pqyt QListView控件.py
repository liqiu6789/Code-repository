from PyQt5.QtWidgets import QApplication, QListView, QVBoxLayout, QWidget
from PyQt5.QtCore import QStringListModel


class ListViewExample(QWidget):
    def __init__(self):
        super().__init__()

        # 设置布局
        layout = QVBoxLayout(self)

        # 创建一个字符串列表
        string_list = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

        # 创建一个 QStringListModel 并设置数据
        model = QStringListModel()
        model.setStringList(string_list)

        # 创建一个 QListView 并设置模型
        list_view = QListView()
        list_view.setModel(model)

        # 添加 QListView 到布局中
        layout.addWidget(list_view)

        # 设置窗口标题和大小
        self.setWindowTitle('QListView Example')
        self.setGeometry(100, 100, 300, 200)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = ListViewExample()
    ex.show()
    sys.exit(app.exec_())