from matplotlib import pyplot as plt
import numpy as np


xData = np.arange(20, 50)
# yData = np.random.randn(30)
yData = xData + 2 * np.random.randn(30)

plt.scatter(xData, yData)
# plt.plot(xData, yData)
plt.title("Real Age vs Physical Age")
plt.xlabel("Real Age")
plt.ylabel("Physical Age")

plt.show()
