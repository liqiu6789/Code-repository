from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout


class MyLabelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个 QVBoxLayout
        layout = QVBoxLayout(self)

        # 创建一个 QLabel
        self.label = QLabel('Hello, PyQt!', self)

        # 设置 QLabel 的 QSS 样式
        self.label.setStyleSheet("""  
            QLabel {
                font-family: "Arial";          /* 字体类型 */    
                font-size: 20px;          /* 字体大小 */  
                color: #FF0000;          /* 字体颜色 */  
                background-color: #EEEEEE; /* 背景颜色 */  
                padding: 10px;           /* 内边距 */  
                border: 2px solid #000000; /* 边框 */  
                border-radius: 5px;      /* 边框圆角 */  
            }  
        """)

        # 将 QLabel 添加到布局中
        layout.addWidget(self.label)

        # 设置窗口标题和大小
        self.setWindowTitle('QLabel QSS Example')
        self.setGeometry(300, 300, 250, 150)


if __name__ == '__main__':
    app = QApplication([])
    ex = MyLabelWidget()
    ex.show()
    app.exec_()