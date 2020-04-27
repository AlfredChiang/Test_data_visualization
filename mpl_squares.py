from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
plt.plot(input_value, square, linewidth = 3)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("square of value", fontsize = 14)
#设置刻度标记的样式 字号
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()