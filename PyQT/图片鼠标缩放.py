# coding:utf-8
import sys

from PyQt5.QtCore import QRect, QRectF, QSize, Qt
from PyQt5.QtGui import QPainter, QPixmap, QWheelEvent
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsPixmapItem,
                             QGraphicsScene, QGraphicsView)


class ImageViewer(QGraphicsView):
    """ 图片查看器 """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.zoomInTimes = 0
        self.maxZoomInTimes = 22
        self.displayedImageSize = None

        # 初始化小部件
        self.initWidget()

    def initWidget(self):
        """ 初始化小部件 """
        self.resize(1200, 900)
        self.graphicsScene = QGraphicsScene()
        self.pixmap = QPixmap(r'liu_2.jpeg')
        self.pixmapItem = QGraphicsPixmapItem(self.pixmap)

        # 隐藏滚动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 以鼠标所在位置为锚点进行缩放
        self.setTransformationAnchor(self.AnchorUnderMouse)

        # 平滑缩放
        self.pixmapItem.setTransformationMode(Qt.SmoothTransformation)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # 设置场景
        self.graphicsScene.addItem(self.pixmapItem)
        self.setScene(self.graphicsScene)

    def wheelEvent(self, e: QWheelEvent):
        """ 滚动鼠标滚轮缩放图片 """
        if e.angleDelta().y() > 0 and self.zoomInTimes < self.maxZoomInTimes:
            self.zoomIn()
        else:
            self.zoomOut()

    def resizeEvent(self, e):
        """ 缩放图片 """
        super().resizeEvent(e)

        # 如果进行了放大操作，则不进行自动调整大小
        if self.zoomInTimes > 0:
            return

            # 调整图片大小
        scale_ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size() * scale_ratio
        if scale_ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
        else:
            self.resetTransform()

            # 其他方法，如 zoomIn, zoomOut, __getScaleRatio 等，保持不变

    def setImage(self, image_path: str):
        """ 设置显示的图片 """
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            # 处理图片加载失败的情况
            print(f"Failed to load image from {image_path}")
            return

        self.pixmap = pixmap
        self.pixmapItem.setPixmap(pixmap)
        self.resetTransform()  # 重置变换，包括 zoomInTimes 和拖拽

        # 调整图片大小
        self.setSceneRect(QRectF(pixmap.rect()))
        self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)

    def resetTransform(self):
        """ 重置变换 """
        super().resetTransform()
        self.zoomInTimes = 0
        self.__setDragEnabled(False)
        self.displayedImageSize = self.pixmap.size() if not self.pixmap.isNull() else None

    def __isEnableDrag(self):
        """ 根据图片的尺寸决定是否启动拖拽功能 """
        return (self.verticalScrollBar().maximum() > 0) or (self.horizontalScrollBar().maximum() > 0)

    def __setDragEnabled(self, is_enabled: bool):
        """ 设置拖拽是否启动 """
        self.setDragMode(QGraphicsView.ScrollHandDrag if is_enabled else QGraphicsView.NoDrag)

    def __getScaleRatio(self):
        """ 获取显示的图像和原始图像的缩放比例 """
        if self.pixmap.isNull():
            return 1

        pw = self.pixmap.width()
        ph = self.pixmap.height()
        rw = min(1, self.width() / pw)
        rh = min(1, self.height() / ph)
        return min(rw, rh)

    def fitInView(self, item: QGraphicsItem, mode=Qt.KeepAspectRatio):
        """ 缩放场景使其适应窗口大小 """
        super().fitInView(item, mode)
        self.displayedImageSize = self.__getScaleRatio() * self.pixmap.size() if not self.pixmap.isNull() else None
        self.zoomInTimes = 0

    def zoomIn(self, view_anchor=QGraphicsView.AnchorUnderMouse):
        """ 放大图像 """
        if self.zoomInTimes == self.maxZoomInTimes:
            return

        self.setTransformationAnchor(view_anchor)
        self.scale(1.1, 1.1)
        self.zoomInTimes += 1
        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def zoomOut(self, view_anchor=QGraphicsView.AnchorUnderMouse):
        """ 缩小图像 """
        if self.zoomInTimes == 0:
            return

        self.setTransformationAnchor(view_anchor)
        self.zoomInTimes -= 1

        # 获取原始图像和当前显示的图像大小
        original_size = self.pixmap.size()
        current_size = self.displayedImageSize

        # 计算新的缩放后的图像大小
        new_size = current_size * (1 / 1.1)

        # 判断是否允许继续缩小
        if self.width() < original_size.width() or self.height() < original_size.height():
            # 窗口尺寸小于原始图像时
            if new_size.width() <= self.width() and new_size.height() <= self.height():
                # 如果缩小后图像仍然适合窗口，则直接适应视图
                self.fitInView(self.pixmapItem)
            else:
                # 否则只缩小到窗口大小
                self.scale(1 / 1.1, 1 / 1.1)
        else:
            # 窗口尺寸大于或等于原始图像时
            if new_size.width() <= original_size.width() and new_size.height() <= original_size.height():
                # 如果缩小后图像仍然大于或等于原始大小，则重置变换
                self.resetTransform()
            else:
                # 否则继续缩小
                self.scale(1 / 1.1, 1 / 1.1)

                # 更新显示的图像大小
        self.displayedImageSize = new_size

        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ImageViewer()
    w.show()
    sys.exit(app.exec_())
