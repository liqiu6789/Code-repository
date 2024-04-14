import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt, QEvent


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建QTextEdit控件
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # 插入一条横线
        self.insert_horizontal_line()

    def insert_horizontal_line(self):
        # 清除之前的横线
        self.text_edit.clear()

        # 计算横线的数量
        line_length = self.text_edit.width() - self.text_edit.contentsMargins().left() - self.text_edit.contentsMargins().right()
        char_width = self.text_edit.fontMetrics().horizontalAdvance('-')  # 使用'-'字符来估计字符宽度
        num_lines = (line_length // char_width) -1

        # 插入横线
        line = '-' * num_lines
        self.text_edit.insertPlainText(line)

    def resizeEvent(self, event: QEvent):
        super().resizeEvent(event)
        # 窗体大小改变时更新横线
        self.insert_horizontal_line()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())