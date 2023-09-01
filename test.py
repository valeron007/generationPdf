
import sys
import json
import ast
from json import JSONDecodeError

if __name__ == '__main__':
    try:
        data = sys.argv[1]
        #data = json.dumps(sys.argv[1], separators=(',', ':'))
        #print('{0}; {1}; {2}; {3};'.format(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4]))
        act = {}
        act["name"] = sys.argv[1]
        act["serial_number"] = sys.argv[2]
        act["cost_center_caller"] = sys.argv[3]
        act["job_title"] = sys.argv[4]
        act["personnel_number"] = sys.argv[5]
        act["fio"] = sys.argv[6]
        act["new_owner_cost_center_caller"] = sys.argv[7]
        act["new_owner_job_title"] = sys.argv[8]
        act["new_owner_personnel_number"] = sys.argv[9]
        act["new_owner_fio"] = sys.argv[10]
        print(sys.argv[4].encode("utf-8"))
        #print(sys.argv[1])
    except BaseException as e:
        print(e)
        with open("log.txt", "wb", encoding="utf-8") as f:
            f.write(sys.argv[1].encode("utf-8"))
            #f.write(inst.args)



"""
{"name":"lenovo l15gen2",
"serial_number":"PF37W6M3",
"cost_center_caller":"RU751DG503",
"job_title":"программист",
"personnel_number":"00010461",
"fio":"Andryuschenko Valeriy",
"new_owner_cost_center_caller":"RU751IN2A2",
"new_owner_job_title":"developer",
"new_owner_personnel_number":"1233333",
"new_owner_fio":"Nikolay Mamchenko"}

arguments
"lenovo l15gen2" "PF37W6M3" "RU751DG503" "программист" "00010461" "Andryuschenko Valeriy" "RU751IN2A2" "developer" "1233333" "Nikolay Mamchenko"   


"""
