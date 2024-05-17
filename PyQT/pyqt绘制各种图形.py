import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QFont, QPolygonF  # 导入 QPolygonF
from PyQt5.QtCore import Qt, QPoint, QPointF, QRect


class DrawShapesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Draw Shapes with PyQt')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rectangle(qp)
        self.draw_ellipse(qp)
        self.draw_polygon(qp)
        self.draw_text(qp)
        qp.end()

    def draw_rectangle(self, qp):
        # 绘制一个矩形
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        qp.drawRect(50, 50, 100, 50)  # 矩形的左上角坐标和宽度、高度

    def draw_ellipse(self, qp):
        # 绘制一个椭圆
        pen = QPen(Qt.blue, 2)
        qp.setPen(pen)
        qp.setBrush(QBrush(QColor(200, 200, 255, 100)))  # 设置填充颜色和透明度
        qp.drawEllipse(180, 50, 100, 50)  # 椭圆的左上角坐标和宽度、高度

    def draw_polygon(self, qp):
        # 绘制一个多边形
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)
        qp.setBrush(QBrush(QColor(255, 100, 100)))  # 设置填充颜色
        points = [QPointF(50, 100), QPointF(100, 150), QPointF(150, 100)]  # 多边形的顶点
        qp.drawPolygon(QPolygonF(points))

    def draw_text(self, qp):
        # 绘制文本
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        font = QFont("Arial", 12)  # 设置字体
        qp.setFont(font)
        qp.drawText(50, 170, "Hello, PyQt!")  # 文本的起始位置和文本内容


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawShapesWidget()
    sys.exit(app.exec_())