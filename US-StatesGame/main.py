# import csv
# with open("weather_data.csv") as data:
#     dat = csv.reader(data)
#     temprature = []
#     for row in dat:
#
#         print(row)
#
import pandas
# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# print(monday.temp)
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "value" : ["Grey", "Red", "Black"],
    "Count" : [grey_count, red_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")


