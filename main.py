from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

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

for destination in sheet_data:
    flight = search.check_flight(destination["iataCode"])
    if flight and destination["lowestPrice"] > flight.price:
        notification = NotificationManager()
        notification.send_alert_email(
            price=flight.price,
            origin_city=flight.origin_city,
            origin_airport=flight.origin_airport,
            destination_city=flight.destination_city,
            destination_airport=flight.destination_airport,
            out_date=flight.out_date,
            return_date=flight.return_date
        )
        print(f"{flight.destination_city} has lower price {flight.price} pounds "
              f"than aim price {destination['lowestPrice']} pounds, alert email sent.")
