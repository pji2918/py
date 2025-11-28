import random
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("class/2/data/csv/countries.csv", index_col=0)

# fig, axes = plt.subplots(1, 2)

# df["population"].plot(kind="bar", color=("b", "darkorange", "g", "r", "m"), ax=axes[0])
# df["population"].plot(kind="pie", ax=axes[1])

df["density"] = df["population"] / df["area"]

print(df)
cmap = plt.get_cmap("hsv")
df["density"].plot(
    kind="bar", color=cmap([random.random() for _ in range(df["density"].count())])
)
plt.show()
