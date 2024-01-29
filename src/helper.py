import json

def kelvinConvert(kelvin: float) -> tuple:
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

class storage:
    def read(now):
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
    
    def write(now):
        f = open('values.json')
        data = json.load(f)
        f.close()
        
    def api_fetch() -> str:
            return