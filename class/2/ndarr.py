import numpy as np

array_a = np.array(list(range(0, 10)))
array_b = np.array(range(0, 10))
array_c = np.array(range(0, 10, 2))

print(f"실습 1 : array_a = {array_a}")
print(f"실습 2 : array_b = {array_b}")
print(f"실습 3 : array_c = {array_c}")
print("실습 4:")
print(f"array_c의 shape : {array_c.shape}")
print(f"array_c의 ndim : {array_c.ndim}")
print(f"array_c의 dtype : {array_c.dtype}")
print(f"array_c의 size : {array_c.size}")
print(f"array_c의 itemsize : {array_c.itemsize}")
