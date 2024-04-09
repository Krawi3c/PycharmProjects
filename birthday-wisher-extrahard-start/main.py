import pandas
import smtplib
import datetime as dt

MY_EMAIL = "krawiec2001k@gmail.com"
PASSWORD = "xrgi yesz evon jfcd"


def send_email(email, message_text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            MY_EMAIL,
            email,
            message_text.encode("utf-8"),
        )


with open("letter_1.txt", "r", encoding="utf-8") as letter_file:
    letter = letter_file.read()

birthdays_csv = pandas.read_csv('birthdays.csv')
names = birthdays_csv['name'].to_list()
emails = birthdays_csv['email'].to_list()
years = birthdays_csv['year'].to_list()
months = birthdays_csv['month'].to_list()
days = birthdays_csv['day'].to_list()

dates = []
for x in range(len(names)):
    dates.append({
        "Name": names[x],
        "Email": emails[x],
        "Year": years[x],
        "Month": months[x],
        "Day": days[x],
    })
this_month = int(dt.datetime.now().strftime('%m').replace('0', ''))
this_day = int(dt.datetime.now().strftime('%d').replace('0', ''))
for x in range(len(dates)):
    month = dates[x].get("Month")
    day = dates[x].get("Day")
    if month == this_month and day == this_day:
        message = letter.replace("[NAME]", dates[x].get("Name"))
        send_email(dates[x].get("Email"), message)
