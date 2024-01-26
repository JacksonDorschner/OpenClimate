def kelvinConvert(kelvin: float) -> tuple:
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit