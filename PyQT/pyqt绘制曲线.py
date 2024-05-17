import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QColor, QBrush
from PyQt5.QtCore import Qt, QPoint, QRectF


class DrawCurvesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Draw Curves with PyQt')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_arc(qp)
        self.draw_ellipse(qp)
        self.draw_bezier_curve(qp)
        qp.end()

    def draw_arc(self, qp):
        # 绘制一个圆弧
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        qp.drawArc(50, 50, 100, 100, 0, 180 * 16)  # 起始角度为0度，跨越180度

    def draw_ellipse(self, qp):
        # 绘制一个椭圆
        pen = QPen(Qt.blue, 2)
        qp.setPen(pen)
        qp.setBrush(QBrush(QColor(200, 200, 255, 100)))  # 设置填充颜色和透明度
        qp.drawEllipse(180, 50, 100, 50)  # 椭圆的位置和大小

    def draw_bezier_curve(self, qp):
        # 绘制一个二次贝塞尔曲线
        path = QPainterPath()
        path.moveTo(50, 150)  # 起始点
        path.quadTo(150, 50, 250, 150)  # 控制点和结束点
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)
        qp.drawPath(path)

        # 绘制一个三次贝塞尔曲线
        path = QPainterPath()
        path.moveTo(50, 170)  # 起始点
        path.cubicTo(100, 10, 200, 100, 250, 170)  # 两个控制点和结束点
        qp.setPen(QPen(Qt.green, 2))
        qp.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCurvesWidget()
    sys.exit(app.exec_())