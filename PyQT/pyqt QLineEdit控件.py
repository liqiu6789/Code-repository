from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt


class LineEditExample(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化布局和控件
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个QLineEdit控件
        self.line_edit = QLineEdit(self)

        # 设置一些初始文本（可选）
        self.line_edit.setText("请输入文本...")

        # 设置为密码输入模式（可选）
        # self.line_edit.setEchoMode(QLineEdit.Password)

        # 创建一个按钮用于获取文本
        button = QPushButton('获取文本', self)
        button.clicked.connect(self.on_button_clicked)

        # 将控件添加到布局中
        layout.addWidget(self.line_edit)
        layout.addWidget(button)

        # 设置窗口布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('QLineEdit 示例')
        self.setGeometry(300, 300, 300, 150)

    def on_button_clicked(self):
        # 当按钮被点击时，获取 QLineEdit 中的文本并打印到控制台
        text = self.line_edit.text()
        print(f"输入的文本是: {text}")


if __name__ == '__main__':
    app = QApplication([])
    ex = LineEditExample()
    ex.show()
    app.exec_()