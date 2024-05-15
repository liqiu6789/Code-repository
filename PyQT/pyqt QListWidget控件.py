import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget


class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化 QListWidget
        self.listWidget = QListWidget(self)

        # 添加 QListWidgetItem 到 QListWidget
        for i in range(5):
            item = QListWidgetItem(f"Item {i + 1}")
            self.listWidget.addItem(item)

            # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.listWidget)

        # 设置窗口标题和大小
        self.setWindowTitle('QListWidget Example')
        self.setGeometry(100, 100, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec_())