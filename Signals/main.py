import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from moreSignal import *


class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		self.setWindowTitle("Signal and Slot")
		# Widgets
		self.dial = QDial()
		self.dial.setNotchesVisible(True)
		self.spinBox = ZeroSpinBox()
		self.textBox = QSpinBox()

		#layout
		layout = QHBoxLayout()
		
		layout.addWidget(self.dial)
		layout.addWidget(self.spinBox)
		layout.addWidget(self.textBox)

		self.setLayout(layout)

		#Signals
		self.connect(self.dial, SIGNAL("valueChanged(int)"), self.spinBox.setValue)
		self.connect(self.spinBox, SIGNAL("valueChanged(int)"), self.dial.setValue)
		self.connect(self.spinBox, SIGNAL("atzeros(int)"), self.textBox.setValue)




if __name__ == "__main__":
    rootApp = QApplication(sys.argv)
    window = Form()
    window.show()
    window.raise_()
    rootApp.exec_()
