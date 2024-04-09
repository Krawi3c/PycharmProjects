import smtplib

MY_EMAIL = "Krawiec2001k@gmail.com"
PASSWORD = "ojhhkgjdhrrjzppq"


class EmailManagement:

    def __init__(self):
        pass

    def send_email(price, price_fraction, title):
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject: Price of your product went down!\n"
                        f"Your product:\n"
                        f"{title}\n"
                        f"Has a price of: {price},{price_fraction}")
                connection.close()
        except UnicodeEncodeError:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject: Price of your product went down!\n"
                        f"Your product:\n"
                        f"{str(title.encode('utf-8'))}\n"
                        f"Has a price of: {price},{price_fraction}")
                connection.close()
