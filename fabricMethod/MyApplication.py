# coding: utf-8
import fabricMethod.ActEmployee, fabricMethod.ActWareHouse
import fabricMethod.Application as application
from fabricMethod import ActEmployee, ActWareHouse


class MyApplication(application.Application):
    def create_document(self, type_, params):
        if type_ == 'employee':
            return ActEmployee.ActEmployee(param_act=params)
        elif type_ == 'warehouse':
            return ActWareHouse.ActWareHouse(param_act=params)


