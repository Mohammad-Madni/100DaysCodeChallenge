# import csv
# with open("weather_data.csv") as data:
#     dat = csv.reader(data)
#     temprature = []
#     for row in dat:
#
#         print(row)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"].max())
