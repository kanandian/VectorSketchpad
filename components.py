import constant

from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer, QRect

class Sketchpad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, constant.screen_width, constant.screen_height)
        self.setWindowTitle('vector_sketchpad')
        self.show()