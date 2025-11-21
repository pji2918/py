import pandas as pd

df = pd.read_csv("class/2/weather.csv", index_col=0)
print(df.head(3))
print()
print(df.tail(3))
print()
print(df.loc["2015-06-06"])
print()
print(df["평균기온"].max())
print()
print(df[df["평균기온"] == df["평균기온"].max()])
print()
print(df[df["평균기온"] >= 30])
