import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        # 调用父类QMainWindow的构造函数
        super().__init__()

        # 调用initUI方法初始化UI
        self.initUI()

    def initUI(self):
        # 设置窗口的标题
        self.setWindowTitle('拖入txt文档并显示内容')
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 600, 400)

        # 创建一个QTextEdit部件，并设置它为只读
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        # 将QTextEdit部件设置为窗口的中心部件
        self.setCentralWidget(self.text_edit)

        # 启用窗口部件的拖放功能
        self.setAcceptDrops(True)

        # 重写dragEnterEvent方法，当鼠标拖拽进入窗口时触发

    def dragEnterEvent(self, event):
        # 检查拖放的数据中是否包含URLs
        if event.mimeData().hasUrls():
            # 如果包含，则接受提议的操作（例如复制或移动）
            event.acceptProposedAction()

            # 重写dropEvent方法，当鼠标释放拖拽的数据到窗口时触发

    def dropEvent(self, event):
        # 从拖放事件中获取URLs
        urls = event.mimeData().urls()
        if urls:
            # 遍历所有拖放的URLs
            for url in urls:
                # 检查URL是否是本地文件
                if url.isLocalFile():
                    # 获取文件的本地路径
                    file_path = url.toLocalFile()
                    # 检查文件是否是txt文档
                    if file_path.endswith('.txt'):
                        try:
                            # 以utf-8编码打开文件并读取内容
                            with open(file_path, 'r', encoding='utf-8') as file:
                                content = file.read()
                                # 将读取的内容设置到QTextEdit部件中
                                self.text_edit.setText(content)
                        except Exception as e:
                            # 如果读取文件时出现异常，打印错误信息
                            print(f"Error reading file: {e}")
                    else:
                        # 如果文件不是txt文档，打印不支持的文件类型信息
                        print(f"Unsupported file type: {file_path}")

                    # 检查当前脚本是否作为主程序运行


if __name__ == '__main__':
    # 创建一个QApplication对象，它是所有PyQt5应用的核心
    app = QApplication(sys.argv)
    # 创建一个MainWindow对象
    window = MainWindow()
    # 显示窗口
    window.show()
    # 进入应用的主事件循环，等待用户操作
    sys.exit(app.exec_())