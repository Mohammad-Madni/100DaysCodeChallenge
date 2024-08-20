import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 61
HEIGHT_CM = 73
AGE = 22

APP_ID = ""
API_KEY = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/25e51d5921145d82e04dc8bfce9c9463/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint,json=sheet_inputs)
    print(sheet_response.text)
