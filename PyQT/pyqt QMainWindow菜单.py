import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu, QMessageBox


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个菜单栏
        menubar = self.menuBar()

        # 创建一个文件菜单
        fileMenu = menubar.addMenu('File')

        # 创建一个退出动作
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.on_exit)

        # 将退出动作添加到文件菜单
        fileMenu.addAction(exitAction)

        # 设置窗口的标题和大小
        self.setWindowTitle('QMainWindow Menu Example')
        self.setGeometry(300, 300, 300, 200)

        # 显示窗口
        self.show()

    def on_exit(self):
        # 弹出一个确认对话框
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())