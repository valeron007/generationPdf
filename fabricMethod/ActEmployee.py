# coding: utf-8
import fabricMethod.Act as act

class ActEmployee(act.Act):
    def __init__(self, param_act):
        super().__init__()
        self.params = param_act
    def show(self):
        print(self.act)

    def setAct(self):
        try:
            self.act["name"] = self.params[2]
            self.act["serial_number"] = self.params[3] if self.params[3] != "no" else ""
            self.act["cost_center_caller"] = self.params[4] if self.params[4] != "no" else ""
            self.act["job_title"] = self.params[5] if self.params[5] != "no" else ""
            self.act["personnel_number"] = self.params[6] if self.params[6] != "no" else ""
            self.act["fio"] = self.params[7]
            self.act["new_owner_cost_center_caller"] = self.params[8] if self.params[8] != "no" else ""
            self.act["new_owner_job_title"] = self.params[9] if self.params[9] != "no" else ""
            self.act["new_owner_personnel_number"] = self.params[10] if self.params[10] != "no" else ""
            self.act["new_owner_fio"] = self.params[11] if self.params[11] != "no" else ""
        except BaseException as e:
            print(e)

    def getValueField(self, name):
        return super().getValueField(name)