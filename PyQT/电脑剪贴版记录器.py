import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QVBoxLayout, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt, QTimer


class ClipboardMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clipboard = QApplication.clipboard()
        self.clipboard_history = []
        self.setupTimer()

    def initUI(self):
        self.setWindowTitle('剪贴板监控器')
        self.setGeometry(300, 300, 800, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.clear_button = QPushButton('清空历史', self)
        self.clear_button.clicked.connect(self.clearClipboardHistory)
        layout.addWidget(self.clear_button)

    def setupTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkClipboard)
        self.timer.start(500)  # 每500毫秒检查一次剪贴板

    def checkClipboard(self):
        current_content = self.clipboard.text()
        if current_content and current_content not in self.clipboard_history:
            self.clipboard_history.insert(0, current_content)  # 将新内容插入到列表的开始位置
            self.updateUI()

    def updateUI(self):
        # 反转历史列表以展示最新记录在前
        reversed_history = self.clipboard_history[::-1]
        # 使用横线分隔每条记录
        text = "\n---------\n".join(reversed_history)
        text += "\n" * (self.text_edit.height() // self.text_edit.fontMetrics().height())  # 添加空行以尝试填满窗口
        self.text_edit.setText(text)

    def clearClipboardHistory(self):
        self.clipboard_history.clear()
        self.text_edit.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = ClipboardMonitor()
    monitor.show()
    sys.exit(app.exec_())