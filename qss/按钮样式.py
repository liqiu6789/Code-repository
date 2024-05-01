import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt


class CenteredButton(QWidget):
    def __init__(self):
        super().__init__()

        # 创建一个按钮
        self.button = QPushButton('Click Me', self)

        # 使用水平布局并添加伸缩因子来实现居中
        layout = QHBoxLayout(self)
        layout.addStretch(1)  # 在按钮左边添加伸缩因子
        layout.addWidget(self.button)  # 添加按钮
        layout.addStretch(1)  # 在按钮右边添加伸缩因子

        # 设置窗口的布局
        self.setLayout(layout)

        # 设置窗口的标题和大小
        self.setWindowTitle('Centered Button')
        self.setGeometry(600, 300, 400, 300)  # x, y, width, height
        # QSS 样式
        style_sheet = """  
        QPushButton {  
            /* 基本设置 */  
            background-color: #4CAF50; /* 绿色背景 */  
            color: white; /* 白色文字 */  
            border: none; /* 无边框 */  
            border-radius: 5px; /* 边框圆角 */  
            padding: 10px 20px; /* 内边距 */  
            font-size: 16px; /* 字体大小 */  
            font-family: "Arial"; /* 字体类型，使用 Arial 或其他你想要的字体 */  
            font-weight: bold; /* 加粗效果 */  
            transition: background-color 0.3s ease-in-out; /* 平滑过渡效果 */  
        }  

        QPushButton:hover {  
            /* 鼠标悬停效果 */  
            background-color: #45a049; /* 更深的绿色背景 */  
        }  

        /* 注意：QPushButton:pressed 的样式需要编程实现 */  
        """

        # 应用样式表
        self.button.setStyleSheet(style_sheet)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    centered_button = CenteredButton()
    centered_button.show()
    sys.exit(app.exec_())