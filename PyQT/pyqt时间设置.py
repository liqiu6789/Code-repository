import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTimeEdit, QLabel, QGroupBox
from PyQt5.QtCore import QTime


class TimeEditFormats(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个分组框来包含不同的 QTimeEdit 控件
        group_box = QGroupBox("不同的时间格式")
        group_layout = QVBoxLayout()

        # 定义不同的时间格式
        formats = ['HH:mm', 'hh:mm:ss', 'h:mm ap']

        for format_str in formats:
            # 为每种格式创建一个 QTimeEdit 控件
            time_edit = QTimeEdit()
            time_edit.setDisplayFormat(format_str)
            time_edit.setTime(self.get_random_time())  # 设置一个随机时间

            # 创建一个标签来描述该格式
            label = QLabel(f"格式: {format_str}")

            # 将标签和 QTimeEdit 控件添加到分组框的布局中
            group_layout.addWidget(label)
            group_layout.addWidget(time_edit)

            # 设置分组框的布局
        group_box.setLayout(group_layout)

        # 将分组框添加到主布局中
        layout.addWidget(group_box)

        # 设置窗口的布局
        self.setLayout(layout)

        # 设置窗口的标题和大小
        self.setWindowTitle('QTimeEdit 不同格式示例')
        self.setGeometry(300, 300, 300, 200)

    def get_random_time(self):
        # 返回一个随机时间，用于初始化 QTimeEdit 控件
        from random import randint
        hour = randint(0, 23)
        minute = randint(0, 59)
        second = randint(0, 59)
        return QTime(hour, minute, second)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimeEditFormats()
    ex.show()
    sys.exit(app.exec_())