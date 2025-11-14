from matplotlib import pyplot as plt


times = [8, 14, 2]
timelabels = ("Sleep", "Study", "Play")

plt.pie(times, labels=timelabels, autopct="%.1f%%")
plt.title("Time Table")
plt.show()
