from PyQt5.QtWidgets import *
from form import Form
import os

class Doc(QInputDialog):
    """Create an doc and populate it based on user input."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.work_dir = os.path.join("C:\\", "Document Manager", "Work environment")
        self.dialog = Form()
        self.template_path = 'invoice_template.pdf'
        input_1 = self.dialog.get_input_1()
        self.data_dict = {
            'business_name_1': f"{input_1}",
            'customer_name': 'company.io'}

        new_pdf = self.process_pdf(self.template_path)
        self.dialog.accepted.connect(lambda: self.produce_invoice(self.output_path, new_pdf))

    def write_custom_pdf(self):
        """Create an invoice based on a pdf template."""
        user_input = QInputDialog()
        active = True
        while active:
            text, ok = user_input.getText(self, "Invoice name", "Please enter a name")
            if ok and text != '':
                self.name = text
                self.output_path = f"{self.work_dir}" + "\\" + f"{self.name}" + ".pdf"
                if not os.path.exists(self.output_path):
                    self.open_dialog()
                    active = False
                else:
                    self.show_popup()
            else:
                active = False

    def open_dialog(self):
        if self.dialog.exec_():
            self.data_dict['business_name_1'] = self.dialog.get_input_1()
            newpdf = self.process_pdf(self.template_path)
            self.produce_invoice(self.output_path, newpdf)

    def process_pdf(self, template_path):
        template_pdf = pdfrw.PdfReader(template_path)
        template_pdf.Root.AcroForm.update(
            pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        annotations = template_pdf.pages[0][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in self.data_dict.keys():
                        annotation.update(pdfrw.PdfDict(
                            V=f"{self.data_dict[key]}"))
        return template_pdf

    def produce_invoice(self, output_path, new_pdf):
        new_invoice = pdfrw.PdfWriter().write(output_path, new_pdf)
        return new_invoice