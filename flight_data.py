import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.fly_from = "LON"
        self.date_from = self.get_now_formatted()
        self.date_to = self.get_six_month_formatted()
        self.stay_from = 7
        self.stay_to = 28
        self.fly_type = "round"
        self.currency = "GBP"


    def get_now_formatted(self):
        now = datetime.datetime.now()
        formatted_now = now.strftime("%d/%m/%Y")
        return formatted_now

    def get_six_month_formatted(self):
        six_month_later = datetime.datetime.now() + datetime.timedelta(days=180)
        formatted_six_month = six_month_later.strftime("%d/%m/%Y")
        return formatted_six_month

