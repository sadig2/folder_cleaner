import os
import time

while(True):
    time.sleep(3)
    directory = os.path.abspath('anki')

    files = os.listdir(directory)

    if len(files)>6:
        for f in files:
            filedir = os.path.join(directory, f)
            os.remove(filedir)
