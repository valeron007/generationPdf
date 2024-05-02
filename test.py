import datetime
import config
import smbclient.shutil

username = 'int\sabx155'
password = 'GGkxXwA0AYPKwiBRfsft'

year = datetime.date.today().year
print(year)

city = 'Москва'

smbclient.shutil.copyfile(
    config.path_template + '\\REQ0005366\\main.pdf',
    config.path_drive + city + '\\' + str(year) + '\\main.pdf',
    username=username,
    password=password)

