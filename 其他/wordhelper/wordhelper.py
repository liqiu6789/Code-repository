import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QTableWidget, \
    QMessageBox
import os
import tools.common as common
import tools.wordtopdf as wordtopdf
import tools.mergepdf as mergepdf
from mainWindow import *
from pageWindow import *
from listWindow import *
from transformWindow import *
import _thread


# 主窗体初始化类
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 600)
        self.setWindowTitle('文档处理系统')  # 设置窗体的标题
        # 设置窗体背景
        palette = QtGui.QPalette()  # 创建调色板类的对象
        # 设置窗体背景自适应
        palette.setBrush(self.backgroundRole(), QBrush(
            QPixmap("./image/bg.png").scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        self.setPalette(palette)
        self.setAutoFillBackground(True)  # 设置自动填充背景
        self.setFixedSize(1024, 600)  # 禁止显示最大化按钮及调整窗体大小



class TransformWindow(QMainWindow, Ui_TransformWindow):
    filelist = []

    def __init__(self):
        super(TransformWindow, self).__init__()
        self.setupUi(self)
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        self.showLoding.setText("")
        self.showLoding.setMinimumWidth(100)

    def _connect_signals(self):
        self.multipleExecute.clicked.connect(self.multipleExecuteClick)
        self.singleExecute.clicked.connect(self.singleExecuteClick)
        self.sourcebrowseButton.clicked.connect(self.sourcebrowseClick)
        self.targetbrowseButton.clicked.connect(self.targetbrowseClick)
        self.listpdf.itemDoubleClicked.connect(self.itemdoubleClick)

    def open(self):
        self.__init__()
        self.show()

    def sourcebrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:\learn\test\doc")
        if not dir_path:
            return
        self.sourcepath.setText(dir_path)
        self.listword.clear()
        global filelist
        filelist = common.getfilenames(dir_path, [], '.doc')
        self.listword.addItems(filelist)

    def targetbrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择目标文件目录", r"E:\learn\test\pdf")
        self.targetpath.setText(dir_path)

    def itemdoubleClick(self, item):
        if os.path.exists(item.text()):
            os.startfile(item.text())
        else:
            QMessageBox.information(self, "温馨提示：", "不是有效的文件名！", QMessageBox.Yes)

    def multipleExecuteClick(self):
        if not self._validate_paths():
            return
        self._start_conversion(self.mExecute)

    def singleExecuteClick(self):
        if not self._validate_paths():
            return
        self._start_conversion(self.sExecute)

    def _validate_paths(self):
        if self.listword.count() == 0:
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
        valueList = wordtopdf.wordtopdf(filelist, targetpath)
        if valueList != -1:
            self.showLoding.clear()
            self.listpdf.addItems(valueList)

    def sExecute(self):
        targetpath = self.targetpath.text()
        valueList = wordtopdf.wordtopdf(filelist, targetpath)
        if valueList != -1:
            mergepdf.mergefiles(targetpath, 'merged.pdf', True)
            self.showLoding.clear()
            self.listpdf.addItems([os.path.join(targetpath, 'merged.pdf')])
            for file in valueList:
                os.remove(file)

class PageWindow(QMainWindow, Ui_PageWindow):
    filelist = []

    def __init__(self):
        super(PageWindow, self).__init__()
        self.setupUi(self)
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        self.pagetable.setColumnWidth(0, 600)
        self.pagetable.setColumnWidth(1, 100)
        self.pagetable.setStyleSheet("background-color: lightblue;"
                                     "selection-background-color:lightblue;")
        self._style_header(self.pagetable.horizontalHeaderItem(0))
        self._style_header(self.pagetable.horizontalHeaderItem(1))
        self.pagetable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.pagetable.setSelectionBehavior(QTableWidget.SelectRows)
        self.pagetable.setSelectionMode(QTableWidget.SingleSelection)
        self.pagetable.setAlternatingRowColors(True)
        self.totalpage.setMinimumWidth(100)

    def _style_header(self, header_item):
        header_item.setBackground(QColor(0, 60, 10))
        header_item.setForeground(QColor(200, 111, 30))

    def _connect_signals(self):
        self.browseButton.clicked.connect(self.sourcebrowseClick)
        self.executeButton.clicked.connect(self.executeClick)

    def open(self):
        self.__init__()
        self.show()

    def sourcebrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:\learn\test\doc")
        if dir_path:
            self.sourcepath.setText(dir_path)
            self.listword.clear()
            global filelist
            filelist = common.getfilenames(dir_path, [], '.doc')
            self.listword.addItems(filelist)

    def executeClick(self):
        if self.listword.count() == 0:
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
        valueList = wordtopdf.wordtopdf1(filelist)
        totalPages = str(valueList[0])
        self.label_2.setText("合计页码：")
        self.totalpage.setText(totalPages)
        self._populate_table(valueList[1])

    def _populate_table(self, resultList):
        self.pagetable.setRowCount(len(resultList))
        for i, row in enumerate(resultList):
            for j, content in enumerate(row):
                self.pagetable.setItem(i, j, QTableWidgetItem(content))


'''提取总目录模块'''


class ListWindow(QMainWindow, Ui_ListWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.setupUi(self)
        self.browseButton.clicked.connect(self.sourcebrowseClick)  # 选择源路径
        self.executeButton.clicked.connect(self.getListClick)  # 按钮事件绑定
        self.openButton.clicked.connect(self.openButtonClick)  # 为打开文件按钮绑定事件

    # 自定义打开子窗体的方法
    def open(self):
        self.__init__()
        self.show()  # 显示子窗体

    def sourcebrowseClick(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录", r"E:\learn\test\doc")
        if dir_path != "":  # 判断已经选择了源文件目录
            self.sourcepath.setText(dir_path)
            self.listword.clear()  # 清空列表
            global filelist
            filelist = common.getfilenames(dir_path, [], '.doc')  # 获取Word文档
            self.listword.addItems(filelist)

    def getListClick(self):  # 子窗体自定义事件
        if self.listword.count() == 0:
            QMessageBox.information(self, "温馨提示：", "没有要提取目录的Word文档！", QMessageBox.Yes)
            return
        self.listfile.setText("")
        self.listfile.setMovie(self.gif)  # 设置gif图片
        self.gif.start()  # 启动图片，实现等待gif图片的显示
        _thread.start_new_thread(self.getList, ())  # 开启新线程执行统计页码

    # 提取目录
    def getList(self):
        sourcepath = self.sourcepath.text()  # 获取源路径
        if not os.path.exists(sourcepath):  # 判断是否选择了源目录
            QMessageBox.information(self, "温馨提示：", "请先选择Word文档所在的文件夹！", QMessageBox.Yes)
            return
        targetpath = os.path.join(sourcepath, "pdf")  # 根据源路径生成目标目录
        if not os.path.exists(targetpath):  # 判断目录是否存在，不存在则创建
            os.makedirs(targetpath)  # 创建目录
        valueList = wordtopdf.wordtopdf(filelist, targetpath)
        if (valueList != -1):
            mergepdf.mergefiles(targetpath, 'merged.pdf', True)  # 合并PDF
            temp = [os.path.join(targetpath, 'merged.pdf')]  # 生成合并后的PDF文件的路径
            for file in valueList:  # 遍历临时生成的PDF文件列表
                os.remove(file)  # 删除PDF文件
            isList = self.checkBox.isChecked()  # 指定是否带目录
            resultvalue = wordtopdf.getPdfOutlines(temp[0], targetpath, isList)  # 提取目录
            os.remove(temp[0])  # 删除合并后的PDF文件
            if valueList != []:
                self.listfile.clear()  # 转换完毕就将等待gif图片清理掉
            self.listfile.setText(resultvalue)  # 将生成的目录文件路径显示到页面中

    # 自定义打开子窗体的方法
    def open(self):
        self.__init__()
        self.show()  # 显示子窗体

    # 打开文件按钮触发的事件函数
    def openButtonClick(self):
        if self.listfile.text() == "还未提取...":
            QMessageBox.information(self, "温馨提示：", "还没有提取目录，请先单击【开始提取】按钮！", QMessageBox.Yes)
        else:
            os.startfile(self.listfile.text())  # 打开文件


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建GUI对象
    main = MyMainWindow()  # 创建主窗体ui类对象
    qmovie = QtGui.QMovie('image/loding.gif')

    transformWindow = TransformWindow()  # 创建Word转PDF窗体对象
    transformWindow.gif = qmovie  # 加载gif图片
    main.actionWord_PDF.triggered.connect(transformWindow.open)  # 为Toolbar上的Word转PDF按钮指定连接槽函数

    pagewindow = PageWindow()  # 创建统计Word文档页码窗体对象
    pagewindow.gif = qmovie  # 加载gif图片
    main.action_Word.triggered.connect(pagewindow.open)  # 为Toolbar上的统计Word文档页码按钮指定连接槽函数

    listwindow = ListWindow()  # 创建提取总目录窗体对象
    listwindow.gif = qmovie  # 加载gif图片
    main.action_list.triggered.connect(listwindow.open)  # 为Toolbar上的提取总目录按钮指定连接槽函数

    main.show()  # 显示主窗体
    sys.exit(app.exec_())  # 除非退出程序关闭窗体，否则一直运行
