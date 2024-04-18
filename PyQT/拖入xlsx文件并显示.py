import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMimeData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('拖入xlsx文档并显示内容')
        self.setGeometry(300, 300, 800, 600)

        # 创建表格部件
        self.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

        # 启用窗口部件的拖放功能
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # 获取拖放的URLs
        urls = event.mimeData().urls()
        if urls:
            # 遍历所有拖放的URLs
            for url in urls:
                # 检查URL是否是本地文件
                if url.isLocalFile():
                    file_path = url.toLocalFile()
                    # 检查文件是否是xlsx文档
                    if file_path.endswith('.xlsx'):
                        try:
                            # 读取xlsx文件内容
                            df = pd.read_excel(file_path)
                            # 设置表格的行列数
                            self.table_widget.setRowCount(df.shape[0])
                            self.table_widget.setColumnCount(df.shape[1])
                            # 设置表格的列标题
                            self.table_widget.setHorizontalHeaderLabels(df.columns)
                            # 填充表格内容
                            for row_index, row in df.iterrows():
                                for col_index, value in enumerate(row):
                                    item = QTableWidgetItem(str(value))
                                    self.table_widget.setItem(row_index, col_index, item)
                                    # 调整表格列宽以适应内容
                            self.table_widget.resizeColumnsToContents()
                            # 调整表格行高以适应内容
                            self.table_widget.resizeRowsToContents()
                        except Exception as e:
                            print(f"Error reading file: {e}")
                    else:
                        print(f"Unsupported file type: {file_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())