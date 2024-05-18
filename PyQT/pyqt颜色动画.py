from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
        QLabel, QHBoxLayout, QSizePolicy)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty  # 这里添加了pyqtProperty的导入
import sys

# 自定义QLabel类，用于支持通过属性系统改变文本颜色
class MyLabel(QLabel):

    # 初始化方法
    def __init__(self, text):
        super().__init__(text)

        # 私有方法，用于设置颜色

    def _set_color(self, col):
        # 获取当前的调色板
        palette = self.palette()
        # 设置前景色（即文本颜色）
        palette.setColor(self.foregroundRole(), col)
        # 应用新的调色板
        self.setPalette(palette)

        # 使用pyqtProperty装饰器定义color属性，使其可通过QPropertyAnimation访问

    color = pyqtProperty(QColor, fset=_set_color)


# 主窗口类
class Example(QWidget):

    def __init__(self):
        super().__init__()

        # 初始化UI
        self.initUI()

    def initUI(self):
        # 创建一个水平布局
        hbox = QHBoxLayout(self)

        # 创建一个按钮，并添加到布局中
        self.button = QPushButton("Start", self)
        self.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        hbox.addWidget(self.button)

        # 在布局中添加一些间距
        hbox.addSpacing(40)

        # 创建一个自定义标签，并设置字体大小和文本，然后添加到布局中
        self.label = MyLabel("颜色")
        font = self.label.font()
        font.setPointSize(35)
        self.label.setFont(font)
        hbox.addWidget(self.label)

        # 创建一个QPropertyAnimation实例，用于动画化MyLabel的color属性
        self.anim = QPropertyAnimation(self.label, b"color")
        # 设置动画的持续时间
        self.anim.setDuration(1000)
        # 设置动画的循环次数
        self.anim.setLoopCount(6)
        # 设置动画的起始值（颜色）
        self.anim.setStartValue(QColor(0, 0, 0))
        # 设置动画的结束值（颜色）
        self.anim.setEndValue(QColor(255, 0, 0))

        # 连接按钮的clicked信号到动画的start槽
        self.button.clicked.connect(self.anim.start)

        # 设置窗口的几何位置和大小
        self.setGeometry(300, 300, 380, 250)
        # 设置窗口标题
        self.setWindowTitle('Color anim')
        # 显示窗口
        self.show()


if __name__ == "__main__":
    # 创建QApplication实例
    app = QApplication([])
    # 创建Example窗口实例
    ex = Example()
    # 显示窗口
    ex.show()
    # 运行应用程序
    sys.exit(app.exec_())