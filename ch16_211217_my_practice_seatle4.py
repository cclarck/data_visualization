#!/usr/bin/env python3
# 12.17.2021 12:10:36 CST
# title = ch16 my practice seatle weather 4 dates using set()
# https://www.ncei.noaa.gov/access/search/data-search/local-climatological-data
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'SEATTLE_SAND_POINT_WEATHER_FORECAST_OFFICE_WA_US.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    #for index, column_header in enumerate(header_row):
        # print(index, column_header)
    # dates, highs = [], []
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S')
        dates.append(current_date.date())
            
        if row[36]:
            high = int(row[36])
            highs.append(high)
        
        if row[37]:
            low = int(row[37])
            lows.append(low)
        # else:
            # high = 0
            # highs.append(high)

# print(dates)
# filtering repeat date from original data      
# dts = []
# for dt in dates:
    # if  dt not in dts:
        # dts.append(dt)
dts = []
print(dates)
dts = list(set(dates))
dts.sort()
# print(dts)

# # plot the high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dts, highs, c='red')
ax.plot(dts, lows, c='blue')

# # format plot
plt.title("Seatle Daily High and Low Dry Bulb Temperature - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('ch16_211217_my_practice_seatle_weather4.png')
plt.show()


