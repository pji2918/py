from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 40, 500)
amp = np.linspace(0, 7, 40)

ySin = x * np.sin(6 * np.pi / 19 * x)
yCos = 20 * np.cos(7 * np.pi / 20 * x)

plt.plot(x, ySin, "r-")
plt.plot(x, yCos, "b--")

plt.show()
