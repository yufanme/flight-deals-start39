from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

sheet_manager = DataManager()
search = FlightSearch()
sheet_data = sheet_manager.get_destination_data()
for data in sheet_data:
    if not data["iataCode"]:
        data["iataCode"] = search.get_destination_code(data["city"])

sheet_manager.destination_data = sheet_data
# sheet_manager.update_destination_codes()

flightdata=FlightData()

# for data in sheet_data:
#     search_data = search.get_price(data["iataCode"])
#     print(search_data["data"][0]["price"])

data = search.get_price(sheet_data[0]["iataCode"])
print(data)