from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from PyPDF4.generic import NameObject, BooleanObject, IndirectObject

from fabricMethod.Act import Act
import base64
import config
import os
import shutil
class FillPdf:
    def __init__(self, data: Act):
        self.writer = PdfFileWriter()
        self.reader = PdfFileReader(config.path_template + "main.pdf", strict=False)
        self.pdf_encode = None
        self.act_data = data

    def create_folder(self):
        os.mkdir(config.path_template + self.act_data.act['number'])

    def copy_empty_template(self):
        shutil.copyfile(config.path_template + "main.pdf", config.path_template + self.act_data.act['number'] + "\\main.pdf")

    #field form and save document
    def fill_template(self):
        self.setUpdateRoot()
        self.catalog = self.writer._root_object
        self.setUpdateCatalog()
        need_appearances = NameObject("/NeedAppearances")
        self.writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        self.needAppearances()
        self.writer.appendPagesFromReader(self.reader)
        self.writer.updatePageFormFieldValues(self.writer.getPage(0), self.act_data.act_pdf)

    def setUpdateRoot(self):
        if "/AcroForm" in self.reader.trailer["/Root"]:
            self.reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)}
            )

    def setUpdateCatalog(self):
        if "/AcroForm" not in self.catalog:
            self.writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(self.writer._objects), 0, self.writer)})

    def needAppearances(self):
        need_appearances = NameObject("/NeedAppearances")
        self.writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)

        if "/AcroForm" in self.writer._root_object:
            self.writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

    def writePdf(self):
        with open(config.path_template + self.act_data.act['number'] + "\\main.pdf", "wb") as f:
            self.writer.write(f)

    def getPdfBaseEncode(self):
        with open(config.path_template + self.act_data.act['number'] + "\\main.pdf", "rb") as pdfFile:
            self.pdf_encode = base64.b64encode(pdfFile.read()).decode('utf-8')

        return self.pdf_encode
