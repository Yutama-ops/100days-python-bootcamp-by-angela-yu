import requests
SHEETY_ENDPOINT = "https://api.sheety.co/43e1951c5c9ac91cd68adc6a3cc50dd5/flightDetails/prices"
SHEETY_TOKEN = "Bearer sdjahcgfikaswudygfc;oajs"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

        # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data
        # to update the Google Sheet with the IATA codes. (Do this using code).

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    # def getData(self):
    #     self.response = requests.get(url=self.endpoint)
    #     self.data = self.response.json()
    #     return self.data['prices']
    #
    # def updateData(self, data, city):
    #     for param in data:
    #         params = {
    #             "price": {
    #                 "city": param["city"],
    #                 "iataCode": city,
    #                 "lowestPrice": param["lowestPrice"]
    #             }
    #         }
    #         self.response = requests.put(url=f"{self.endpoint}/{param['id']}", json=params, headers=self.token)
    #         print("a")

    # def updateData(self,sheet_data):
    #     for data in sheet_data:
    #         data['iataCode'] = location_type

    #This class is responsible for talking to the Google Sheet.
    pass