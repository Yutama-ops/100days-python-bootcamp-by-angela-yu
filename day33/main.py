import requests
from datetime import datetime
LATITUDE = -6.175110
LONGITUDE = 106.865036
# uerel = "http://api.open-notify.org/iss-now.json"
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # raise the response
# response.raise_for_status()
#
# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_pos = (longitude, latitude)
# print(iss_pos)

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

timenow = datetime.now()
print(timenow.hour)