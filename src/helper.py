import requests
import json

utc_Offset = 19

def kelvinConvert(kelvin: float) -> tuple:
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

class storage:
    def read(now: int) -> tuple:
        """returns tuple for setting current values for the system to maintain

        Args:
            now (int): current hour of the day (24h time)

        Returns:
            tuple: all the data for current conditions
        """
        f = open('values.json')
        data = json.load(f)

        env_control = tuple(dict(data[now]).values())

        f.close()
        return env_control
    
    def write(now: int, self):
        f = open('values.json')
        data = json.load(f)
        futureTime = int(now) + utc_Offset
        if futureTime > 24:
            futureTime = futureTime - 24
        self.api_fetch()

        
        f.close()
        
    def api_fetch() -> tuple:
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
        return temp_fahrenheit, humidity