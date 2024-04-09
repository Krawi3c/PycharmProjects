# try:
#     response = requests.get(url="http://api.open-notify.org/is-now.json")
#     response.raise_for_status()
# except:
#     print("Nie znaleziono")
# else:
#     data = response.json()["iss_position"]
#     print(data)

import requests
from datetime import datetime
import smtplib

MY_EMAIL = "Krawiec2001k@gmail.com"
PASSWORD = "ojhhkgjdhrrjzppq"
MY_LAT = 51.507351  # Your latitude
MY_LNG = -0.127758  # Your longitude
PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night_time():
    response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour = datetime.now().hour
    if hour >= sunset:
        return True


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:ISS\n\n"
                                "Look up!")
    connection.close()


if is_iss_overhead() and is_night_time():
    send_mail()
