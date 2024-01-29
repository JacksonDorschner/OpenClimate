from helper   import kelvinConvert, storage
from schedule import repeat, every
import datetime as dt
import requests
import json
import time

#API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=-22.6127615&lon=167.4874067&appid="
API_KEY = open('api_key', 'r').read()
url = BASE_URL + API_KEY
response = requests.get(url).json()

#Data Values:
temp_kelvin  = response['main']['temp'    ]
humidity     = response['main']['humidity']
sunrise_time = response['sys' ]['sunrise' ] + response['timezone']
sunset_time  = response['sys' ]['sunset'  ] + response['timezone']

#helping bits
temp_celcius, temp_fahrenheit = kelvinConvert(temp_kelvin)
now = str(dt.datetime.now().hour)

if __name__ == '__main__':
    def init():
        return
    storage.read(now)
    
'''
@repeat(every().minute.at(':30'))
while True:
    schedule.run_pending()
    time.sleep(1)'''