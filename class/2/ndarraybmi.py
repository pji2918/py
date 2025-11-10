import numpy as np

heights = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weights = np.array([86, 74, 59, 95, 80, 68])
bmi = weights / (heights**2)

print(f"Height : {heights}")
print(f"Weight : {weights}")
print(f"BMI : {bmi}")
print(f"B-Mhan : {bmi[bmi > 25]}")
