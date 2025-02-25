import requests
from twilio.rest import Client
OWM_Endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
api_key = ""
weather_params = {
    "lon": #yourlogitude,
    "lat": ,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_="your trail number from twilio",
        to="to whom you want to send but first verify it from twilio",
    )
    print(message.status)
