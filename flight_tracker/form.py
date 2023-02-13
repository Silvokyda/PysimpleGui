from PyQt5.QtWidgets import *

class Form(QDialog):
    """Show a pop-up form for the user to input file data."""
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, parent=None):
        super().__init__(parent)
        self.input_1 = QLineEdit(self)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok |
                                       QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.formbox = QGroupBox("Please provide data below: ")
        layout = QFormLayout()
        layout.addRow(QLabel("Business name: "), self.input_1)
        layout.addRow(QLabel("Customer name: "), self.input_2)
        self.formbox.setLayout(layout) 

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.formbox)
        main_layout.addWidget(self.button_box)
        self.setLayout(main_layout)

    def get_input_1(self):
        return self.input_1.text()

    def get_input_2(self):
        return self.input_2.text()