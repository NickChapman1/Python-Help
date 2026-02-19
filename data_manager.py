import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

# URL specification will narrow it down to prices.
SHEETY_GET_URL = "https://api.sheety.co/124ba08e87e53eb3aae86c4e25d5dec9/flightDeals/sheet1"
SHEETY_PUT_URL = "https://api.sheety.co/124ba08e87e53eb3aae86c4e25d5dec9/flightDeals/sheet1"
class DataManager:
    def __init__(self):
        self.SHEETY_PW = os.getenv("SHEETY_PW")
        self.SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
        # self.authorization = HTTPBasicAuth(self.SHEETY_USERNAME, self.SHEETY_PW)
        self.headers = {"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}",
                        "Content-Type": "application/json"
                        }
        #self.verify = verify
        self.destination_data = []
        self.FLIGHT_ENDPOINT = os.getenv("FLIGHT_ENDPOINT") #Flight_endpoint shows to be the same as the get and post

    def get_destination_data(self):
        # SECURITY RISK: disables TLS validation
        Flight_resp = requests.get(SHEETY_GET_URL,headers=self.headers,verify=False)
        Flight_resp.raise_for_status()
        data = Flight_resp.json()
        self.destination_data = data["sheet1"]
        #Could also do... sheet_data = Flight_resp.json()["prices"]
        return self.destination_data

        #making the PUT call for this program
    def update_destination_codes(self):
        # ---- One-off write test with a known-existing row id ----
        # if self.destination_data:
        #     test_id = self.destination_data[0]["id"]  # e.g., 2
        #     test_patch = {"sheet1": {"iataCode": "PING"}}
        #     t = requests.put(
        #         f"{SHEETY_PUT_URL}/{test_id}",
        #         headers=self.headers,
        #         json=test_patch,
        #         verify=False
        #     )
        #     print("Write test:", t.status_code, t.text[:200])
        # ---- End one-off write test ----

        for city in self.destination_data:
            new_data = {
                "sheet1": {
                "city": city["city"],
                "iataCode": city["iataCode"],
                "lowestPrice": city["lowestPrice"]
                }
            }
            # SECURITY RISK: disables TLS validation
            response = requests.put(
                url=f"{SHEETY_PUT_URL}/{city['id']}",
                headers=self.headers,
                json=new_data,
                verify=False)
            print(response.text, response.status_code)

    def _debug_headers(self):
        token = os.getenv("SHEETY_TOKEN")
        print("Has token? ->", bool(token))
        if token:
            print("Token prefix:", token[:8], "(masked)")
        print("GET URL:", SHEETY_GET_URL)
        print("PUT URL (example):", f"{SHEETY_PUT_URL}/")
        print("Auth header present? ->", "Authorization" in self.headers)