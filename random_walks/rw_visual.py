import matplotlib.pyplot as plt
from random_walk import RandomWalk


# keep making new walks, as long as the program is active

while True:


    # Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plt the points on the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges,
    edgecolors='none', s=1)

    # ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)


    # Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break