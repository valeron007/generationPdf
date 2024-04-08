from employee import Employee as emp
from generateStamp.generate_stamp import GenerateStamp
import shutil
import config
import os

class CreatorStamp:
    @staticmethod
    def created_stamp(data: dict, folder_name):
        employee = emp.Employee(data['fio'], data['job_title'], data['number'])
        stamp = GenerateStamp(employee)
        stamp.init_stamp()
        stamp.save_stamp()
        #create folder
        # копируем stamp pdf
        shutil.copy(config.path_template + 'stamp.pdf',
                    config.path_template + folder_name + '\\' + stamp.get_rand_name() + "_stamp.pdf")

        return stamp

    @staticmethod
    def remove_folder(name):
        os.remove(config.path_template + name)
    @staticmethod
    def create_folder_signer(name):
        os.mkdir(config.path_template + name)
    @staticmethod
    def copy_original_template(folder_name):
        shutil.copy(config.path_template + 'original.pdf', config.path_template + folder_name + '\\main' + ".pdf")

    @staticmethod
    def copy_to_drive():
        shutil.copy(config.path_template + 'original.pdf', config.path_template + 'main' + ".pdf")

