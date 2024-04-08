from datetime import date


class Employee:
    def __init__(self, fio, job_title, personal_number):
        self.__fio = fio
        self.__job_title = job_title
        self.__personal_number = personal_number
        self.__data_sign = ''

    def get_fio(self):
        return self.__fio

    def get_job_title(self):
        return self.__job_title

    def get_personal_number(self):
        return self.__personal_number

    def get_sign_date(self):
        today = date.today()
        self.__data_sign = today.strftime("%d.%m.%Y")
        return self.__data_sign
