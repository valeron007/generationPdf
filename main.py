import json
import sys
import fabricMethod.MyApplication as myapplication
import FillPdf.fillpdf as fill
import logging
import brcodeAct.generateBRCode as code
import config
from generateStamp.createStampPdf import CreateStampPdf
from generateStamp.drawing_stamp import SignDocument

"""
    поля для заполнения
    |имя поля в файле | имя поля в самой форме
    1. наименование оборудования | model
    2. Серийный номер | serial_number
    3. принимаемого в эксплуатацию от отдела | personnel_number
    4. отделу | tabel_number
    5. имеет инвентарный номер | inv_number
    6. персональная стоимость | cost
    7. должность | job_title
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
        act_pdf = app.create_document(sys.argv[1], [x for x in sys.argv])
        act_pdf.setAct()
        act_pdf.setActPdf()
        fillPdf = fill.FillPdf(act_pdf)
        fillPdf.create_folder()
        # config.path_template + self.act_data.act['number']
        fillPdf.copy_empty_template()
        fillPdf.fill_template()
        fillPdf.writePdf()

        # generate brcode
        gen_code = code.GenerateCode(config.path_template + act_pdf.act['number'], act_pdf.act['serial_number'])
        gen_code.generate_image_code()
        # generate pdf brcode
        CreateStampPdf.create_brcode_pdf(gen_code.path_image, gen_code.brcode_pdf,
                                         {'x': 400, 'y': 750}, 150, 50, act_pdf.act['number'])

        # brcode added
        act_file_path = config.path_template + act_pdf.act['number'] + '\\' + act_pdf.act['equipment'] + '.pdf'
        brcode_file_path = config.path_template + act_pdf.act['number'] + '\\' + act_pdf.act['serial_number'] + '_brcode.pdf'
        SignDocument.added_brcode(act_file_path, brcode_file_path)

        result = {"pdf": fillPdf.getPdfBaseEncode()}
        content = json.dumps(result)
        print(content)
    except BaseException as e:
        logging.basicConfig(level=logging.DEBUG, filename='error.log')
        logging.debug('error: %s', e)
        logging.debug([x for x in sys.argv])
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
