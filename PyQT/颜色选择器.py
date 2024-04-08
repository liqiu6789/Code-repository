import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QColorDialog


class ColorChooserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()

        # 创建按钮
        self.button = QPushButton('选择颜色')
        self.button.clicked.connect(self.showColorDialog)

        # 将按钮添加到布局中
        layout.addWidget(self.button)

        # 设置窗口的布局
        self.setLayout(layout)

        # 设置窗口的标题和大小
        self.setWindowTitle('颜色选择器')
        self.setGeometry(300, 300, 200, 100)

    def showColorDialog(self):
        # 显示颜色选择器对话框
        color = QColorDialog.getColor()

        # 如果用户选择了颜色（未点击取消），则更新按钮的样式
        if color.isValid():
            self.button.setStyleSheet(f"QPushButton {{ background-color: {color.name()}; }}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorChooserApp()
    ex.show()
    sys.exit(app.exec_())