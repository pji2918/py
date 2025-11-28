import pandas as pd


weather = pd.read_csv("class/2/data/csv/weather.csv")
print(weather[weather["최대풍속"] >= 10])
