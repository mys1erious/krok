import numpy as np
import random

array = np.array([random.randint(-10, 15) for i in range(10)])
array2 = np.zeros(0)

for i in array:
    if i in range(-2, 10):
        array2 = np.append(array2, i)

meanarr2 = array2.mean()
print(array2)
print(meanarr2)