import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        btn1 = QPushButton('Button 1', self)
        btn1.clicked.connect(self.on_button1_clicked)
        btn2 = QPushButton('Button 2', self)
        btn2.clicked.connect(self.on_button2_clicked)

        # 创建水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        # 设置窗口布局
        self.setLayout(hbox)

        # 设置窗口标题和大小
        self.setWindowTitle('Buttons in Horizontal Layout')
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def on_button1_clicked(self):
        print('Button 1 clicked')

    def on_button2_clicked(self):
        print('Button 2 clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())