# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#
#     for row in data:
#         temperatures.append(row[1])
#     del temperatures[0]
#     for i in range(len(temperatures)):
#         temperatures[i] = int(temperatures[i])
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # temp_avg = sum(temp_list) / len(temp_list)
# # print(data["condition"])
#
# data["temp"].max()
# # print(data[data["temp"] == data["temp"].max()])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp*1.8 + 32)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# pd_data = pd.DataFrame(data_dict)
# print(pd_data)
# pd_data.to_csv("new_data.csv")

data = pd.read_csv("2018_Central_Park_Squirrel.csv")
fur_data = data["Primary Fur Color"].to_list()
Gray = fur_data.count("Gray")
Cinnamon = fur_data.count("Cinnamon")
Black = fur_data.count("Black")

fur_data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [Gray, Cinnamon, Black]
}
fur_data_dict = pd.DataFrame(fur_data_dict)
fur_data_dict.to_csv("squirrel_count.csv")