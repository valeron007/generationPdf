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
        self.act["inventor_number"] = self.params[9] if self.params[9] != "no" else ""
        self.act["initial_cost"] = self.params[10] if self.params[10] != "no" else ""
        self.act["act_date"] = self.params[11]
        self.act["number"] = self.params[12] if self.params[12] != "no" else ""
        self.act["equipment"] = self.params[13] if self.params[13] != "no" else ""

    def setActPdf(self):
        try:
            self.act_pdf["model"] = self.params[2]
            self.act_pdf["serial_number"] = self.params[3] if self.params[3] != "no" else ""
            self.act_pdf["personnel_number"] = self.params[4] if self.params[4] != "no" else ""
            self.act_pdf["job_title"] = self.params[5] if self.params[5] != "no" else ""
            self.act_pdf["Personnel"] = self.params[6] if self.params[6] != "no" else ""
            self.act_pdf["initials"] = self.params[7]
            self.act_pdf["tabel_number"] = self.params[8] if self.params[8] != "no" else ""
            self.act_pdf["inventor_number"] = self.params[9] if self.params[9] != "no" else ""
            self.act_pdf["initial_cost"] = self.params[10] if self.params[10] != "no" else ""
            self.act_pdf["act_date"] = self.params[11]
        except BaseException as e:
            print(e)

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
        elif name == 'inventor_number':
            return self.act['inventor_number'] if 'inventor_number' in self.act else ""
        elif name == 'initial_cost':
            return self.act['initial_cost'] if 'initial_cost' in self.act else ""
        elif name == 'act_date':
            return self.act['act_date'] if 'act_date' in self.act else ""

