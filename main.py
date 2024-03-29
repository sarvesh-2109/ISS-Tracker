import requests
from datetime import datetime
import smtplib
import time

MY_LAT = # Your latitude
MY_LONG = # Your longitude

MY_EMAIL = #Your email
PASSWORD = # Your password

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def my_position():
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= MY_LONG <= (MY_LONG + 5):
        return True
    else:
        return False


current_location = my_position()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

while True:
    time.sleep(60)
    if current_location:
        if current_hour >= sunset or current_hour <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:ISS Alert!\n\nThe ISS Tracker is now visible in the sky."
                )
