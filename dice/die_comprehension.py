"""
15-9. Die Comprehensions: For clarity, the listings in this section use the long
form of for loops. If you’re comfortable using list comprehensions, try writing a
comprehension for one or both of the loops in each of these programs.
"""

import plotly.express as px
from die import Die


# Create a D10 and  D6 die
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# Analyze results
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)


frequencies = [results.count(value) for value in poss_results]

# Visualize results
title = "Results of rolling a D6 and a D10 in poss_results"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()
