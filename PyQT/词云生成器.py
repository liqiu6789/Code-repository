import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QPainter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super(MatplotlibCanvas, self).__init__(fig)
        self.setParent(parent)

        self.plot()

    def plot(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 1, 3, 5, 4]
        self.axes.plot(x, y)
        self.draw()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        vbox = QVBoxLayout()

        # 第一部分：横向排列的四个按钮
        hbox1 = QHBoxLayout()
        for i in range(4):
            btn = QPushButton(f'Button {i + 1}')
            hbox1.addWidget(btn)
        vbox.addLayout(hbox1)

        # 第二部分：一个按钮
        btn_single = QPushButton('Single Button')
        vbox.addWidget(btn_single)

        # 第三部分：matplotlib绘制的折线图
        self.canvas = MatplotlibCanvas(self, width=5, height=4, dpi=100)
        vbox.addWidget(self.canvas)

        # 设置窗口属性
        self.setLayout(vbox)
        self.setWindowTitle('PyQt with Matplotlib')
        self.setGeometry(300, 300, 300, 220)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())