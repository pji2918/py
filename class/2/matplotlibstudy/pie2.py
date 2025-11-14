from matplotlib import pyplot as plt


volume = [15.7, 19.8, 11.2, 24.0]
name_labels = ["Sedan", "RV", "Premium Car", "etc"]
explode = (0.03, 0.03, 0.03, 0.03)

plt.pie(volume, labels=name_labels, autopct="%.1f%%", explode=explode, startangle=90)
plt.show()
