import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QSpacerItem,QSizePolicy


class SpacerItemExample(QWidget):
    def __init__(self):
        super().__init__()

        # 创建按钮
        button1 = QPushButton("按钮 1")
        button2 = QPushButton("按钮 2")

        # 创建水平布局
        layout = QHBoxLayout()

        # 添加按钮到布局中
        layout.addWidget(button1)

        # 创建一个水平方向的间隔项，固定宽度为 50 像素，高度可以伸缩
        spacer = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        layout.addItem(spacer)

        # 添加第二个按钮到布局中
        layout.addWidget(button2)

        # 在布局的右侧再添加一个伸展的间隔项，以填充剩余空间
        stretch_spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(stretch_spacer)

        # 设置窗口部件的布局
        self.setLayout(layout)

        # 设置窗口部件的标题和大小
        self.setWindowTitle('QSpacerItem 示例')
        self.setGeometry(100, 100, 300, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = SpacerItemExample()
    example.show()
    sys.exit(app.exec_())