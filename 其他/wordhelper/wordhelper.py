import sys
from PyQt5.QtGui import QColor, QMovie, QPixmap, QBrush, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QTableWidget, QMessageBox
from PyQt5 import QtCore
import os
import _thread
import tools.common as common
import tools.wordtopdf as wordtopdf
import tools.mergepdf as mergepdf
from mainWindow import Ui_MainWindow
from pageWindow import Ui_PageWindow
from listWindow import Ui_ListWindow
from transformWindow import Ui_TransformWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 600)
        self.setWindowTitle('文档处理系统')
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap("./image/bg.png").scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFixedSize(1024, 600)

class TransformWindow(QMainWindow, Ui_TransformWindow):
    def __init__(self):
        super(TransformWindow, self).__init__()
        self.setupUi(self)
        self.showLoding.setText("")
        self.showLoding.setMinimumWidth(100)
        self.multipleExecute.clicked.connect(self.multipleExecuteClick)
        self.singleExecute.clicked.connect(self.singleExecuteClick)
        self.sourcebrowseButton.clicked.connect(self.sourcebrowseClick)
        self.targetbrowseButton.clicked.connect(self.targetbrowseClick)
        self.listpdf.itemDoubleClicked.connect(self.itemdoubleClick)
        self.filelist = []

    def open(self):
        self.__init__()
        self.show()

    def sourcebrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:\learn\test\doc")
        if dir_path:
            self.sourcepath.setText(dir_path)
            self.listword.clear()
            self.filelist = common.getfilenames(dir_path, [], '.doc')
            self.listword.addItems(self.filelist)

    def targetbrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择目标文件目录", r"E:\learn\test\pdf")
        self.targetpath.setText(dir_path)

    def itemdoubleClick(self, item):
        if os.path.exists(item.text()):
            os.startfile(item.text())
        else:
            QMessageBox.information(self, "温馨提示：", "不是有效的文件名！", QMessageBox.Yes)

    def multipleExecuteClick(self):
        if self._validate_paths():
            self._start_conversion(self.mExecute)

    def singleExecuteClick(self):
        if self._validate_paths():
            self._start_conversion(self.sExecute)

    def _validate_paths(self):
        if not self.listword.count():
            QMessageBox.information(self, "温馨提示：", "没有要转换的Word文档！", QMessageBox.Yes)
            return False
        if not os.path.exists(self.targetpath.text()):
            QMessageBox.information(self, "温馨提示：", "请选择正确的目标路径！", QMessageBox.Yes)
            return False
        return True

    def _start_conversion(self, target_method):
        self.listpdf.clear()
        self.showLoding.setMovie(self.gif)
        self.gif.start()
        _thread.start_new_thread(target_method, ())

    def mExecute(self):
        targetpath = self.targetpath.text()
        valueList = wordtopdf.wordtopdf(self.filelist, targetpath)
        if valueList != -1:
            self.showLoding.clear()
            self.listpdf.addItems(valueList)

    def sExecute(self):
        targetpath = self.targetpath.text()
        valueList = wordtopdf.wordtopdf(self.filelist, targetpath)
        if valueList != -1:
            mergepdf.mergefiles(targetpath, 'merged.pdf', True)
            self.showLoding.clear()
            self.listpdf.addItems([os.path.join(targetpath, 'merged.pdf')])
            for file in valueList:
                os.remove(file)

class PageWindow(QMainWindow, Ui_PageWindow):
    def __init__(self):
        super(PageWindow, self).__init__()
        self.setupUi(self)
        self.pagetable.setColumnWidth(0, 600)
        self.pagetable.setColumnWidth(1, 100)
        self.pagetable.setStyleSheet("background-color: lightblue; selection-background-color:lightblue;")
        self._style_header(self.pagetable.horizontalHeaderItem(0))
        self._style_header(self.pagetable.horizontalHeaderItem(1))
        self.pagetable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.pagetable.setSelectionBehavior(QTableWidget.SelectRows)
        self.pagetable.setSelectionMode(QTableWidget.SingleSelection)
        self.pagetable.setAlternatingRowColors(True)
        self.totalpage.setMinimumWidth(100)
        self.browseButton.clicked.connect(self.sourcebrowseClick)
        self.executeButton.clicked.connect(self.executeClick)
        self.filelist = []

    def _style_header(self, header_item):
        header_item.setBackground(QColor(0, 60, 10))
        header_item.setForeground(QColor(200, 111, 30))

    def open(self):
        self.__init__()
        self.show()

    def sourcebrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:\learn\test\doc")
        if dir_path:
            self.sourcepath.setText(dir_path)
            self.listword.clear()
            self.filelist = common.getfilenames(dir_path, [], '.doc')
            self.listword.addItems(self.filelist)

    def executeClick(self):
        if not self.listword.count():
            QMessageBox.information(self, "温馨提示：", "没有要统计页码的Word文档！", QMessageBox.Yes)
            return
        self._start_processing()

    def _start_processing(self):
        self.totalpage.setText("")
        self.totalpage.setMovie(self.gif)
        self.label_2.setText("正在统计：")
        self.gif.start()
        _thread.start_new_thread(self.execute, ())

    def execute(self):
        valueList = wordtopdf.wordtopdf1(self.filelist)
        totalPages = str(valueList[0])
        self.label_2.setText("合计页码：")
        self.totalpage.setText(totalPages)
        self._populate_table(valueList[1])

    def _populate_table(self, resultList):
        self.pagetable.setRowCount(len(resultList))
        for i, row in enumerate(resultList):
            for j, content in enumerate(row):
                self.pagetable.setItem(i, j, QTableWidgetItem(content))

class ListWindow(QMainWindow, Ui_ListWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.setupUi(self)
        self.browseButton.clicked.connect(self.sourcebrowseClick)
        self.executeButton.clicked.connect(self.getListClick)
        self.openButton.clicked.connect(self.openButtonClick)
        self.filelist = []

    def open(self):
        self.__init__()
        self.show()

    def sourcebrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:\learn\test\doc")
        if dir_path:
            self.sourcepath.setText(dir_path)
            self.listword.clear()
            self.filelist = common.getfilenames(dir_path, [], '.doc')
            self.listword.addItems(self.filelist)

    def getListClick(self):
        if not self.listword.count():
            QMessageBox.information(self, "温馨提示：", "没有要提取目录的Word文档！", QMessageBox.Yes)
            return
        self.listfile.setText("")
        self.listfile.setMovie(self.gif)
        self.gif.start()
        _thread.start_new_thread(self.getList, ())

    def getList(self):
        sourcepath = self.sourcepath.text()
        if not os.path.exists(sourcepath):
            QMessageBox.information(self, "温馨提示：", "请先选择Word文档所在的文件夹！", QMessageBox.Yes)
            return
        targetpath = os.path.join(sourcepath, "pdf")
        os.makedirs(targetpath, exist_ok=True)
        valueList = wordtopdf.wordtopdf(self.filelist, targetpath)
        if valueList != -1:
            mergepdf.mergefiles(targetpath, 'merged.pdf', True)
            temp = [os.path.join(targetpath, 'merged.pdf')]
            for file in valueList:
                os.remove(file)
            isList = self.checkBox.isChecked()
            resultvalue = wordtopdf.getPdfOutlines(temp[0], targetpath, isList)
            os.remove(temp[0])
            if valueList:
                self.listfile.clear()
            self.listfile.setText(resultvalue)

    def openButtonClick(self):
        if self.listfile.text() == "还未提取...":
            QMessageBox.information(self, "温馨提示：", "还没有提取目录，请先单击【开始提取】按钮！", QMessageBox.Yes)
        else:
            os.startfile(self.listfile.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMainWindow()
    qmovie = QMovie('image/loding.gif')

    transformWindow = TransformWindow()
    transformWindow.gif = qmovie
    main.actionWord_PDF.triggered.connect(transformWindow.open)

    pagewindow = PageWindow()
    pagewindow.gif = qmovie
    main.action_Word.triggered.connect(pagewindow.open)

    listwindow = ListWindow()
    listwindow.gif = qmovie
    main.action_list.triggered.connect(listwindow.open)

    main.show()
    sys.exit(app.exec_())

