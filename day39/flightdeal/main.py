#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
from data_manager import DataManager
from flight_search import FlightSearch

# use flight search

# use sheety api
sheet_data = DataManager()
sheet_data.get_data()
sheet_data = sheet_data.data
# print(sheet_data)
for data in sheet_data:
    if data['iataCode'] == "":
        flight_search = FlightSearch()
        data['iataCode'] = flight_search.update_iata(data['city'])
        print(data['iataCode'])

# use flight search api to check for the cheapest flight between tromorrow to 6 month latter for all the cities in google sheet

# if the price is lower than the lowest price the app will send you a message use twilio API

# the sms should include the departure airport IATA code