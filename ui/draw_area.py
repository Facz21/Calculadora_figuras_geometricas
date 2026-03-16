from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt


class DrawArea(QWidget):

    def __init__(self):
        super().__init__()
        self.shape = None

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        pen = QPen(Qt.GlobalColor.black, 2)
        painter.setPen(pen)

        w = self.width()
        h = self.height()

        if self.shape == "circle":
            painter.drawEllipse(w//4, h//4, w//2, h//2)

        elif self.shape == "square":
            painter.drawRect(w//4, h//4, w//2, w//2)

        elif self.shape == "triangle":
            painter.drawLine(w//2, h//4, w//4, 3*h//4)
            painter.drawLine(w//2, h//4, 3*w//4, 3*h//4)
            painter.drawLine(w//4, 3*h//4, 3*w//4, 3*h//4)

        elif self.shape == "cube":
            painter.drawRect(80,80,120,120)
            painter.drawRect(120,40,120,120)