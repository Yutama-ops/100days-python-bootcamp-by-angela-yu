import requests
from datetime import datetime

USERNAME = "tama"
TOKEN = "bi2q3j3b45213"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
parameters_graph = {
    "id": graph_id,
    "name": "onemonth",
    "unit": "day",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=parameters_graph, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime(year=2022, month=4, day=15)
formated_time = today.strftime("%Y%m%d")
param_pixel = {
    "date": formated_time,
    "quantity": "1"
}

# response = requests.post(url=pixel_endpoint, json=param_pixel, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{graph_endpoint}/{graph_id}/{formated_time}"


param_pixel_update = {
    "quantity": "10"
}


response = requests.put(url=pixel_update_endpoint, json=param_pixel_update, headers=headers)
print(response.text)