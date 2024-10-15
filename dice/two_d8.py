"""
15-6. Two D8s: Create a simulation showing what happens when you roll two
eight-sided dice 1,000 times. Try to picture what you think the visualization will
look like before you run the simulation, then see if your intuition was correct.
Gradually increase the number of rolls until you start to see the limits of your
system’s capabilities.
"""

import plotly.express as px
from die import Die

# Create 2 D8s
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of rolling two D8s 50,000 Times."
labels = {'x': 'Result', 'y': 'Frequency of Resul'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()