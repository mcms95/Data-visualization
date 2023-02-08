# Ex -> Sitka is located in a temperate rainforest, so it gets a fair amount of rainfall. In the data file sitka_weather_2021_full.csv is a header called PRCP, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.

from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# print(header_row)

# for index, header_name in enumerate(header_row):
#    print(f"{index} {header_name}")

# Extract high temperatures
rainfalls, dates = [], []

for row in reader:
    rainfall = float(row[5])
    rainfalls.append(rainfall)
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)

# Plot high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='red')

# Format plot
ax.set_title("daily rainfall amounts in Sitka", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Rain amount', fontsize=16)
# fig.autofmt_xdate()
ax.tick_params(labelsize=16)

plt.show()
