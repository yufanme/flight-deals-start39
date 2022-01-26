import requests
from pprint import pprint
import datetime
from flight_data import FlightData

TEQUILA_API_KEY = "h5n2UC41Yp-wGnD5tmYfZFXb8OKjNJSH"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

ORIGINAL_CITY_CODE = "LON"
DATE_FROM = 1
DATE_TO = 180
NIGHT_IN_DST_FROM = 7
NIGHT_IN_DST_TO = 28
FLIGHT_TYPE = "round"
ONE_FOR_CITY = 1
CURRENCY = "GBP"
MAX_STOPOVERS = 0


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

    def check_flight(self, destination_city_code):
        # handle time.
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=DATE_FROM)
        six_month_later = datetime.datetime.now() + datetime.timedelta(days=DATE_TO)
        # search flight with arguments and get results.
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        search_params = {
            "fly_from": ORIGINAL_CITY_CODE,
            "fly_to": destination_city_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_month_later.strftime("%d/%m/%Y"),
            "nights_in_dst_from": NIGHT_IN_DST_FROM,
            "nights_in_dst_to": NIGHT_IN_DST_TO,
            "flight_type": FLIGHT_TYPE,
            "curr": CURRENCY,
            "max_stopovers": MAX_STOPOVERS,
            "one_for_city": ONE_FOR_CITY
        }
        response = requests.get(url=search_endpoint, headers=headers, params=search_params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flight found in {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: ￡{flight_data.price}")
            return flight_data


f = FlightSearch()
f.check_flight("PAR")
