import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QTimer


class ProgressBarDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 进度条示例')
        self.setGeometry(300, 300, 250, 150)
        self.layout = QVBoxLayout()
        # 创建进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        # 创建按钮来开始进度
        self.btn = QPushButton('开始', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)

        self.layout.addWidget(self.pbar)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100)  # 设置定时器每隔100ms触发一次
            self.btn.setText('停止')

    def updateProgress(self):
        value = self.pbar.value() + 1
        self.pbar.setValue(value)

        if value == 100:
            self.timer.stop()
            self.btn.setText('开始')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ProgressBarDemo()
    demo.show()
    sys.exit(app.exec_())