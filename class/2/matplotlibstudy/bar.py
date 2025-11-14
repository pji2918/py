from matplotlib import pyplot as plt


years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

plt.bar(range(len(years)), gdp)
plt.xticks(range(len(years)), tuple(map(str, years)))

plt.title("GDP per capita")
plt.xlabel("years")
plt.ylabel("dollars")

plt.show()
