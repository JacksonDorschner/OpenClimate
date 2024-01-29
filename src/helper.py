from main import temp_celcius, temp_fahrenheit, humidity, sunrise_time, sunset_time, json
import json

def kelvinConvert(kelvin: float) -> tuple:
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

class storage:
    def read(now) -> tuple:
        """returns tuple for setting current values for the system to maintain

        Args:
            now (int): current hour of the day (24h time)

        Returns:
            tuple: all the data for current conditions
        """
        f = open('values.json')
        data = json.load(f)
        
        for i in data['']:
            return
    
    def write(now):
        f = open('values.json')
        data = json.load(f)
        
    def api_fetch() -> str:
        print(f'Temp: {temp_fahrenheit}F, {temp_celcius}C \n Humidity: {humidity}% \n Sunrise: {sunrise_time} \n Sunset: {sunset_time}')