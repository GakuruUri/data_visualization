import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
output_values = [1, 2, 27, 64, 125]


plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.plot(input_values, output_values, linewidth=3)

# Set chart title and label axes
ax.set_title("Cube numbers", fontsize=240)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()


# import matplotlib.pyplot as plt
#
# # values = [1, 2, 3, 4, 5]
# cubes =[1, 6, 27, 256, 3125]
#
# fig, ax = plt.subplots()
# ax.plot(cubes)
# plt.sh
