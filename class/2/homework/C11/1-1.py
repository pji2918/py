from matplotlib import pyplot as plt

user = [456, 492, 578, 599, 670, 854]
month = [7, 8, 9, 10, 11, 12]

fig, axis = plt.subplots(1, 4)

axis[0].bar(month, user)
axis[0].set_title("Bar chart")

axis[1].plot(month, user)
axis[1].set_title("Line chart")

axis[2].scatter(month, user, marker="^")
axis[2].set_title("Scatter chart")

axis[3].barh(month, user)
axis[3].set_title("Horizontal Bar chart")

plt.show()
