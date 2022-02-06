import random
import numpy as np

elemsList= [0, 1, 5]
arr = np.array([random.choice(elemsList) for i in range(10)])
arr = np.sort(arr)

print(arr)