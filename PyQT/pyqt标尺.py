import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, \
    QGraphicsTextItem,QGraphicsLineItem
from PyQt5.QtGui import QPen, QFont
from PyQt5.QtCore import Qt, QPointF


class RulerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('标尺')
        self.setGeometry(300, 300, 800, 600)

        # 创建 QGraphicsScene 和 QGraphicsView
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)

        # 创建标尺线
        self.drawRuler()

        # 设置布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.view)

    def drawRuler(self):
        # 设置标尺的单位长度和数量
        unit_length = 20
        num_units = 30
        long_tick_interval = 5  # 长刻度的间隔（每隔几个单位长度）

        # 创建画笔
        pen = QPen(Qt.black, 1)

        # 创建主标尺线
        main_line = QGraphicsLineItem(0, 0, 800, 0)
        main_line.setPen(pen)
        self.scene.addItem(main_line)

        # 在场景中添加标尺刻度线
        for i in range(num_units + 1):  # +1 是为了包括最后一个单位
            if i % long_tick_interval == 0:
                # 长刻度线
                long_tick = QGraphicsLineItem(0, i * unit_length, 10, i * unit_length)
                long_tick.setPen(pen)
                self.scene.addItem(long_tick)
                # 添加数字标签
                text_item = QGraphicsTextItem(str(i * unit_length))  # 创建文本项
                text_item.setFont(QFont("Arial", 8))
                text_item.setPos(20, i * unit_length)  # 设置文本项的位置
                self.scene.addItem(text_item)
            else:
                # 小刻度线
                short_tick = QGraphicsLineItem(0, i * unit_length, 5, i * unit_length)
                short_tick.setPen(pen)
                self.scene.addItem(short_tick)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RulerWindow()
    ex.show()
    sys.exit(app.exec_())