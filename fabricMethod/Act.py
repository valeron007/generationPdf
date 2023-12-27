# coding: utf-8

class Act(object):
    def __init__(self):
        self.act = {}
        self.act_pdf = {}
    def show(self):
        raise NotImplementedError()

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
            return self.act['new_owner_cost_center_caller'] if 'new_owner_cost_center_caller' in self.act else ""
        elif name == 'Должность':
            return self.act['job_title'] if 'job_title' in self.act else ""
        elif name == 'Personnel':
            return self.act['personnel_number'] if 'personnel_number' in self.act else ""
        elif name == 'tenure':
            return self.act['new_owner_job_title'] if 'new_owner_job_title' in self.act else ""
        elif name == 'receiving':
            return self.act['new_owner_personnel_number'] if 'new_owner_personnel_number' in self.act else ""
        elif name == 'inv_number':
            return self.act['inv_number'] if 'inv_number' in self.act else ""
        elif name == 'cost':
            return self.act['initial_cost'] if 'initial_cost' in self.act else ""
        elif name == 'act_date':
            return self.act['act_date'] if 'act_date' in self.act else ""
