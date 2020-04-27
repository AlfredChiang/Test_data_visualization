import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
 	"""docstring for RandomWalk"""
 	def __init__(self, number_points):
 		"""初始化随机漫步属性"""
 		self.number_points = number_points

 		#所有随机漫步都始于(0,0)
 		self.x_values = [0]
 		self.y_values = [0]

 	def fill_walk(self):

 		while len(self.x_values) < self.number_points:
 			x_direction = choice([-1, 1])
 			x_distance = choice([0, 1, 2, 3, 4])
 			x_step = x_direction * x_distance

 			y_direction = choice([-1, 1])
 			y_distance = choice([0, 1, 2, 3, 4])
 			y_step = y_direction * y_distance

 			if x_step == 0 and y_step == 0:
 				continue

 			next_x = self.x_values[-1] + x_step
 			next_y = self.y_values[-1] + y_step

 			self.x_values.append(next_x)
 			self.y_values.append(next_y)

random_walk = RandomWalk(number_points=30000)
random_walk.fill_walk()

#绘图窗口的设置
plt.figure(dpi = 128, figsize = (10, 6))

point_numbers = list(range(random_walk.number_points))
plt.scatter(random_walk.x_values, random_walk.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 2)

#突出起点和终点
plt.scatter(0, 0, c = 'red', edgecolor = 'none', s = 10)
plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c = 'red', edgecolor = 'none', s = 10)

#隐藏坐标轴
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

plt.show()
