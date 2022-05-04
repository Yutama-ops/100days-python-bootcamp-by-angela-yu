import requests

SHEETY_ENDPOINT = "https://api.sheety.co/43e1951c5c9ac91cd68adc6a3cc50dd5/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def get_data(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.data = self.response.json()['prices']
        return self.data

    def put_data(self, sheet_data):
        for data in sheet_data:
            self.response = requests.put(url=f"{SHEETY_ENDPOINT}/{data['id']}", json=self.data)
            self.data = self.response.json()['prices']
            return self.data