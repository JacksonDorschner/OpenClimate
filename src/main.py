import datetime as dt
import requests

lat = "-22.6127615"
lon = "167.4874067"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

print(requests.get(BASE_URL).json())