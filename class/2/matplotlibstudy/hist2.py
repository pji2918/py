from matplotlib import pyplot as plt
import numpy as np

n_bins = 500
cnt = 100000

x = np.random.randn(cnt)
y = 10 + 2 * np.random.randn(cnt)
z = -6 + 3 * np.random.randn(cnt)

plt.figure(figsize=(10, 6))
plt.hist(x, n_bins, color="blue", alpha=0.3)
plt.hist(y, n_bins, color="green", alpha=0.3)
plt.hist(z, n_bins, color="red", alpha=0.3)

plt.show()
