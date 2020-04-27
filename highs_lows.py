import csv
import matplotlib.pyplot as plt

from datetime import datetime 

filename = 'death_valley_2018_simple.csv'

#打开这个文件，并将结果对象存储于f中
with open(filename) as f:
	reader = csv.reader(f)
	head_row = next(reader)
#	print(head_row)

	for index, column_name in enumerate(head_row):
		print(index, column_name)

	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[2], '%Y-%m-%d')
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(current_date, 'missing date')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#	print(highs)

fig = plt.figure(figsize = (10, 6), dpi = 128)

plt.plot(dates, highs, c = (0, 0.7, 0), linewidth = 2, alpha = 0.5)
plt.plot(dates, lows, c = (0, 0, 0.9), linewidth = 2, alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'red', alpha = 0.2)

plt.title("Daily high and low temperatures, July 2018, CA", fontsize = 24)
plt.xlabel('Date', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperatures(F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'both', labelsize = 16)

plt.show()