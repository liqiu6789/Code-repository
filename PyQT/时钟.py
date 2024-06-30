import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt

class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 48px;")

        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClockWindow()
    window.show()
    sys.exit(app.exec_())
