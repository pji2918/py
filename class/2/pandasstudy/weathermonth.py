from matplotlib import pyplot as plt
import pandas as pd


weather = pd.read_csv("class/2/data/csv/weather.csv", encoding="UTF-8")
# weather["year"] = pd.DatetimeIndex(weather["일시"]).year
weather["month"] = pd.DatetimeIndex(weather["일시"]).month

# y_means = weather.groupby("year").mean(numeric_only=True)
m_means = weather.groupby("month").mean(numeric_only=True)
m_means["평균풍속"].plot(kind="bar")

# y_max = weather.groupby("year").max(numeric_only=True)
# print(y_max)
plt.show()
