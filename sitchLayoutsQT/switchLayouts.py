
import sys
from PyQt4 import QtCore, QtGui
from guiElements import *

def navegationEvents(GUI):
    GUI.pushButton.clicked.connect(lambda: changeWindow(GUI, GUI.pushButton))
    GUI.pushButton_2.clicked.connect(lambda: changeWindow(GUI, GUI.pushButton_2))

def changeWindow(GUI, btn):
    stackTo = int(btn.objectName())
    GUI.stackedWidget.setCurrentIndex(stackTo)


        

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    navegationEvents(ui)

    MainWindow.show()
    sys.exit(app.exec_())

