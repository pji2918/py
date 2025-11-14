import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 360)
y = np.radians(x)
plt.plot(x, np.sin(y), label="sin(x)")
plt.plot(x, np.cos(y), "r-", label="cos(x)")
# plt.plot(x, np.tan(y), "g-", label="tan(x)")
plt.title("SINE + COSINE WAVE")
plt.legend()
plt.show()
