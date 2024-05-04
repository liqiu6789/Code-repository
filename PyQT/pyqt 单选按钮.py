import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建一个垂直布局
        vbox = QVBoxLayout()

        # 创建三个单选按钮
        self.radio1 = QRadioButton('选项 1')
        self.radio2 = QRadioButton('选项 2')
        self.radio3 = QRadioButton('选项 3')

        # 将单选按钮添加到布局中
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)

        # 设置单选按钮的互斥性（默认就是互斥的）
        # 这里通常不需要显式设置，因为 QRadioButton 默认就是互斥的

        # 创建一个标签来显示当前选中的选项（可选）
        self.label = QLabel('没有选项被选中')
        vbox.addWidget(self.label)

        # 连接单选按钮的状态改变信号到一个槽函数
        self.radio1.toggled.connect(self.onRadioButtonToggled)
        self.radio2.toggled.connect(self.onRadioButtonToggled)
        self.radio3.toggled.connect(self.onRadioButtonToggled)

        # 设置主窗口的布局
        self.setLayout(vbox)

        # 设置窗口标题和大小
        self.setWindowTitle('QRadioButton 示例')
        self.setGeometry(300, 300, 200, 150)

    def onRadioButtonToggled(self, state):
        # 当单选按钮的状态改变时，这个函数会被调用
        if self.radio1.isChecked() and state:
            self.label.setText('选项 1 被选中')
        elif self.radio2.isChecked() and state:
            self.label.setText('选项 2 被选中')
        elif self.radio3.isChecked() and state:
            self.label.setText('选项 3 被选中')
        else:
            self.label.setText('没有选项被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())