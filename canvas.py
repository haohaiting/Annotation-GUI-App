"""
@author: Haiting Hao
@version: 1.0.1
@email: hh7702@rit.edu
"""

# import PyQt5 libraries
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)

        self.begin = QPoint()
        self.end = QPoint()
        self.show_top_left = QPoint()
        self.show_bottom_right = QPoint()
        self.top_left = QPoint()
        self.bottom_right = QPoint()

        self.originalWidth = -1
        self.originalHeight = -1
        self.xoffset = 0.0
        self.yoffset = 0.0
        self.xscale = 1.0
        self.yscale = 1.0

        self.drawing = False
        self.load = False
        self.repaint()
        
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.drawing:
            p = QPainter(self)
            p.setRenderHint(QPainter.Antialiasing)
            p.setRenderHint(QPainter.HighQualityAntialiasing)
            p.setRenderHint(QPainter.SmoothPixmapTransform)
            br = QBrush(QColor(100, 10, 10, 40))
            p.setBrush(br)
            p.drawRect(QRect(self.begin, self.end))
        elif self.load == False and self.begin != QPoint() and self.end != QPoint():
            p = QPainter(self)
            br = QBrush(QColor(100, 10, 10, 40))
            p.setBrush(br)
            p.drawRect(QRect(self.show_top_left, self.show_bottom_right))
        elif self.load:
            p = QPainter(self)
            br = QBrush(QColor(100, 10, 10, 40))
            p.setBrush(br)
            # print(self.show_top_left, self.show_bottom_right)
            p.drawRect(QRect(self.show_top_left, self.show_bottom_right))
            self.load = False

    def mousePressEvent(self, event):
        if self.drawing:
            self.begin = event.pos()
            # print("Begin", self.begin.x(), self.begin.y())
            self.end = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing:
            self.end = event.pos()
            self.update()

            self.drawing = False
            self.calculateOffsets()
            self.calculateScaleFactors()
            self.calculateRealCoordinate()
            self.calculateShowCoordinate()
            QLabel.mouseReleaseEvent(self, event)

    def calculateOffsets(self):
        self.xoffset = (self.parent().parent().width() -
                        self.pixmap().size().width()) / 2
        self.yoffset = (self.parent().parent().height() -
                        self.pixmap().size().height()) / 2

    def calculateScaleFactors(self):
        self.xscale = self.pixmap().size().width() / self.originalWidth
        self.yscale = self.pixmap().size().height() / self.originalHeight

    def calculateRealCoordinate(self):
        x1, y1, x2, y2 = self.findTopLeftAndBottomRightPoint()

        # handle offsets
        x1 -= self.xoffset
        y1 -= self.yoffset
        x2 -= self.xoffset
        y2 -= self.yoffset
        
        # snap to pixmap size
        x1, y1 = self.snapRealPointToPixmap(x1, y1)
        x2, y2 = self.snapRealPointToPixmap(x2, y2)

        # handle scale factor
        x1 /= self.xscale
        y1 /= self.yscale
        x2 /= self.xscale
        y2 /= self.yscale

        self.top_left = QPoint(int(x1), int(y1))
        self.bottom_right = QPoint(int(x2), int(y2))

    def calculateShowCoordinate(self):
        x1, y1, x2, y2 = self.findTopLeftAndBottomRightPoint()

        # snap to pixmap size
        x1, y1 = self.snapShowPointToPixmap(x1, y1)
        x2, y2 = self.snapShowPointToPixmap(x2, y2)

        self.show_top_left = QPoint(int(x1), int(y1))
        self.show_bottom_right = QPoint(int(x2), int(y2))

    def transformToShowPoints(self):
        self.calculateOffsets()
        self.calculateScaleFactors()
        
        x1 = self.top_left.x() * self.xscale + self.xoffset
        y1 = self.top_left.y() * self.yscale + self.yoffset
        x2 = self.bottom_right.x() * self.xscale + self.xoffset
        y2= self.bottom_right.y() * self.yscale + self.yoffset

        self.show_top_left = QPoint(int(x1), int(y1))
        self.show_bottom_right = QPoint(int(x2), int(y2))

        print(self.show_top_left, self.show_bottom_right)
        
    def findTopLeftAndBottomRightPoint(self):
        # find the top-left and bottom right point of the rectangle
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        return x1, y1, x2, y2

    def snapRealPointToPixmap(self, x, y):
        if x < 0 or x > self.pixmap().size().width() or \
            y < 0 or y > self.pixmap().size().height():

            x = max(x, 0)
            y = max(y, 0)
            x = min(x, self.pixmap().size().width())
            y = min(y, self.pixmap().size().height())

        return x, y

    def snapShowPointToPixmap(self, x, y):
        if x < self.pixmap().size().width() or \
                y < 0 or y > self.pixmap().size().height():

            x = max(x, self.xoffset)
            y = max(y, self.yoffset)
            x = min(x, self.pixmap().size().width() + self.xoffset - 2)
            y = min(y, self.pixmap().size().height() + self.yoffset - 2)

        return x, y
