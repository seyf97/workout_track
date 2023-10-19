import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
EX_ENDPOINT = os.getenv("EX_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER = os.getenv("SHEETY_BEARER")

GENDER = "male"
WEIGHT = 80
HEIGHT = 178
AGE = 26



ex_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

ex_config = {
    "query": input("Tell me which exercises you did today:"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

sheety_header = {
    "Authorization": SHEETY_BEARER
}

resp = requests.post(url=EX_ENDPOINT, json=ex_config, headers=ex_headers)
exercises = resp.json()["exercises"]


for exercise in exercises:
    sheety_config = {
        "workout":
            {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise["name"].capitalize(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
    }
    resp = requests.post(url=SHEETY_ENDPOINT, json=sheety_config, headers=sheety_header)
