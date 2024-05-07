import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个工具栏
        self.toolbar = QToolBar("My Toolbar")

        # 创建一些动作
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)

        # 将动作添加到工具栏
        self.toolbar.addAction(new_action)
        self.toolbar.addAction(open_action)
        self.toolbar.addAction(save_action)

        # 将工具栏添加到主窗口
        self.addToolBar(self.toolbar)

        # 设置主窗口的大小和标题
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("QToolBar Example")

    def new_file(self):
        print("New file action triggered!")

    def open_file(self):
        print("Open file action triggered!")

    def save_file(self):
        print("Save file action triggered!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())