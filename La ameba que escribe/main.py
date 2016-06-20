import sys
from PyQt4 import QtCore, QtGui
from gui import *

files = {
	'gitBtn' : '.gitignore',
	'htaccessBtn' : '.htaccess'
}


def navegationEvents(GUI):
    GUI.gitBtn.clicked.connect(lambda: changeWindow(GUI, 1, file=GUI.gitBtn))
    GUI.htaccessBtn.clicked.connect(lambda: changeWindow(GUI, 1, file=GUI.htaccessBtn))
    GUI.birraBtn.clicked.connect(lambda: changeWindow(GUI, 1))
    GUI.backBtn.clicked.connect(lambda: changeWindow(GUI, 0))

def changeWindow(GUI, to, **kargs):
    # Reset editor
    GUI.textEdit.setPlainText(" ")
    GUI.editPageTitle.setText(" ")
	# Move to editor
    GUI.stackedWidget.setCurrentIndex(to)
    # Get Content to editor
    btn = kargs.get('file', None)

    if type(btn) is QtGui.QPushButton:
    	btnName = str(btn.objectName())
    	fileName = files[btnName]

    	fileContent = open(fileName, 'r').read()

    	GUI.editPageTitle.setText(fileName)
    	GUI.textEdit.setPlainText(fileContent)




        

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    navegationEvents(ui)

    MainWindow.show()
    sys.exit(app.exec_())