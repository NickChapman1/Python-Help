import requests
import time
import smtplib
from datetime import datetime, timezone

#while True:
MyEmail = "your email"
password = "your pw"  # Use an App Password if you're using Gmail with 2FA
app_password = "your pw"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
#sending parameters into api call in form of a dictionary

def is_iss_overhead():
    #Get ISS info
    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT+5 and  MY_LONG -5 <= iss_latitude <= MY_LONG+5:
        return True

def is_night():
    my_parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=my_parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour
    if time_now >= sunset or time_now <= sunrise:
        return True

# Then send me an email to tell me to look up.
while True:
    # BONUS:  run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as g_connection:
            g_connection.login(user=MyEmail, password=app_password)
            g_connection.sendmail(
                from_addr=MyEmail,
                to_addrs=MyEmail,
                msg="Subject:Test Email\n\nLook UP! \n ISS is above you in the sky"
            )