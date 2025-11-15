from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 360)
y = np.radians(x)

amp = np.linspace(0, 7, 360)

plt.plot(x, np.sin(y * 7) * amp, "r-")
plt.plot(x, np.cos(y * 7) * amp, "b--")

plt.show()
