from PyPDF2 import PdfFileReader, PdfFileWriter, PdfReader, PdfWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import sys
import base64
import fabricMethod.MyApplication as myapplication


def set_need_appearances_writer(writer):
    # See 12.7.2 and 7.7.2 for more information:
    # http://www.adobe.com/content/dam/acom/en/devnet/acrobat/
    #     pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree and add "/NeedAppearances attribute
        if "/AcroForm" not in catalog:
            writer._root_object.update(
                {
                    NameObject("/AcroForm"): IndirectObject(
                        len(writer._objects), 0, writer
                    )
                }
            )

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print("set_need_appearances_writer() catch : ", repr(e))
        return writer

app = myapplication.MyApplication()
act_pdf = app.create_document(sys.argv[1], [x for x in sys.argv])  # Open document format
act_pdf.setAct()
act_pdf.setActPdf()
print(act_pdf.act_pdf)

reader = PdfReader("template2.pdf", strict=False)
if "/AcroForm" in reader.trailer["/Root"]:
    reader.trailer["/Root"]["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)}
    )

writer = PdfWriter()
set_need_appearances_writer(writer)
if "/AcroForm" in writer._root_object:
    writer._root_object["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)}
    )

writer.add_page(reader.pages[0])

writer.update_page_form_field_values(writer.pages[0], act_pdf.act_pdf)

with open("templates/1.pdf", "wb") as fp:
    writer.write(fp)

