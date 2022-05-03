#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
Data = DataManager()
FlightSearch = FlightSearch()

sheet_data = Data.getData()
# print(sheet_data)

# FlightSearch.updateData(sheet_data)
# print(sheet_data)
# print(Data.putData(sheet_data))
# print("a")

FlightSearch.get_destination_code()
