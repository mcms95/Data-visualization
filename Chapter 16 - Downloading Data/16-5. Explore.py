# Ex -> Generate a few more visualizations that examine any other weather aspect you’re interested in for any locations you’re curious about.

from datetime import datetime
import csv
import matplotlib.pyplot as plt


def get_rainfall(filename, date, rainfall):

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_index = header_row.index('DATE')
        rainfall = header_row.index('PRCP')

        for row in reader:
            date = date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                rain = float(row[rainfall])
            except ValueError:
                print(f"Data missing from day {date}")
            else:
                rainfalls.append(rain)
                dates.append(date)


# Sitka
rainfalls, dates = [], []
filename = 'weather_data/sitka_weather_2021_full.csv'
get_rainfall(filename, dates, rainfalls)


# plot Sitka data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='blue', alpha=0.5)

# Deathvalley
filename = 'weather_data/death_valley_2021_full.csv'
dates, rainfalls = [], []
get_rainfall(filename, dates, rainfalls)

ax.plot(dates, rainfalls, color='red', alpha=0.5)

# Format plot
ax.set_title("Daily Rainfalls in Valley and Sitka", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rain', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
