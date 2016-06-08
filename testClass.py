import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		self.setGeometry(50,150,767,200)
		self.setWindowTitle("Awesome window class")
		self.setWindowIcon( QIcon("pycon.svg") )
		self.show();
		

app = QApplication(sys.argv)
mainWindow = Window()

sys.exit(app.exec_())