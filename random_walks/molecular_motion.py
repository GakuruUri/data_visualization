
""" 
15-3. Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with
ax.plot(). To simulate the path of a pollen grain on the surface of a drop of
water, pass in the rw.x_values and rw.y_values, and include a linewidth argu-
ment. Use 5,000 instead of 50,000 points to keep the plot from being too busy.
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Make a random walk
rw =  RandomWalk(5_000)
rw.fill_walk()

#Plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect('equal')


#Emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()