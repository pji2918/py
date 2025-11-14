import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.01)
y = [i**2 for i in x]
z = [i**3 for i in x]
p = [2**i for i in x]

plt.plot(x, x, label="linear")
plt.plot(x, y, label="quadratic")
plt.plot(x, z, label="cubic")
plt.plot(x, p, label="power")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("My Plot")
plt.legend()
plt.show()
