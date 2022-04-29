import requests
from datetime import datetime

today = datetime.now()
formated_time = today.strftime("%d/%m/%Y")
print(formated_time)
# query = input("Tell me what you did today: ")



APP_ID = "83262296"
API_KEY = "257304e0fd934c06e45d36505afd0cde"
nutriotionixEndpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {
    "query": "ran 10 miles strength training for 1 hour"
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=nutriotionixEndpoint, json=parameters, headers=headers)
print(response)

wson = response.json()

ex = wson["exercises"][0]
print(ex)
