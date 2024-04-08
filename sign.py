import binascii
import json
import os
import sys
from employee import EmployeeData as data
from generateStamp.CreatorStamp import CreatorStamp
from generateStamp import drawing_stamp as draw
from generateStamp.createStampPdf import CreateStampPdf
import logging

if __name__ == '__main__':
    try:
        employee_data = data.EmployeeData([x for x in sys.argv])
        employee_data.set_data()
        employee_data.add_name_folder(binascii.hexlify(os.urandom(8)).decode('utf-8'))

        CreatorStamp.create_folder_signer(employee_data.get_folder())
        CreatorStamp.copy_original_template(employee_data.get_folder())

        employee_stamp = CreatorStamp.created_stamp(employee_data.get_data(), employee_data.get_folder())
        CreateStampPdf.createPdf(employee_stamp, employee_data.get_position(), employee_data.get_folder())

        administrator_signed = draw.SignDocument(employee_stamp.get_rand_name() + '_stamp.pdf', 'main.pdf', "main.pdf", employee_data.get_folder())
        administrator_signed.signed_file()

        print(json.dumps(employee_data.get_data()))
    except BaseException as e:
        logging.basicConfig(level=logging.DEBUG, filename='error.log')
        logging.debug('error: %s', e)
        print('1111')

