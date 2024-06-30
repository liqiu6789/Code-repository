import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QToolBar, QAction, QFileSystemModel, QTreeView, QListView, QSplitter
from PyQt5.QtCore import Qt, QSize, QDir

class FileBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('File Browser')
        self.setGeometry(100, 100, 800, 600)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.rootPath()))
        self.tree.setColumnWidth(0, 250)

        self.list_view = QListView()
        self.list_view.setModel(self.model)
        self.list_view.setRootIndex(self.model.index(QDir.rootPath()))
        self.list_view.setViewMode(QListView.IconMode)
        self.list_view.setIconSize(QSize(64, 64))

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.list_view)

        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.splitter)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar("视图选择")
        self.addToolBar(toolbar)

        list_view_action = QAction("列表视图", self)
        list_view_action.triggered.connect(self.set_list_view)
        toolbar.addAction(list_view_action)

        icon_view_action = QAction("图标视图", self)
        icon_view_action.triggered.connect(self.set_icon_view)
        toolbar.addAction(icon_view_action)

    def set_list_view(self):
        self.list_view.setViewMode(QListView.ListMode)
        self.list_view.setIconSize(QSize(32, 32))

    def set_icon_view(self):
        self.list_view.setViewMode(QListView.IconMode)
        self.list_view.setIconSize(QSize(64, 64))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileBrowser()
    window.show()
    sys.exit(app.exec_())
