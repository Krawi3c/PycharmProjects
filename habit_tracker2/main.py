import requests
import pandas
import time

USERNAME = "krawiecki"
TOKEN = "hjk2fkj7jhk290df"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixels_endpoint = f"{graph_endpoint}/graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_params = {
    "id": "graph1",
    "name": "Taxi Statistics",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.delete(url=pixels_endpoint, headers=headers)
# print(response.text)
#
# response2 = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response2.text)

data = pandas.read_csv("luty.csv")
km = [float(n) for n in data["Odległość"]]
dates = [n for n in data["Czas zamówienia"]]
for x in range(len(dates)):
    dates_mod = dates[x].replace(".", "")
    dates_mod = dates_mod[:8]
    year = dates_mod[4:8]
    month = dates_mod[2:4]
    day = dates_mod[:2]
    whole_dates = year + month + day
    dates[x] = whole_dates

dates_index = []
for date in dates:
    if date in date:
        dates_index.append(dates.index(date))

indexes = []
for x in range(len(dates_index)):
    if dates_index[x - 1] != dates_index[x]:
        indexes.append(dates_index[x])

new_date_list = []
for x in range(len(dates_index)):
    if dates[x - 1] != dates[x]:
        new_date_list.append(dates[x])
new_km_list = []
s = 0
for index in indexes:
    if index != 0:
        new_km_list.append(round(sum(km[s:int(index)]), 2))
    s = index
    if s == indexes[-1]:
        new_km_list.append(round(sum(km[s:len(km)]), 2))

for x in range(len(new_date_list)):
    pixel_data = {
        "date": new_date_list[x],
        "quantity": str(new_km_list[x]),
    }
    response = requests.post(url=pixels_endpoint, json=pixel_data, headers=headers)
    while response.text != '{"message":"Success.","isSuccess":true}':
        response = requests.post(url=pixels_endpoint, json=pixel_data, headers=headers)
    print(f"{x}, {response.text}")
