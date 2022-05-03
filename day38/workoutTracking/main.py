import requests
from datetime import datetime

today = datetime.now()
formated_date = today.strftime("%d/%m/%Y")
formated_hour = today.strftime("%H:%M:%S")

print(formated_date)
print(formated_hour)

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

ex = wson["exercises"]
for exercise in ex:
    print(exercise)
    ex_params = {
        "workout": {
            "date": formated_date,
            "time": formated_hour,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {
        "Authorization": "Bearer nyeheheasfdghdsfger"
    }
    print(ex_params)
    sheety_get = 'https://api.sheety.co/43e1951c5c9ac91cd68adc6a3cc50dd5/myWorkout/workouts'
    sheety_post = 'https://api.sheety.co/43e1951c5c9ac91cd68adc6a3cc50dd5/myWorkout/workouts'
    response = requests.get(url=sheety_post, headers=headers)
    print(response)
    response = requests.post(url=sheety_post, json=ex_params, headers=headers)
    print(response)


