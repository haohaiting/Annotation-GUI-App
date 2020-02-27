# import PyQt5 libraries
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


# CURSOR_DEFAULT = Qt.ArrowCursor
# CURSOR_POINT = Qt.PointingHandCursor
# CURSOR_DRAW = Qt.CrossCursor
# CURSOR_MOVE = Qt.ClosedHandCursor
# CURSOR_GRAB = Qt.OpenHandCursor


class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.begin = QPoint()
        self.end = QPoint()
        self.drawing = False
        # self.show()

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

    def mousePressEvent(self, event):
        if self.drawing:
            self.begin = event.pos()
            print("Begin", self.begin.x(), self.begin.y())
            self.end = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing:
            # self.begin = event.pos()
            self.end = event.pos()
            print("End", self.end.x(), self.end.y())
            self.update()
            self.drawing = False
