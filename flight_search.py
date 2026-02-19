import sys
import requests
import os
import time
import math
from typing import Optional, Dict, Any, Tuple, List, Iterable

class FlightSearch:
    """
    For now: ensures every row has an iataCode. If missing/empty, set to 'TESTING'.
    Later: replace 'TESTING' with a real lookup (e.g., via a flight API).
    """
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._url_amadeus = os.getenv("AMADEUS_AUTH_TOKEN_ENDPOINT")
        self._amadeus_api_base = (os.getenv("AMADEUS_API_BASE") or "https://test.api.amadeus.com").rstrip("/")
        #If a city has no match, returning None lets you decide in your calling code whether to skip or log
        #self._token: Optional[str] = None
        self._token = self._get_new_token()
        # Optional, lightweight debug prints; set DEBUG_FLIGHTS to control behavior:
        #   - "1"      => log requests + errors
        #   - "errors" => log only errors (4xx/5xx)
        #   - other    => off
        self.debug = os.getenv("DEBUG_FLIGHTS","0")

    # ---------- tiny debug helpers (no external deps) ----------
    def _is_debug_on(self):
        return self.debug == "1"

    def _is_debug_errors_only(self) -> bool:
        return self.debug == "errors"

    def _dbg(self, *parts, error: bool = False):
        """Prints only when debug is enabled. Set error=True to respect 'errors' mode."""
        if self._is_debug_on() or (error and self._is_debug_errors_only()):
            print(*parts, file=sys.stderr)

        #Adding in type hints for returns.
    def _get_new_token(self) -> str:
        #Check to make sure the data keys are passing
        missing = []
        if not self._api_key:
            missing.append("AMADEUS_API_KEY")
        if not self._api_secret:
            missing.append("AMADEUS_API_SECRET")
        if not self._url_amadeus:
            missing.append("AMADEUS_AUTH_TOKEN_ENDPOINT")

        if missing:
            raise RuntimeError(f"Missing Amadeus env vars: {', '.join(missing)}")

        #Header with content type as per Amadeus doc
        header = {'Content-Type' : 'application/x-www-form-urlencoded'}
        body = {
            'grant_type' : 'client_credentials',
            'client_id' : self._api_key,
            'client_secret' : self._api_secret
        }
        response = requests.post(url=self._url_amadeus, data=body, headers=header)
        response.raise_for_status()
        js = response.json()
        token = js["access_token"]
        # New bearer token. Typically expires in 1799 seconds (30min) Leaving for debug now
        # Security keeping it bloocked: print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return token

    def _auth_header(self):
        if not self._token:
            self._token = self._get_new_token()
        return {'Authorization': f'Bearer {self._token}'}
##################################################################
    def _get(self, url: str, params: Dict[str, Any], *, retries: int=2, backoff: float = .06) -> requests.Response:
        """Minimal GET with 401K refresh + light backoff for 429/5xx"""
        attempt = 0
        while True:
            resp = requests.get(url=url, headers={**self._auth_header(), "Accept": "application/json"}, params=params)
            #ligthweight request logging (Can turn it on or off)
            self._dbg("DEBUG url:", resp.request.url)
            self._dbg("DEBUG status:", resp.status_code)
            if resp.status_code >= 400:
                self._dbg("DEBUG body:", resp.text[:600], error=True)

            if resp.status_code == 401:
                self._token = self._get_new_token()
                resp = requests.get(url, headers={**self._auth_header(), "Accept": "application/json"}, params=params)

            if resp.status_code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(backoff * (2 ** attempt))
                attempt += 1
                continue

            resp.raise_for_status()
            return resp

    def _post(self, url: str, json_body: Dict[str, Any], *, retries: int=2, backoff: float = .06) -> requests.Response:
        """minimal POST with 401K refresh + light backoff"""
        attempt = 0
        while True:
            resp = requests.post(url=url,headers={**self._auth_header(), "Accept": "application/json", "Content-Type":
                "application/json"},json=json_body)
                # lightweight request logging (toggleable)
            self._dbg("DEBUG url:", resp.request.url)
            self._dbg("DEBUG status:", resp.status_code)
            if resp.status_code >= 400:
                self._dbg("DEBUG body:", resp.text[:600], error=True)

            if resp.status_code == 401:
                self._token = self._get_new_token()
                resp = requests.post(
                    url,
                    headers={**self._auth_header(), "Accept": "application/json", "Content-Type": "application/json"},
                    json=json_body
                )

            if resp.status_code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(backoff * (2 ** attempt))
                attempt += 1
                continue

            resp.raise_for_status()
            return resp

#Static will make it so this method can be called without needing an instance. You can still use an instance
    @staticmethod
    def _pick_cheapest(offers: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Return the offer with the lowest price.total."""
        if not offers:
            return None
        #P is only used here, so its a function in a function. Keeps namespace less clutered.
        def p(ofr):
            try:
                return float(((ofr.get("price") or {}).get("total")) or math.inf)
            except Exception:
                return math.inf
        return min(offers, key=p)
#Min is a built in python function that'll return the smallest. You can do an optional
 # key function to define hwo to measure the "Smallest". Key=P means to pass the function object the p function
# everytime to compare item.Min calls p(item) internally for each element. It does this before comparing items
#min is a built‑in. Adding () will make it actually call the function and error out on missing params.
# key=p passes the function p (not calling it yet).
# min then calls p(ofr) on each offer to get a numeric price, and returns the offer with the smallest price.
    #passing a function object rather than trying to get the results of calling that function.


    def get_destination_code(self, city_name: str):
        """
        Return the 3-letter IATA metropolitan or city code for a given city name.
        Strategy:
          1) Query subType=CITY,AIRPORT with a larger limit, no 'view'.
          2) Prefer exact/starts-with CITY matches (metro codes like TYO, PAR, CHI).
          3) If no CITY, but Tokyo airports found (HND/NRT), return TYO.
          4) Fallback to first CITY (if any) or first AIRPORT code (last resort).
          5) Return None if nothing is found.
        """
        if not city_name:
            raise RuntimeError("Missing city name.")

        base_url = (self._amadeus_api_base or 'https://test.api.amadeus.com').rstrip('/')
        url = f"{base_url}/v1/reference-data/locations"

        city_q = (city_name or "").strip()
        params = {
            "subType": "CITY,AIRPORT",
            "keyword": city_q,
            "page[limit]": 20
            # optionally: "countryCode": "JP"  # if you want to constrain Tokyo lookups
        }

        def _name_matches(item):
            n = (item.get("name") or "").lower()
            cq = city_q.lower()
            return n == cq or n.startswith(cq)

        # do the request with token auto-refresh
        def _do_get(p):
            resp = requests.get(url=url, headers=self._auth_header(), params=p)

            print("DEBUG url:", resp.request.url)
            print("DEBUG headers:", resp.request.headers)
            print("DEBUG status:", resp.status_code)
            print("DEBUG body:", resp.text[:600])  # first 600 chars is enough

            if resp.status_code == 401:
                self._token = self._get_new_token()
                resp = requests.get(url=url, headers=self._auth_header(), params=p)
            resp.raise_for_status()
            return resp.json().get("data", [])

        items = _do_get(params)

        if not items:
            # Sometimes the dataset differs with FULL view off/on; try without/with as a toggle
            # (Try adding view=FULL as a fallback)
            params_alt = dict(params)
            params_alt["view"] = "FULL"
            items = _do_get(params_alt)

        if not items:
            # Final debug print
            print(f"No results for '{city_name}' with CITY,AIRPORT; tried with and without view=FULL")
            return None

        # 1) Prefer CITY with exact/starts-with name
        city_item = next((x for x in items if x.get("subType") == "CITY" and _name_matches(x)), None)
        if city_item:
            return city_item.get("iataCode")

        # 2) Any CITY
        city_item = next((x for x in items if x.get("subType") == "CITY"), None)
        if city_item:
            return city_item.get("iataCode")

        # 3) Special-case Tokyo: if airports HND or NRT appear, map to TYO
        airport_codes = {(x.get("iataCode") or "").upper() for x in items if x.get("subType") == "AIRPORT"}
        if "HND" in airport_codes or "NRT" in airport_codes:
            return "TYO"

        # You could add other metro mappings here (e.g., JFK/LGA/EWR -> NYC; LHR/LGW -> LON).

        # 4) Last resort: first item’s iataCode (likely an airport)
        first = items[0]
        return first.get("iataCode")


#Old attempts and ways of doing it.
        # #Trying to return the 3 letter IATA city Code, given a city name
        # if not city_name:
        #     raise RuntimeError("Missing city name.")
        #
        # # add safe default for base URL if env missing
        # url = f"{(self._amadeus_api_base or 'https://test.api.amadeus.com')}/v1/reference-data/locations"
        # city_q = (city_name or "").strip()
        #
        # # ---- Attempt 1: CITY only (slightly more generous) ----
        # params = {
        #     "subType":"CITY",
        #     "keyword": city_q,
        #     "page[limit]": 5, #take the first best match now first 5
        #     "view":"FULL" #Illedgidally improves output
        # }
        # response = requests.get(url=url, headers=self._auth_header(), params=params)
        # if response.status_code == 401:
        #     #token likely expired refresh this again
        #     self._token = self._get_new_token()
        #     response = requests.get(url=url, headers=self._auth_header(), params=params)
        #
        # response.raise_for_status()
        # js = response.json()
        # items = js.get("data", [])
        #
        # # prefer CITY with name match (exact/starts-with), else any CITY
        # def _name_matches(it):
        #     n = (it.get("name") or "").lower()
        #     cq = city_q.lower()
        #     return n == cq or n.startswith(cq)
        #
        # city_item = next((x for x in items if x.get("subType") == "CITY" and _name_matches(x)), None)
        # if city_item:
        #     return city_item.get("iataCode")
        #
        # city_item = next((x for x in items if x.get("subType") == "CITY"), None)
        # if city_item:
        #     return city_item.get("iataCode")
        #
        # if not items:
        #     # TEMP DEBUG: print what Amadeus returned for this city
        #     print(f"No results for '{city_name}'; response:", js)
        #
        # # ---- Attempt 2: CITY,AIRPORT fallback with larger limit ----
        # params2 = {
        #     "subType": "CITY,AIRPORT",
        #     "keyword": city_q,
        #     "page[limit]": 10
        # }
        # response2 = requests.get(url=url, headers=self._auth_header(), params=params2)
        # if response2.status_code == 401:
        #     # token likely expired refresh this again
        #     self._token = self._get_new_token()
        #     response2 = requests.get(url=url, headers=self._auth_header(), params=params2)
        #
        # response2.raise_for_status()
        # js2 = response2.json()
        # items2 = js2.get("data", [])
        #
        # # prefer CITY with name match, then any CITY, else first item (likely airport)
        # city_item2 = next((x for x in items2 if x.get("subType") == "CITY" and _name_matches(x)), None)
        # if city_item2:
        #     return city_item2.get("iataCode")
        #
        # city_item2 = next((x for x in items2 if x.get("subType") == "CITY"), None)
        # if city_item2:
        #     return city_item2.get("iataCode")
        #
        # if items2:
        #     return items2[0].get("iataCode")
        #
        # # locations with iataCode for CITY
        # # (kept for reference, but unreachable if we got here with no items)
        # # code = items[0].get("iataCode")
        # # return code
        #
        # return None

