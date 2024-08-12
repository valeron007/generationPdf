import logging

import code128
from PIL import Image, ImageDraw, ImageFont

class GenerateCode:
    def __init__(self, act_path, serial_number):
        self.path = act_path
        self.serial_number = serial_number
        self.path_image = self.path + '\\' + self.serial_number + '.png'
        self.brcode_pdf = serial_number + '_brcode.pdf'

    def generate_image_code(self):
        barcode_image = code128.image(self.serial_number, height=100)
        w, h = barcode_image.size
        margin = 20
        new_h = h + (2 * margin)
        new_image = Image.new('RGB', (w, new_h), (255, 255, 255))
        # put barcode on new image
        new_image.paste(barcode_image, (0, margin))
        # object to draw text
        draw = ImageDraw.Draw(new_image)
        # draw text
        # fnt = ImageFont.truetype("arial.ttf", 40)
        draw.text((30, new_h - 20), self.serial_number, fill=(0, 0, 0))  # , font=fnt)  #
        # save in file

        new_image.save(self.path_image, 'PNG')
