import requests
from datetime import datetime as dt

html_graph1 = "https://pixe.la/v1/users/krawiec2001k/graphs/graph1.html"
user_html = "https://pixe.la/@krawiec2001k"
USERNAME = "krawiec2001k"
TOKEN = "hg1423f54gh5jhg"
pixela_endpoint ="https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
graphID = "graph1"
today = dt.now()
date = today.strftime("%Y%m%d")
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": graphID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# habit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"
# today = dt.now()
# habit_config = {
#     "date": date,
#     "quantity": "9.74",
# }
#
# response = requests.post(url=habit_endpoint, json=habit_config, headers=headers)
# print(response.text)
# change_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{date}"
# change_config = {
#     "quantity": "9.00"
# }
# response = requests.put(url=change_endpoint, json=change_config, headers=headers)
# print(response.text)
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{date}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)