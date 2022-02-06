import numpy as np
import random

array = np.array([random.randint(10, 100) for i in range(10)])
array = np.sort(array)
print(array)