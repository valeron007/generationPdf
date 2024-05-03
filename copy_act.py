import logging
import sys

try:
    import datetime
    import config
    import smbclient.shutil

    year = datetime.date.today().year
    print(year)

    city = 'Москва'
    name = '171344940797819622.pdf'
    number = 'REQ0005995'

    smbclient.shutil.copyfile(
        config.path_template + '\\REQ0005366\\main.pdf',
        config.path_drive + city + '\\' + str(year) + '\\main.pdf',
        username=config.username,
        password=config.password)

except BaseException as e:
    logging.basicConfig(level=logging.DEBUG, filename='er.log')
    logging.debug('error: %s', e)
    logging.debug([x for x in sys.argv])

