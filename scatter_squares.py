import matplotlib.pyplot as plt

#Plotting a Series of Points with scatter(pass x and y to scatter())

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]


# Calculating Data Automatically
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)


#Plotting and Styling Individual Points with scatter()
# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)


# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])


plt.show()
