import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont,QPen
from PyQt5.QtCore import Qt


class WatermarkedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Watermarked Window')
        self.setGeometry(100, 100, 400, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置水印文本和字体
        watermark_text = "WATERMARK"
        font = QFont()
        font.setPointSize(20)
        font.setItalic(True)
        font.setWeight(QFont.Light)
        painter.setFont(font)

        # 设置水印颜色（通常为半透明）
        color = QColor(0, 0, 0, 128)  # RGB(0, 0, 0) with alpha 128 (50% opacity)
        painter.setPen(QPen(color))

        # 绘制水印（可能需要调整位置和角度以使其看起来像水印）
        width, height = self.width(), self.height()
        tilt = 45  # 水印文本的倾斜角度（可选）
        for i in range(5):  # 绘制多个水印以增加效果
            for j in range(5):
                x = i * (width // 6) - width // 10
                y = j * (height // 6) - height // 10
                painter.save()  # 保存当前状态
                painter.translate(x, y)  # 移动到指定位置
                painter.rotate(tilt)  # 旋转文本（可选）
                painter.drawText(0, font.pointSize(), watermark_text)  # 绘制文本
                painter.restore()  # 恢复之前保存的状态

        # 如果有其他绘制内容，可以在这里添加


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WatermarkedWindow()
    ex.show()
    sys.exit(app.exec_())