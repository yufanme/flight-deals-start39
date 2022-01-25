import requests
from pprint import pprint
from flight_data import FlightData

TEQUILA_API_KEY = "h5n2UC41Yp-wGnD5tmYfZFXb8OKjNJSH"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

flightdata = FlightData()
departure_city = flightdata.fly_from
stay_from = flightdata.stay_from
stay_to = flightdata.stay_to
from_time = flightdata.date_from
to_time = flightdata.date_to
fly_type = flightdata.fly_type
currency = flightdata.currency


class FlightSearch:

    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_params = {
            "term": city_name,
            "location_types": "city"
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        location_response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=location_params,
                                         headers=headers)
        code = location_response.json()["locations"][0]["code"]
        return code

    def get_price(self, to_city):
        search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        search_params = {
            "fly_from": departure_city,
            "fly_to": to_city,
            "nights_in_dst_from": stay_from,
            "nights_in_dst_to": stay_to,
            "date_from": from_time,
            "date_to": to_time,
            "flight_type": fly_type,
            "curr": currency
        }
        response = requests.get(url=search_endpoint, headers=headers, params=search_params)
        data = response.json()
        pprint(data)
        return data

#
# params = {
#     "fly_from": "HKG",
#     "fly_to": "PAR",
#     "date_from": "02/01/2022",
#     "date_to": "06/09/2022",
# }
# headers = {"apikey": TEQUILA_API_KEY}
# response = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=params, headers=headers)
# data = response.json()
# print(data)
