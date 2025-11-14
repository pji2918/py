from matplotlib import pyplot as plt
import numpy as np

pos = np.random.randint(0, 51, (30, 30))
plt.scatter(pos[0], pos[1])
plt.show()
