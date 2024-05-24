import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QPointF
import numpy as np

class HeartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Heart Shape with PyQt5')
        self.setGeometry(100, 100, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Generate heart shape coordinates
        t = np.linspace(0, 2 * np.pi, 1000)
        x = 16 * np.sin(t)**3
        y = -(13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))

        # Normalize coordinates
        x = (x - min(x)) / (max(x) - min(x)) * self.width()
        y = (y - min(y)) / (max(y) - min(y)) * self.height()

        # Set gradient colors
        colors = [QColor.fromHsvF(i / len(t), 1.0, 1.0) for i in range(len(t))]

        # Draw heart shape
        for i in range(len(t) - 1):
            painter.setPen(QPen(colors[i], 2))
            painter.drawLine(QPointF(x[i], y[i]), QPointF(x[i + 1], y[i + 1]))

        # Fill heart shape with gradient colors
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.SolidPattern))
        for i in range(len(t) - 1):
            painter.setBrush(QBrush(colors[i]))
            painter.drawPolygon(QPointF(x[i], y[i]), QPointF(x[i + 1], y[i + 1]), QPointF(self.width() / 2, self.height() / 2))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Heart Shape with PyQt5')
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(HeartWidget())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
