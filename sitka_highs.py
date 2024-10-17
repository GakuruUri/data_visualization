from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()


reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

print(highs)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot
ax.set_title("Daily High Tempratures, 2021", fontsize=24)
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