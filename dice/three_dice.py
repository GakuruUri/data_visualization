"""
15-7. Three Dice: When you roll three D6 dice, the smallest number you can roll
is 3 and the largest number is 18. Create a visualization that shows what hap-
pens when you roll three D6 dice.
"""

import plotly.express as px
from die import Die

# Create 3 D6s
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)


# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of rolling three D6s 50,000 Times."
labels = {'x':'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.show()
