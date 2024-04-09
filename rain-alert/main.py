import requests
from twilio.rest import Client

twilio_recovery_code = "1O2ZpPVDETlzBvAuYpZJfPQ1gDikj80lKZ9CdoEm"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = 'AC3d1bf4faa7a08e15c8bae6afa06f2fc5'
auth_token = '495ac29417777e6b837ebbf795ab941a'
api_key = "69f04e4613056b159c2761a9d9e664d2"

MY_LAT = 51.507351
MY_LNG = -0.127758
PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()
data = response.json()["hourly"]

weather_slice = data[:12]

will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+12707137151",
        to="+48730342138"
    )
