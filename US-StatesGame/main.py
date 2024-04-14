# import csv
# with open("weather_data.csv") as data:
#     dat = csv.reader(data)
#     temprature = []
#     for row in dat:
#
#         print(row)

import pandas
data = pandas.read_csv("weather_data.csv")
monday = data[data.day == "Monday"]
print(monday.temp)
