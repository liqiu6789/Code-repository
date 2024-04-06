import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个QWidget实例
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # 创建一个QVBoxLayout实例
        layout = QVBoxLayout(self.centralWidget)

        # 创建一个matplotlib的Figure和Axes实例
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # 创建一个matplotlib的canvas，并将其添加到布局中
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        # 生成一些随机数据
        data = np.random.randn(1000)

        # 在Axes上绘制直方图
        self.ax.hist(data, bins=30)

        # 刷新canvas以显示图表
        self.canvas.draw()

        # 设置窗口标题和大小
        self.setWindowTitle('PyQt直方图示例')
        self.setGeometry(300, 300, 800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())