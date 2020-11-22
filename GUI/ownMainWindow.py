import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("C:/Users/Julia/Desktop/mainWindow.ui", self)

    def browseFiles(self):
        fileName = QFileDialog.getOpenFileName(self, "Open file", "C:/Users/Julia/Desktop", "ascii files (*.asc)")
        self.pathLineEdit.setText(fileName[0])


app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)

widget.setFixedWidth(1273)
widget.setFixedHeight(948)
widget.show()
sys.exit(app.exec_())
