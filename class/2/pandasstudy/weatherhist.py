from matplotlib import pyplot as plt
import pandas as pd

weather = pd.read_csv("class/2/data/csv/weather.csv", encoding="UTF-8")

plt.rcParams["font.family"] = "Pretendard JP Variable"
weather["평균풍속"].plot(kind="hist", bins=33)
plt.show()
