#!/usr/bin/env python3
# 12.17.2021 14:09:37 CST
# title = ch16 my practice seatle weather 6 error checking
# https://www.ncei.noaa.gov/access/search/data-search/local-climatological-data
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'SEATTLE_SAND_POINT_WEATHER_FORECAST_OFFICE_WA_US.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # for index, column_header in enumerate(header_row):
        # print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S')
        try:
            high = int(row[36])
            low = int(row[37])
        except ValueError:
            # ValueError: invalid literal for int() with base 10: ''
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date.date())
            highs.append(high)
            lows.append(low)
            
# # plot the high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # format plot
title = "Daily High and Low Dry Bulb Temperature - 2018\nSeatle, WA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('ch16_211217_my_practice_seatle_weather6.png')
plt.show()

            
