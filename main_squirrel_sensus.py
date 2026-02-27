import pandas
#
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_counts = data["Primary Fur Color"].value_counts().reset_index()
#color_counts.columns = ["Color", "Count"]
df = pandas.DataFrame(color_counts)
df.to_csv("squirrel count.csv")

#OR

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(color_counts)
df.to_csv("squirrel count1.csv")