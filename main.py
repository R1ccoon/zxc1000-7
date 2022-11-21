import math
import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.lodaui('ui.ui', self)

    def mouseMoveEvent(self, event):
        self.point = event.x(), event.y()

    def mousePressEvent(self, event):
        self.point = event.x(), event.y()
        if event.button() == Qt.LeftButton:
            self.kn = 1
        if event.button() == Qt.RightButton:
            self.kn = 0
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.kn = 2
        self.update()

    def paintEvent(self, event):

        if self.kn == 0:
            x, y = self.point
            # Рисовать будем на самом себе
            painter = QPainter(self)
            s = random.randint(10, 100)
            # Для рисования точки хватит setPen, но для других фигур (типо rect) понадобится setBrush
            painter.setPen(QPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), s))
            # Рисование точки
            painter.drawPoint(x, y)

        elif self.kn == 1:
            painter = QPainter(self)
            x, y = self.point
            s = random.randint(10, 100)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setPen(QPen(color, 8, Qt.SolidLine))
            painter.setBrush(QBrush(color, Qt.SolidPattern))

            painter.drawEllipse(x, y, s, s)

        elif self.kn == 2:
            self.drawing.begin(self)
            s = random.randint(10, 150)
            r = a = s
            x, y = self.point
            self.drawing.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            coordss = [(x, y + r ), (x + a, y - r), (x - a, y - r)]
            path = QPainterPath()
            path.moveTo(*coordss[0])
            path.lineTo(*coordss[1])
            path.lineTo(*coordss[2])
            self.drawing.drawPath(path)
            self.drawing.end()


if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()

    app.exec()
    sys.exit(app.exec())