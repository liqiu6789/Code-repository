from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        ListWindow.setObjectName("ListWindow")
        ListWindow.resize(800, 588)
        ListWindow.setStyleSheet("background-color: lightblue;")

        self.centralwidget = QtWidgets.QWidget(ListWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Setup layouts
        self._setup_layouts()
        # Setup widgets
        self._setup_widgets()

        ListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        ListWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListWindow)
        self.statusbar.setObjectName("statusbar")
        ListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListWindow)
        QtCore.QMetaObject.connectSlotsByName(ListWindow)

    def _setup_layouts(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_3 = self._create_hbox_layout(self.verticalLayoutWidget)
        self.groupBox = self._create_group_box(self.verticalLayoutWidget)
        self.horizontalLayout = self._create_hbox_layout(self.groupBox)
        self.groupBox_2 = self._create_group_box(self.verticalLayoutWidget)
        self.horizontalLayout_2 = self._create_hbox_layout(self.groupBox_2)

    def _setup_widgets(self):
        self.checkBox = self._create_check_box(self.horizontalLayout_3, "checkBox")
        self.executeButton = self._create_push_button(self.horizontalLayout_3, "executeButton")
        self.label = self._create_label(self.horizontalLayout, "label")
        self.sourcepath = self._create_line_edit(self.horizontalLayout, "sourcepath")
        self.browseButton = self._create_tool_button(self.horizontalLayout, "browseButton")
        self.listword = self._create_list_widget(self.groupBox, "listword")
        self.label_2 = self._create_label(self.horizontalLayout_2, "label_2")
        self.listfile = self._create_label(self.horizontalLayout_2, "listfile")
        self.openButton = self._create_push_button(self.horizontalLayout_2, "openButton")

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.groupBox_2)

    def _create_hbox_layout(self, parent):
        layout = QtWidgets.QHBoxLayout(parent)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    def _create_group_box(self, parent):
        group_box = QtWidgets.QGroupBox(parent)
        return group_box

    def _create_check_box(self, layout, name):
        check_box = QtWidgets.QCheckBox(layout.parentWidget())
        check_box.setObjectName(name)
        layout.addWidget(check_box)
        return check_box

    def _create_push_button(self, layout, name):
        button = QtWidgets.QPushButton(layout.parentWidget())
        button.setObjectName(name)
        layout.addWidget(button)
        return button

    def _create_label(self, layout, name):
        label = QtWidgets.QLabel(layout.parentWidget())
        label.setObjectName(name)
        layout.addWidget(label)
        return label

    def _create_line_edit(self, layout, name):
        line_edit = QtWidgets.QLineEdit(layout.parentWidget())
        line_edit.setObjectName(name)
        layout.addWidget(line_edit)
        return line_edit

    def _create_tool_button(self, layout, name):
        tool_button = QtWidgets.QToolButton(layout.parentWidget())
        tool_button.setObjectName(name)
        layout.addWidget(tool_button)
        return tool_button

    def _create_list_widget(self, parent, name):
        list_widget = QtWidgets.QListWidget(parent)
        list_widget.setObjectName(name)
        return list_widget

    def retranslateUi(self, ListWindow):
        _translate = QtCore.QCoreApplication.translate
        ListWindow.setWindowTitle(_translate("ListWindow", "提取总目录"))
        self.checkBox.setText(_translate("ListWindow", "包含页码"))
        self.executeButton.setText(_translate("ListWindow", "开始提取"))
        self.groupBox.setTitle(_translate("ListWindow", "源"))
        self.label.setText(_translate("ListWindow", "请选择Word文档所在目录："))
        self.browseButton.setText(_translate("ListWindow", "..."))
        self.groupBox_2.setTitle(_translate("ListWindow", "结果"))
        self.label_2.setText(_translate("ListWindow", "目录文件保存位置："))
        self.listfile.setText(_translate("ListWindow", "还未提取..."))
        self.openButton.setText(_translate("ListWindow", "打开文件"))




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PageWindow(object):
    def setupUi(self, PageWindow):
        PageWindow.setObjectName("PageWindow")
        PageWindow.resize(792, 676)
        PageWindow.setStyleSheet("background-color: lightblue;")

        self.centralwidget = QtWidgets.QWidget(PageWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Setup layouts and widgets
        self._setup_main_layout()
        self._setup_source_group()
        self._setup_result_group()

        PageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 23))
        self.menubar.setObjectName("menubar")
        PageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PageWindow)
        self.statusbar.setObjectName("statusbar")
        PageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PageWindow)
        QtCore.QMetaObject.connectSlotsByName(PageWindow)

    def _setup_main_layout(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

    def _setup_source_group(self):
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout.addWidget(self.groupBox)

        self.sourceLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.sourceLayout.setContentsMargins(20, 20, 20, 20)
        self.sourceLayout.setObjectName("sourceLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.sourcepath = QtWidgets.QLineEdit(self.groupBox)
        self.sourcepath.setObjectName("sourcepath")
        self.horizontalLayout.addWidget(self.sourcepath)

        self.browseButton = QtWidgets.QToolButton(self.groupBox)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)

        self.sourceLayout.addLayout(self.horizontalLayout)

        self.listword = QtWidgets.QListWidget(self.groupBox)
        self.listword.setObjectName("listword")
        self.sourceLayout.addWidget(self.listword)

    def _setup_result_group(self):
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")

        self.verticalLayout.addWidget(self.groupBox_2)

        self.resultLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.resultLayout.setContentsMargins(20, 20, 20, 20)
        self.resultLayout.setObjectName("resultLayout")

        self.pagetable = QtWidgets.QTableWidget(self.groupBox_2)
        self.pagetable.setObjectName("pagetable")
        self.pagetable.setColumnCount(2)
        self.pagetable.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem())
        self.pagetable.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem())
        self.resultLayout.addWidget(self.pagetable)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.totalpage = QtWidgets.QLabel(self.groupBox_2)
        self.totalpage.setObjectName("totalpage")
        self.horizontalLayout_2.addWidget(self.totalpage)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.executeButton = QtWidgets.QPushButton(self.groupBox_2)
        self.executeButton.setObjectName("executeButton")
        self.horizontalLayout_2.addWidget(self.executeButton)

        self.resultLayout.addLayout(self.horizontalLayout_2)

    def retranslateUi(self, PageWindow):
        _translate = QtCore.QCoreApplication.translate
        PageWindow.setWindowTitle(_translate("PageWindow", "统计Word文档页码"))
        self.groupBox.setTitle(_translate("PageWindow", "源"))
        self.label.setText(_translate("PageWindow", "请选择Word文档所在目录："))
        self.browseButton.setText(_translate("PageWindow", "..."))
        self.groupBox_2.setTitle(_translate("PageWindow", "结果"))
        self.pagetable.horizontalHeaderItem(0).setText(_translate("PageWindow", "文件名"))
        self.pagetable.horizontalHeaderItem(1).setText(_translate("PageWindow", "页码"))
        self.label_2.setText(_translate("PageWindow", "合计页码："))
        self.totalpage.setText(_translate("PageWindow", "未统计"))
        self.executeButton.setText(_translate("PageWindow", "开始统计"))

