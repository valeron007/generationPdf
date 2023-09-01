import fabricMethod.MyApplication as myapplication
import sys

try:
    print(x for x in sys.argv)
    app = myapplication.MyApplication()
    employee = app.create_document(sys.argv[1], [x.encode('utf-8') for x in sys.argv])  # Open document format
    employee.setAct()
    #warehouse = app.create_document(sys.argv[1], [x.encode('utf-8') for x in sys.argv])
    #warehouse.setAct()
    #employee.show()
    #warehouse.show()
    #print()
    model_name = employee.getValueField("Модель")
    print(employee.show())
    data = [x for x in sys.argv]
    #asciidata = [word.decode('ascii', "ignore") for word in data]
    print(data)
except BaseException as e:
    print(e)


