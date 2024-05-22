import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QTimer, Qt


class ProgressBarExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt ProgressBar 示例')
        self.setGeometry(300, 300, 300, 200)

        # 创建进度条
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)
        self.progressBar.setValue(0)  # 初始值

        # 创建按钮
        self.button = QPushButton('开始任务', self)
        self.button.setGeometry(100, 80, 100, 30)
        self.button.clicked.connect(self.startTask)

        # 布局（在这个简单示例中，我们使用绝对定位，但在复杂的应用中建议使用布局）

        # 显示窗口
        self.show()

    def startTask(self):
        # 禁用按钮以防止多次点击
        self.button.setDisabled(True)

        # 初始化计数器
        self.counter = 0

        # 设置进度条的范围
        self.progressBar.setRange(0, 100)

        # 使用定时器来模拟任务进度
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(100)  # 每100毫秒更新一次进度

    def updateProgress(self):
        self.counter += 1
        self.progressBar.setValue(self.counter)

        # 当进度达到100时，停止定时器并启用按钮
        if self.counter >= 100:
            self.timer.stop()
            self.button.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProgressBarExample()
    sys.exit(app.exec_())