import pandas as pd
import babel.numbers, decimal 
import matplotlib.pyplot as plt

df = pd.read_csv("london_house_prices.csv")

def distance(miles):
    return miles * 1609.34

df["nearest_station_meters"] = df["nearest_station_meters"].apply(distance)

df["postcode_outer"].fillna(-1, inplace=True)
df["size_sqft"].fillna(-1, inplace=True)



# less_500 = df[df["nearest_station_meters"]<500]["price_pounds"].mean()
# more_500 = df[df["nearest_station_meters"]>500]["price_pounds"].mean()

# less_500 = round(less_500, 2)
# more_500 = round(more_500, 2)

# print("Цена домов ближе, чем 500 метров от публичного транспорта: ", babel.numbers.format_currency(decimal.Decimal(less_500), "GBP" ))
# print("Цена домов дальше, чем 500 метров от публичного транспорта:", babel.numbers.format_currency(decimal.Decimal(more_500), "GBP" ))


maxless = round(df[df["nearest_station_meters"]<500]["price_pounds"].max(), 2)
maxmore = round(df[df["nearest_station_meters"]>500]["price_pounds"].max(), 2)

minless = round(df[df["nearest_station_meters"]<500]["price_pounds"].min(), 2)
minmore = round(df[df["nearest_station_meters"]>500]["price_pounds"].min(), 2)

meanless = round(df[df["nearest_station_meters"]<500]["price_pounds"].mean(), 2)
meanmore = round(df[df["nearest_station_meters"]>500]["price_pounds"].mean(), 2)

midless = round(df[df["nearest_station_meters"]<500]["price_pounds"].median(), 2)
midmore = round(df[df["nearest_station_meters"]>500]["price_pounds"].median(), 2)

less = round(midless / 1000000, 2)
more = round(midmore / 1000000, 2)

# s0 = pd.Series(data = [maxless, maxmore], index = ["ближе", "дальше"])
# s0.plot(kind="bar")
# plt.show()


# fig, ax = plt.subplots()
# name = ["ближе, чем 500 метров" + "\n" + "от общественного транспорта", "дальше, чем 500 метров" + "\n" + "от общественного транспорта"]
# counts = [less, more]
# bar_colours = ["tab:red", "tab:blue"]

# ax.bar(name, counts, color=bar_colours)

# ax.set_ylabel("Фунты (в миллионах)")
# ax.set_title("Среднее значения цен квартир в Лондоне")
# plt.show()


counter = 0
central = 0
suburban = 0

def central_apply(row):
    global central, counter
    if row["nearest_station_name"].strip() == "Oxford Circus Station":
        counter += 1
        central += row["price_pounds"]

def central_apply(row):
    global suburban, counter
    if row["nearest_station_name"].strip() == "Epping Station":
        counter += 1
        suburban += row["price_pounds"]

df.apply(central_apply, axis=1)
central /= counter
suburban /= counter
central /= 1000000
suburban /= 1000000

fig, ax = plt.subplots()
name = ["Рядом со станцией в центральном Лондоне", "Рядом со станцией на оркаине Лондона"]
counts = [central, suburban]
bar_colours = ["tab:red", "tab:blue"]

ax.bar(name, counts, color=bar_colours)

ax.set_ylabel("Фунты (в миллионах)")
ax.set_title("Среднее цена квартир в Лондоне")
plt.show()

# s0 = pd.Series(data = [minless, minmore], index = ["ближе", "дальше"])
# s0.plot(kind="bar")
# plt.show()
# s0 = pd.Series(data = [meanless, meanmore], index = ["ближе", "дальше"])
# s0.plot(kind="bar")
# plt.show()
# s0 = pd.Series(data = [midless, midmore], index = ["ближе", "дальше"])
# s0.plot(kind="bar")
# plt.show()

