import numpy as np
import time

startTime = time.time()

total = 0
# for i in np.arange(1000000):
#     total += i
total = np.sum(np.arange(10000000))
endTime = time.time()

print(f"total = {total}")
print(f"Time elapsed: {endTime - startTime:.10f} sec")
