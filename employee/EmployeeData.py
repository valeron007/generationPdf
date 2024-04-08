class EmployeeData:
    def __init__(self, params):
        self.__data = {}
        self.__params = params
        self.__position = {}

    def get_position(self):
        return self.__position
    def add_name_folder(self, name):
        self.__data['folder'] = name + '_' + self.__data["number"]

    def get_folder(self):
        return self.__data['folder']

    def set_data(self):
        self.__data["fio"] = self.__params[1]
        self.__data["number"] = self.__params[2] if self.__params[2] != "no" else ""
        self.__data["job_title"] = self.__params[3] if self.__params[3] != "no" else ""
        self.__data["type_sign"] = self.__params[4]
        self.__data["number"] = self.__params[5]

        if self.__data["type_sign"] == 'transferrer':
            self.__position['x'] = 15
            self.__position['y'] = 120
        else:
            self.__position['x'] = 350
            self.__position['y'] = 80

    def get_data(self):
        return self.__data