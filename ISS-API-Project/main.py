import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "appbrewarycourse@gmail.com"
MY_PASSWORD = "vmmxcvtruxxojklu"

MY_LAT = 26.867487
MY_LNG = 67.983352


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()


    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset and time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="madnikorejo9@gmail.com",
                            msg="Subject:Look Up\n\nThe ISS is above you in the Sky!")
