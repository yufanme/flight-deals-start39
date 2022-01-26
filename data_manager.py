import requests
SHEET_PRICES_ENDPOINT = "https://api.sheety.co/ceecbf3b3e374ffa88da8b446ee81ce6/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {
                        "iataCode": city["iataCode"],
                    }
            }
            response = requests.put(
                url=f"{SHEET_PRICES_ENDPOINT}/{city['id']}",
                json=new_data)
            response.raise_for_status()
            print(response.text)




