from schedule import repeat, every
from helpers import storage
import datetime as dt

#helping bits
now = str(dt.datetime.now().hour)

if __name__ == '__main__':
    storage.write(now, storage)
    
'''
@repeat(every().minute.at(':30'))
while True:
    schedule.run_pending()
    time.sleep(1)'''