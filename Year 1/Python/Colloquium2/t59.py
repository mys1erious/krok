import numpy as np
import random

arr = np.array([random.randint(0, 10) for i in range(10)])
print(arr)

uni = np.unique(arr)
print(len(uni))