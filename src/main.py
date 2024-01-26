from schedule import repeat, every
from helper import kelvinConvert
from helper import get_time
import datetime as dt
import requests
import schedule
import asyncio
import json
import time
import os

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=-22.6127615&lon=167.4874067&appid="
API_KEY = open('api_key', 'r').read()
url = BASE_URL + API_KEY
response = requests.get(url).json()

f = open('values.json')
data = json.load(f)

#Data Values:
temp_kelvin  = response['main']['temp'    ]
humidity     = response['main']['humidity']
sunrise_time = response['sys' ]['sunrise' ] + response['timezone']
sunset_time  = response['sys' ]['sunset'  ] + response['timezone']

temp_celcius, temp_fahrenheit = kelvinConvert(temp_kelvin)
now = str(dt.datetime.now().hour)

#@repeat(every().minute.at(':30')) Temp: %(temp_fahrenheit)F, %(temp_celcius)C \n Humidity: %(humidity) \n Sunrise: %(sunrise_time) \n Sunset: %(sunset_time)
def fetch() -> str:
    print(f'Temp: {temp_fahrenheit}F, {temp_celcius}C \n Humidity: {humidity}% \n Sunrise: {sunrise_time} \n Sunset: {sunset_time}')
    
    
'''
while True:
    schedule.run_pending()
    time.sleep(1)'''