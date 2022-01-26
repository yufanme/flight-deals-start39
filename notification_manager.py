import smtplib

EMAIL = "562937707@qq.com"
PASSWORD = "bpyjiqjylklcbdhe"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_alert_email(self, price, origin_city, origin_airport, destination_city, destination_airport,
                         out_date, return_date):
        with smtplib.SMTP("smtp.qq.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL, msg=f"Subject:Low price flight alert!\n\n"
                                    f"only {price} pounds to fly from {origin_city}-{origin_airport} to "
                                    f"{destination_city}-{destination_airport}, from"
                                    f"{out_date} to {return_date}.")
