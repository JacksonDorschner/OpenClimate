from schedule import repeat, every
from helper import kelvinConvert
import datetime as dt
import requests
import schedule
import asyncio
import json
import time
import os

#API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=-22.6127615&lon=167.4874067&appid="
API_KEY = open('api_key', 'r').read()
url = BASE_URL + API_KEY
response = requests.get(url).json()

#storage
current_parrams = ''

#helping bits
temp_celcius, temp_fahrenheit = kelvinConvert(temp_kelvin)
now = str(dt.datetime.now().hour)

#Data Values:
temp_kelvin  = response['main']['temp'    ]
humidity     = response['main']['humidity']
sunrise_time = response['sys' ]['sunrise' ] + response['timezone']
sunset_time  = response['sys' ]['sunset'  ] + response['timezone']

if __name__ == '__main__':
    def init():
        return

    
'''
@repeat(every().minute.at(':30')) Temp: %(temp_fahrenheit)F, %(temp_celcius)C \n Humidity: %(humidity) \n Sunrise: %(sunrise_time) \n Sunset: %(sunset_time)
while True:
    schedule.run_pending()
    time.sleep(1)'''