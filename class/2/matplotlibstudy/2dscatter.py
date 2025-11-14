from matplotlib import pyplot as plt
import numpy as np

cnt = 10000

xData = np.random.randn(cnt)
yData = np.random.randn(cnt)

plt.scatter(xData, yData, alpha=0.15)
# plt.plot(xData, yData)
plt.title("Random Position")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
