import numpy as np
import random

array = np.array([random.randint(10, 100) for i in range(10)])
arraySort = sorted(array, reverse=True)
check = True

for i in range(len(array)):
    if array[i] != arraySort[i]:
        check = False
        break

print(array)
print(arraySort)

print(check)