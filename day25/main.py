# with open("weather_data.csv") as data:
#     weather_data = data.readlines()

# import csv
#
# with open("weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     # for row in weather_data:
#     #     print(row)
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
#
# datadict = data.to_dict()
# print(datadict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in columns

# data.temp

# get data in row
# max_temp_data = data[data.temp == data.temp.max()]
# print(max_temp_data)

# monday = data[data.day == "Monday"]
# print(monday.temp.add(300))

# hello sayangnya aku yutama budiman hffhfhugnbfsagfgubfwrbgbduhgbegaohtfg

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_d = pandas.DataFrame(data_dict)
# print(data_d)
# data_d.to_csv("new_data.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_data = data["Primary Fur Color"]

color_data_grey = len(data[data["Primary Fur Color"] == "Gray"])
# grey = color_data_grey["Primary Fur Color"].value_counts()
# print(grey)

color_data_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# cinnamon = color_data_cinnamon["Primary Fur Color"].value_counts()
# print(cinnamon)

color_data_black = len(data[data["Primary Fur Color"] == "Black"])
# black = color_data_black["Primary Fur Color"].value_counts()
# print(black)

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [color_data_grey, color_data_cinnamon, color_data_black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Newest_Data.csv")


