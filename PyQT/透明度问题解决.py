from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
import cv2
import numpy as np

class WorkThread(QThread):
    my_signal = pyqtSignal()

    def __init__(self):
        super(WorkThread, self).__init__()
        self.image_path = []

    def run(self):
        # 模拟一个工作线程，在完成后发出信号
        import time
        time.sleep(5)  # 模拟长时间操作
        self.my_signal.emit()

class Label(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)
        self.thread = WorkThread()
        self.thread.my_signal.connect(self.timeStop)
        self.drawing = False
        self.drawing1 = True
        self.lastPoint = QPoint()
        self.image_path = "img.png"
        self.thread.image_path = [self.image_path]
        self.image_cv = cv2.imread(self.image_path)
        self.image = QPixmap(self.image_path)
        self.pen_size = 20
        self.pen_color = QColor(255, 0, 0, 76)  # 红色，透明度为 30%
        self.temp_image = QPixmap(self.image.size())
        self.temp_image.fill(Qt.transparent)
        self.lastPoint = QPoint()

    def timeStop(self):
        # 处理线程结束后的操作
        print("Thread finished")

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(QtCore.QPoint(0, 0), self.image.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        painter.drawPixmap(QtCore.QPoint(0, 0), self.temp_image.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True

            x = event.pos().x()
            y = event.pos().y()
            scale = self.height() / self.image.height()
            x0 = int(x / scale)
            y0 = int(y / scale)
            self.lastPoint = QPoint(x0, y0)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing and self.drawing1:
            x = event.pos().x()
            y = event.pos().y()
            scale = self.height() / self.image.height()
            x0 = int(x / scale)
            y0 = int(y / scale)
            self.nowPoint = QPoint(x0, y0)

            # 清空临时图像
            self.temp_image.fill(Qt.transparent)

            # 在临时图像上绘制轮廓
            painter = QPainter(self.temp_image)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setPen(QPen(self.pen_color, self.pen_size, Qt.SolidLine))
            painter.drawEllipse(self.nowPoint, int(self.pen_size / 2) + 1, int(self.pen_size / 2) + 1)
            self.lastPoint = self.nowPoint

            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

            # 将临时图像的内容合并到主图像
            painter = QPainter(self.image)
            painter.drawPixmap(0, 0, self.temp_image)
            self.update()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    label = Label()
    label.show()
    sys.exit(app.exec_())
