# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thirdWindow(object):
    def setupUi(self, thirdWindow):
        thirdWindow.setObjectName("thirdWindow")
        thirdWindow.resize(778, 415)
        self.centralwidget = QtWidgets.QWidget(thirdWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plotLabel = QtWidgets.QLabel(self.centralwidget)
        self.plotLabel.setGeometry(QtCore.QRect(200, 10, 361, 351))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.plotLabel.setFont(font)
        self.plotLabel.setObjectName("plotLabel")

        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(50, 170, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(608, 170, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")

        thirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(thirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")
        thirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(thirdWindow)
        self.statusbar.setObjectName("statusbar")
        thirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(thirdWindow)
        QtCore.QMetaObject.connectSlotsByName(thirdWindow)

    def retranslateUi(self, thirdWindow):
        _translate = QtCore.QCoreApplication.translate
        thirdWindow.setWindowTitle(_translate("thirdWindow", "MainWindow"))
        self.plotLabel.setText(_translate("thirdWindow", "Here will be a plot"))
        self.previousButton.setText(_translate("thirdWindow", "Previous plot"))
        self.nextButton.setText(_translate("thirdWindow", "Next plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thirdWindow = QtWidgets.QMainWindow()
    ui = Ui_thirdWindow()
    ui.setupUi(thirdWindow)
    thirdWindow.show()
    sys.exit(app.exec_())