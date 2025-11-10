import numpy as np
import matplotlib.pyplot as plt

# x = np.array([["a", "b", "c", "d"], ["c", "c", "g", "h"]])

# print(x[x == "c"])

# mat_a = np.array([[10, 20, 30], [10, 20, 30]])
# mat_b = np.array([[2, 2, 2], [1, 2, 3]])

# print(mat_a - mat_b)

x = np.array(
    [
        [1.83, 1.76, 1.69, 1.86, 1.77, 1.73, 1.8, 1.5],
        [86.0, 74.0, 59.0, 95.0, 80.0, 68.0, 62.5, 70.0],
    ]
)
print(x.flatten())
print(x.reshape(4, -1))
plt.plot(np.linspace(0, 10))
plt.plot(np.logspace(0, 1))
plt.show()
