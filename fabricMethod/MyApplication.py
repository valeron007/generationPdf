# coding: utf-8
import fabricMethod.ActEmployee, fabricMethod.ActWareHouse
import fabricMethod.Application as application
from fabricMethod import ActEmployee, ActWareHouse, ActFromWarehouse, Test


class MyApplication(application.Application):
    def create_document(self, type_, params):
        if type_ == 'employee':
            return ActEmployee.ActEmployee(param_act=params)
        elif type_ == 'warehouse':
            return ActWareHouse.ActWareHouse(param_act=params)
        elif type_ == 'fromWarehouse':
            return ActFromWarehouse.ActFromWarehouse(param_act=params)
        # elif type_ == 'toTest':                                          don't delete - it's for future test
        #     return Test.ActWareHouse(param_act=params)
        # elif type_ == 'fromTest':
        #     return Test.ActFromWarehouse(param_act=params)
        # elif type_ == 'userTest':
        #     return Test.ActEmployee(param_act=params)



