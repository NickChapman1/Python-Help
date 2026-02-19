import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

from Class_Data_Manager import DataManager
from Class_Flight_Search import FlightSearch
from Class_flight_data import find_cheapest_flight
from notification_manager_2 import NotificationManager


# Load environment variables from .env file
load_dotenv()
SENDER_EMAIL = os.getenv("SEND_EMAIL")
EMAIL_PASSWORD = os.getenv("APP_PW_GMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVE_EMAIL")
ORIGIN_CITY_IATA = "DEN"

# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager(sender=SENDER_EMAIL, app_password=EMAIL_PASSWORD)


# ==================== Update the Airport Codes in Google Sheet ====================

#  In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the API.
#  You should use the code you get back to update the sheet_data dictionary.

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now()+timedelta(days=(6*30))

for destination in sheet_data:
    print(f"Getting Flights from {destination['city']}")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
cheapest_flight = find_cheapest_flight(flights)
if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
    print(f"cheaper flight found at {cheapest_flight.price} for destination {cheapest_flight.destination['city']}")
    #Add notification manager call
    notification_manager.send_email_simple(
        subject="Price Drop Happened!",
        body_text = f"Found a cheaper price, {cheapest_flight.price} at {cheapest_flight.destination['city']}",
        recipients= [f"{RECEIVER_EMAIL}"],
    )

