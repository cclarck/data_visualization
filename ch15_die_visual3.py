#!/usr/bin/env python3
# 2021.12.12 14:37:44 CST
# title = ch15 rolling the die - making a histogram
from plotly.graph_objs import Bar, Layout
from plotly import offline
from ch15_die import Die

# create a D6
die = Die()

# make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# check each number from 1 through 6.    
#print(results)

# analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# check 1 through 6 in the case.    
# print(frequencies)

# visualize the  results.
x_values = list(range(1, die.num_sides+1))
data = [ Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', \
xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

