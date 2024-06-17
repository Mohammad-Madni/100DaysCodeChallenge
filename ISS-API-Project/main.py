import requests
from datetime import datetime


now = datetime.now()


MY_LAT = 26.867487
MY_LNG = 67.983352

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


response = requests.get(url="http://api.open-notify.org/iss-now.json", params=parameters)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude =  float(data["iss_position"]["longitude"])
print(iss_latitude)
print(iss_longitude)
