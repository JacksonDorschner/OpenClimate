from helper   import kelvinConvert, storage
from schedule import repeat, every
import datetime as dt
import json
import time

#helping bits
now = str(dt.datetime.now().hour)

if __name__ == '__main__':
    def init():
        return
    #storage.read(now)
    storage.write(now)
    
'''
@repeat(every().minute.at(':30'))
while True:
    schedule.run_pending()
    time.sleep(1)'''