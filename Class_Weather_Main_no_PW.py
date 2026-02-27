import requests
import os
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MyEmailSend = os.getenv("SEND_EMAIL")
app_password = os.getenv("APP_PW_GMAIL")
api_key = os.getenv("OWM_API_KEY")
MyEmailRecieve = os.environ.get("RECIEVE_EMAIL")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
url = "?lat=&lon=&appid="
umbrella_needed = False
#testing used to make sure it was populating.
if not MyEmailSend or not app_password:
    raise ValueError("Missing SEND_EMAIL or APP_PW_GMAIL in .env file")

# Make the GET request
weather_params = {
    "lat":39.739235,
    "lon":-104.990250,
    "appid":api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint,params=weather_params)
#below will raise an expection if it doesn't get the 200 code
response.raise_for_status()
data = response.json()#convert response to python dict
#print(data["list"][0]["weather"][0]["id"]) #Testing for navigating the
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    # check if the code is less than 700 print out bring an umbrella,
    if int(condition_code) < 700:
        umbrella_needed = True
#Keeping this logic seperate this way, makes it so it sends an email either way. Could build so it only sends with rain
if umbrella_needed:
    message = "Bring an umbrella."
else:
    message = "No umbrella needed today."
# Send email regardless
with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as g_connection:
    g_connection.starttls()
    g_connection.login(user=MyEmailSend, password=app_password)
    g_connection.sendmail(
        from_addr=MyEmailSend,
        to_addrs=MyEmailRecieve,
        msg=message
    )
    g_connection.close()
#My inital version loop, class condenses it
# for forecast in data["list"]:
#     print(forecast["weather"][0])
#     for weather_item in forecast["weather"]:
#         if weather_item["id"] < 700:
#             umbrella_needed = True
#             break  # No need to check further for this forecast
#     if umbrella_needed:
#         print("Bring an umbrella")
#         break  # No need to check further forecasts
# else:
#     print("No umbrella needed now..")