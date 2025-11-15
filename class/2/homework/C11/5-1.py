from matplotlib import pyplot as plt
import numpy as np


dachshund = np.array(
    [[77, 78, 85, 83, 73, 77, 73, 80], [25, 28, 19, 30, 21, 22, 17, 35]]
)
samoyed = np.array([[75, 77, 86, 86, 79, 83, 83, 88], [56, 57, 50, 53, 60, 53, 49, 61]])
maltese = np.array([[34, 38, 38, 41, 30, 37, 41, 35], [22, 25, 19, 30, 21, 24, 28, 18]])

fig, axes = plt.subplots(1, 3)

axes[0].scatter(*dachshund, c="red", marker="o")
axes[0].set_title("Dachshund size")
axes[0].set_xlabel("Length")
axes[0].set_ylabel("Height")

axes[1].scatter(*samoyed, c="blue", marker="s")
axes[1].set_title("Samoyed size")
axes[1].set_xlabel("Length")
axes[1].set_ylabel("Height")

axes[2].scatter(*maltese, c="green", marker="^")
axes[2].set_title("Maltese size")
axes[2].set_xlabel("Length")
axes[2].set_ylabel("Height")

plt.show()
