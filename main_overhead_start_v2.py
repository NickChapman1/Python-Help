import requests
import time
import smtplib
from datetime import datetime, timezone

while True:
    MyEmail = "your email"
    password = "your pw"  # Use an App Password if you're using Gmail with 2FA
    app_password = "your app pw"
    MY_LAT = 51.507351 # Your latitude
    MY_LONG = -0.127758 # Your longitude
    #sending parameters into api call in form of a dictionary

    #Get ISS info
    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    iss_parameters = {
        "Lat": iss_latitude,
        "lng": iss_longitude,
        "formatted": 0,
    }

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
    # Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        iss_close = True
    else:
        iss_close = False
    #Is it currently dark
    time_now = datetime.now(timezone.utc).hour
    is_dark = time_now >= sunset or time_now <= sunrise
    if not iss_close and is_dark:
        print("Look up! The ISS is overhead and it's dark.")
        # Create a secure SSL connection   # Then send me an email to tell me to look up.
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as g_connection:
            g_connection.login(user=MyEmail, password=app_password)
            g_connection.sendmail(
                from_addr=MyEmail,
                to_addrs=MyEmail,
                msg="Subject:Test Email\n\nLook up"
            )
    # BONUS:  run the code every 60 seconds.

    time.sleep(60)




