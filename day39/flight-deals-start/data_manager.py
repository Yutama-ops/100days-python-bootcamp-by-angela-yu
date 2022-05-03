import requests
class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/43e1951c5c9ac91cd68adc6a3cc50dd5/flightDetails/prices"
        self.token = "Bearer sdjahcgfikaswudygfc;oajs"

    def getData(self):
        self.response = requests.get(url=self.endpoint)
        self.data = self.response.json()
        return self.data['prices']

    def putData(self, data):
        for param in data:
            params = {
                "price": {
                    "city": param["city"],
                    "iataCode": param["iataCode"],
                    "lowestPrice": param["lowestPrice"]
                }
            }
            self.response = requests.put(url=f"{self.endpoint}/{param['id']}", json=params)
            print("a")

    def updateData(self,sheet_data):
        for data in sheet_data:
            data['iataCode'] = location_type

    #This class is responsible for talking to the Google Sheet.
    pass