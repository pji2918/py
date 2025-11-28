import pandas as pd


weather = pd.read_csv("class/2/data/csv/weather.csv", index_col=0)

weather.fillna(weather["평균풍속"].mean(), inplace=True)
print(weather.loc["2012-02-11"])
