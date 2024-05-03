import json
import sys

import config
from employee import EmployeeData as data
from generateStamp.CreatorStamp import CreatorStamp
from generateStamp import drawing_stamp as draw
from generateStamp.createStampPdf import CreateStampPdf
import logging

from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from PyPDF4.generic import NameObject, BooleanObject, IndirectObject

if __name__ == '__main__':
    try:
        employee_data = data.EmployeeData([x for x in sys.argv])
        employee_data.set_data()
        employee_data.add_name_folder()

        input_file = config.path_template + employee_data.get_folder() + '\\' + employee_data.get_equipment() + '.pdf'
        writer = PdfFileWriter()
        reader = PdfFileReader(input_file, strict=False)
        data_pdf = employee_data.get_data()
        act_pdf = {"tenure": data_pdf['job_title'], "receivingInitials": data_pdf['fio'],
                   "receiving": data_pdf['number']}
        if data_pdf['warehouse'] == 'yes':
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
            writer.updatePageFormFieldValues(writer.getPage(0), act_pdf)

            with open(input_file, "wb") as f:
                writer.write(f)

        employee_stamp = CreatorStamp.created_stamp(employee_data.get_data(), employee_data.get_folder())
        CreateStampPdf.createPdf(employee_stamp, employee_data.get_position(), employee_data.get_folder())

        employee_signed = draw.SignDocument(employee_stamp.get_rand_name() + '_stamp.pdf',
                                            employee_data.get_equipment() + '.pdf',
                                            employee_data.get_equipment() + ".pdf",
                                            employee_data.get_folder())
        employee_signed.signed_file()

        '''
        if employee_data.get_type_act() == 'receveing':
            employee_signed.copy_act(employee_data.get_location(), employee_data.get_name_number_request())
        '''

        result = {"pdf": employee_signed.get_sign()}
        print(json.dumps(result))
    except BaseException as e:
        logging.basicConfig(level=logging.DEBUG, filename='er.log')
        logging.debug('error: %s', e)
        logging.debug([x for x in sys.argv])
