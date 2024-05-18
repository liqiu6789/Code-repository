from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import qApp,QFileDialog

import sys
import pandas as pd
import os
import glob
root=""
fileNum = 0
myrow=0

def SaveExcel(df,isChecked):
    # 将提取后的数据保存到Excel
    if (isChecked):
        writer = pd.ExcelWriter('mycell.xls')
    else:
        global temproot
        writer = pd.ExcelWriter(temproot + '/mycell.xls')
    df.to_excel(writer, 'sheet1')
    writer.save()
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list1 = QtWidgets.QListView(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(1, 1, 171, 801))
        self.list1.setObjectName("list1")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 0, 861, 801))
        #水平滚动条
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMouseTracking(False)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.button1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("导入EXCEL")
        icon.addPixmap(QtGui.QPixmap("image/图标-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button1.setIcon(icon)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/图标-02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/图标-03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon1)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/图标-04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button4.setIcon(icon2)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QAction(MainWindow)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/图标-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button5.setIcon(icon3)
        self.button5.setObjectName("button5")
        self.button7 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/图标-07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button7.setIcon(icon5)
        self.button7.setObjectName("button7")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button1)
        self.toolBar.addAction(self.button2)
        self.toolBar.addAction(self.button3)
        self.toolBar.addAction(self.button4)
        self.toolBar.addAction(self.button5)
        self.toolBar.addAction(self.button7)
        self.toolBar.addSeparator()
        # 单击工具栏“退出”按钮退出程序
        self.button7.triggered.connect(qApp.quit)
        # 单击工具栏按钮触发自定义槽函数

        self.button1.triggered.connect(self.click1)
        self.button2.triggered.connect(self.click2)
        self.button3.triggered.connect(self.click3)
        self.button4.triggered.connect(self.click4)
        self.button5.triggered.connect(self.click5)

        # 单击QListView列表触发自定义的槽函数
        self.list1.clicked.connect(self.clicked)
        # 设置Dataframe对象显示所有列
        pd.set_option('display.max_columns', None)
        # 设置Dataframe对象列宽为200，默认为50
        pd.set_option('max_colwidth', 200)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excel数据处理系统"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.button1.setText(_translate("MainWindow", "选择文件夹"))
        self.button2.setText(_translate("MainWindow", "转换为csv"))
        self.button3.setText(_translate("MainWindow", "过滤器"))
        self.button4.setText(_translate("MainWindow", "多表合并"))
        self.button5.setText(_translate("MainWindow", "多表统计排行"))
        self.button7.setText(_translate("MainWindow", "退出"))



    def click1(self):
        # 文件夹路径
        global root
        root = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        mylist = []
        # 遍历文件夹文件
        for dirpath, dirnames, filenames in os.walk(root):
            for filepath in filenames:
                # mylist.append(os.path.join(dirpath, filepath))
                mylist.append(os.path.join(filepath))
        # 实例化列表模型，添加数据列表
        self.model = QtCore.QStringListModel()
        # 添加列表数据
        self.model.setStringList(mylist)
        self.list1.setModel(self.model)
        self.list1 = mylist

    # 单击左侧目录右侧表格显示数据
    def clicked(self, qModelIndex):
        global root
        global myrow
        myrow=qModelIndex.row()
        # 获取当前选中行的数据
        a = root + '/' + str(self.list1[qModelIndex.row()])
        df = pd.DataFrame(pd.read_excel(a))
        self.textEdit.setText(str(df))

    #提取列数据
    def click2(self):
        global root
        global myrow
        # 获取当前选中行的数据
        a = root + '/' + str(self.list1[myrow])
        df = pd.DataFrame(pd.read_excel(a))
        #显示指定列数据
        df1 = df[['买家会员名', '收货人姓名', '联系手机','宝贝标题']]
        self.textEdit.setText(str(df1))
        #调用SaveExcel函数，保存数据到Excel
        SaveExcel(df1,self.rButton2.isChecked())

    #定向筛选
    def click3(self):
        global root
        global myrow
        #合并Excel表格
        filearray = []
        filelocation = glob.glob(root + "\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)
        # 显示指定列数据
        df1 = res[['买家会员名', '收货人姓名', '联系手机','宝贝标题']]
        df2 = df1.loc[df1['宝贝标题'] == '零基础学Python']
        self.textEdit.setText(str(df2))
        #调用SaveExcel函数，保存定向筛选结果到Excel
        SaveExcel(df2,self.rButton2.isChecked())

    #多表合并
    def click4(self):
        global root
        # 合并指定文件夹下的所有Excel表
        filearray = []
        filelocation = glob.glob(root+"\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)

        self.textEdit.setText(str(res.index))
        # 调用SaveExcel函数，将合并后的数据保存到Excel
        SaveExcel(res, self.rButton2.isChecked())

    #多表统计排行
    def click5(self):
        global root
        # 合并Excel表格
        filearray = []
        filelocation = glob.glob(root + "\*.xls")
        for filename in filelocation:
            filearray.append(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res, A], ignore_index=False, sort=True)
        # 分组统计排序
        # 通过reset_index()函数将groupby()的分组结果转成DataFrame对象
        df = res.groupby(["宝贝标题"])["宝贝总数量"].sum().reset_index()
        df1 = df.sort_values(by='宝贝总数量', ascending=False)
        self.textEdit.setText(str(df1))
        # 调用SaveExcel函数，将统计排行结果保存到Excel
        SaveExcel(df1, self.rButton2.isChecked())





# 定义载入主窗体的方法
def show_MainWindow():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
        show_MainWindow()
        path=root

