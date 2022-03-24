import requests
import json
from twilio.rest import Client

number = "(904) 877-8332"
api = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "e4251157d06a1f6125060e2c982933bb"
LAT = -33.868820
LONG = 151.209290
EX = "current,minutely,daily"
parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "exclude": EX

}

account_sid = "AC3d5697b0c7e520f48d66fd1492755370"
auth_token = "bd6d31d367ce85ed828d7c3252721ef2"
number = "+19048778332"



response = requests.get(api, params=parameters)
response.raise_for_status()
r_j = response.json()
# with open("w_json.json", "w") as file:
#     json.dump(r_j, file, indent=4)

# bring umbrela if any of 12 houirs less than 700
for i in range(0,13):
    weather = r_j["hourly"][i]["weather"][0]["id"] > 700
    # print(r_j["hourly"][i]["weather"][0]["id"])
# or

# weather_slice = r_j["hourly"][:12]
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) > 700:
#         print("Bring an Umbrella")

if 700 > int(weather):
    print("rain")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrela.",
        from_=number,
        to='+61460707773'
    )

    print(message.sid)