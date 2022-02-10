# with open("weather_data.csv") as data:
#     weather_data = data.readlines()

import csv

with open("weather_data.csv") as data:
    weather_data = csv.reader(data)
    temperatures = []
    # for row in weather_data:
    #     print(row)
    for row in weather_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)