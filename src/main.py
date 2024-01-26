from   func import kelvinConvert
import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=-22.6127615&lon=167.4874067&appid="
API_KEY = open('api_key', 'r').read()

url = BASE_URL + API_KEY
response = requests.get(url).json()

#Data Values:
temp_kelvin  = response['main']['temp'    ]
humidity     = response['main']['humidity']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys' ]['sunrise' ] + response['timezone'])
sunset_time  = dt.datetime.utcfromtimestamp(response['sys' ]['sunset'  ] + response['timezone'])

temp_celcius, temp_fahrenheit = kelvinConvert(temp_kelvin)

print(f'Temp: {temp_fahrenheit}F, {temp_celcius}C \n Humidity: {humidity}% \n Sunrise: {sunrise_time} \n Sunset: {sunset_time}')