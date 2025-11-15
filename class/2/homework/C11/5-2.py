from matplotlib import pyplot as plt
import numpy as np


dachshund = np.array(
    [[77, 78, 85, 83, 73, 77, 73, 80], [25, 28, 19, 30, 21, 22, 17, 35]]
)
samoyed = np.array([[75, 77, 86, 86, 79, 83, 83, 88], [56, 57, 50, 53, 60, 53, 49, 61]])
maltese = np.array([[34, 38, 38, 41, 30, 37, 41, 35], [22, 25, 19, 30, 21, 24, 28, 18]])


plt.scatter(*dachshund, c="red", marker="o", label="Dachshund")
plt.scatter(*samoyed, c="blue", marker="^", label="Samoyed")
plt.scatter(*maltese, c="green", marker="s", label="Maltese")

plt.title("Dog size")
plt.xlabel("Length")
plt.ylabel("Height")
plt.legend()
plt.show()
