from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit
import sys
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个 QDockWidget 实例
        dock = QDockWidget("Dockable", self)

        # 在 QDockWidget 中创建一个文本编辑器控件
        text_edit = QTextEdit()
        dock.setWidget(text_edit)

        # 将 QDockWidget 添加到 QMainWindow 的左侧停靠区
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        # 设置主窗口的大小和标题
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('QDockWidget Example')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())