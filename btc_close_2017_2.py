import json
import pygal
import math

#将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
closes = []

#打印每一天的信息
for btc_dict in btc_data:
	date = btc_dict['date']
	dates.append(date)
	month = int(btc_dict['month'])
	months.append(month)
	week = int(btc_dict['week'])
	weeks.append(week)
	weekday = btc_dict['weekday']
	weekdays.append(weekday)
	close = int(float(btc_dict['close']))
	closes.append(close)

#	print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
line_chart.title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
closes_log = [math.log10(_) for _ in closes]
line_chart.add('log收盘价', closes_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')
#line_chart.show()