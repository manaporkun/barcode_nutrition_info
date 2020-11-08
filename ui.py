import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'Product'

        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()
        self.layout = QVBoxLayout()

    def initUI(self):
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        title = QLabel(self, text = 'Product Informations')
        title.move(10, 10)
        title.setFont(QFont('Times', 36))
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.exect_()
        

