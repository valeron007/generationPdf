# coding: utf-8
import fabricMethod.Act as act

class ActWareHouse(act.Act):
    def __init__(self, param_act):
        super().__init__()
        self.params = param_act

    def show(self):
        print(self.act)

    def setAct(self):
        self.act["name"] = self.params[2]
        self.act["serial_number"] = self.params[3] if self.params[3] != "no" else ""
        self.act["cost_center_caller"] = self.params[4] if self.params[4] != "no" else ""
        self.act["job_title"] = self.params[5] if self.params[5] != "no" else ""
        self.act["personnel_number"] = self.params[6] if self.params[6] != "no" else ""
        self.act["fio"] = self.params[7]
        self.act["warehouse"] = self.params[8]

    def getValueField(self, name):
        if name == 'Модель':
            return self.act["name"] if 'name' in self.act else ""
        elif name == 'serial_number':
            return self.act['serial_number'] if 'serial_number' in self.act else ""
        elif name == 'initials':
            return self.act['fio'] if 'fio' in self.act else ""
        elif name == 'receivingInitials':
            return self.act['new_owner_fio'] if 'new_owner_fio' in self.act else ""
        elif name == 'personnel_number':
            return self.act['cost_center_caller'] if 'cost_center_caller' in self.act else ""
        elif name == 'Табельный номер отдела':
            return self.act['warehouse'] if 'warehouse' in self.act else ""
        elif name == 'Должность':
            return self.act['job_title'] if 'job_title' in self.act else ""
        elif name == 'Personnel':
            return self.act['personnel_number'] if 'personnel_number' in self.act else ""
        elif name == 'tenure':
            return self.act['new_owner_job_title'] if 'new_owner_job_title' in self.act else ""
        elif name == 'receiving':
            return self.act['new_owner_personnel_number'] if 'new_owner_personnel_number' in self.act else ""




