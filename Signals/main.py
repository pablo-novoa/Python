import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial

from functions import *


class Form(QDialog):

	zeros = 0

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

		#new syntaxt (require furder studie)
		self.dial.valueChanged.connect(self.spinBox.setValue)
		self.spinBox.valueChanged.connect(self.dial.setValue)
		self.spinBox.valueChanged.connect( lambda: self.someCallback(self.spinBox.value()) )

		self.show()
		self.raise_()

	def someCallback(self, valUe):
		if valUe == 0:
			self.zeros += 1
			self.textBox.setValue(self.zeros)


if __name__ == "__main__":
    rootApp = QApplication(sys.argv)
    window = Form()
    rootApp.exec_()
