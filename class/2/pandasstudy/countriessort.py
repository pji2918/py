import pandas as pd
# from matplotlib import pyplot as plt

df = pd.read_csv("class/2/data/csv/countries.csv", index_col=0)
sorted_df = df.sort_values("population")
df.sort_values("area", ascending=False, inplace=True)
print(sorted_df)
print(df)
