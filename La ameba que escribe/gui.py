# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Jun 20 00:58:13 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"    background-color: #303039;\n"
"}\n"
"QLabel{\n"
"    color:#fff;\n"
"}\n"
"QPushButton{\n"
"    border:1px solid #ffffff;\n"
"    background-color: transparent;\n"
"    color:#ffffff;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:visited{\n"
"    background-color: #86ba6a;\n"
"    border: 1px solid #86ba6a;\n"
"    color: #303039;\n"
"}\n"
""))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.initial = QtGui.QWidget()
        self.initial.setObjectName(_fromUtf8("initial"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.initial)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(self.initial)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("img1.svg")))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gitBtn = QtGui.QPushButton(self.initial)
        self.gitBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gitBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gitBtn.setAutoDefault(False)
        self.gitBtn.setDefault(False)
        self.gitBtn.setFlat(False)
        self.gitBtn.setObjectName(_fromUtf8("gitBtn"))
        self.verticalLayout.addWidget(self.gitBtn)
        self.htaccessBtn = QtGui.QPushButton(self.initial)
        self.htaccessBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.htaccessBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.htaccessBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.htaccessBtn.setObjectName(_fromUtf8("htaccessBtn"))
        self.verticalLayout.addWidget(self.htaccessBtn)
        self.birraBtn = QtGui.QPushButton(self.initial)
        self.birraBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.birraBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.birraBtn.setMouseTracking(False)
        self.birraBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.birraBtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.birraBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.birraBtn.setObjectName(_fromUtf8("birraBtn"))
        self.verticalLayout.addWidget(self.birraBtn)
        spacerItem3 = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.initial)
        self.editor = QtGui.QWidget()
        self.editor.setObjectName(_fromUtf8("editor"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.editor)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.editPageTitle = QtGui.QLabel(self.editor)
        self.editPageTitle.setObjectName(_fromUtf8("editPageTitle"))
        self.horizontalLayout_5.addWidget(self.editPageTitle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.textEdit = QtGui.QPlainTextEdit(self.editor)
        self.textEdit.setPlainText(_fromUtf8(""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.backBtn = QtGui.QPushButton(self.editor)
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setMouseTracking(False)
        self.backBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.horizontalLayout_4.addWidget(self.backBtn)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.fileLocation = QtGui.QLineEdit(self.editor)
        self.fileLocation.setObjectName(_fromUtf8("fileLocation"))
        self.horizontalLayout_4.addWidget(self.fileLocation)
        self.editLocation = QtGui.QToolButton(self.editor)
        self.editLocation.setObjectName(_fromUtf8("editLocation"))
        self.horizontalLayout_4.addWidget(self.editLocation)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.saveBtn = QtGui.QPushButton(self.editor)
        self.saveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout_4.addWidget(self.saveBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.editor)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "La ameba que escribe", None))
        self.gitBtn.setText(_translate("MainWindow", ".gitignore", None))
        self.htaccessBtn.setText(_translate("MainWindow", ".htaccess", None))
        self.birraBtn.setText(_translate("MainWindow", "birra", None))
        self.editPageTitle.setText(_translate("MainWindow", ".gitignore", None))
        self.backBtn.setText(_translate("MainWindow", "Atras", None))
        self.editLocation.setText(_translate("MainWindow", "...", None))
        self.saveBtn.setText(_translate("MainWindow", "Guardar", None))

