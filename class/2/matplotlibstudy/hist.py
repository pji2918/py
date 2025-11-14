from matplotlib import pyplot as plt
import numpy as np

# books = [1, 6, 2, 3, 1, 2, 0, 2]

n_bins = 20

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hist(x, n_bins, histtype="bar", color="red")
plt.hist(y, n_bins, histtype="bar", color="blue", alpha=0.3)

# plt.xlabel("books")
# plt.ylabel("frequency")
plt.show()
