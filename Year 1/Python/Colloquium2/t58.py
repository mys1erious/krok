import numpy as np
import random

arr = np.array([random.randint(0, 10) for i in range(20)])
print(arr)

uni, count = np.unique(arr, return_counts=True)
print(max(count))