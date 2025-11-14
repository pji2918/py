from matplotlib import pyplot as plt
import numpy as np

years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
cn = [100, 200, 290, 540, 1760, 7940]

x_range = np.arange(len(years)) * 1.2

plt.bar(x_range - 0.3, ko, label="KO", width=0.25)
plt.bar(x_range, jp, label="JP", width=0.25)
plt.bar(x_range + 0.3, cn, label="CN", width=0.25)

plt.xticks(x_range, tuple(map(str, years)))

plt.title("GDP per capita")
plt.xlabel("years")
plt.ylabel("dollars")
plt.legend()
plt.show()
