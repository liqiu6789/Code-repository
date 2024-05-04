import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QPushButton, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        # 初始化界面
        self.initUI()

    def initUI(self):
        # 创建 QVBoxLayout
        vbox = QVBoxLayout()

        # 创建一个 QGroupBox
        groupBox = QGroupBox('我的控件组')

        # 在 QGroupBox 内创建一个 QVBoxLayout
        vbox_group = QVBoxLayout()

        # 在 QGroupBox 内添加控件
        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        lbl = QLabel('这是一个标签')

        vbox_group.addWidget(btn1)
        vbox_group.addWidget(btn2)
        vbox_group.addWidget(lbl)

        # 将 QVBoxLayout 设置为 QGroupBox 的布局
        groupBox.setLayout(vbox_group)

        # 在主 QVBoxLayout 中添加 QGroupBox
        vbox.addWidget(groupBox)

        # 设置主窗口的布局
        self.setLayout(vbox)

        # 设置窗口标题和大小
        self.setWindowTitle('QGroupBox 示例')
        self.setGeometry(300, 300, 250, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())