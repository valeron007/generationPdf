import json
import sys
from employee import EmployeeData as data
from generateStamp.CreatorStamp import CreatorStamp
from generateStamp import drawing_stamp as draw
from generateStamp.createStampPdf import CreateStampPdf
import logging

if __name__ == '__main__':
    try:
        data_test = [x for x in sys.argv]
        employee_data = data.EmployeeData([x for x in sys.argv])
        employee_data.set_data()

        employee_data.add_name_folder()

        #fill form
        data_pdf = employee_data.get_data()
        act_pdf = {}
        act_pdf["tenure"] = data_pdf['fio']
        act_pdf["receivingInitials"] = data_pdf['job_title']
        act_pdf["receiving"] = data_pdf['number']

        employee_stamp = CreatorStamp.created_stamp(employee_data.get_data(), employee_data.get_folder())
        CreateStampPdf.createPdf(employee_stamp, employee_data.get_position(), employee_data.get_folder())

        employee_signed = draw.SignDocument(employee_stamp.get_rand_name() + '_stamp.pdf', 'main.pdf', "main.pdf", employee_data.get_folder())
        employee_signed.signed_file()

        result = {"pdf": employee_signed.get_sign()}
        print(json.dumps(result))
    except BaseException as e:
        logging.basicConfig(level=logging.DEBUG, filename='error.log')
        logging.debug('error: %s', e)
        print(json.dumps(e))

