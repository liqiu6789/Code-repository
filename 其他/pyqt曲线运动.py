# 导入必要的PyQt5模块
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPainterPath
from PyQt5.QtCore import QObject, QPointF, QPropertyAnimation, pyqtProperty
import sys


# 自定义的Ball类，继承自QLabel
class Ball(QLabel):
    def __init__(self, parent):
        super().__init__(parent)  # 调用父类QLabel的构造函数

        # 加载图片并设置到QLabel上
        pix = QPixmap("car.png")
        self.h = pix.height()  # 图片的高度
        self.w = pix.width()  # 图片的宽度
        self.setPixmap(pix)

        # 自定义setter方法，用于更新Ball的位置

    def _set_pos(self, pos):
        # 移动QLabel到新的位置，考虑图片的中心点
        self.move(int(pos.x() - self.w / 2), int(pos.y() - self.h / 2))

        # 使用pyqtProperty将_set_pos方法包装为一个属性，以便与Qt属性系统兼容

    pos = pyqtProperty(QPointF, fset=_set_pos)


# 自定义的Example类，继承自QWidget
class Example(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget的构造函数

        # 初始化视图和动画
        self.initView()
        self.initAnimation()

        # 初始化视图

    def initView(self):
        # 创建一个QPainterPath对象，并设置其路径
        self.path = QPainterPath()
        self.path.moveTo(30, 30)
        self.path.cubicTo(30, 30, 200, 350, 350, 30)

        # 创建一个Ball对象，并添加到当前窗口上
        self.ball = Ball(self)

        # 设置Ball的初始位置（这里虽然直接设置了属性，但它是通过pyqtProperty定义的，所以没有问题）
        self.ball.pos = QPointF(30, 30)

        # 设置窗口标题和大小，并显示窗口
        self.setWindowTitle("Animation along curve")
        self.setGeometry(300, 300, 400, 300)
        self.show()

        # 重写paintEvent方法，用于绘制QPainterPath

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)  # 开始绘制
        qp.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿渲染
        qp.drawPath(self.path)  # 绘制QPainterPath
        qp.end()  # 结束绘制

    # 初始化动画
    def initAnimation(self):
        # 创建一个QPropertyAnimation对象，用于动画化Ball的pos属性
        self.anim = QPropertyAnimation(self.ball, b'pos')
        self.anim.setDuration(7000)  # 设置动画时长为7000毫秒（7秒）

        # 设置动画的起始值
        self.anim.setStartValue(QPointF(30, 30))

        # 创建一个列表，用于计算贝塞尔曲线上的点
        vals = [p / 100 for p in range(0, 101)]

        # 为动画设置关键帧值
        for i in vals:
            self.anim.setKeyValueAt(i, self.path.pointAtPercent(i))

            # 设置动画的结束值（虽然在这里设置了，但实际上由于关键帧的存在，这个值可能不会被直接使用）
        self.anim.setEndValue(QPointF(350, 30))
        self.anim.start()  # 开始动画


# 主程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象
    ex = Example()  # 创建Example对象（即主窗口）
    sys.exit(app.exec_())  # 进入Qt的事件循环，等待用户操作，直到应用程序关闭