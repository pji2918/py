from typing import Tuple
from matplotlib import pyplot as plt
import numpy as np
from numpy.typing import NDArray


def getGaussPos(
    n: int, m: int, s: int, *args
) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    mY = m
    sY = s
    if len(args) == 2:
        mY = args[0]
        sY = args[1]
    x: NDArray[np.float64] = m + s * np.random.randn(n)
    y: NDArray[np.float64] = mY + sY * np.random.randn(n)
    return x, y


fig, axis = plt.subplots(1, 3)

axis[0].scatter(*getGaussPos(1000, 25, 6), c="blue")
axis[1].scatter(*getGaussPos(1000, 25, 6, 25, 3), c="red")

tempX = getGaussPos(1000, 25, 6)[0]
axis[2].scatter(tempX, tempX + np.random.randn(), c="green")

axis[0].axis((0, 50, 0, 50))
axis[1].axis((0, 50, 0, 50))
axis[2].axis((0, 50, 0, 50))

plt.show()
