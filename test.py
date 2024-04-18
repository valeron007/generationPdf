import os
import config
import shutil
import subprocess

#print(config.path_drive)
#print(os.path.exists(config.path_drive))

import smbclient.shutil

username = 'int\A828835'
password = 'Ahjv0792!'

smbclient.shutil.copyfile(
    config.path_template + '\\REQ0005366\\main.pdf',
    config.path_drive,
    username=username,
    password=password)


