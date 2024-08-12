import config
from reportlab.pdfgen import canvas


class StampGen:
    def __init__(self, name_image, template, width, height, position_x, position_y):
        self.name_image = name_image
        self.template = template
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y

    def generateStampForEmployee(self, folder_name) -> None:
        stamp = canvas.Canvas(config.root_project + '\\template\\' + folder_name + '\\' + self.template)
        stamp.drawImage(config.root_project + '\\image\\' + self.name_image, self.position_x, self.position_y, self.width, self.height)
        stamp.save()

    def generateBRCodeForEmployee(self, folder_name) -> None:
        stamp = canvas.Canvas(config.root_project + '\\template\\' + folder_name + '\\' + self.template)
        stamp.drawImage(self.name_image, self.position_x, self.position_y, self.width, self.height)
        stamp.save()

