from PyQt5.QtWidgets import QApplication, QTreeView, QVBoxLayout, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


class TreeViewExample(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化布局和视图
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个模型
        model = QStandardItemModel()

        # 创建根节点
        root_item = model.invisibleRootItem()

        # 添加一些子节点到根节点
        item1 = QStandardItem('Item 1')
        item11 = QStandardItem('Item 1.1')
        item12 = QStandardItem('Item 1.2')
        item1.appendRow([item11, item12])
        root_item.appendRow(item1)

        item2 = QStandardItem('Item 2')
        item21 = QStandardItem('Item 2.1')
        item2.appendRow(item21)
        root_item.appendRow(item2)

        # 创建一个视图并设置模型
        tree_view = QTreeView()
        tree_view.setModel(model)

        # 设置视图的扩展标志以允许所有列展开
        tree_view.setExpandsOnDoubleClick(False)
        tree_view.setRootIsDecorated(False)
        tree_view.setSortingEnabled(True)

        # 添加视图到布局
        layout.addWidget(tree_view)

        # 设置窗口布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('QTreeView Example')
        self.setGeometry(300, 300, 300, 200)


if __name__ == '__main__':
    app = QApplication([])
    ex = TreeViewExample()
    ex.show()
    app.exec_()