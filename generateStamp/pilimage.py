import os
import config
from employee import Employee as emp
from PIL import Image, ImageDraw, ImageFont

employee = emp.Employee('Валерий', 'Андрющенко', 'Геннадьевич', 'программист', '10461')

width = 315
height = 100
font_size_title = 11
font_size_text = 10

shape = [(0, 0), (width, height)]

font_title = ImageFont.truetype(config.root_project + '\\fonts\\arialmt.ttf', font_size_title)
font_text = ImageFont.truetype(config.root_project + '\\fonts\\arialmt.ttf', font_size_text)
stamp = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
canvas = ImageDraw.Draw(stamp)
canvas.rectangle(shape, fill='#ffffff', outline='#31317A', width=2)
canvas.text((90, 10), "ДОКУМЕНТ ПОДПИСАН", fill='#8e90a0', font=font_title)
canvas.text((55, 20), "ПРОСТОЙ ЭЛЕКТРОННОЙ ПОДПИСЬЮ", fill='#8e90a0', font=font_title)
canvas.text((20, 40), "Владелец", fill='#8e90a0', font=font_text)
canvas.text((70, 40), employee.get_fio(), fill='#8e90a0', font=font_text)
canvas.text((20, 50), employee.get_job_title(), fill='#8e90a0', font=font_text)
canvas.text((20, 60), 'Личный номер', fill='#8e90a0', font=font_text)
canvas.text((93, 60), employee.get_personal_number(), fill='#8e90a0', font=font_text)
canvas.text((20, 70), 'Дата подписания', fill='#8e90a0', font=font_text)
canvas.text((110, 70), employee.get_sign_date(), fill='#8e90a0', font=font_text)
stamp.show()

path_project = os.path.abspath(os.getcwd())
stamp.save(config.root_project + '\\image\\stamp.png')
