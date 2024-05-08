from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QColor


class Example(QWidget):
    """
    一个示例类，继承自QWidget，用于展示一个简单的动画效果。
    """

    def __init__(self):
        """
        构造函数，初始化QWidget并调用initUI方法。
        """
        super().__init__()  # 调用父类QWidget的构造函数

        self.initUI()  # 初始化UI

    def initUI(self):
        """
        初始化UI，包括按钮、框架以及设置窗口的基本属性。
        """
        self.button = QPushButton("Start", self)  # 创建一个QPushButton对象，文本为"Start"，父对象为self
        self.button.clicked.connect(self.doAnim)  # 将按钮的clicked信号连接到doAnim槽函数
        self.button.move(30, 30)  # 移动按钮到指定位置

        self.frame = QFrame(self)  # 创建一个QFrame对象，父对象为self
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)  # 设置框架的样式为面板且凸起
        self.frame.setStyleSheet("QFrame { background-color: blue; }")  # 设置框架的背景色为蓝色
        self.frame.setGeometry(QRect(150, 30, 100, 100))  # 设置框架的初始位置和大小

        self.setGeometry(300, 300, 380, 300)  # 设置窗口的初始位置和大小
        self.setWindowTitle('Animation')  # 设置窗口的标题为"Animation"
        self.show()  # 显示窗口

    def doAnim(self):
        """
        定义动画效果，包括创建动画对象、设置动画参数以及启动动画。
        """
        self.anim = QPropertyAnimation(self.frame,
                                       b"geometry")  # 创建一个QPropertyAnimation对象，用于对self.frame的geometry属性进行动画处理
        self.anim.setDuration(1000)  # 设置动画的持续时间为1000毫秒（1秒）
        self.anim.setStartValue(QRect(150, 30, 100, 100))  # 设置动画开始时的值为初始位置和大小
        # 注释了放大的代码，改为缩小
        # self.anim.setEndValue(QRect(150, 30, 200, 200))  # 如果要放大，可以取消注释这行代码，注释下面的缩小代码
        self.anim.setEndValue(QRect(150, 30, 50, 50))  # 设置动画结束时的值为缩小后的位置和大小
        self.anim.start()  # 启动动画


if __name__ == "__main__":
    app = QApplication([])  # 创建一个QApplication对象，作为整个应用程序的入口
    ex = Example()  # 创建一个Example对象，即主窗口
    ex.show()  # 显示主窗口
    app.exec_()  # 进入应用程序的主事件循环，等待用户操作或程序结束