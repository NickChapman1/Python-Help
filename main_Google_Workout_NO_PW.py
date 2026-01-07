from datetime import datetime
import requests
import os

GENDER = "male"
WEIGHT_KG = 225
HEIGHT_CM = 175
AGE = 72
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_PW = os.getenv("SHEETY_PW")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
exercise_endpoint = os.getenv("EXERCISE_ENDPOINT")
SHEETY_BASE_URL= "https://api.sheety.co/124ba08e87e53eb3aae86c4e25d5dec9/chapmanWorkouts/workouts"
# 1. Using the Nutrition & Exercise API Guide, figure out how to print the exercise stats for plain text input.
exercise_done = input("Tell me which exercises you did today and the duration:")
#Creates a page here https://pixe.la/@nickwon123 #URL Endpoint for specific graph https://pixe.la/v1/users/nickwon123/graphs/graph1
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",  # helps disambiguate user context
    "User-Agent": "NickExerciseApp/1.0"
}

parameters = {
    "query": exercise_done,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_resp = requests.post(exercise_endpoint, headers= headers, json=parameters)
exercise_resp.raise_for_status()
exercise_data = exercise_resp.json()
print("Exercise API result:", exercise_data)



#******************************For part 4,
today = datetime.now()
date_str = today.strftime("%Y-%m-%d")
time_str = today.strftime("%H:%M:%S")

# Sheety requires the body to be nested under the singular root key. [1](https://sheety.co/docs/requests)[2](https://stackoverflow.com/questions/75590746/adding-a-row-to-a-sheet-using-sheety-and-python)
for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": date_str,
            "time": time_str,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_BASE_URL,json=sheet_inputs,auth=(SHEETY_USERNAME, SHEETY_PW))
    print(f"test test chapman /n/n/n{sheet_response.text}")