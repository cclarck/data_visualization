#!/usr/bin/env python3
# 2021.12.09 13:34:31 CST
# title = calculatintg data automatically using colormap
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [ x**2 for x in x_values ]
# y_values = []
# for x in x_values:
    # y_values.append(x ** 2)
#print(f"y_values: {y_values}")

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
#ax.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('1209_ch15_scatter_square5-1.png', bbox_inches='tight')
plt.show()
