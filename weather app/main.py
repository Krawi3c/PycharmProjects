import requests

parameters = {
    "lat": 54.316731,
    "lon": 18.570391,
    "appid": "880dfefd21255462f362ee299479e271",
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
data = response.json()
print(data)