import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt


class SliderDemo(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化布局和标签
        self.initUI()

    def initUI(self):
        # 创建布局
        vbox = QVBoxLayout()

        # 创建水平滑块
        self.hslider = QSlider(Qt.Horizontal)
        self.hslider.setMinimum(0)
        self.hslider.setMaximum(100)
        self.hslider.setValue(50)
        self.hslider.valueChanged[int].connect(self.on_hslider_value_changed)

        # 创建标签来显示水平滑块的值
        self.hlabel = QLabel("Horizontal Slider: 50")

        # 添加到布局
        vbox.addWidget(self.hslider)
        vbox.addWidget(self.hlabel)

        # 创建垂直滑块
        self.vslider = QSlider(Qt.Vertical)
        self.vslider.setMinimum(0)
        self.vslider.setMaximum(100)
        self.vslider.setValue(50)
        self.vslider.valueChanged[int].connect(self.on_vslider_value_changed)

        # 创建标签来显示垂直滑块的值
        self.vlabel = QLabel("Vertical Slider: 50")

        # 添加到布局
        vbox.addWidget(self.vslider)
        vbox.addWidget(self.vlabel)

        # 设置窗口的布局
        self.setLayout(vbox)

        # 设置窗口的标题和大小
        self.setWindowTitle('Slider Demo')
        self.setGeometry(300, 300, 300, 200)

        # 水平滑块值改变的槽函数

    def on_hslider_value_changed(self, value):
        self.hlabel.setText(f"Horizontal Slider: {value}")

        # 垂直滑块值改变的槽函数

    def on_vslider_value_changed(self, value):
        self.vlabel.setText(f"Vertical Slider: {value}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SliderDemo()
    ex.show()
    sys.exit(app.exec_())