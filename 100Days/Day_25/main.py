# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

# average = data["temp"].mean()
# print(f"average: {average}")
#
# maximum = data["temp"].max()
# print(f"Maximum: {maximum}")

# Get data in columns :
# print(data["condition"])
# print(data.condition)

# Get data in rows :
# print(data[data.day == "Sunday"])

# print(data[data.temp == data.temp.max()])


data_dict = {
    "students": ["Arjun", "Anu", "Viji"],
    "scores": [89, 94, 92]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")