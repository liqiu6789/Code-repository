import sys
from PyQt5.QtWidgets import QApplication, QSplitter, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class SplitterExample(QWidget):
    def __init__(self):
        super().__init__()

        # 创建两个文本编辑器部件
        text_edit_1 = QTextEdit()
        text_edit_2 = QTextEdit()

        # 创建 QSplitter 对象，并设置为垂直方向
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(text_edit_1)
        splitter.addWidget(text_edit_2)

        # 设置主窗口的布局，并将 QSplitter 添加到其中
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('QSplitter 示例')
        self.setGeometry(100, 100, 500, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = SplitterExample()
    example.show()
    sys.exit(app.exec_())