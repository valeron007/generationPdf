from PyPDF4 import PdfFileWriter, PdfFileReader
from PyPDF4.generic import BooleanObject, NameObject, IndirectObject

def set_need_appearances_writer(writer: PdfFileWriter):
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

infile = "DOTAZNIK_ADULT.pdf"
outfile = "DOTAZNIK_ADULT_VYPLNENY.pdf"

inputStream = open(infile, "rb")
pdf = PdfFileReader(inputStream, strict=False)
if "/AcroForm" in pdf.trailer["/Root"]:
    pdf.trailer["/Root"]["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)})

pdf2 = PdfFileWriter()
set_need_appearances_writer(pdf2)
if "/AcroForm" in pdf2._root_object:
    pdf2._root_object["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)})

field_dictionary = {"Textové pole60": "123456789"}

pdf2.addPage(pdf.getPage(0))
pdf2.updatePageFormFieldValues(pdf2.getPage(0), field_dictionary)

outputStream = open(outfile, "wb")
pdf2.write(outputStream)
inputStream.close()
outputStream.close()