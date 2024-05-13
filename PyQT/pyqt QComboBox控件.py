import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建垂直布局
        vbox = QVBoxLayout()

        # 创建 QComboBox 控件
        self.comboBox = QComboBox(self)

        # 添加项目到 QComboBox
        self.comboBox.addItem("选项1")
        self.comboBox.addItem("选项2")
        self.comboBox.addItem("选项3")

        # 创建一个标签来显示当前选中的项目
        self.label = QLabel("选择一个选项", self)

        # 连接 currentIndexChanged 信号到 on_combobox_changed 槽函数
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)

        # 将控件添加到布局中
        vbox.addWidget(self.comboBox)
        vbox.addWidget(self.label)

        # 设置窗口的布局
        self.setLayout(vbox)

        # 设置窗口的标题和大小
        self.setWindowTitle('QComboBox 示例')
        self.setGeometry(300, 300, 250, 150)

    def on_combobox_changed(self, index):
        # 当 QComboBox 的当前索引改变时，更新标签的文本
        self.label.setText("你选择了: " + self.comboBox.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())