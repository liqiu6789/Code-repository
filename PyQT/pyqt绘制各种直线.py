import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QPainterPath, QColor, QBrush
from PyQt5.QtCore import Qt, QPoint, QLineF, QPointF


class DrawLinesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Draw Lines with PyQt')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_straight_line(qp)
        self.draw_wavy_line(qp)
        self.draw_dashed_line(qp)
        qp.end()

    def draw_straight_line(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(10, 50, 280, 50)

    def draw_wavy_line(self, qp):
        path = QPainterPath()
        path.moveTo(50, 100)
        for i in range(10):
            x = 50 + i * 20
            y = 100 + 10 * (-1) ** i
            path.cubicTo(x, y, x + 10, y + 10, x + 20, y)
        qp.setPen(QPen(Qt.blue, 2))
        qp.drawPath(path)

    def draw_dashed_line(self, qp):
        pen = QPen(Qt.red, 2, Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(10, 150, 280, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawLinesWidget()
    sys.exit(app.exec_())