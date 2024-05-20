from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TextEditExample(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化布局和视图
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个QTextEdit控件
        text_edit = QTextEdit(self)

        # 设置一些初始文本
        text_edit.setPlainText("这是一个QTextEdit控件的示例。\n你可以在这里输入和编辑多行文本。")

        # 你可以设置字体样式
        font = QFont("Arial", 12)
        text_edit.setFont(font)

        # 还可以设置文本编辑控件是只读的
        # text_edit.setReadOnly(True)

        # 添加QTextEdit到布局中
        layout.addWidget(text_edit)

        # 设置窗口布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('QTextEdit 示例')
        self.setGeometry(300, 300, 300, 200)


if __name__ == '__main__':
    app = QApplication([])
    ex = TextEditExample()
    ex.show()
    app.exec_()