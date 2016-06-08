import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ZeroSpinBox(QSpinBox):
	zeros = 0

	def __init__(self, parent=None):
		super(ZeroSpinBox, self).__init__(parent)

		self.connect(self, SIGNAL("valueChanged(int)"), self.checkZero)

	def checkZero(self):
		if self.value() == 0:
			self.zeros += 1
			self.emit(SIGNAL("atzeros(int)"), self.zeros) 
