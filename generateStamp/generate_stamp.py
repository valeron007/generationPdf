import binascii
import os
import aiofiles

import config
import shutil
from PIL import Image, ImageDraw, ImageFont


class GenerateStamp:
    def __init__(self, employee):
        self.__width = 330
        self.__height = 100
        self.__font_size_title = 12
        self.__font_size_first_word = 10
        self.__font_size_text = 15
        self.__shape = [(0, 0), (self.__width, self.__height)]
        self.__font_title = ImageFont.truetype(config.root_project + '\\fonts\\arial_bold.ttf', self.__font_size_title)
        self.__font_text = ImageFont.truetype(config.root_project + '\\fonts\\arial_bold.ttf', self.__font_size_text)
        self.__stamp = Image.new(mode="RGB", size=(self.__width, self.__height), color=(255, 255, 255))
        self.__canvas = ImageDraw.Draw(self.__stamp)
        self.__employee = employee
        self.__path_project = os.path.abspath(os.getcwd())
        self.__rand_name = binascii.hexlify(os.urandom(8)).decode('utf-8')
        self.__stamp_name = self.__rand_name + '.pdf'

    def get_number(self):
        return self.__employee.get_personal_number()
    def get_rand_name(self):
        return self.__rand_name

    def create_rectangle(self):
        self.__canvas.rectangle(self.__shape, fill='#ffffff', outline='#31317A', width=2)

    def create_title(self):
        self.__canvas.text((90, 10), "ДОКУМЕНТ ПОДПИСАН", fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((55, 20), "ПРОСТОЙ ЭЛЕКТРОННОЙ ПОДПИСЬЮ", fill='#8e90a0', font=self.__font_title, spacing=10)

    def create_content(self):
        self.__canvas.text((20, 40), "Владелец", fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((90, 40), self.__employee.get_fio(), fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((20, 50), self.__employee.get_job_title(), fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((20, 60), 'Личный номер', fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((110, 60), self.__employee.get_personal_number(), fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((20, 70), 'Дата подписания', fill='#8e90a0', font=self.__font_title, spacing=10)
        self.__canvas.text((130, 70), self.__employee.get_sign_date(), fill='#8e90a0', font=self.__font_title, spacing=10)

    def copy(self):
        self.dest = shutil.copyfile(config.path_template + 'stamp.pdf', config.path_template + self.get_rand_name() + ".pdf")
    def show_stamp(self):
        self.__stamp.show()

    def init_stamp(self):
        self.create_rectangle()
        self.create_title()
        self.create_content()

    async def save_image(path: str, image: memoryview) -> None:
        async with aiofiles.open(path, "wb") as file:
            await file.write(image)
    def save_stamp(self):
        self.__stamp.save(config.root_project + '\\image\\' + self.__rand_name + '.png')
