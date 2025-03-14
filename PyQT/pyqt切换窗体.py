import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, \
    QDockWidget, QListWidget, QListWidgetItem,QFrame
from PyQt5.QtCore import Qt


class SubWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        layout = QVBoxLayout()
        label = QLabel(f"This is the {title} window.")
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置主窗口的背景颜色
        self.setStyleSheet("QMainWindow { background-color: lightgray; }")

        # 创建中心堆叠窗口部件
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        # 创建子窗体并添加到堆叠部件中
        self.subWindow1 = SubWindow("Window 1")
        self.subWindow2 = SubWindow("Window 2")
        self.stackedWidget.addWidget(self.subWindow1)
        self.stackedWidget.addWidget(self.subWindow2)

        # 创建侧边栏的框架
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(1)
        self.frame.setGeometry(30, 30, 150, 300)  # 设置框架的位置和大小

        # 创建菜单列表
        self.listWidget = QListWidget()
        self.listWidget.addItem('Window 1')
        self.listWidget.addItem('Window 2')
        self.listWidget.itemClicked.connect(self.on_listwidget_item_clicked)  # 连接信号到槽

        # 设置侧边栏的布局
        dockLayout = QVBoxLayout()
        dockLayout.addWidget(self.listWidget)

        frameContents = QWidget()
        frameContents.setLayout(dockLayout)
        self.frame.setLayout(dockLayout)  # 将布局设置到框架中

        # 设置窗口的标题和大小
        self.setWindowTitle('Menu with Windows')
        self.setGeometry(300, 300, 600, 400)

    def on_listwidget_item_clicked(self, item):
        # 当菜单项被点击时，切换到对应的子窗体
        index = self.listWidget.row(item)
        self.stackedWidget.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())