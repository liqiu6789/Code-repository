import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer


class StickFigureWalking(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Stick Figure Walking Animation')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(100)  # Update every 100 milliseconds
        self.position = 50
        self.walking_phase = 0
        self.show()

    def update_animation(self):
        self.position += 5
        if self.position > self.width():
            self.position = 0
        self.walking_phase = (self.walking_phase + 1) % 4
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)

        # Draw the head
        painter.drawEllipse(self.position, 50, 20, 20)

        # Draw the body
        painter.drawLine(self.position + 10, 70, self.position + 10, 120)

        # Draw the arms
        if self.walking_phase in [0, 2]:
            # Arms up and down
            painter.drawLine(self.position + 10, 80, self.position, 100)
            painter.drawLine(self.position + 10, 80, self.position + 20, 100)
        else:
            # Arms in alternate positions
            painter.drawLine(self.position + 10, 80, self.position + 20, 90)
            painter.drawLine(self.position + 10, 80, self.position, 90)

        # Draw the legs
        if self.walking_phase == 0:
            painter.drawLine(self.position + 10, 120, self.position, 150)
            painter.drawLine(self.position + 10, 120, self.position + 20, 150)
        elif self.walking_phase == 1:
            painter.drawLine(self.position + 10, 120, self.position + 10, 150)
            painter.drawLine(self.position + 10, 120, self.position + 20, 140)
        elif self.walking_phase == 2:
            painter.drawLine(self.position + 10, 120, self.position + 20, 150)
            painter.drawLine(self.position + 10, 120, self.position, 150)
        else:
            painter.drawLine(self.position + 10, 120, self.position + 10, 150)
            painter.drawLine(self.position + 10, 120, self.position, 140)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StickFigureWalking()
    sys.exit(app.exec_())
