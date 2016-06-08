import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from guiElements import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Main Window")
        #self.showMaximized()
        self.callWindowComponenst()

    def callWindowComponenst(self):
        #create widget element
        self.radio_buttons = RadioButtonWidget("Title", "Lorem impusm text", ("btn 1", "btn 2"))
        #create layout for the widget
        self.main_layout = QVBoxLayout()
        #add widget to the layout
        self.main_layout.addWidget(self.radio_buttons)
        #add layout to window
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)        

def initWindow():
    rootApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    rootApp.exec_()

if __name__ == "__main__":
    initWindow()