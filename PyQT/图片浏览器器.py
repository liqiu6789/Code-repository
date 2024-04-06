import copy
import cv2
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, \
    QFrame, QToolButton, QSpacerItem, QLabel, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QIcon, QPainter, QPen, QFont, QColor
from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5 import QtWidgets, QtGui
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
class HistWidget(QWidget):
    def __init__(self, image_path = None):
        super().__init__()
        if image_path is not None:
            self.img_path = image_path
            self.initUI()

    def initUI(self):
        # 创建一个QVBoxLayout实例
        layout = QVBoxLayout(self)

        # 读取图片
        image_path = self.img_path # 替换为你的图片路径
        image = cv2.imread(image_path)

        # OpenCV读取的图像默认是BGR格式，我们需要将其转换为RGB格式
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 提取R, G, B通道数据
        r, g, b = cv2.split(image)

        # 创建三个matplotlib的Figure和Axes实例，分别对应R, G, B通道
        figs = [Figure() for _ in range(3)]
        axes = [fig.add_subplot(111) for fig in figs]

        # 创建三个matplotlib的canvas，并添加到布局中
        canvases = [FigureCanvas(fig) for fig in figs]

        # 遍历每个通道，绘制直方图并添加到布局中
        for i, (canvas, ax, channel_data) in enumerate(zip(canvases, axes, [r, g, b])):
            ax.hist(channel_data.flatten(), bins=30, color=['red', 'green', 'blue'][i], alpha=0.7,
                    label=f'{["R", "G", "B"][i]}通道')
            ax.legend()
            ax.set_title(f'{["R", "G", "B"][i]} 通道直方图')

            # 将canvas添加到布局中
            layout.addWidget(canvas)

            # 设置窗口的标题和大小
        self.setWindowTitle('通道直方图')
        self.setGeometry(300, 300, 800, 600)
class ImageLabel(QLabel):
    """"
    用于显示图片的 Label
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False  # 标记是否能够绘制矩形
        self.__isClear = False  # 标记是否是清除矩形
        self.setAlignment(Qt.AlignCenter)  # 居中对齐
        self.setFrameShape(QtWidgets.QFrame.Box)  # 设置边框
        self.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(218, 218, 218)")
        self.setText("")
        self.__w, self.__h = 0, 0
        self.pixmap_width, self.pixmap_height = 0, 0  # pixmap 的宽度、高度
        self.pixmap_x_start, self.pixmap_y_start = 0, 0  # pixmap 在 label 中的起点位置
        self.pixmap_x_end, self.pixmap_y_end = 0, 0  # pixamp 在 label 中的终点位置
        self.img_x_start, self.img_y_start = 0, 0  # 图片中选择的矩形区域的起点位置
        self.img_x_end, self.img_y_end = 0, 0  # 图片中选择的矩形区域的终点位置
        self.autoFillBackground()

    # 鼠标点击事件
    def mousePressEvent(self, event):
        # self.flag = True
        # 鼠标点击，相当于开始绘制矩形，将 isClear 置为 False
        self.__isClear = False
        self.x0 = event.x()
        self.y0 = event.y()
        # 计算 Pixmap 在 Label 中的位置
        self.__w, self.__h = self.width(), self.height()
        self.pixmap_x_start = (self.__w - self.pixmap_width) / 2
        self.pixmap_y_start = (self.__h - self.pixmap_height) / 2
        self.pixmap_x_end = self.pixmap_x_start + self.pixmap_width
        self.pixmap_y_end = self.pixmap_y_start + self.pixmap_height

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        # self.flag = False
        self.setCursor(Qt.ArrowCursor)  # 鼠标释放，矩形已经绘制完毕，恢复鼠标样式

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def setPixmap(self, pixmap):
        super().setPixmap(pixmap)
        self.pixmap_width, self.pixmap_height = pixmap.width(), pixmap.height()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)

        # 判断是否是清除
        if self.__isClear:
            return  # 是清除，则不需要执行下面的绘制操作。即此次 paint 事件没有绘制操作，因此界面中没有绘制的图形（从而相当于清除整个界面中已有的图形）

        # 判断用户起始位置是否在图片区域，只有在图片区域才画选择的矩形图
        if (self.pixmap_x_start <= self.x0 <= self.pixmap_x_end) \
                and (self.pixmap_y_start <= self.y0 <= self.pixmap_y_end):
            # 判断结束位置是否在图片区域内，如果超过，则直接设置成图片区域的终点
            if self.x1 > self.pixmap_x_end:
                self.x1 = self.pixmap_x_end
            elif self.x1 < self.pixmap_x_start:
                self.x1 = self.pixmap_x_start

            if self.y1 > self.pixmap_y_end:
                self.y1 = self.pixmap_y_end
            elif self.y1 < self.pixmap_y_start:
                self.y1 = self.pixmap_y_start
            rect = QRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect)
            # 计算矩形区域在图片中的位置
            self.img_x_start = int(self.x0 - self.pixmap_x_start)
            self.img_x_end = int(self.x1 - self.pixmap_x_start)
            self.img_y_start = int(self.y0 - self.pixmap_y_start)
            self.img_y_end = int(self.y1 - self.pixmap_y_start)

    def clearRect(self):
        # 清除
        self.__isClear = True
        self.update()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        """
        Initialize the user interface and set initial states.
        """
        self.setup_ui()
        self.set_initial_states()

    def setup_ui(self):
        """
        Set up the main window layout and components.
        """
        self.setWindowTitle("图片信息查看器")
        self.resize(1200, 900)

        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        # Title bar with open, save, and undo buttons
        self.title_bar = QFrame(self.central_widget)
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.title_layout = QHBoxLayout(self.title_bar)

        self.btn_open = QToolButton(self.title_bar)
        self.btn_save = QToolButton(self.title_bar)
        self.btn_undo = QToolButton(self.title_bar)

        self.title_layout.addWidget(self.btn_open)
        self.title_layout.addWidget(self.btn_save)
        self.title_layout.addWidget(self.btn_undo)

        # Control bar with confirm and cancel buttons
        self.control_bar = QFrame(self.title_bar)
        self.control_layout = QHBoxLayout(self.control_bar)
        self.btn_confirm = QToolButton(self.control_bar)
        self.btn_cancel = QToolButton(self.control_bar)

        self.control_layout.addWidget(self.btn_confirm)
        self.control_layout.addWidget(self.btn_cancel)
        self.title_layout.addWidget(self.control_bar)

        # Add a spacer item to the title layout
        self.title_layout.addItem(QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Image frame with an ImageLabel widget to display images
        self.img_frame = QFrame(self.central_widget)
        self.img_frame.setFrameShape(QFrame.StyledPanel)
        self.img_frame.setFrameShadow(QFrame.Raised)
        self.img_layout = QVBoxLayout(self.img_frame)
        self.img_display = ImageLabel(self.img_frame)
        self.img_info = QFrame(self.img_frame)

        self.hist_win = QFrame()

        self.hist_win_layout = QHBoxLayout()
        self.hist_win.setLayout(self.hist_win_layout)
        self.img_hist_win = HistWidget()
        self.hist_win_layout.addWidget(self.img_display)
        self.hist_win_layout.addWidget(self.img_hist_win)

        self.img_info.setFixedHeight(50)
        self.img_info_layout = QHBoxLayout()
        self.img_info.setLayout(self.img_info_layout)
        self.w_label = QLabel('宽度: xxx 像素')
        self.h_label = QLabel('高度: xxx 像素')
        self.c_label = QLabel('通道数: x ')
        # 创建标签来显示信息
        labels = [
            self.w_label,
            self.h_label,
            self.c_label,
        ]

        # 设置字体样式、大小和颜色
        font = QFont()
        font.setFamily('Arial')  # 设置字体类型，例如 'Arial'
        font.setPointSize(12)  # 设置字体大小，例如 12

        # 应用字体和颜色到每个标签
        for label in labels:
            label.setFont(font)  # 设置字体
            label.setStyleSheet("color: rgb(35, 184, 80);")  # 设置颜色，也可以使用QLabel的setPalette方法

        # 添加标签到布局中
        for label in labels:
            self.img_info_layout.addWidget(label)

        self.img_layout.addWidget(self.hist_win)
        self.img_layout.addWidget(self.img_info)
        self.central_layout.addWidget(self.title_bar)
        self.central_layout.addWidget(self.img_frame)

        # Set button text, icons, styles, and layout styles
        self.set_buttons_text_icons()
        self.set_buttons_styles()
        self.set_layout_styles()

    def set_initial_states(self):
        """
        Set initial states for UI components.
        """
        self.control_bar.setVisible(False)

    def set_buttons_text_icons(self):
        """
        Set button texts, icons, and style for open and save buttons.
        """
        self.btn_open.setText("打开")
        self.btn_open.setIcon(QIcon("./icon/open.png"))
        self.btn_open.setIconSize(QSize(36, 36))
        self.btn_open.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_open.clicked.connect(self.open_img)

        self.btn_save.setText("保存")
        self.btn_save.setIcon(QIcon("./icon/save.png"))
        self.btn_save.setIconSize(QSize(36, 36))
        self.btn_save.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_save.clicked.connect(self.save_img)

    def set_buttons_styles(self):
        """
        Set styles for all buttons and the control bar.
        """
        transparent_button_style = "background: rgba(0, 0, 0, 0); color: rgb(255, 255, 255);"
        gray_button_style = "background: rgb(80, 80, 80); color: rgb(255, 255, 255);"

        buttons = [self.btn_open, self.btn_save, self.btn_undo, self.btn_confirm, self.btn_cancel]
        for btn in buttons:
            btn.setStyleSheet(transparent_button_style)

        self.control_bar.setStyleSheet(gray_button_style)

    def set_layout_styles(self):
        """
        Set styles for central layout and title bar.
        """
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)

        self.title_bar.setMinimumSize(QSize(0, 55))
        self.title_bar.setMaximumSize(QSize(188888, 55))

        self.control_bar.setMinimumSize(QSize(0, 45))
        self.control_bar.setMaximumSize(QSize(120, 45))

        self.img_frame.setMinimumSize(QSize(100, 0))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.setFont(font)
        self.btn_open.setFont(font)
        self.btn_save.setFont(font)

        self.central_widget.setStyleSheet("background: rgb(252, 255, 255);")
        self.title_bar.setStyleSheet("background: rgb(146, 6, 213);")

    def open_img(self):
        """
        Open an image file using a file dialog and display it.
        """
        img_name, img_type = QFileDialog.getOpenFileName(
            self, "打开图片", "", "*.jpg;*.png;*.jpeg"
        )
        if img_name == "" or img_name is None:
            self.show_warning_message_box("未选择图片")
            return
        self.img_path = img_name
        img = cv2.imread(img_name)
        self.show_image(img)
        self.current_img = img
        self.last_img = self.current_img
        self.original_img = copy.deepcopy(self.current_img)
        self.original_img_path = img_name

    def show_image(self, img, is_grayscale=False):
        """
        Display an image in the ImageLabel widget.

        Args:
            img (numpy.ndarray): The image to display (in BGR or grayscale format).
            is_grayscale (bool, optional): Whether the image is grayscale. Defaults to False.
        """
        if len(img.shape) == 3:  # Color image
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

        height, width, channels = img.shape
        bytes_per_line = channels * width

        if len(img.shape) == 2:  # Grayscale image
            format = QImage.Format_Grayscale8
            bytes_per_line *= 1  # Treat grayscale image as having one channel
        else:  # RGB image
            format = QImage.Format_RGB888

        qimage = QImage(img.data, width, height, bytes_per_line, format)
        pixmap = QPixmap.fromImage(qimage)
        if pixmap.width() > 600 or pixmap.height() > 600:
            pixmap = pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_display.setPixmap(pixmap)
        self.img_hist_win=HistWidget(self.img_path)
        self.hist_win_layout.addWidget(self.img_hist_win)
        self.img_display.repaint()
        height, width = img.shape[:2]
        # 获取图片的通道数
        channels = img.shape[2] if len(img.shape) > 2 else 1
        self.w_label.setText(f"宽度: {width} 像素")
        self.h_label.setText(f"高度: {height} 像素")
        self.c_label.setText(f"通道数: {channels}")

    def crop_image(self, src_img, x_start, x_end, y_start, y_end):
        """
        Crop an image.

        Args:
            src_img (numpy.ndarray): The source image to crop.
            x_start (int): Starting x-coordinate of the crop region.
            x_end (int): Ending x-coordinate of the crop region.
            y_start (int): Starting y-coordinate of the crop region.
            y_end (int): Ending y-coordinate of the crop region.

        Returns:
            numpy.ndarray: The cropped image.
        """
        return src_img[y_start:y_end, x_start:x_end]

    def show_warning_message_box(self, msg):
        """
        Show a warning message box with the given message.

        Args:
            msg (str): The message to display.
        """
        QMessageBox.warning(self, "警告", msg, QMessageBox.Ok)

    def show_info_message_box(self, msg):
        """
        Show an information message box with the given message.

        Args:
            msg (str): The message to display.
        """
        QMessageBox.information(self, "提示", msg, QMessageBox.Ok)

    def save_img(self):
        """
        Save the current image to a file using a file dialog.
        """
        if self.current_img is None:
            self.show_warning_message_box("未选择图片")
            return

        ext_name = self.original_img_path[self.original_img_path.rindex("."):]
        img_path, img_type = QFileDialog.getSaveFileName(
            self, "保存图片", self.original_img_path, f"*{ext_name}"
        )
        cv2.imwrite(img_path, self.current_img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
