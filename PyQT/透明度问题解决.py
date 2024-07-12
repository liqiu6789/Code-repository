import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QColorDialog, QSlider, QWidget, QPushButton, QDockWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QMouseEvent
from PyQt5.QtCore import Qt

class DrawingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Drawing with PyQt5')

        self.drawing_widget = DrawingWidget(self)
        self.setCentralWidget(self.drawing_widget)

        self.color_button = QPushButton('Choose Color', self)
        self.color_button.clicked.connect(self.choose_color)

        self.alpha_slider = QSlider(Qt.Horizontal, self)
        self.alpha_slider.setRange(0, 255)
        self.alpha_slider.setValue(255)
        self.alpha_slider.valueChanged.connect(self.change_alpha)

        layout = QVBoxLayout()
        layout.addWidget(self.color_button)
        layout.addWidget(self.alpha_slider)
        container = QWidget()
        container.setLayout(layout)

        dock_widget = QDockWidget("Tools", self)
        dock_widget.setWidget(container)
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)

        self.show()

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.drawing_widget.set_pen_color(color)

    def change_alpha(self, value):
        self.drawing_widget.set_pen_alpha(value)

class DrawingWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.pen_color = QColor(0, 0, 0, 255)
        self.pen = QPen(self.pen_color, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.drawing = False
        self.last_point = None
        self.image = None

    def set_pen_color(self, color):
        self.pen_color = QColor(color.red(), color.green(), color.blue(), self.pen_color.alpha())
        self.pen.setColor(self.pen_color)

    def set_pen_alpha(self, alpha):
        self.pen_color.setAlpha(alpha)
        self.pen.setColor(self.pen_color)

    def paintEvent(self, event):
        if self.image is None:
            self.image = self.grab().toImage()
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
        if self.drawing and self.last_point:
            painter.setPen(self.pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing and event.buttons() & Qt.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(self.pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.last_point = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingWindow()
    sys.exit(app.exec_())
