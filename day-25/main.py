# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])

# import pandas
#
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("squirrel_data.csv")

squirrel_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [],
}
grey = len(data[data["Primary Fur Color"]=="Gray"])
black = len(data[data["Primary Fur Color"]=="Black"])
cinnamon = len(data[data["Primary Fur Color"]=="Cinnamon"])
squirrel_dict["Count"] = [grey, black, cinnamon]
squirrel = pandas.DataFrame(squirrel_dict)
squirrel.to_csv("squirrel_count.csv")
