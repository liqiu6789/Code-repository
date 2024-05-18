import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QScreen
from PyQt5.QtCore import Qt, QRect


class CenteredWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口的标题和大小
        self.setWindowTitle('Centered Window')
        self.setGeometry(self.getScreenCenterGeometry(800, 600))  # 800x600 大小的窗口

    def getScreenCenterGeometry(self, width, height):
        # 获取主屏幕
        screen = QApplication.primaryScreen()

        # 获取屏幕的几何尺寸
        screen_rect = screen.geometry()

        # 计算窗口在屏幕上的中心位置
        x = (screen_rect.width() - width) // 2
        y = (screen_rect.height() - height) // 2

        # 返回包含位置和大小的矩形
        return QRect(x, y, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个居中的窗口实例
    window = CenteredWindow()

    # 显示窗口
    window.show()

    # 运行应用
    sys.exit(app.exec_())