import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel


class StackedWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()

        # 创建堆叠窗口部件
        self.stack = QStackedWidget()

        # 创建两个标签作为页面
        self.label1 = QLabel("这是第一个页面")
        self.label2 = QLabel("这是第二个页面")

        # 将标签添加到堆叠中
        self.stack.addWidget(self.label1)
        self.stack.addWidget(self.label2)

        # 创建按钮来控制堆叠的显示
        self.button1 = QPushButton("显示第一个页面")
        self.button1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.button2 = QPushButton("显示第二个页面")
        self.button2.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.stack)

        # 设置窗口部件的布局
        self.setLayout(layout)

        # 设置窗口部件的标题和大小
        self.setWindowTitle('QStackedWidget 示例')
        self.setGeometry(100, 100, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedWidgetDemo()
    demo.show()
    sys.exit(app.exec_())