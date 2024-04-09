import smtplib
from random import choice
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt", "r") as data_file:
    all_quotes = data_file.readlines()
    quote = choice(all_quotes)

my_email = "Krawiec2001k@gmail.com"
password = "ojhhkgjdhrrjzppq"

print(weekday)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password = password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject: Monday Motivation\n\n"
            f"{quote}")
connection.close()