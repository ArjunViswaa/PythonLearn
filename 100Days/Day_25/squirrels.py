import pandas

squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Black"])

# print(gray_squirrel_count, red_squirrel_count, black_squirrel_count)

data_dict = {
    "Squirrel Color": ["Gray", "Red", "Black"],
    "Squirrel Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

solCSV = pandas.DataFrame(data_dict)
print(solCSV)