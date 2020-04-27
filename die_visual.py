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
die = Die(side_num = 6)
results = []

for roll_num in range(1000):
	result = die.roll()
	results.append(result)

#分析结果
frequencies = []

for value in range(1, die.side_num +1):
	frequency =  results.count(value)
	frequencies.append(frequency)

print(frequencies)

#条形图

hist = pygal.Bar()

hist.title = "Results of rolling D6 1000 times"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_frequency.svg')



