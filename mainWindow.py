# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import shutil

from EEGData import *


class Ui_MainWindow(object):
    inputData = []
    isArtifactOutput = []
    message = ""
    resultsPath = ""
    detectionMethod = "performEEPDetection"
    blockNumber = 0
    fileList = []
    index = 0

    EEG = None

    def browseFiles(self):
        self.warnLabel.setText("")

        fileName = QFileDialog.getOpenFileName(self.centralwidget, "Open file", "C:/Users/" + getpass.getuser() +
            "/Desktop", "ascii or txt files (*.asc *.txt)")
        path = fileName[0]
        if path is not None:
            if not dE.checkFile(path):
                self.warnLabel.setText("You chose a file which doesn't contain EEG examination data. Please "
                                       "choose a proper file.")

            else:
                self.pathLineEdit.setText(path)

                global EEG
                EEG = EEGData(path)

                self.browseButton.setEnabled(False)
                self.uploadButton.setEnabled(True)
                if path.endswith("txt"):
                    self.methodComboBox.model().item(1).setEnabled(False)
                if path.endswith("asc"):
                    self.methodComboBox.model().item(1).setEnabled(True)

    def uploadFile(self):
        self.inputData = EEG.getInputData()

        self.uploadButton.setEnabled(False)
        self.methodComboBox.setEnabled(True)
        self.performButton.setEnabled(True)

    def chooseDetectionMethod(self):
        currIndex = self.methodComboBox.currentIndex()
        if currIndex == 0:
            self.detectionMethod = "performEEPDetection"
        elif currIndex == 1:
            self.detectionMethod = "performECGDetection"
            self.warnLabel.setText("Please wait, it might take a while...")
        elif currIndex == 2:
            self.detectionMethod = "performLFPDetection"

        self.methodComboBox.setEnabled(False)

    def performDetection(self):
        self.methodComboBox.setEnabled(False)

        if self.detectionMethod == "performEEPDetection":
            result = EEG.performEEPDetection()
        elif self.detectionMethod == "performECGDetection":
            result = EEG.performECGDetection()
        elif self.detectionMethod == "performLFPDetection":
            result = EEG.performLFPDetection()

        self.isArtifactOutput = result[0]
        self.blockNumber = len(self.isArtifactOutput)
        self.message = result[1]

        print(self.isArtifactOutput)
        print(self.blockNumber)
        print(self.message)

        EEG.plotAllBlocks()

        self.resultsPath = EEG.getResultsPath()

        self.performButton.setEnabled(False)
        self.showButton.setEnabled(True)

    def showPlot(self):
        self.showButton.setEnabled(False)
        self.nextButton.setEnabled(True)
        self.previousButton.setEnabled(True)
        self.againButton.setEnabled(True)

        dir = self.resultsPath

        for file in os.listdir(dir):
            fpath = os.path.join(dir, file)
            if os.path.isfile(fpath):
                self.fileList.append(fpath)

        self.fileList.sort(key=aF.sortList)

        pixmap = QtGui.QPixmap(self.fileList[self.index])
        self.plotLabel.setScaledContents(True)
        self.plotLabel.setPixmap(pixmap)

    def nextPlot(self):
        if self.fileList:
            try:
                self.index += 1
                filename = self.fileList[self.index]
                pixmap = QtGui.QPixmap(filename)
                if pixmap.isNull():
                    self.fileList.remove(filename)
                    self.nextPlot()
                else:
                    self.plotLabel.setScaledContents(True)
                    self.plotLabel.setPixmap(pixmap)
            except:
                # iteration is finished, restart it
                # self.dirIterator = iter(self.fileList)
                self.index = -1
                self.nextPlot()
        else:
            # no file list found, load an image
            self.showPlot()

    def previousPlot(self):
        if self.fileList:
            try:
                self.index -= 1
                filename = self.fileList[self.index]
                pixmap = QtGui.QPixmap(filename)
                if pixmap.isNull():
                    # the file is not a valid image, remove it from the list
                    # and try to load the next one
                    self.fileList.remove(filename)
                    self.previousPlot()
                else:
                    self.plotLabel.setScaledContents(True)
                    self.plotLabel.setPixmap(pixmap)
            except:
                # the iterator has finished, restart it
                # self.dirIterator = iter(self.fileList)
                self.index = 0
                self.previousPlot()
        else:
            # no file list found, load an image
            self.showPlot()

    def performAgain(self):
        self.deleteResultsFiles()

        self.inputData = []
        self.isArtifactOutput = []
        self.message = ""
        self.resultsPath = ""
        self.detectionMethod = "performEEPDetection"
        self.blockNumber = 0
        self.fileList = []
        self.index = 0

        self.pathLineEdit.setText("")
        self.plotLabel.clear()
        self.warnLabel.setText("")

        self.nextButton.setEnabled(False)
        self.previousButton.setEnabled(False)
        self.againButton.setEnabled(False)
        self.browseButton.setEnabled(True)

    def deleteResultsFiles(self):
        folder = self.resultsPath
        """for filename in os.listdir(folder):
            fpath = os.path.join(folder, filename)
            try:
                if os.path.isfile(fpath) or os.path.islink(fpath):
                    os.unlink(fpath)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (fpath, e))"""

        shutil.rmtree(folder, ignore_errors=True)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1442, 1019)
        MainWindow.setFixedSize(1442, 1019)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")





        self.pathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(10, 20, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pathLineEdit.setFont(font)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.pathLineEdit.setReadOnly(True)



        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(390, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")

        # connecting clicking browseButton with function which browses file (browseFiles)
        self.browseButton.clicked.connect(self.browseFiles)





        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(530, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uploadButton.setFont(font)
        self.uploadButton.setObjectName("uploadButton")
        self.uploadButton.setEnabled(False)

        # connecting clicking uploadButton with function which uploads file (uploadFile)
        self.uploadButton.clicked.connect(self.uploadFile)





        self.methodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.methodComboBox.setGeometry(QtCore.QRect(680, 20, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.methodComboBox.setFont(font)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.setCurrentIndex(0)
        self.methodComboBox.setEnabled(False)

        self.methodComboBox.activated.connect(self.chooseDetectionMethod)




        self.performButton = QtWidgets.QPushButton(self.centralwidget)
        self.performButton.setGeometry(QtCore.QRect(1090, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.performButton.setFont(font)
        self.performButton.setObjectName("performButton")
        self.performButton.setEnabled(False)

        # connecting clicking performButton with function which performs artifact's detection (performDetection)
        self.performButton.clicked.connect(self.performDetection)




        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(10, 450, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")
        self.previousButton.setEnabled(False)

        # connecting clicking previousButton with function which shows previous plot (previousPlot)
        self.previousButton.clicked.connect(self.previousPlot)



        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(1360, 450, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setEnabled(False)

        # connecting clicking nextButton with function which shows next plot (nextPlot)
        self.nextButton.clicked.connect(self.nextPlot)





        self.plotLabel = QtWidgets.QLabel(self.centralwidget)
        self.plotLabel.setGeometry(QtCore.QRect(100, 130, 1241, 876))
        self.plotLabel.setText("")
        self.plotLabel.setObjectName("plotLabel")





        self.showButton = QtWidgets.QPushButton(MainWindow)
        self.showButton.setGeometry(QtCore.QRect(10, 70, 710, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showButton.setFont(font)
        self.showButton.setObjectName("showButton")
        self.showButton.setEnabled(False)

        # connecting clicking showButton with function which shows plots (showPlot)
        self.showButton.clicked.connect(self.showPlot)



        self.againButton = QtWidgets.QPushButton(MainWindow)
        self.againButton.setGeometry(QtCore.QRect(729, 70, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.againButton.setFont(font)
        self.againButton.setObjectName("againButton")
        self.againButton.setEnabled(False)

        # connecting clicking againButton with function which performs detection again (performAgain)
        self.againButton.clicked.connect(self.performAgain)

        self.warnLabel = QtWidgets.QLabel(MainWindow)
        self.warnLabel.setGeometry(QtCore.QRect(10, 110, 711, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.warnLabel.setFont(font)
        self.warnLabel.setObjectName("warnLabel")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Artifact detection in EEG"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.uploadButton.setText(_translate("MainWindow", "Upload file"))
        self.methodComboBox.setItemText(0, _translate("MainWindow", "Method 1: detect external electrostatic potentials"))
        self.methodComboBox.setItemText(1, _translate("MainWindow", "Method 2: detect potentials derived from ECG"))
        self.methodComboBox.setItemText(2, _translate("MainWindow", "Method 3: detect low-frequency potentials"))
        self.performButton.setText(_translate("MainWindow", "Perform artifact detection"))
        self.previousButton.setText(_translate("MainWindow", "Previous"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.showButton.setText(_translate("MainWindow", "Show plots containing artifacts"))
        self.againButton.setText(_translate("MainWindow", "Perform detection again"))
        self.warnLabel.setText(_translate("MainWindow", ""))

    def __del__(self):
        print("deleting")
        self.deleteResultsFiles()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
