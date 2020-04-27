from random import randint
import pygal

class Die():
	"""docstring for Die"""
	def __init__(self, side_num):
		self.side_num = side_num

	def roll(self):
		"""返回一个位于1和骰子面数之间的随机数"""
		return randint(1, self.side_num)

#创建实例
die_1 = Die(side_num = 6)
die_2 = Die(side_num = 10)

results = []

for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#分析结果
frequencies = []

max_side_num = die_1.side_num + die_2.side_num

for value in range(2, max_side_num +1):
	frequency =  results.count(value)
	frequencies.append(frequency)

print(frequencies)

#条形图

hist = pygal.Bar()

hist.title = "Results of rolling D6 and D10 dict 50000 times"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('D6D10_die_frequency.svg')



