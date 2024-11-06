from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# path = Path('weather_data/sitka_weather_2021_simple.csv')
path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()


reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
        # high = int(row[4])
        # low = int(row[5])

    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(highs)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Format plot
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()



"""
# Extract high tempratures
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
"""


"""
Printing the Headers and Their Positions

for index, column_header in enumerate(header_row):
    print(index, column_header)
# print(header_row)
"""



# from pathlib import Path
# import csv

# path = Path('weather_data/death_valley_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# for Index, column_header in enumerate(header_row):
#     print(Index, column_header)