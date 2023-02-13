from PyQt5 import QtWidgets, QtCore

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("File Manager")
        MainWindow.resize(1120, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 80, 121, 41))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("File Manager", "File Manager"))
        self.button1.setText(_translate("MainWindow", "+ New File"))