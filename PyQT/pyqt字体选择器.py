from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFontDialog
from PyQt5.QtGui import QFont


class FontSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体选择器')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('点击按钮选择字体')
        layout.addWidget(self.label)

        self.button = QPushButton('选择字体', self)
        self.button.clicked.connect(self.showFontDialog)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
            print("所选字体：",font.family())


if __name__ == '__main__':
    app = QApplication([])
    ex = FontSelector()
    ex.show()
    app.exec_()