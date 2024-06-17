import requests
from datetime import datetime


now = datetime.now()


MY_LAT = 26.869119
MY_LNG = 67.982050

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunsrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =  data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunsrise)
print(sunset)
