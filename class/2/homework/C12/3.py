import pandas as pd

p_df = pd.DataFrame(
    {
        "name": ["A", "B", "C", "D", "E", "F", "G"],
        "horse power": [130, 250, 190, 300, 210, 220, 170],
        "weight": [1.9, 2.6, 2.2, 2.9, 2.4, 2.3, 2.2],
        "efficiency": [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2],
    }
)
p_df.set_index("name", inplace=True)
q_df = pd.DataFrame(
    {
        "name": ["A", "B", "C", "D"],
        "horse power": [120, 220, 120, 200],
        "weight": [1900, 2100, 1500, 2900],
        "efficiency": [18.3, 19.2, 21.1, 17.3],
    },
)
q_df.set_index("name", inplace=True)

print(q_df)

print()
print(pd.concat([p_df, q_df]))

print()
p_df["com"] = "P"
q_df["com"] = "Q"
print(pd.concat([p_df, q_df]))

print()
p_df["hp x mile"] = p_df["horse power"] * p_df["efficiency"]
q_df["hp x mile"] = q_df["horse power"] * q_df["efficiency"]
print(
    pd.concat([p_df, q_df])
    .groupby("com")["hp x mile"]
    .mean(numeric_only=True)
    .to_string()
)
