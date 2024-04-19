import base64

from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from PyPDF4.generic import NameObject, BooleanObject, IndirectObject
from pdfrw import PdfReader, PdfWriter, PageMerge
import config

class SignDocument:
    def __init__(self, stamp: str, input_name: str, output: str, folder: str):
        self.stamp_file = config.path_template + folder + '\\' + stamp
        self.input_file = config.path_template + folder + '\\' + input_name
        self.output_file = config.path_template + folder + '\\' + output
        self.reader_input = PdfReader(self.input_file)
        self.watermark_input = PdfReader(self.stamp_file)
        self.page_stamp = self.watermark_input.pages[0]
        self.writer_file = PdfWriter()
        #for update form
        self.writer = PdfFileWriter()
        self.reader = PdfFileReader(self.input_file, strict=False)

    def signed_file(self):
        for current_page in range(len(self.reader_input.pages)):
            merge_page = PageMerge(self.reader_input.pages[current_page])
            merge_page.add(self.page_stamp).render()

        # write the modified content to disk
        self.writer_file.write(self.output_file, self.reader_input)

    def get_sign(self):
        with open(self.output_file, "rb") as pdfFile:
            pdf_encode = base64.b64encode(pdfFile.read()).decode('utf-8')

        return pdf_encode

    def fill_form(self, act_pdf):
        if "/AcroForm" in self.reader.trailer["/Root"]:
            self.reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)}
            )
        self.catalog = self.writer._root_object

        if "/AcroForm" not in self.catalog:
            self.writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(self.writer._objects), 0, self.writer)})

        need_appearances = NameObject("/NeedAppearances")
        self.writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)

        if "/AcroForm" in self.writer._root_object:
            self.writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        self.writer.appendPagesFromReader(self.reader)
        self.writer.updatePageFormFieldValues(self.writer.getPage(0), act_pdf)

        self.writePdf()

    def writePdf(self):
        with open(self.input_file, "wb") as f:
            self.writer.write(f)