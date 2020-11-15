# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from GUI.thirdWindow import Ui_thirdWindow


class Ui_secondWindow(object):
    # function opening third window (after pushing a button)
    def openThirdWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_thirdWindow()
        self.ui.setupUi(self.window)
        secondWindow.hide()
        self.window.show()

    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.resize(778, 415)
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.orderLabel = QtWidgets.QLabel(self.centralwidget)
        self.orderLabel.setGeometry(QtCore.QRect(100, 110, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orderLabel.setFont(font)
        self.orderLabel.setObjectName("orderLabel")

        self.method1RadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.method1RadioButton.setGeometry(QtCore.QRect(100, 160, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.method1RadioButton.setFont(font)
        self.method1RadioButton.setChecked(True)
        self.method1RadioButton.setObjectName("method1RadioButton")

        self.method2RadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.method2RadioButton.setGeometry(QtCore.QRect(100, 200, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.method2RadioButton.setFont(font)
        self.method2RadioButton.setObjectName("method2RadioButton")

        self.method3RadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.method3RadioButton.setGeometry(QtCore.QRect(100, 240, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.method3RadioButton.setFont(font)
        self.method3RadioButton.setObjectName("method3RadioButton")

        self.detectButton = QtWidgets.QPushButton(self.centralwidget)
        self.detectButton.setGeometry(QtCore.QRect(460, 330, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.detectButton.setFont(font)
        self.detectButton.setObjectName("detectButton")

        # connecting clicking detectButton with function which opens third window (openThirdWindow)
        self.detectButton.clicked.connect(self.openThirdWindow)

        secondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(secondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")
        secondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "MainWindow"))
        self.orderLabel.setText(_translate("secondWindow", "Please choose the detection method you want your file to be processed with:"))
        self.method1RadioButton.setText(_translate("secondWindow", "Method 1"))
        self.method2RadioButton.setText(_translate("secondWindow", "Method 2"))
        self.method3RadioButton.setText(_translate("secondWindow", "Method 3"))
        self.detectButton.setText(_translate("secondWindow", "Detect artifacts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
