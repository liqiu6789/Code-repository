import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QColor

class RainbowClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Rainbow Digital Clock')
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.time_layout = QHBoxLayout()
        self.time_layout.setSpacing(0)  # 设置标签之间的间距为0

        self.hour_label = QLabel(self)
        self.hour_label.setAlignment(Qt.AlignCenter)
        self.hour_label.setStyleSheet("font-size: 48px;")

        self.colon1_label = QLabel(self)
        self.colon1_label.setAlignment(Qt.AlignCenter)
        self.colon1_label.setStyleSheet("font-size: 48px;")
        self.colon1_label.setText(":")

        self.minute_label = QLabel(self)
        self.minute_label.setAlignment(Qt.AlignCenter)
        self.minute_label.setStyleSheet("font-size: 48px;")

        self.colon2_label = QLabel(self)
        self.colon2_label.setAlignment(Qt.AlignCenter)
        self.colon2_label.setStyleSheet("font-size: 48px;")
        self.colon2_label.setText(":")

        self.second_label = QLabel(self)
        self.second_label.setAlignment(Qt.AlignCenter)
        self.second_label.setStyleSheet("font-size: 48px;")

        self.time_layout.addWidget(self.hour_label)
        self.time_layout.addWidget(self.colon1_label)
        self.time_layout.addWidget(self.minute_label)
        self.time_layout.addWidget(self.colon2_label)
        self.time_layout.addWidget(self.second_label)

        layout.addLayout(self.time_layout)
        layout.setAlignment(Qt.AlignCenter)  # 居中对齐

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        current_time = QTime.currentTime()
        hour = current_time.toString('hh')
        minute = current_time.toString('mm')
        second = current_time.toString('ss')

        # Generate random colors for hour, minute, and second
        hour_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        minute_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        second_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.hour_label.setText(hour)
        self.hour_label.setStyleSheet(f"font-size: 48px; color: {hour_color.name()};")

        self.minute_label.setText(minute)
        self.minute_label.setStyleSheet(f"font-size: 48px; color: {minute_color.name()};")

        self.second_label.setText(second)
        self.second_label.setStyleSheet(f"font-size: 48px; color: {second_color.name()};")

        # Colon colors
        self.colon1_label.setStyleSheet(f"font-size: 48px; color: #000000;")
        self.colon2_label.setStyleSheet(f"font-size: 48px; color: #000000;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RainbowClockWindow()
    window.show()
    sys.exit(app.exec_())
