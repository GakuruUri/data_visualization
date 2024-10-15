""""
15-8. Multiplication: When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if you
multiply these numbers by each other instead.
"""

import plotly.express as px

from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)