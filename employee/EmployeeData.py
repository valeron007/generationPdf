class EmployeeData:
    def __init__(self, params):
        self.__data = {}
        self.__params = params
        self.__position = {}

    def get_position(self):
        return self.__position

    def add_name_folder(self):
        self.__data['folder'] = self.__data["request"]

    def get_folder(self):
        return self.__data['folder']

    def get_act_id(self):
        return self.__data["act_id"]

    def get_equipment(self):
        return self.__data["equipment"]

    def set_data(self):
        self.__data["fio"] = self.__params[1]
        self.__data["number"] = self.__params[2] if self.__params[2] != "no" else ""
        self.__data["job_title"] = self.__params[3] if self.__params[3] != "no" else ""
        self.__data["type_sign"] = self.__params[4]
        self.__data["request"] = self.__params[5]
        self.__data["warehouse"] = self.__params[6]
        self.__data["equipment"] = self.__params[7]
        self.__data["location"] = self.__params[8]

        if self.__data["type_sign"] == 'transferrer':
            self.__position['x'] = 15
            self.__position['y'] = 120
        else:
            self.__position['x'] = 350
            self.__position['y'] = 80

    def get_data(self):
        return self.__data

    def get_name_number_request(self):
        return self.__data["request"]

    def get_type_act(self):
        return self.__data["type_sign"]

    def get_location(self):
        return self.__data["location"]
