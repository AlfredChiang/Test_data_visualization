import matplotlib.pyplot as plt 

plt.scatter(2, 4, s=100)

plt.title("Square Numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("value of square", fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()