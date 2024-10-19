import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QFontMetrics, QFont
from PyQt5.QtCore import Qt, QTimer


class MovingRectangle(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moving Rectangle')
        self.setGeometry(300, 300, 640, 480)

        # 设置矩形的初始位置
        self.rect_pos = 0
        # 创建一个定时器，每50毫秒调用move_rectangle方法
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_rectangle)
        self.timer.start(50)  # 每50毫秒移动一次

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 反锯齿效果

        # 绘制红色矩形
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QBrush(Qt.red))
        painter.drawRect(self.rect_pos, 100, 100, 100)

        # 绘制白色数字 "1"
        font = QFont()
        font.setPixelSize(50)  # 设置字体大小
        painter.setFont(font)
        painter.setPen(Qt.white)

        # 获取字体的度量信息
        fm = QFontMetrics(font)
        # 计算文本宽度和高度
        text_width = fm.horizontalAdvance("1")
        text_height = fm.height()

        # 计算文本在矩形内的居中位置
        # 矩形的中心点
        rect_center_x = self.rect_pos + 50
        rect_center_y = 125

        # 文本的中心点相对于矩形中心的位置
        text_center_x = rect_center_x - (text_width / 2)
        text_center_y = rect_center_y + fm.ascent()  # 垂直居中对齐

        # 在矩形中心绘制文本
        painter.drawText(int(text_center_x), int(text_center_y), '1')

    def move_rectangle(self):
        # 更新矩形的位置
        self.rect_pos += 10
        if self.rect_pos > self.width():
            # 如果矩形的右侧超出了窗口的宽度，则将它移回左侧
            self.rect_pos = -100
        self.update()  # 强制重绘窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MovingRectangle()
    ex.show()
    sys.exit(app.exec_())