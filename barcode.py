import brcodeAct
import config
from brcodeAct.generateBRCode import GenerateCode
from generateStamp.createStampPdf import CreateStampPdf
from generateStamp.drawing_stamp import SignDocument

request = 'REQ0007899'
path = config.path_template + request
#brcode = GenerateCode(path, 'test12345')
#brcode.generate_image_code()


"""convert brcode to pdf"""
path_image = path + '\\' +  'test12345' + '.png'

#CreateStampPdf.create_brcode_pdf(path_image, 'test12345' + '_code.pdf',
#                                 {'x': 400, 'y': 750}, 150, 50, request)

#print(path_image)

pdf_act = path + '\\171422529896093411.pdf'
brcode_pdf = path + '\\171422529896093411_brcode.pdf'

print(pdf_act)
print(brcode_pdf)
SignDocument.added_brcode(pdf_act, brcode_pdf)





