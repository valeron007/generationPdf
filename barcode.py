import brcodeAct
import config
from brcodeAct.generateBRCode import GenerateCode
from generateStamp.createStampPdf import CreateStampPdf

request = 'REQ0007819'
path = config.path_template + request
brcode = GenerateCode(path, 'test12345')
brcode.generate_image_code()


"""convert brcode to pdf"""
path_image = path + '\\' +  'test12345' + '.png'

CreateStampPdf.create_brcode_pdf(path_image, 'test12345' + '_code.pdf',
                                 {'x': 400, 'y': 750}, 150, 50, request)

print(path_image)

