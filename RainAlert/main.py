import requests

OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
api_key = ""
weather_params = {
    "lon": 67.980330,
    "lat": 26.870970,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

