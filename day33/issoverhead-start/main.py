import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -33.868820 # Your latitude
MY_LONG = 151.209290 # Your longitude



#Your position is within +5 or -5 degrees of the ISS position.
def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():

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

    time_now = datetime.now().hour

    if sunset >= time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_position() and is_night():
        my_email = "yutama.py@gmail.com"
        my_password = "satuDuatiga!"
        email_to = "yutama.iw@gmail.com"
        email_v = "vienettachristina@yahoo.com"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(
                user=my_email,
                password=my_password
            )
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_to,
                msg=f"Subject: The ISS Position \n\n is above you"
            )


