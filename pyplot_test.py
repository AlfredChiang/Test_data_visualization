import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_value, squares, linewidth = 3)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("squares", fontsize =14)
plt.tick_params(axis = 'both', which = 'both', labelsize = 14)

plt.show()

x_value = [1, 3, 5, 7, 9]
y_value = [1, 9, 25, 49, 81]

plt.scatter(x_value, y_value, c = 'green', s = 30)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("squares", fontsize =14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

x_values = list(range(1, 1001))
y_value = [x**2 for x in x_values]

#红绿蓝 值越接近于0，指定颜色越深
plt.scatter(x_values, y_value, c=(0, 0.1, 0), edgecolor = 'none', s=10)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("squares", fontsize =14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

x_values = list(range(1, 1001))
y_value = [x**2 for x in x_values]

#颜色映射
plt.scatter(x_values, y_value, c = y_value, cmap = plt.cm.Greens, edgecolor = 'none', s=10)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("squares", fontsize =14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig('color_cmap.jpeg', bbox_inches = 'tight')
