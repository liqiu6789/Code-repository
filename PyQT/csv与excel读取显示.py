import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTableWidget, \
    QTableWidgetItem
import pandas as pd


class CSVViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('CSV/Excel Viewer')
        self.setGeometry(300, 300, 800, 600)

        # 创建按钮
        self.btn_open_csv = QPushButton('Open CSV File', self)
        self.btn_open_csv.clicked.connect(self.openCSVFile)

        self.btn_open_excel = QPushButton('Open Excel File', self)
        self.btn_open_excel.clicked.connect(self.openExcelFile)

        # 创建表格用于显示文件内容
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(0)  # 初始时没有列
        self.table_widget.setRowCount(0)  # 初始时没有行

        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.btn_open_csv)
        layout.addWidget(self.btn_open_excel)
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def openCSVFile(self):
        # 打开文件对话框并选择CSV文件
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', '.', 'CSV Files (*.csv)')
        if file_name:
            self.loadDataFrame(file_name)

    def openExcelFile(self):
        # 打开文件对话框并选择Excel文件
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Excel File', '.', 'Excel Files (*.xlsx)')
        if file_name:
            self.loadDataFrame(file_name)

    def loadDataFrame(self, file_name):
        # 读取文件
        df = pd.read_excel(file_name) if file_name.endswith('.xlsx') else pd.read_csv(file_name)

        # 设置表格的列数和行数
        self.table_widget.setColumnCount(df.shape[1])
        self.table_widget.setRowCount(df.shape[0])

        # 设置表格的列名
        self.table_widget.setHorizontalHeaderLabels(df.columns)

        # 填充表格内容
        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row_index, col_index, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CSVViewer()
    ex.show()
    sys.exit(app.exec_())