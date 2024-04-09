import requests
import os
from datetime import datetime as dt

nutritionix_html = "https://developer.nutritionix.com/admin/applications/1409623178453"
sheety_html = "https://dashboard.sheety.co/projects/63f7e2af67632421c6c52ee8/sheets/workouts"
google_docs = "https://docs.google.com/spreadsheets/d/1phjBO8t44AOKs2vUSDOiJbZsLLX2z9-3Drpqc8bXmdo/edit#gid=0"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NUTRITIONIX_ENDPOINT = os.environ.get("NUTRITIONIX_ENDPOINT")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
TOKEN = os.environ.get("TOKEN")
print(NUTRITIONIX_ENDPOINT)
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

def get_calories(workout_input):

    request = {
        "query": workout_input,
        "gender": "male",
        "weight_kg": 94,
        "height_cm": 174.5,
        "age": 21
    }
    response = requests.post(NUTRITIONIX_ENDPOINT, request, headers=HEADERS)
    response.raise_for_status()
    return response.json()["exercises"]

def import_by_username(row):

    exercise = row["name"]
    duration = row["duration_min"]
    calories = row["nf_calories"]
    now = dt.now()
    data_dict = {
        "workout": {
            "date": now.strftime("%Y/%m/%d"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(SHEET_ENDPOINT, json=data_dict, auth=(USERNAME, PASSWORD))
    response.raise_for_status()

def import_by_token(row):

    exercise = row["name"]
    duration = row["duration_min"]
    calories = row["nf_calories"]
    now = dt.now()
    data_dict = {
        "workout": {
            "date": now.strftime("%Y/%m/%d"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.post(SHEET_ENDPOINT, json = data_dict, headers=bearer_headers)
    response.raise_for_status()


workout_input = input("Tell me which exercises you did: ")

for row in get_calories(workout_input):
    import_by_token(row)








