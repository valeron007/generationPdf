# This is a sample Python script.
import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from PyPDF4.generic import NameObject, BooleanObject, IndirectObject
from PyPDF4.generic import TextStringObject
import sys
import base64
import fabricMethod.MyApplication as myapplication

"""
    поля для заполнения
    |имя поля в файле | имя поля в самой форме
    1. наименование оборудования | модель
    2. Серийный номер | serial_number
    3. принимаемого в эксплуатацию от отдела | personnel_number
    4. отделу | Табельный номер отдела
    5. имеет инвентарный номер | inv_number
    6. персональная стоимость | cost
    7. должность | Должность
    8. должность(принимающего) | tenure
    9. Табельный номер | Personnel
    10. Табельный номер | receiving
    11. ФИО | initials
    12. ФИО | receivingInitials

"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        app = myapplication.MyApplication()
        act_pdf = app.create_document(sys.argv[1], [x for x in sys.argv])  # Open document format
        act_pdf.setAct()
        act_pdf.setActPdf()

        writer = PdfFileWriter()
        reader = PdfFileReader("template2.pdf", strict=False)
        # number_of_pages = len(reader.pages)
        # page = reader.pages[0]
        if "/AcroForm" in reader.trailer["/Root"]:
            reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)}
            )

        catalog = writer._root_object
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)

        if "/AcroForm" in writer._root_object:
            writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        writer.appendPagesFromReader(reader)
        """
        page = writer.getPage(0)

        fields = reader.getFields()
        annot = page['/Annots']
        # objects = reader.resolved_objects
        # dictionary = reader.get_form_text_fields()
        
        for annot in page["/Annots"]:
            writer_annot = annot.getObject()
            field = writer_annot["/T"]

            if writer_annot["/FT"] == "/Btn":
                value = act_pdf.getValueField(writer_annot['/TU'])
                if value != None:
                    writer_annot.update(
                        {
                            NameObject("/AS"): NameObject("/On"),
                            NameObject("/V"): NameObject("/On"),
                        }
                    )
            elif writer_annot["/FT"] == "/Tx":
                value = act_pdf.getValueField(writer_annot['/T'])
                if value != None:
                    writer_annot.update(
                        {
                            NameObject("/V"): TextStringObject(value),
                        }
                    )
        """
        writer.updatePageFormFieldValues(writer.getPage(0), act_pdf.act_pdf)

        with open("templates/1.pdf", "wb") as f:
            writer.write(f)

        with open("templates/1.pdf", "rb") as pdfFile:
            pdf_encode = base64.b64encode(pdfFile.read()).decode('utf-8')

        result = {}
        result["pdf"] = pdf_encode
        content = json.dumps(result)
        print(content)
    except BaseException as e:
        print(e)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Наименование оборудования - наименование(equipment)
серийный номер - серийный номер(equipment)
принимаемого в эксплуатацию от отдела - мвз caller
отделу - мвз если передача оборудования от пользователя к пользователю то ивз получаемого пользователя
если на склад то мвз склада
Москва - RU751OPR41
Краснодар - RU751OPR43
Воронеж - RU751OPR42 

передано должность: - должность caller
Табельный номер - serial number caller

получено
если передаётся человеку то заполняем должгность, Табельный номер, ФИО:
если передача на склад то поля не заполняются


arguments
"lenovo l15gen2" "PF37W6M3" "RU751DG503" "программист" "00010461" "Andryuschenko Valeriy" "RU751IN2A2" "developer" "1233333" "Nikolay Mamchenko"

"""
