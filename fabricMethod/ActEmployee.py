# coding: utf-8
import fabricMethod.Act as act

class ActEmployee(act.Act):
    def __init__(self, param_act):
        super().__init__()
        self.params = param_act
    def show(self):
        print(self.act)
    """ 
    "employee" 
    "lenovo l15gen2" 
    "PF37W6M3" 
    "RU751DG503" 
    "программист" 
    "00010461" 
    "Andryuschenko Valeriy" 
    "RU751DW102" 
    "Вентра" 
    "no" 
    "Makhinov Maksim"
    """
    def setActPdf(self):
        try:
            self.act_pdf["model"] = self.params[2]
            self.act_pdf["serial_number"] = self.params[3] if self.params[3] != "no" else ""
            self.act_pdf["personnel_number"] = self.params[4] if self.params[4] != "no" else ""
            self.act_pdf["job_title"] = self.params[5] if self.params[5] != "no" else ""
            self.act_pdf["Personnel"] = self.params[6] if self.params[6] != "no" else ""
            self.act_pdf["initials"] = self.params[7]
            self.act_pdf["tabel_number"] = self.params[8] if self.params[8] != "no" else ""
            self.act_pdf["tenure"] = self.params[9] if self.params[9] != "no" else ""
            self.act_pdf["receiving"] = self.params[10] if self.params[10] != "no" else ""
            self.act_pdf["receivingInitials"] = self.params[11] if self.params[11] != "no" else ""
            self.act_pdf["inventor_number"] = self.params[12] if self.params[12] != "no" else ""
            self.act_pdf["initial_cost"] = self.params[13] if self.params[13] != "no" else ""
            self.act_pdf["act_date"] = self.params[14]
            self.act_pdf["number"] = self.params[15]
            self.act_pdf["equipment"] = self.params[16]

        except BaseException as e:
            print(e)
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
            self.act["inventor_number"] = self.params[12] if self.params[12] != "no" else ""
            self.act["initial_cost"] = self.params[13] if self.params[13] != "no" else ""
            self.act["act_date"] = self.params[14]
            self.act["number"] = self.params[15]
            self.act["equipment"] = self.params[16]

        except BaseException as e:
            print(e)

    def getValueField(self, name):
        return super().getValueField(name)