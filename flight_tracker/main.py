from PyQt5 import QtWidgets, QtCore
from gui import UiMainWindow
from excel import Doc
import sys

class Logic(QtWidgets.QMainWindow, UiMainWindow, Doc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button1.clicked.connect(self.write_custom_pdf)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    logic = Logic()
    logic.show()
    sys.exit(app.exec_())