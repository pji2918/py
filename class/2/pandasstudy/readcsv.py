import csv

from matplotlib import pyplot as plt

with open("class/2/data/csv/weather.csv") as f:
    data = csv.reader(f)
    header = next(data)

    monthly_wind = [0.0 for _ in range(12)]
    days_counted = [0 for _ in range(12)]

    for row in data:
        month = int(row[0][5:7])
        if row[3] != "":
            wind = float(row[3])
            monthly_wind[month - 1] += wind
            days_counted[month - 1] += 1

    for i in range(12):
        monthly_wind[i] /= days_counted[i]

    plt.rcParams["font.family"] = "Pretendard JP Variable"
    plt.plot(monthly_wind, "blue")
    plt.xticks(
        range(12),
        labels=[f"{i + 1}월" for i in range(12)],
    )
    plt.show()
