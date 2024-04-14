import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


class RandomPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()
        self.setWindowTitle("抽签小程序")
        # 创建第一个文本框用于输入选项
        self.input_text_edit = QTextEdit(self)
        self.input_text_edit.setPlaceholderText("请输入选项，每行一个")
        layout.addWidget(self.input_text_edit)

        # 创建抽签按钮
        self.draw_button = QPushButton('抽签', self)
        self.draw_button.clicked.connect(self.draw_random)
        layout.addWidget(self.draw_button)

        # 创建第二个文本框用于显示结果
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setReadOnly(True)  # 设置为只读
        layout.addWidget(self.output_text_edit)

        # 设置窗口的布局
        self.setLayout(layout)

        # 设置窗口的标题和大小
        self.setWindowTitle('随机抽签程序')
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def draw_random(self):
        # 获取输入文本框中的文本，并按行分割成选项列表
        options = self.input_text_edit.toPlainText().strip().split('\n')
        if not options:
            QMessageBox.warning(self, '警告', '请输入至少一个选项！')
            return

            # 从选项中随机选择三个不重复的结果
        try:
            drawn_options = random.sample(options, 3)
        except ValueError:
            QMessageBox.warning(self, '警告', '选项不足，无法抽取三个结果！')
            return

            # 将结果设置为第二个文本框的文本
        self.output_text_edit.setPlainText('\n'.join(drawn_options))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomPicker()
    sys.exit(app.exec_())